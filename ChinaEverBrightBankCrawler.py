"""
中国光大银行加币汇率爬虫
"""
import requests
import re


def get_html_text(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('爬取失败')
        return None


def parse_page(html):
    # print(html)
    pattern = re.compile(
        '<td.*?>.*?加拿大元\(CAD\)</td>.*?(\d+.\d+)</td>.*?(\d+.\d+)</td>.*?(\d+.\d+)</td>.*?(\d+.\d+)</td>',
        re.S)
    items = re.findall(pattern, html)
    # print(len(items))  # 结果应该是1
    item = items[0]
    # print(item)
    #  购汇汇率      购钞汇率     结汇汇率     结钞汇率
    # ('527.2085', '527.2085', '523.0077', '506.2042')

    pattern2 = re.compile('更新时间:(.*?)</span>', re.S)
    items2 = re.findall(pattern2, html)
    # print(len(items2))  # 结果应该是1
    item2 = items2[0]
    # print(item2)
    # 2020-01-18 07:00
    return {
        'bank_name': '光大银行',
        'price': item[0],
        'update_time': item2,
    }


def main():
    html_text = get_html_text('http://www.cebbank.com/eportal/ui?pageId=477257')
    china_ever_bright_bank_dictionary = parse_page(html_text)
    mail_content = china_ever_bright_bank_dictionary['bank_name'] + ' ' + china_ever_bright_bank_dictionary['price'] + ' ' \
                   + china_ever_bright_bank_dictionary['update_time']
    return mail_content
