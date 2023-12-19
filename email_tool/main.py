# import fitz  # PyMuPDF
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os


# 读取PDF文件
# def read_pdf(file_path):
#     pdf_document = fitz.open(file_path)
#     text = ""
#     for page_number in range(pdf_document.page_count):
#         page = pdf_document[page_number]
#         text += page.get_text()
#     pdf_document.close()
#     return text

# 发送邮件
def send_email(subject, body, to_emails, smtp_server, smtp_port, smtp_username, smtp_password, attachment_path):
    from_email = "UIM@softline.sh.cn"  # 发件人邮箱地址

    # 设置邮件内容
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    # 添加邮件正文
    msg.attach(MIMEText(body, 'plain'))

    # 添加PDF文件附件
    with open(attachment_path, "rb") as attachment:
        attachment_part = MIMEBase('application', 'pdf')
        attachment_part.set_payload(attachment.read())
        encoders.encode_base64(attachment_part)
        #attachment_part.add_header('Content-Disposition', f'attachment; filename={attachment_path.split("/")[-1]}')
        attachment_part.add_header('Content-Disposition', f'attachment;', filename='未命名1.pdf')
        msg.attach(attachment_part)

    print(os.path.basename(attachment_path))

    # 连接SMTP服务器并发送邮件
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, to_emails, msg.as_string())


if __name__ == "__main__":
    # 本地PDF文件路径
    #pdf_file_path = "D:\软中\厦门项目\厦门三期\实时态推送\\20231215选举实时态第四期.pdf"

    pdf_file_path = r"C:\Users\RZ\OneDrive\桌面\未命名1.pdf"

    print(os.path.basename(pdf_file_path))

    #pdf_file_path = "D:\软中\厦门项目\厦门三期\委托民调\文件\厦门出差12月份.pdf"

    # 读取PDF文件内容
    # pdf_content = read_pdf(pdf_file_path)

    # 设置邮件参数
    email_subject = "20231215选举实时态第四期"
    # email_body = pdf_content
    email_body = """
    选举实时态（第四期）

    尊敬的老师，

    附件《20231215选举实时态第四期》为本次推送的选举结果。如有任何疑问或需要进一步信息，请随时告知，我将立即提供支持。

    感谢您的理解和支持。

    祝好，

    上海软中信息技术有限公司
    UIM@softline.sh.cn
    """

    to_email_address = ["dyj@softline.sh.cn"]

    # # SMTP服务器配置
    # smtp_server_address = "smtp.gmail.com"
    # smtp_server_port = 587
    # smtp_username = "your_email@gmail.com"
    # smtp_password = "your_email_password"
    #
    # # 发送邮件并附加PDF文件
    # send_email(email_subject, email_body, to_email_address, smtp_server_address, smtp_server_port, smtp_username, smtp_password, pdf_file_path)

    # SMTP服务器配置
    smtp_server_address = "smtp.exmail.qq.com"
    smtp_server_port = 587
    smtp_username = "UIM@softline.sh.cn"
    smtp_password = "1qaz2@WSX"

    # 发送邮件并附加PDF文件
    send_email(email_subject, email_body, to_email_address, smtp_server_address, smtp_server_port, smtp_username,
               smtp_password, pdf_file_path)
