import schedule
import time
import smtplib
from email.message import EmailMessage
from fetcher import fetch_api_data
import pandas as pd
import os
from getpass import getpass

PASSWORD = os.environ.get("EMAIL_PASSWORD")
if not PASSWORD:
    PASSWORD = getpass("Enter your email app password: ")

def download_data():
    print("📥 download data from API...")
    url = "https://catfact.ninja/fact"
    df = fetch_api_data(url, n=5)
    df.to_csv("fact_auto.csv", index=False)

    print("✅ the database saved in file - facts_auto.csv")
    return "fact_auto.csv"

def send_email(file_path):
    print("📧 sending email...")

    sender = "tftf9790tftf@gmail.com"
    password = PASSWORD
    recipient = "tftf9790tftf@gmail.com"

    msg = EmailMessage()
    msg["Subject"] = "Cat Fact today 🐱 "
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content("שלום! מצורף הקובץ עם העובדות החדשות שהבוט הוריד.")
    
    with open(file_path, "rb") as f:
        msg.add_attachment(f.read(), maintype = "text", subtype="csv", filename="facts_auto.csv")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

    print("✅ email sending")

def job():
    file_path = download_data()
    send_email(file_path)

schedule.every()day.at("09:00".do(job))

print("🤖 the bot is activate... (running once now)")
job()
print("✅ finished running once successfully!")

 while True:
    schedule.run_pending()
    time.sleep(1)