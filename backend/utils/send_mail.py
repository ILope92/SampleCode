import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version
from backend.database.crud import CRUD_USER
from backend.config import NAME_SERVICE, SERVER_SMPT, EMAIL, PASSWORD, HOST_URL
from jinja2 import Template, Environment, FileSystemLoader
from backend.schemas.users import Registration


async def send_email(emails: str, data: Registration):
    subject = f"Активация аккаунта на сервисе {NAME_SERVICE}"
    file_loader = FileSystemLoader("data\emails")
    env = Environment(loader=file_loader)
    template = env.get_template("simple.html")
    HTML = template.render(
        first_name=data.first_name,
        last_name=data.last_name,
        activate=f"{HOST_URL}api/accounts/activate/?email={data.email}",
        email=EMAIL,
    )
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = "Python script <" + EMAIL + ">"
    msg["To"] = ", ".join([emails])
    msg["Reply-To"] = EMAIL
    msg["Return-Path"] = EMAIL
    msg["X-Mailer"] = "Python/" + (python_version())

    part_html = MIMEText(HTML, "html")
    msg.attach(part_html)
    mail = smtplib.SMTP_SSL(SERVER_SMPT)
    mail.login(EMAIL, PASSWORD)
    mail.sendmail(EMAIL, [emails], msg.as_string())
    mail.quit()
