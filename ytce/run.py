'''
The file tha will actually be called directly to collect data
'''
import argparse
import comments_collector as cc

def get_comments(video_url, api_key_file, order = 'time', 
                   part = 'snippet', maxResults = 100):
    '''
    the function to fetch comments from the helper module
    '''
    # build the service for YT API
    yt_service = cc.build_service(api_key_file)

    # extract video id
    video_ID = cc.get_id(video_url)
    
    # get the comments
    comments_dict, title = cc.comments_helper(video_ID, api_key_file, yt_service)
    
    # save the output dict to storage as a csv file
    cc.save_to_csv(comments_dict, title + '.csv')
    
    print(f'Done for {video_url}.')



def main():
    ''' get the arguments '''
    # parser = argparse.ArgumentParser()

    # parser.add_argument('--video_url', required=True, help = 'Enter the video url')
    # parser.add_argument('--api_key_file', required=True, help = 'Enter the api key json file path+name')
    # parser.add_argument('--csv_filename', required=True, help = 'Enter the csv filename to save video to')

    # args = parser.parse_args()
    get_comments('https://www.youtube.com/watch?v=Lm7fb4zrz54', '../creds.json')


if __name__ == '__main__':
    main()







