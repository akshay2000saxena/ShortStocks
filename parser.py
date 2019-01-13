import requests

url = 'https://api.diffbot.com/v3/article?token=eac77c2dca2a627f47278a19e38506a6&url=https://www.marketwatch.com/story/money-flows-show-netflix-amd-and-amazon-shares-may-rocket-on-good-news-2019-01-11'
json_data = requests.get(url).json()

result = json_data['objects'][0]['text']

print(result)