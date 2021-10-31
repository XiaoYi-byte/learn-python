import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
response = requests.get('https://movie.douban.com/top250?start=0&filter=',headers=headers)
print(response)
