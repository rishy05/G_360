#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

import requests
import json
from newspaper import Article

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}

API_URL_1 = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers_1 = {"Authorization": "Bearer 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"}

def senti(payload):
	for i in payload:
		data = json.dumps(i)
		response = requests.post(API_URL_1, headers=headers_1, data = data)
		contn = response.json()
		return contn[0][0]['label']

# def parser(url):
#     article = Article(url)
#     article.download()
#     article.parse()
#     article.nlp()
#     info = [article.summary, article.authors, article.publish_date, article.source_url]
#     return info

def query(payload):
	data = json.dumps(payload)
    
	response = requests.post(API_URL, headers=headers, data = data)
	contn = response.json()
	return contn[0]['summary_text']


# print(senti(parser("https://www.ndtv.com/india-news/prince-salman-state-visit-g20-pm-meets-saudi-crown-prince-today-trade-connectivity-defence-on-agenda-4378507")[0]))
	