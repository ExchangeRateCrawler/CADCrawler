"""
北京银行加币汇率爬虫
"""
import requests
import re
from Utils import get_time


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
        '<td>CAD/CNY</td>.*?<td>(\d+)</td><td>(\d+.\d+)</td><td>(\d+.\d+)</td><td>(\d+.\d+)</td><td>(\d+.\d+)</td><td>(\d+.\d+)</td>',
        re.S)

    items = re.findall(pattern, html)
    # print(len(items))  # 结果应该是1的，如果不是1就是正则表达式出问题了
    item = items[0]
    # print(item)
    # 报价单位  现汇买入  现钞买入    卖出价    中间价     基准价
    # ('100', '524.97', '512.33', '528.27', '526.62', '530.17')
    return {
        'bank_name': '北京银行',
        'price': item[3],
        'update_time': get_time()['str_time'],
    }


def main():
    html_page = get_html_text("http://www.bankofbeijing.com.cn/personal/whpj.aspx")
    bank_of_beijing_dictionary = parse_page(html_page)
    mail_content = bank_of_beijing_dictionary['bank_name'] + ' ' + bank_of_beijing_dictionary['price'] + ' ' + \
                   bank_of_beijing_dictionary['update_time']
    return mail_content
