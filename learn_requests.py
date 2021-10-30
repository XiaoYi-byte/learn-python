import requests

# get请求
r = requests.get('https://api.github.com/events')
# 获取服务器响应文本
r.text
# 获取字节响应内容
r.content
# 获取响应码
r.status_code
# 获取响应头
r.headers
# 获取 Json 响应内容
r.json()

# post请求
r = requests.post('https://httpbin.org/post', data={'key': 'value'})

# 其他请求
r = requests.put('https://httpbin.org/put', data={'key': 'value'})

r = requests.delete('https://httpbin.org/delete')

r = requests.head('https://httpbin.org/get')

r = requests.options('https://httpbin.org/get')

# 携带参数
payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.get('https://httpbin.org/get', params=payload)

# 假装是浏览器
url = 'https://api.github.com/some/endpoint'

headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)

