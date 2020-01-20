import smtplib
import time
from email.mime.text import MIMEText


def get_time():
    # 2020-01-14-11-58-41
    str_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    return {
        'str_time': str_time,
        'hour': str_time[11:13],
        'minute': str_time[14:16],
        'second': str_time[17:19],
    }


def send_email(mail_content, mail_subject, sender_email_address, sender_email_password, receiver_email_addresses,
               sender_mail_host, sender_mail_port):
    """
    发邮件函数
    :param mail_content: 邮件内容
    :param mail_subject: 邮件主题
    :param sender_email_address: 发送方邮箱地址
    :param sender_email_password: 发送方邮箱第三方授权码
    :param receiver_email_addresses: 所有接受方的邮箱地址列表
    :param sender_mail_host: SMTP服务器地址
    :param sender_mail_port: SMTP服务器端口
    :return:
    """
    # 邮件内容设置
    message = MIMEText(mail_content, 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = mail_subject
    # 发送方电子邮箱
    message['From'] = sender_email_address
    # 接收方电子邮箱
    message['To'] = receiver_email_addresses[0]
    print('From', message['From'])
    print('To', message['To'])

    try:
        # 登录并发送邮件
        smtp_obj = smtplib.SMTP_SSL(host=sender_mail_host)
        # 连接服务器 587为Outlook邮箱SMTP服务的端口号
        smtp_obj.connect(sender_mail_host, sender_mail_port)
        # print('111')
        # 登录到服务器
        smtp_obj.login(sender_email_address, sender_email_password)
        # print('222')
        # 发送
        smtp_obj.sendmail(sender_email_address, receiver_email_addresses[0], message.as_string())
        # print('333')
        # 退出
        smtp_obj.quit()
        print('From Utils: Mail Send Success!')
    except smtplib.SMTPException as e:
        print('From Utils: error', e)  # 打印异常信息
