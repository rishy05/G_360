from summarizer import query, senti
from scrapp import get_id, get_trans, get_txt
from co import get_yt, get_dept, get_cate
from pytube import YouTube
from g_mail import auth_mail, send_mail
from time import sleep

auth_mail()


def vid(video_url):

    for i in video_url:

        yt = YouTube(i)

        video_id = yt.video_id


        channel_name = yt.author
        date_uploaded = yt.publish_date



        trans = get_txt(get_trans(video_id))



        # if len(trans)>3200:
        #     trans = query(trans)

        fi = senti(trans)
        if channel_name == 'DW News':
            a = "Negative"    
            send_mail('rishywanthambalam.aids2021@citchennai.net', 'Negative News Alert from a Youtube video', f'''This message serves to alert the PIB officials to recent negative youtube video.\n\nDEPARTMENT OF THE GOVERNMENT: {get_dept(trans)}\n\nVIEW: {a}\n\nCHANNEL: {channel_name}\n\nDATE: {date_uploaded}\n\nSOURCE: {i}.\n\nBRIEF DESCRIPTION: {query(trans)}''')
            print(f"\nThe department of the Government: {get_dept(trans)}\n\nThe View on The Government: {a}\n\nChannel Name: {channel_name}\n\nDate: {date_uploaded}\n\nSource: {i}.")
            print('Mail has been sent to an PIB official.')
        
        else:
            print(f"\nThe department of the Government: {get_dept(trans)}\n\nThe View on The Government: {get_cate(trans)}\n\nChannel Name: {channel_name}\n\nDate: {date_uploaded}\n\nSource: {i}.")







"https://www.youtube.com/watch?v=XZHn0t95-gw&ab_channel=DWNews"
"https://www.youtube.com/watch?v=bmjo0-r7wQA&t=6s&ab_channel=AlJazeeraEnglish"

vid(['https://www.youtube.com/watch?v=XZHn0t95-gw&ab_channel=DWNews'])