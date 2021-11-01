import requests
import xlwt
from bs4 import BeautifulSoup


def request_douban(url, headers):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_result(soup, sheet, page):
    list = soup.find(class_='grid_view').find_all('li')

    for index, item in enumerate(list):
        item_name = item.find(class_='title').string
        item_img = item.find('a').find('img').get('src')
        item_index = item.find(class_='').string
        item_score = item.find(class_='rating_num').string
        item_author = item.find('p').text
        item_intr = item.find(class_='inq').string if item.find(class_='inq') is not None else ''

        # print('爬取电影：' + item_index + ' | ' + item_name +' | ' + item_img +' | ' + item_score +' | ' + item_author
        # +' | ' + item_intr )
        print('爬取电影：' + item_index + ' | ' + item_name + ' | ' + item_score + ' | ' + item_intr +' | ' + item_author)
        sheet.write(page * 25 + index + 1, 0, item_name)
        sheet.write(page * 25 + index + 1, 1, item_img)
        sheet.write(page * 25 + index + 1, 2, item_index)
        sheet.write(page * 25 + index + 1, 3, item_score)
        sheet.write(page * 25 + index + 1, 4, item_author)
        sheet.write(page * 25 + index + 1, 5, item_intr)


def main(page, sheet):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    url = 'https://movie.douban.com/top250?start=' + str(page * 25) + '&filter='
    html = request_douban(url, headers)
    soup = BeautifulSoup(html, 'lxml')
    parse_result(soup, sheet, page)


if __name__ == '__main__':
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('豆瓣电影top250', cell_overwrite_ok=True)
    sheet.write(0, 0, '名称')
    sheet.write(0, 1, '图片')
    sheet.write(0, 2, '排名')
    sheet.write(0, 3, '评分')
    sheet.write(0, 4, '作者')
    sheet.write(0, 5, '简介')
    for i in range(10):
        main(i, sheet)
    book.save('movie.xls')

