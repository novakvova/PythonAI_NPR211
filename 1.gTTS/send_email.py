import asyncio
from aiosmtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

async def send_email():
    # Конфігурація
    smtp_server = "smtp.ukr.net"
    port = 2525
    sender_email = "super.novakvova@ukr.net"
    receiver_email = "novakvova@gmail.com"
    username = sender_email
    password = "lztIFOBL0IglRisS"

    # Створення повідомлення
    email_message = MIMEMultipart("mixed")
    email_message["From"] = sender_email
    email_message["To"] = receiver_email
    email_message["Subject"] = "Тестовий лист з Python через ukr.net"

    body = "<h3>Це тестовий лист, надісланий через SMTP сервер ukr.net з Python.</h3>"
    body_part = MIMEText(body, "html")
    email_message.attach(body_part)

    # Надсилання
    try:
        client = SMTP(hostname=smtp_server, port=port, use_tls=True)
        await client.connect()
        await client.login(username, password)
        await client.send_message(email_message)
        await client.quit()
        print("Лист успішно надіслано!")
    except Exception as e:
        print(f"Помилка при надсиланні EMAIL: {e}")

# Запуск
asyncio.run(send_email())
