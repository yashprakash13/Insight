import os
import sys
import time
import base64
from PIL import Image

sys.path.append('data')
sys.path.append('modules')

from commentsextractor import run_comments_collector
from clustering import cluster_maker
from emojitask import emoji_extractor
from retrieval import relevant_comments
from prettylittlewordclouds import cloudmaker
from constants import *


import streamlit as st


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

        self.engine_done = False
    
    def get_list_of_data_files(self):
        file_list = os.listdir('data/')
        return [str(filename) for filename in file_list if str(filename).endswith('.csv')]

    def get_icon_code_from_selected_cloud_image(self, selected = 'Simple Cloud'):
        return DICT_OF_CLOUDS[selected]
    
    def get_binary_file_downloader_html(self, bin_file, file_label='File'):
        with open(bin_file, 'rb') as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href


    def run_all(self):
        self.list_of_files = self.get_list_of_data_files()
        st.sidebar.subheader('Load data')
        self.data_file_selected = st.sidebar.selectbox(label = 'Select the data to load:', \
                                                        options = self.list_of_files)
        st.sidebar.write(f'Selected: {self.data_file_selected}')
        
        self.short_comments_list, self.long_comments_list, self.df = cluster_maker.load_data(self.data_file_selected)

        if st.sidebar.button('Load'):
            st.spinner('Loading data...')
            time.sleep(1.5)
            st.success('Data loaded!')

        if st.sidebar.checkbox('Show dataframe'):
            with st.beta_expander('See Dataframe:'):
                st.subheader('Dataframe:')
                st.write(self.df)
        if st.sidebar.checkbox('Show list of comments'):
            with st.beta_expander('See List of Comments:'):
                st.subheader('Showing top 20 comments:')
                st.write(self.long_comments_list[:20])
        
        
        with st.beta_container():
            st.sidebar.subheader('Find different topics from comments')
            start_clustering_btn = st.sidebar.button('Get topics')
            self.all_clusters = cluster_maker.get_clusters_from_file(self.data_file_selected, self.long_comments_list)

            if start_clustering_btn:
                with st.spinner('Getting topics...'):
                    time.sleep(3)
                
                         
                with st.beta_expander('See topics extracted from comments:', expanded = True):
                    for i, cluster in enumerate(self.all_clusters[:10]):
                        with st.beta_container():
                            st.subheader(f'Topic {i}:')
                            sentences = set()
                            num = 0
                            for sentence_id in cluster:
                                if num >= 5:
                                    break
                                if self.long_comments_list[sentence_id] not in sentences:
                                    st.write("\t", self.long_comments_list[sentence_id])
                                    sentences.add(self.long_comments_list[sentence_id])
                                    num += 1
                            
                            st.write('-------------')
                
        
        with st.beta_container():
            st.sidebar.subheader('Find top emojis from the comments')
            count_of_emojis = st.sidebar.slider('Top:', min_value = 3, max_value = 10)
            if st.sidebar.button('Get'):
                self.top_emojis = emoji_extractor.get_most_freq_emojis(self.short_comments_list, 10)
                with st.spinner('Getting top emojis...'):
                    time.sleep(1)
                with st.beta_expander(label = f'Top {count_of_emojis} emojis used in the comments are:', \
                                        expanded=True):
                    st.write(self.top_emojis[:count_of_emojis])

        with st.beta_container():
            st.sidebar.subheader('Enter a query here to fetch related comments')
            query = st.sidebar.text_input('Type here.')
            if st.sidebar.button('Get comments'):
                with st.spinner('Fetching...'):
                    time.sleep(3)
                with st.beta_expander(label = 'Comments that match', expanded = True):
                    hits = relevant_comments.get_relevant_comments(query, self.data_file_selected, \
                                                            self.long_comments_list)
                    top_comments_retreived = []
                    for hit in hits:
                        top_comments_retreived.append(self.long_comments_list[hit['corpus_id']])
                    st.write(top_comments_retreived)

        with st.beta_container():
            st.sidebar.subheader('Make a pretty little cloud of words from the comments')
            selected_cloud_image = st.sidebar.selectbox(label = 'Select a mask image:', \
                                                        options = OPTION_OF_CLOUDS)
            
            icon_selected = self.get_icon_code_from_selected_cloud_image(selected_cloud_image)

            if st.sidebar.button('Generate'):
                generated_cloud_name = cloudmaker.get_styled_cloud(self.long_comments_list, \
                                                                    icon_selected = icon_selected)
                st.image(os.path.join(PRETTY_LITTLE_WORD_CLOUD_PATH, generated_cloud_name))

                cloud_image_file_path = os.path.join(PRETTY_LITTLE_WORD_CLOUD_PATH, generated_cloud_name)

                st.markdown(self.get_binary_file_downloader_html(cloud_image_file_path, 'this image'), unsafe_allow_html=True)

            





starter = Starter()
starter.run_all()






