import BankOfChinaCrawler
import ChinaMerchantBankCrawler
import IndustrialAndCommercialBankOfChinaCrawler
import ChinaConstructionBankCrawler
import BankOfBeijingCrawler
import ChinaEverBrightBankCrawler
from Utils import send_email
from Config import *

if __name__ == '__main__':
    print('正在爬取中国银行的汇率....')
    bank_of_china_content = BankOfChinaCrawler.main()
    print('Done.')

    print('正在爬取招商银行的汇率....')
    china_merchant_bank_content = ChinaMerchantBankCrawler.main()
    print('Done.')

    print('正在爬取中国工商银行的汇率....')
    industrial_and_commercial_bank_content = IndustrialAndCommercialBankOfChinaCrawler.main()
    print('Done.')

    print('正在爬取建设银行的汇率....')
    china_construction_bank_content = ChinaConstructionBankCrawler.main()
    print('Done.')

    print('正在爬取北京银行的汇率....')
    bank_of_beijing_content = BankOfBeijingCrawler.main()
    print('Done.')

    print('正在爬取光大银行的汇率....')
    china_ever_bright_bank_content = ChinaEverBrightBankCrawler.main()
    print('Done.')

    mail_content = bank_of_china_content + '\n' + china_merchant_bank_content + '\n' + industrial_and_commercial_bank_content + '\n' + china_construction_bank_content + '\n' + bank_of_beijing_content + '\n' + china_ever_bright_bank_content
    send_email(mail_content=mail_content, mail_subject=mail_subject, sender_email_address=sender_email_address,
               sender_email_password=sender_email_password, receiver_email_addresses=receiver_email_addresses,
               sender_mail_host=sender_mail_host, sender_mail_port=sender_mail_port)

    # while True:
    #     time_dictionary = get_time()
    #     current_hour = time_dictionary['hour']
    #     current_minute = time_dictionary['minute']
    #     current_second = time_dictionary['second']
    #     # 每20分钟爬取一次
    #     if int(current_minute) % 20 == 0 and int(current_second) % 60 == 0:
    #         # 开始爬取
    #         # print('hello', current_hour + '-' + current_minute + '-' + current_second)
    #         time.sleep(1)
    #         html_page = get_html_text("https://www.boc.cn/sourcedb/whpj/")
    #         china_bank_dictionary = parse_page(html_page)
    #         mail_host = 'smtp.163.com'
    #         mail_port = 25
    #         mail_user = 'buctyukangyin'
    #         mail_pwd = '13693221019Yinyk'  # 从第三方登录的授权码
    #         sender_email_address = 'buctyukangyin@163.com'
    #         receivers_email_address = ['buctyukangyin@163.com']  # 自己给自己发
    #
    #         mail_content = china_bank_dictionary['bank_name'] + ' ' + china_bank_dictionary['price'] + ' ' + \
    #                        china_bank_dictionary['update_time']
    #
    #         send_email(mail_content=mail_content, mail_host=mail_host, mail_port=mail_port, mail_user=mail_user,
    #                    mail_pwd=mail_pwd,
    #                    sender_email_address=sender_email_address, receivers_email_address=receivers_email_address)
