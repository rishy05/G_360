import urllib.request
from newspaper import Article
import requests
import json
from pprint import pprint
from g_mail import auth_mail, send_mail
from summarizer import query
from scrapp import get_id, get_trans, get_txt
from urllib.parse import urlparse
from test import new


def get_cate(headl):
    api_key = "API KEY"
    model = "text-davinci-003"  # or any other model you prefer
    prompt = f"give me just the category of the news im giving you belongs to category 1'positive view on indian government' category2 'Neutral view on indian government' category 3 'Negative view on indian government. if it belongs to category 1 then return (positive) if it comes under category 2 then return (neutral) if it comes under category 3 then return (negative)'{headl}' just the category no extra words the response should just be the category. If it doesn't fit in any of the categories then return NONE"

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    data = {"model": model, "prompt": prompt, "temperature": 0.5, "max_tokens": 50}

    response = requests.post(
        "https://api.openai.com/v1/completions", headers=headers, data=json.dumps(data)
    )

    if response.status_code == 200:
        details = response.json()
        code = details["choices"][0]["text"]
        return code
    else:
        print(f"Error: {response.text}")


def get_dept(headl):
    api_key = "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"
    model = "text-davinci-003"  # or any other model you prefer
    prompt = f"give me which department of the indian government the news is talking about for example the news might talk about the ministry of railways wtc {headl}' just the category no extra words the response should just be the category. If it's not talking about any departments of indian government then return NONE"

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    data = {"model": model, "prompt": prompt, "temperature": 0.5, "max_tokens": 50}

    response = requests.post(
        "https://api.openai.com/v1/completions", headers=headers, data=json.dumps(data)
    )

    if response.status_code == 200:
        details = response.json()
        code = details["choices"][0]["text"]
        return code.strip()
    else:
        print(f"Error: {response.text}")


def get_yt(headl):
    api_key = "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"
    model = "text-davinci-003"  # or any other model you prefer
    prompt = f"give me just the category of captions of a youtube video you must categorise it into category 1'positive view on indian government' category2 'Neutral view on indian government' category 3 'Negative view on indian government. if it belongs to category 1 then return (positive) if it comes under category 2 then return (neutral) if it comes under category 3 then return (negative)'{headl}' just the category no extra words the response should just be the category. If it doesn't fit in any of the categories then return NONE"

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    data = {"model": model, "prompt": prompt, "temperature": 0.2, "max_tokens": 50}

    response = requests.post(
        "https://api.openai.com/v1/completions", headers=headers, data=json.dumps(data)
    )

    if response.status_code == 200:
        details = response.json()
        code = details["choices"][0]["text"]
        return code.strip()
    else:
        print(f"Error: {response.text}")


def parser(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    title = article.title

    meta_data = article.meta_data
    if "og" in meta_data:
        og_data = meta_data["og"]

        if "title" in og_data:
            headlines = og_data["title"]
        else:
            headlines = "Title not found in OG data"
    else:
        headlines = "OG data not found"

    info = [
        article.summary,
        article.authors,
        article.publish_date,
        article.source_url,
        title,
    ]
    return info


def extract_domain(url):
    parsed_url = urlparse(url)

    domain_parts = parsed_url.netloc.split(".")

    if domain_parts[0] == "www":
        domain_parts.pop(0)

    main_domain = ".".join(domain_parts[:-1])

    return main_domain
