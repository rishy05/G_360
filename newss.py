from co import get_cate, get_dept, parser
from g_mail import auth_mail, send_mail
from time import sleep
from summarizer import query
from test import new

auth_mail()


def ne(newss, m):
    d = []

    for i in newss:
        con = parser(i)
        # print((con))
        view = get_cate(con[0])
        dep = get_dept(con[0])
        try:
            print(
                f"\nSentiment of the article: {view}\n\nDepartment of government talked about: {dep}\n\nSOURCE: {con[-2]}\n\nAUTHOR: {con[1][0]}\n\nDATE PUBLISHED: {con[2]}\n\nARTICLE LINK: {i}"
            )
        except IndexError:
            print(
                f"\nSentiment of the article: {view}\n\nDepartment of government talked about: {dep}\n\nSOURCE: {con[-2]}\n\nAUTHOR: Not mentioned.\n\nDATE PUBLISHED: {con[2]}\n\nARTICLE LINK: {i}"
            )

        if view.strip() == "Negative":
            try:
                send_mail(
                    m,
                    "Negative News Alert from a news article",
                    f"""This message serves to alert the PIB officials to recent negative news coverage.\n\nSOURCE: {con[-2]}\n\nAUTHOR: {con[1][0]}\n\nDEPARTMENT OF GOVERNMENT TALKED ABOUT: {dep}\n\nDATE PUBLISHED: {con[2]}\n\nARTICLE LINK: {i}\n\nBRIEF SUMMARY: {con[0]}""",
                )
                print("\n\nMail sent to PIB official")
            except IndexError:
                send_mail(
                    m,
                    "Negative News Alert from a news article",
                    f"""This message serves to alert the PIB officials to recent negative news coverage.\n\nSOURCE: {con[-2]}\n\nAUTHOR: None\n\nDEPARTMENT OF GOVERNMENT TALKED ABOUT: {dep}\n\nDATE PUBLISHED: {con[2]}\n\nARTICLE LINK: {i}\n\nBRIEF SUMMARY: {con[0]}""",
                )
                print("\n\nMail sent to PIB official.")
                # source  #author    #date
    try:
        return [view, dep, con[-2], con[1][0], con[2]]
    except:
        return [view, dep, con[-2], con[2]]


# https://www.cnbctv18.com/economy/india-has-made-extraordinary-progress-in-its-g20-presidency-brazilian-president-lula-firstpost-exclusive-17765251.htm
# https://www.rediff.com/business/report/tech-more-bad-news-for--indian-it-sector/20230623.htm
# https://thewire.in/media/m20-india-press-freedom-g20-impunity-it-cell
# https://theworld.org/stories/2023-08-15/indian-women-do-less-paid-work-it-s-bad-news-economy
# https://www.thehindu.com/news/national/tamil-nadu/speaking-for-ine(dia-podcast-bjp-is-using-religion-as-a-weapon-to-hide-its-shortcomings-stalin-says/article67269005.ece
# https://religionnews.com/2023/08/09/violence-in-manipur-india/

ne(
    ["https://religionnews.com/2023/08/09/violence-in-manipur-india/"],
    "rishy69420@gmail.com",
)
