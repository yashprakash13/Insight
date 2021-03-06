import os
import sys
import time
import base64
from PIL import Image

sys.path.append('data')
sys.path.append('modules')

from commentsextractor import run_comments_collector
from clustering import cluster_maker, chart_maker
from emojitask import emoji_extractor
from retrieval import relevant_comments
from prettylittlewordclouds import cloudmaker
from constants import *


import streamlit as st



# title and logo
st.sidebar.image(os.path.join(IMAGES_PATH, 'logo.png'), width=250)
st.sidebar.title('Insight Explorer')
st.empty()

class Starter:
    def __init__(self):
        self.data_file_selected = None
        self.list_of_files = None
        self.short_comments_list = None
        self.long_comments_list = None
        self.df = None
        self.all_clusters = None
        self.top_emojis = None
    

    def get_data_from_url(self, url):
        video_titles = run_comments_collector.get_comments_from_urls([url])
        return video_titles[0]

    def get_list_of_data_files(self):
        '''to load a csv file from data folder'''
        file_list = os.listdir('data/')
        return [str(filename) for filename in file_list if str(filename).endswith('.csv')]

    def get_icon_code_from_selected_cloud_image(self, selected = 'Simple Cloud'):
        '''to get the corresponding icon code for loud masl'''
        return DICT_OF_CLOUDS[selected]
    
    def get_binary_file_downloader_html(self, bin_file, file_label='File'):
        '''display button for downloading cloud image as png file'''
        with open(bin_file, 'rb') as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href
    
    def get_sentences_in_cluster(self, cluster):
        '''get a set of 5 unique sentences from each cluster'''
        sentences = set()
        num = 0
        for sentence_id in cluster:
            if num >= 5:
                break
            if self.long_comments_list[sentence_id] not in sentences:
                sentences.add(self.long_comments_list[sentence_id])
                num += 1
        return sentences


    def run_all(self):
        '''
        main function to display all widgets and functionalities
        '''

        st.sidebar.subheader('Fetch comments from URL')
        url_input = st.sidebar.text_input(label = 'Enter a Youtube Video URL')
        
        if st.sidebar.button('Get and Load'):
            if not url_input:
                st.sidebar.error('URL cannot be empty!')
            else:
                with st.spinner('Fetching comments...'):
                    video_title = self.get_data_from_url(url_input)
                    st.sidebar.success(f'Comments fetched from "{video_title}"! Now select it from the below list.')

        st.sidebar.write('OR')

        self.list_of_files = self.get_list_of_data_files()
        st.sidebar.subheader('Load data from an existing file')
        self.data_file_selected = st.sidebar.selectbox(label = 'Select the data to load:', \
                                                        options = self.list_of_files)
        st.sidebar.write(f'Selected: {self.data_file_selected}')
        self.short_comments_list, self.long_comments_list, \
                    self.df = cluster_maker.load_data(self.data_file_selected)

        # load data + show data buttons
        if st.sidebar.button('Load'):
            with st.spinner('Loading data...'):
                time.sleep(0.5)
                st.success('Data loaded!')

        if st.sidebar.checkbox('Show dataframe'):
            with st.beta_expander('See Dataframe:'):
                st.subheader('Dataframe:')
                st.write(self.df)
        if st.sidebar.checkbox('Show list of comments'):
            with st.beta_expander('See List of Comments:'):
                st.subheader('Showing top 20 comments:')
                st.write(self.long_comments_list[:20])
                
        # for getting all topics
        with st.beta_container():
            st.sidebar.subheader('Find different topics from comments')
            start_clustering_btn = st.sidebar.button('Get topics')

            if start_clustering_btn:
                with st.spinner('Getting topics...'):  
                    time.sleep(1)
                    # get all clusters from comments
                    # st.write(self.data_file_selected)
                    self.all_clusters = cluster_maker.get_clusters_from_file(self.data_file_selected, \
                                                                                self.long_comments_list)
                    with st.beta_expander('Topics talked about from the comments:', expanded = True):
                        # print clusters as 2 x 5 matrix of beta columns
                        for i in range(1, 20, 2):
                            c1, c2 = st.beta_columns(2)
                            try:
                                curr_cluster1 = self.all_clusters[i-1]
                                curr_cluster2 = self.all_clusters[i]
                                with c1:
                                    st.subheader(f'Topic {i}:')
                                    st.write(list(self.get_sentences_in_cluster(curr_cluster1)))

                                with c2:
                                    st.subheader(f'Topic {i+1}:')
                                    st.write(list(self.get_sentences_in_cluster(curr_cluster2)))
                                st.write('------------------------------')
                            except Exception as e:
                                pass

                    # display plotly donut of topics
                    st.plotly_chart(chart_maker.get_donut_of_topics(self.all_clusters))
        
                
        # for getting top emotes from comments
        with st.beta_container():
            st.sidebar.subheader('Find top emojis from the comments')
            count_of_emojis = st.sidebar.slider('Top:', min_value = 3, max_value = 10)
            if st.sidebar.button('Get'):
                with st.spinner('Getting top emojis...'):
                    self.top_emojis = emoji_extractor.get_most_freq_emojis(self.short_comments_list, 10)
                    with st.beta_expander(label = f'Top {count_of_emojis} emojis from the comments are:', \
                                        expanded=True):
                        st.write(self.top_emojis[:count_of_emojis])
                    


        # for getting related comments from a search item
        with st.beta_container():
            st.sidebar.subheader('Enter a query here to fetch related comments')
            query = st.sidebar.text_input('Type here.')
            if st.sidebar.button('Get comments'):
                with st.beta_expander(label = 'Comments that match', expanded = True):
                    with st.spinner('Fetching comments...'):
                        hits = relevant_comments.get_relevant_comments(query, self.data_file_selected, \
                                                                self.long_comments_list)
                        top_comments_retreived = []
                        for hit in hits:
                            top_comments_retreived.append(self.long_comments_list[hit['corpus_id']])
                        st.write(top_comments_retreived)


        # for making, displaying and downloading the pretty little word cloud of comments
        with st.beta_container():
            st.sidebar.subheader('Make a pretty little cloud of words from the comments')
            selected_cloud_image = st.sidebar.selectbox(label = 'Select a mask image:', \
                                                        options = OPTION_OF_CLOUDS)
            
            icon_selected = self.get_icon_code_from_selected_cloud_image(selected_cloud_image)

            if st.sidebar.button('Generate'):
                with st.spinner('Building the word cloud...'):
                    generated_cloud_name = cloudmaker.get_styled_cloud(self.long_comments_list, \
                                                                        icon_selected = icon_selected)
                    st.image(os.path.join(PRETTY_LITTLE_WORD_CLOUD_PATH, generated_cloud_name), width = 720)

                cloud_image_file_path = os.path.join(PRETTY_LITTLE_WORD_CLOUD_PATH, generated_cloud_name)

                st.markdown(self.get_binary_file_downloader_html(cloud_image_file_path, 'this image'), \
                                unsafe_allow_html=True)

            

# run everything and display the app
starter = Starter()
starter.run_all()






