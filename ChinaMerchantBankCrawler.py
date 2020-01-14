"""
招商银行加币汇率爬虫
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
    pattern = re.compile(
        '<tr>.*?加拿大元.*?</td>.*?(\d+).*?(\d+.\d+).*?(\d+.\d+).*?(\d+.\d+).*?(\d+.\d+).*?(\d+:\d+:\d+)',
        re.S)
    items = re.findall(pattern, html)
    # print(len(items))  # 结果应该是1
    item = items[0]
    # print(item)
    # 交易币单位 现汇卖出   现钞卖出   现汇买入   现钞买入   时间
    # ('100', '528.74', '528.74', '524.52', '507.93', '13:48:19')
    return {
        'bank_name': '招商银行',
        'price': item[1],
        'update_time': item[5]
    }


def main():
    html_text = get_html_text('http://fx.cmbchina.com/hq/')
    china_merchant_bank_dictionary = parse_page(html_text)
    mail_content = china_merchant_bank_dictionary['bank_name'] + ' ' + china_merchant_bank_dictionary['price'] + ' ' \
                   + china_merchant_bank_dictionary['update_time']
    return mail_content
