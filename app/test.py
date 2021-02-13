import os
import sys
import time
import emoji
import re
from collections import defaultdict

sys.path.append('data')
sys.path.append('modules')

from commentsextractor import run_comments_collector
from clustering import cluster_maker
from retrieval import relevant_comments
from prettylittlewordclouds import cloudmaker

from constants import *

filename = "'Just a YouTuber'.csv"

short_comments_list, long_comments_list, df = cluster_maker.load_data(filename)
# print(short_comments_list[:5])
clusters_to_show = cluster_maker.get_clusters_from_file(filename, long_comments_list)

sum = 0
NUM_CLUSTERS_TO_USE = len(clusters_to_show)
if NUM_CLUSTERS_TO_USE > 20:
    NUM_CLUSTERS_TO_USE = 20

for cluster in clusters_to_show[:NUM_CLUSTERS_TO_USE]:
    sum += len(cluster)

for cluster in clusters_to_show:
    percentages.append((len(cluster)/sum)*100.0)

import plotly.graph_objects as go
labels = [f"Topic{i}" for i in range(1, NUM_CLUSTERS_TO_USE)]
values = percentages

fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])



# for i, cluster in enumerate(clusters_to_show):
#         print(f'Topic {i}: ')
#         for sentence_id in cluster:
#             print("\t", comments_list[sentence_id])
        
#         print('-------------')

# text = emoji.demojize(' '.join(short_comments_list))
# text = re.findall(r'(:[!_\-\w]+:)', text)
# # text = re.findall(r'(:[^:]*:)', text)
# list_emoji = [emoji.emojize(x) for x in text]
# # print(list_emoji)

# all_emojis_count = defaultdict(int)

# for emoji in list_emoji:
#     all_emojis_count[emoji] += 1

# sorted_emojis_count = [k for k, v in sorted(all_emojis_count.items(), key = lambda item: item[1], reverse = True)]
# print(sorted_emojis_count[:10])

# print(cluster_maker.get_clusters_from_file("'Just a YouTuber'.csv"))

# relevant_comments.get_relevant_comments('What an inspiration!', "How to Vlog.csv", long_comments_list)


# extra_stop_words = ['Peter', 'McKinnon', 'Thank', 'Youtube', 'Youtuber', 'Video', 'film', 'filmmaker']

# filepath_of_saved_image = cloudmaker.get_styled_cloud(long_comments_list, \
#                                                         extra_stop_words = extra_stop_words,\
#                                                         icon_selected = 'fas fa-film')

# print(filepath_of_saved_image)

