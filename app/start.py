import os
import sys
import time

sys.path.append('data')
sys.path.append('modules')

from commentsextractor import run_comments_collector
from clustering import cluster_maker
from emojitask import emoji_extractor
from constants import *


import streamlit as st



st.sidebar.title('Insight Explorer')

class Starter:
    def __init__(self):
        self.data_file_selected = None
        self.list_of_files = None
        self.short_comments_list = None
        self.long_comments_list = None
        self.df = None
        self.clusters_to_show = None
        self.top_emojis = None
    
    def get_list_of_data_files(self):
        file_list = os.listdir('data/')
        return [str(filename) for filename in file_list if str(filename).endswith('.csv')]

    def run_clustering(self):
        self.list_of_files = self.get_list_of_data_files()
        self.data_file_selected = st.sidebar.selectbox(label = 'Select the data to load.', \
                                                        options = self.list_of_files)
        st.sidebar.write(f'Selected: {self.data_file_selected}')
        
        self.short_comments_list, self.long_comments_list, self.df = cluster_maker.load_data(self.data_file_selected)

        if st.sidebar.button('Load Data'):
            st.spinner('Loading data...')
            time.sleep(1.5)
            st.success('Data loaded!')

        if st.sidebar.checkbox('Show dataframe'):
            st.subheader('Dataframe:')
            st.write(self.df)
        if st.sidebar.checkbox('Show list of comments'):
            st.subheader('List of comments:')
            st.write(self.long_comments_list[:10])
        

        start_clustering_btn = st.sidebar.button('Start Clustering Process')

        if start_clustering_btn:
            self.clusters_to_show = cluster_maker.get_clusters_from_file(self.data_file_selected, \
                                                                        self.long_comments_list)
            # st.write(self.clusters_to_show)
            for i, cluster in enumerate(self.clusters_to_show):
                st.write(f'Topic {i}:')
                for sentence_id in cluster[:5]:
                    st.write("\t", self.long_comments_list[sentence_id])
                
                st.write('-------------')
        
        
        st.sidebar.write('Find top emojis from the comments!')
        count_of_emojis = st.sidebar.slider('Top:', min_value = 3, max_value = 10)

        self.top_emojis = emoji_extractor.get_most_freq_emojis(self.short_comments_list, 10)

        with st.spinner('Getting top emojis...'):
            time.sleep(1)
        
        st.write(self.top_emojis[:count_of_emojis])



starter = Starter()
starter.run_clustering()






