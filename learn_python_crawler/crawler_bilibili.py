import xlwt
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.binary_location = "D:\Google\chrome\Application\chrome.exe"
chrome_driver_binary = "D:\Google\chrome\Application\chromedriver"
chrome_service = Service(executable_path=chrome_driver_binary)
driver = webdriver.Chrome(service=chrome_service, options=options)
WAIT = WebDriverWait(driver, 10)
driver.set_window_size(1400, 900)

book = xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet = book.add_sheet('蔡徐坤篮球', cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
sheet.write(0, 1, '地址')
sheet.write(0, 2, '描述')
sheet.write(0, 3, '观看次数')
sheet.write(0, 4, '弹幕数')
sheet.write(0, 5, '发布时间')

n = 1


def search():
    driver.get('https://www.bilibili.com/')
    input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#nav-searchform > input')))
    submit = WAIT.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-searchform"]/div')))

    # 登录选项会挡住搜素框，搜索之前刷新一下
    # refresh = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    #                                                  '#i_cecream > div.bili-header.large-header > div.bili-header__bar > ul.left-entry > li:nth-child(1)')))
    # refresh.click()
    input.send_keys('蔡徐坤 篮球')
    submit.click()
    # 跳转到新的窗口
    print('跳转到新窗口')
    all_h = driver.window_handles
    driver.switch_to.window(all_h[1])
    get_resource()
    total = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#all-list > div.flow-loader > div.page-wrap > div > ul > li.page-item.last > button')))
    return int(total.text)


def save_to_excel(soup):
    list = soup.find(class_='video-list').find_all(class_='info')

    for item in list:
        item_title = item.find('a').get('title')
        item_link = item.find('a').get('href')
        item_dec = item.find(class_='des hide').text
        item_view = item.find(class_='so-icon watch-num').text
        item_biubiu = item.find(class_='so-icon hide').text
        item_date = item.find(class_='so-icon time').text

        print('爬取：' + item_title)

        global n

        sheet.write(n, 0, item_title)
        sheet.write(n, 1, item_link)
        sheet.write(n, 2, item_dec)
        sheet.write(n, 3, item_view)
        sheet.write(n, 4, item_biubiu)
        sheet.write(n, 5, item_date)

        n = n + 1


def get_resource():
    WAIT.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#all-list > div.flow-loader')))
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    save_to_excel(soup)


def next_page(page_num):
    try:
        print('获取下一页数据')
        next_btn = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                          '#all-list > div.flow-loader > div.page-wrap > div > ul > li.page-item.next > button')))
        next_btn.click()
        WAIT.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                     '#all-list > div.flow-loader > div.page-wrap > div > ul > li.page-item.active > button'),
                                                    str(page_num)))
        get_resource()
    except TimeoutException:
        driver.refresh()
        return next_page(page_num)


def main():
    try:
        total = search()
        print(total)
        for i in range(2, int(total + 1)):
            next_page(i)
    finally:
        driver.close()


if __name__ == '__main__':
    main()
    book.save('bilibili1.xlsx')
