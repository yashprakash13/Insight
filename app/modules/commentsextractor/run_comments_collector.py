'''
The file that will actually be called directly to collect data
'''
from .comments_collector import *
import constants

def get_comments(video_url, api_key_file, order = 'time', 
                   part = 'snippet', maxResults = 100):
    '''
    the function to fetch comments from the helper module for ONE video
    '''
    # build the service for YT API
    yt_service = build_service(api_key_file)

    # extract video id
    video_ID = get_id(video_url)
    
    # get the comments
    comments_dict, title = comments_helper(video_ID, api_key_file, yt_service)
    
    # save the output dict to storage as a csv file
    save_to_csv(comments_dict, title)
    
    # print(f'Done for {video_url}.')
    return title



def run(urls):
    ''' get the arguments '''

    api_key_path = constants.PATH_TO_API_KEY
    
    i = 1
    video_titles = []
    for url in urls:
        title = get_comments(url, api_key_path)
        # print(f'Done for video: {i}')
        i += 1
        video_titles.append(title)
    
    return video_titles








