from youtube_transcript_api import YouTubeTranscriptApi
from pprint import pprint
import re

def get_id(link):
    # Define a regular expression pattern to match the video ID
    pattern = r'v=([a-zA-Z0-9_-]+)'

    # Use re.search to find the video ID
    match = re.search(pattern, link)

    if match:
        video_id = match.group(1)
        return video_id
    else:
        return None




def get_trans(cod):

    srt = YouTubeTranscriptApi.get_transcript(cod)
    
    return(srt)


def get_txt(input_list):
    text_list = []  # Initialize an empty list to store the 'text' values

    # Iterate through the dictionaries in the input list
    for dictionary in input_list:
        if 'text' in dictionary:
            text_list.append(dictionary['text'])
    fi = ' '.join(text_list)

  
    res = ''.join(map(str, fi))


    return res
    


# print(get_txt(get_trans(get_id('https://www.youtube.com/watch?v=bmjo0-r7wQA&ab_channel=AlJazeeraEnglish'))))   

