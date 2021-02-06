import os
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import numpy as np
import pickle


from constants import *

df = None
comments_list = None

def load_data(filename):
    df = pd.read_csv(os.path.join(PATH_TO_DATA, filename), \
                                    usecols = [1, 4]).sort_values(by = [COLUMN_LIKE_COUNT], \
                                    ascending = False).reset_index(drop = True)

    comments_list = df[COLUMN_COMMENT].tolist()

    return comments_list, df



def _detect_clusters(embeddings, threshold=0.85, min_community_size=15, init_max_size=1000):
    # Compute cosine similarity scores
    cos_scores = util.pytorch_cos_sim(embeddings, embeddings)

    # Minimum size for a community
    top_k_values, _ = cos_scores.topk(k=min_community_size, largest=True)

    # Filter for rows >= min_threshold
    extracted_communities = []
    for i in range(len(top_k_values)):
        if top_k_values[i][-1] >= threshold:
            new_cluster = []

            # Only check top k most similar entries
            top_val_large, top_idx_large = cos_scores[i].topk(k=init_max_size, largest=True)
            top_idx_large = top_idx_large.tolist()
            top_val_large = top_val_large.tolist()

            if top_val_large[-1] < threshold:
                for idx, val in zip(top_idx_large, top_val_large):
                    if val < threshold:
                        break

                    new_cluster.append(idx)
            else:
                # Iterate over all entries (slow)
                for idx, val in enumerate(cos_scores[i].tolist()):
                    if val >= threshold:
                        new_cluster.append(idx)

            extracted_communities.append(new_cluster)

    # Largest cluster first
    extracted_communities = sorted(extracted_communities, key=lambda x: len(x), reverse=True)

    # Step 2) Remove overlapping communities
    unique_communities = []
    extracted_ids = set()

    for community in extracted_communities:
        add_cluster = True
        for idx in community:
            if idx in extracted_ids:
                add_cluster = False
                break

        if add_cluster:
            unique_communities.append(community)
            for idx in community:
                extracted_ids.add(idx)

    return unique_communities



def get_clusters_from_file(filename, comments_list = None):
    if not os.path.isfile(os.path.join(PATH_TO_DATA_CACHE, f'{filename}_embedding_cache.pkl')):
        model = SentenceTransformer('distilbert-base-nli-stsb-quora-ranking')
        corpus_embeddings = model.encode(comments_list, show_progress_bar=True, convert_to_numpy=True)

        with open(os.path.join(PATH_TO_DATA_CACHE, f'{filename}_embedding_cache.pkl'), 'wb') as f:
            pickle.dump(corpus_embeddings, f)
    else:
        # load embeddings from cache
        with open(os.path.join(PATH_TO_DATA_CACHE, f'{filename}_embedding_cache.pkl'), 'rb') as f:
            corpus_embeddings = pickle.load(f)

    all_clusters = _detect_clusters(corpus_embeddings)
        
        
    all_clusters.sort()
    clusters_to_show = all_clusters[:5]

    # for i, cluster in enumerate(clusters_to_show):
    #     print(f'Topic {i}: ')
    #     for sentence_id in cluster[:5]:
    #         print("\t", comments_list[sentence_id])
        
    #     print('-------------')

    return clusters_to_show




def get_clusters_from_url(url):
    pass


def get_clusters():
    if os.path.isfile(os.path.join(PATH_TO_DATA_CACHE, filename)):
        pass
    else:
        pass



def print_all_clusters(clusters):
    '''
    To print all clusters
    '''
    for i, cluster in enumerate(clusters):
        print("\Topic {}, #{} Elements ".format(i+1, len(cluster)))
        for sentence_id in cluster:
            print("\t", comments_list[sentence_id])