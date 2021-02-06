import os
import sys
import time

sys.path.append('data')
sys.path.append('modules')

from commentsextractor import run_comments_collector
from clustering import cluster_maker
from constants import *

filename = "'Just a YouTuber'.csv"

comments_list, _ = cluster_maker.load_data(filename)
print(comments_list[:5])
clusters_to_show = cluster_maker.get_clusters_from_file(filename, comments_list)

for i, cluster in enumerate(clusters_to_show):
        print(f'Topic {i}: ')
        for sentence_id in cluster:
            print("\t", comments_list[sentence_id])
        
        print('-------------')




# print(cluster_maker.get_clusters_from_file("'Just a YouTuber'.csv"))