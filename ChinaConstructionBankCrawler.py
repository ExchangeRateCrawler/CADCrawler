"""
建行加币汇率爬虫
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
    """
    <BidRateOfCash>5.0974</BidRateOfCash>
<OfrRateOfCash>5.287</OfrRateOfCash>
<BidRateOfCcy>5.2475</BidRateOfCcy>
<OfrRateOfCcy>5.287</OfrRateOfCcy>
<LstPr_Dt>20200114</LstPr_Dt>
<LstPr_Tm>162802</LstPr_Tm>
    :param html:
    :return:
    """
    pattern = re.compile(
        '<ReferencePriceSettlement name="7">.*?<BidRateOfCash>(\d+.\d+)</BidRateOfCash>.*?<OfrRateOfCash>(\d+.\d+)</OfrRateOfCash>'
        '.*?<BidRateOfCcy>(\d+.\d+)</BidRateOfCcy>.*?<OfrRateOfCcy>(\d+.\d+)</OfrRateOfCcy>.*?<LstPr_Dt>(\d+)</LstPr_Dt>'
        '.*?<LstPr_Tm>(\d+)</LstPr_Tm>',
        re.S)
    items = re.findall(pattern, html)
    # print(len(items))  # 结果应该是1的，如果不是1就是正则表达式出问题了
    item = items[0]
    # print(item)
    #  现钞买入   现汇卖出   现汇买入   现钞卖出  发布时间
    # ('5.0974', '5.287', '5.2475', '5.287', '20200114', '164404')
    # 2020-01-14 16:48:04
    # print(item[4][0:4] + '-' + item[4][4:6] + '-' + item[4][6:8] + ' ' + item[5][0:2] + ':' + item[5][2:4] + ':' + item[5][4:6])
    return {
        'bank_name': '中国建设银行',
        'price': item[1],
        'update_time': item[4][0:4] + '-' + item[4][4:6] + '-' + item[4][6:8] + ' ' + item[5][0:2] + ':' + item[5][2:4] + ':' + item[5][4:6],
    }


def main():
    html_page = get_html_text("http://forex1.ccb.com/cn/home/news/jshckpj_new.xml")
    china_construction_bank_dictionary = parse_page(html_page)
    mail_content = china_construction_bank_dictionary['bank_name'] + ' ' + china_construction_bank_dictionary['price'] + ' ' + \
                   china_construction_bank_dictionary['update_time']
    return mail_content
