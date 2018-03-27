import requests
import json


def sentiment(text):
    documents = {'documents': [
        {'id': '1', 'language': 'en',
         'text': text}
    ]}

    subscription_key = "ce2e46b3f111441bb9327ec9fb43db16"
    assert subscription_key

    text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"

    sentiment_api_url = text_analytics_base_url + "sentiment"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}

    f = requests.Session()

    # response = requests.post(sentiment_api_url, headers=headers, json=documents)
    response = requests.post(sentiment_api_url, headers=headers, data=json.dumps(documents))
    sentiments = response.json()
    return dict(sentiments)['documents'][0]['score']
