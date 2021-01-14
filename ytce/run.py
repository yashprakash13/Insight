'''
The file tha will actually be called directly to collect data
'''
import sys
import comments_collector as cc
import constants

def get_comments(video_url, api_key_file, order = 'time', 
                   part = 'snippet', maxResults = 100):
    '''
    the function to fetch comments from the helper module for ONE video
    '''
    # build the service for YT API
    yt_service = cc.build_service(api_key_file)

    # extract video id
    video_ID = cc.get_id(video_url)
    
    # get the comments
    comments_dict, title = cc.comments_helper(video_ID, api_key_file, yt_service)
    
    # save the output dict to storage as a csv file
    cc.save_to_csv(comments_dict, title)
    
    print(f'Done for {video_url}.')



def main():
    ''' get the arguments '''

    api_key_path = constants.PATH_TO_API_KEY

    print(sys.argv[1:])
    
    #get_comments('https://www.youtube.com/watch?v=Lm7fb4zrz54', api_key_path)


if __name__ == '__main__':
    main()







