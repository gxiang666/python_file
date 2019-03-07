import requests
from bs4 import BeautifulSoup


def get_page(url):
	headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36"
	}
	res = requests.get(url, headers=headers)
	return res.text


def main(start_url):
	