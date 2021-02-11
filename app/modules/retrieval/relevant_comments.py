import os
import pickle
from sentence_transformers import SentenceTransformer, CrossEncoder, util
from constants import *


def _get_relevant_comments_helper(comments, query, query_embedding, corpus_embeddings):
    hits = util.semantic_search(query_embedding, corpus_embeddings, top_k = 10)
    hits = hits[0]  
    
    cross_encoder = CrossEncoder('cross-encoder/ms-marco-TinyBERT-L-6')

    cross_inp = [[query, comments[hit['corpus_id']]] for hit in hits]
    cross_scores = cross_encoder.predict(cross_inp)
    
    for idx in range(len(cross_scores)):
        hits[idx]['cross-score'] = cross_scores[idx]
        
    hits = sorted(hits, key=lambda x: x['cross-score'], reverse=True)
    
    #print top 10 hits
    for hit in hits[:10]:
        #print(hit['score'], comments[hit['corpus_id']])
    
    return hits[:10]



def get_relevant_comments(query, filename, comments_list = None):
    encoder = SentenceTransformer('distilbert-base-nli-stsb-quora-ranking')
    
    if not os.path.isfile(os.path.join(PATH_TO_DATA_CACHE, f'{filename}_embedding_cache.pkl')):
        corpus_embeddings = encoder.encode(comments_list, show_progress_bar=True, convert_to_numpy=True)

        with open(os.path.join(PATH_TO_DATA_CACHE, f'{filename}_embedding_cache.pkl'), 'wb') as f:
            pickle.dump(corpus_embeddings, f)
    else:
        # load embeddings from cache
        with open(os.path.join(PATH_TO_DATA_CACHE, f'{filename}_embedding_cache.pkl'), 'rb') as f:
            corpus_embeddings = pickle.load(f)

    query_embedding = encoder.encode(query, convert_to_tensor=True)

    top_retrieved_comments = _get_relevant_comments_helper(comments_list, query, query_embedding, corpus_embeddings)

    return top_retrieved_comments


