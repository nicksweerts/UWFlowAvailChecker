import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.text import MIMEText
import os

old_value1 = ""
old_value2 = ""

def scrape_and_send():
    url = "https://classes.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?level=under&sess=1251&subject=CLAS&cournum=202"  # Replace with your target website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    target_table = soup.find('table')
    all_tds = target_table.find_all('td')

    # We want to check td 12 and 13 to see if they have the same value.
    # If they don't, we want to send a text message.
    # YOU NEED TO REPLACE THIS WITH THE CORRECT INDEXES FOR YOUR CLASS' PAGE
    value = all_tds[12].text
    print(value)
    value2 = all_tds[13].text
    print(value2)

    if value != value2 and (old_value1 != value or old_value2 != value2):
        print("Values are different! Sending text message.")

        # Send an email (must get this password from creating an 'app' using your gmail account)
        # Get from env variables
        sender = os.environ.get('SENDER_EMAIL')
        password = os.environ.get('SENDER_PASSWORD')
        
        msg = MIMEText(f"The current value is: {value2}/ {value}")
        msg['Subject'] = "Website Update"
        msg['From'] = sender
        msg['To'] = os.environ.get('RECEIVER_EMAIL')
        
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender, password)
        smtp_server.send_message(msg)
        smtp_server.quit()

        return value, value2

    else:
        print("Values are the same.")
        return value, value2

while True:
    old_value1, old_value2 = scrape_and_send()
    time.sleep(30)