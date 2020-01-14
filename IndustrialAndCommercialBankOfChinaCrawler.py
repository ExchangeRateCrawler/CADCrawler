"""
工商银行加币汇率爬虫
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
        '<td.*?>加拿大元.*?</td>.*?(\d+.\d+)</td>.*?(\d+.\d+)</td>.*?(\d+.\d+)</td>.*?(\d+.\d+)</td><td.*?>(.*?)</td>',
        re.S)
    items = re.findall(pattern, html)
    # print(len(items))  # 结果应该是1的，如果不是1就是正则表达式出问题了
    item = items[0]
    # print(item)
    #  现汇买入    现钞买入   现汇卖出   现钞卖出   发布时间
    # ('524.91', '509.89', '528.80', '528.80', '2020年01月14日 16:09:16')
    return {
        'bank_name': '中国工商银行',
        'price': item[2],
        'update_time': item[4],
    }


def main():
    pass
    html_page = get_html_text('http://www.icbc.com.cn/ICBCDynamicSite/Optimize/Quotation/QuotationListIframe.aspx')
    industrial_and_commercial_bank_dictionary = parse_page(html_page)
    mail_content = industrial_and_commercial_bank_dictionary['bank_name'] + ' ' + \
                   industrial_and_commercial_bank_dictionary['price'] + ' ' + \
                   industrial_and_commercial_bank_dictionary['update_time']
    return mail_content
