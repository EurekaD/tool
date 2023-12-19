
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


def txt_to_pdf(input_file):
    pdfmetrics.registerFont(TTFont('SimSun', r'simsun.ttc'))
    with open(input_file, 'r', encoding='utf-8') as txt_file:
        content = txt_file.read()
        print(content)
    output_file = input_file[:-4] + '.pdf'
    pdf = canvas.Canvas(output_file, pagesize=letter)
    pdf.setFont('SimSun', 12)
    pdf.drawString(100, 800, content)
    pdf.save()
    return output_file


def send_email(subject, body, to_emails, smtp_server, smtp_port, smtp_username, smtp_password, attachment_path):
    from_email = "chenlin_091@163.com"  # 发件人邮箱地址

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
        attachment_part.add_header('Content-Disposition', f'attachment;', filename=os.path.basename(attachment_path))
        msg.attach(attachment_part)

    print(os.path.basename(attachment_path))

    # 连接SMTP服务器并发送邮件
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, to_emails, msg.as_string())


if __name__ == "__main__":
    email_subject = "Convert"
    pdf_file_path = txt_to_pdf(r"C:\Users\23145\Desktop\test.txt")
    email_body = ""
    # to_email_address = ["chenlin_091_mX7ikd@kindle.cn"]
    to_email_address = ["2314590553@qq.com"]
    smtp_server_address = "smtp.163.com"
    smtp_server_port = 465
    smtp_username = "chenlin_091"
    smtp_password = "KZKHLXWCBDIMOQMZ"
    # 发送邮件并附加PDF文件
    send_email(email_subject, email_body, to_email_address, smtp_server_address, smtp_server_port, smtp_username,
               smtp_password, pdf_file_path)
