import os
import sys

sys.path.append('data')
sys.path.append('modules')

from commentsextractor import run_comments_collector
from clustering import cluster_maker


cluster_maker.get_clusters_from_file("'Just a YouTuber'.csv")
