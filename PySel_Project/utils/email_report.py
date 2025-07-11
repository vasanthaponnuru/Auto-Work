import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email_report(sender, password, recipient, smtp_server, smtp_port, report_path):
    msg = MIMEMultipart()
    msg['Subject'] = 'Automated Pytest Report'
    msg['From'] = sender
    msg['To'] = recipient

    msg.attach(MIMEText("Hi,\n\nFind the attached HTML test report.\n\nRegards,\nQA Automation", 'plain'))

    with open(report_path, 'rb') as f:
        report = MIMEApplication(f.read(), _subtype='html')
        report.add_header('Content-Disposition', 'attachment', filename='report.html')
        msg.attach(report)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender, password)
        server.send_message(msg)
