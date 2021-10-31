from bs4 import BeautifulSoup

html_doc = """

<html><head><title>学习python的正确姿势</title></head>
<body>
<p class="title"><b>小帅b的故事</b></p>

<p class="story">有一天，小帅b想给大家讲两个笑话
<a href="http://example.com/1" class="sister" id="link1">一个笑话长</a>,
<a href="http://example.com/2" class="sister" id="link2">一个笑话短</a> ,
他问大家，想听长的还是短的？</p>

<p class="story">...</p>

"""

soup = BeautifulSoup(html_doc,'lxml')

# 获取标题的内容
print(soup.title.string)
# 获取 p 标签里面的内容
print(soup.p.string)
# 获取 title 的父级标签
print(soup.title.parent.name)
# 获取超链接
print(soup.a)
# 获取所有超链接
print(soup.find_all('a'))
# 获取 id 为 link2 的超链接
print(soup.find(id="link2"))
# 获取网页中所有的内容
print(soup.get_text())

# select
print(soup.select("title"))
print(soup.select("body a"))
print(soup.select("p > #link1"))
