import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://coinmarketcap.com/currencies/bitcoin/'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

def check_price():
	page = requests.get(URL, headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')

	coin_name = soup.find(attrs='cmc-details-panel-header__name').get_text()
	btc_price = soup.find(attrs='cmc-details-panel-price__price').get_text()
	converted_price = float(btc_price[1:7].replace(",", '.'))

	if (converted_price < 10.000):
		send_mail()

	print(coin_name.strip())
	print(converted_price)

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('youremail@gmail.com', 'yourpassword')
	subject = "Bitcoin price has fallen!"
	body = "It's time to buy more coins!"
	msg = f'Subject: {subject}\n\n{body}'

	server.sendmail(
		'mymail@gmail.com',
		'mymail@yahoo.com',
		msg
	)

	print("Email Sent!")
	server.quit()

check_price()