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
from constants import *

filename = "'Just a YouTuber'.csv"

short_comments_list, long_comments_list, df = cluster_maker.load_data(filename)
# print(short_comments_list[:5])
# clusters_to_show = cluster_maker.get_clusters_from_file(filename, comments_list)

# for i, cluster in enumerate(clusters_to_show):
#         print(f'Topic {i}: ')
#         for sentence_id in cluster:
#             print("\t", comments_list[sentence_id])
        
#         print('-------------')

text = emoji.demojize(' '.join(short_comments_list))
text = re.findall(r'(:[!_\-\w]+:)', text)
# text = re.findall(r'(:[^:]*:)', text)
list_emoji = [emoji.emojize(x) for x in text]
# print(list_emoji)

all_emojis_count = defaultdict(int)

for emoji in list_emoji:
    all_emojis_count[emoji] += 1

sorted_emojis_count = [k for k, v in sorted(all_emojis_count.items(), key = lambda item: item[1], reverse = True)]
print(sorted_emojis_count[:10])


# print(cluster_maker.get_clusters_from_file("'Just a YouTuber'.csv"))