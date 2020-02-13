import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/dp/B07DJHXTLJ?pf_rd_p=fa25496c-7d42-4f20-a958-cce32020b23e&pf_rd_r=7XT1692ENQR22ZWHT0VZ'

headers = {"User-agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'}

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id = "productTitle").get_text()

price = soup.find(id="priceblock_dealprice").get_text()

print(title.strip())

sep ='.'
con_price = price.split(sep, 1)[0]
print(con_price)
con_price = con_price.strip("₹")
print(con_price)
converted_price = int(con_price.replace(',',''))

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()

    server.starttls()

    server.ehlo()

    server.login('killershaina@gmail.com', 'killershaina')

    subject = 'price fell down!'

    body = 'check the link: https://www.amazon.in/dp/B07DJHXTLJ?pf_rd_p=fa25496c-7d42-4f20-a958-cce32020b23e&pf_rd_r=7XT1692ENQR22ZWHT0VZ'

    msg = f'Subject:{subject}\n\n{body}'

    server.sendmail('Price check', 'killershaina@gmail.com', msg)

    print('hey email sent')

    server.quit()


if converted_price < 35000:
    send_mail()
else:
    print("nochange")


