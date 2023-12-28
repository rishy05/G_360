from co import parser, get_dept, extract_domain
from summarizer import senti, query
import datetime
import pytz
import pandas as pd
from g_mail import auth_mail, send_file, send_mail


#[article.summary, article.authors, article.publish_date, article.source_url]
auth_mail()

def rep(arti):
    df = pd.DataFrame()
    key_wo = []
    cat = []
    com = []
    auth = []
    li = []
    summ = []


    for j in arti:
        m = 1
        c = parser(j)

        k_w = c[-1]
        sent = senti(c[0])
        comp = extract_domain(j)
        au = c[1]
        ll = j
        su = c[0]


        key_wo.append(k_w)
        cat.append(sent)
        com.append(comp)
        auth.append(au)
        li.append(ll)
        summ.append(su)
        
    for i in summ:
        i = query(query(i))

    df['KEYWORDS'] = key_wo
    df['SENTIMENT'] = cat
    df['COMPANY'] = com
    df['AUTHOR'] = auth
    df['ARTICLE LINK'] = li
    df['SUMMARY OF THE ARTICLE'] =  summ
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    nam = f"{current_time.day}_{current_time.month}_{current_time.year}.xlsx"
    df.to_excel(nam, index = False)

    send_file('rishywanthambalam.aids2021@citchennai.net', 'REPORT FOR TODAY', '', nam)
    print('mail sent')


rep(['https://www.cnbctv18.com/economy/india-has-made-extraordinary-progress-in-its-g20-presidency-brazilian-president-lula-firstpost-exclusive-17765251.htm',
'https://www.rediff.com/business/report/tech-more-bad-news-for--indian-it-sector/20230623.htm',
'https://thewire.in/media/m20-india-press-freedom-g20-impunity-it-cell',
'https://theworld.org/stories/2023-08-15/indian-women-do-less-paid-work-it-s-bad-news-economy',
'https://www.thehindu.com/news/national/tamil-nadu/speaking-for-india-podcast-bjp-is-using-religion-as-a-weapon-to-hide-its-shortcomings-stalin-says/article67269005.ece',
'https://religionnews.com/2023/08/09/violence-in-manipur-india/'])