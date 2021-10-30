import re

content = 'Xiaoshuaib has 100 bananas'
res = re.findall('\d+', content)
print(res)
