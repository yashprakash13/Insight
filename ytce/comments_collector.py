'''
The helper file to get the comments from a particular video url
'''

import requests
import pandas as pd
import json

from apiclient.discovery import build
from csv import writer
from urllib.parse import urlparse, parse_qs


def get_keys(filename):
    '''
    To get youtube API key from the specified json file
    '''
    with open(filename) as f:
        key = f.readline()
    DEVELOPER_KEY = key
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    return {'key': key, 'name': 'youtube', 'version': 'v3'}


def build_service(filename):
    '''
    To build the YT API service
    '''
    with open(filename) as f:
        key = f.readline()

    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    return build(YOUTUBE_API_SERVICE_NAME,
                 YOUTUBE_API_VERSION,
                 developerKey=key)
            

def get_id(url):
    '''
    To get the video id from the video url, example: 'https://www.youtube.com/watch?v=_bwfAPXlFu8', videoId = _bwfAPXlFu8
    '''
    u_pars = urlparse(url)
    quer_v = parse_qs(u_pars.query).get('v')
    if quer_v:
        return quer_v[0]
    pth = u_pars.path.split('/')
    if pth:
        return pth[-1]


def save_to_csv(output_dict, filename):
    '''
    To save the comments + other columns to the csv file specified with name
    '''
    output_df = pd.DataFrame(output_dict, columns = output_dict.keys())
    output_df.to_csv(f'data/{filename}.csv')


def comments_helper(video_ID, api_key, service):
    '''
    To get the comments in the form of a dictionary containing: 
    1. Comment id
    2. Comment text
    3. Comment author
    4. Comment likes

    This is the main function that will be called from the other module (the run module)
    '''

    # put comments extracted in specific lists for each column
    comments, commentsId, likesCount, authors = [], [], [], []
    
    # response to get the title of the video
    response_title = service.videos().list(
        part = 'snippet',
        id = video_ID
    ).execute()

    # get the video title
    video_title = response_title['items'][0]['snippet']['title']
    #print(video_title)
 

    #get the first response from the YT service
    response = service.commentThreads().list(
        part="snippet", 
        videoId = video_ID, 
        textFormat="plainText").execute()
    

    # page number of comments
    page = 0
    

    #until we get response or until we break with condition that len(comments) > 1000
    while response:
        #print(f'Page no: {page}')
        page += 1
        index = 0
        
        # for every comment in the response received
        for item in response['items']:
            #print(f"comment {index}")
            
            index += 1

            comment = item["snippet"]["topLevelComment"]
            
            author = comment["snippet"]["authorDisplayName"]
            text = comment["snippet"]["textDisplay"]
            comment_id = item['snippet']['topLevelComment']['id']
            like_count = item['snippet']['topLevelComment']['snippet']['likeCount']


            # append the comment to the lists
            comments.append(text)
            commentsId.append(comment_id)
            likesCount.append(like_count)
            authors.append(author)

            # with open(f'{csv_filename}.csv', 'a+') as f:
            #     csv_writer = writer(f)
            #     csv_writer.writerow([text, comment_id, like_count, author])

        
        # get next page of comments
        if 'nextPageToken' in response: # can also specify if number of comments intended to collect reached like: len(comments) > 1001
            response = service.commentThreads().list(
                part="snippet", 
                videoId = video_ID, 
                textFormat="plainText",
                pageToken=response['nextPageToken']
            ).execute()

        # if no response is received, break
        else:
            break

    # return the whole thing as a dict and the video title to calling function in run.py
    return dict({'Comment' : comments, 'Author' : authors, 'Comment ID' : commentsId, 'Like Count' : likesCount}), video_title
    