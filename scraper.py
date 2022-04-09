from bs4 import BeautifulSoup
import requests
import argparse
from slackbot import SlackBot

parser = argparse.ArgumentParser(description='Sold Out Scraper')
parser.add_argument("-u", "--urls", nargs='+', help="URLs to scrape")

class Scraper:
  def __init__(self, urls):
    self.urls = urls
    self.slackbot = SlackBot()

  def check_urls(self):
    page_by_url = self.grab_html()
    for url in self.parse_html(page_by_url):
      self.slackbot.send_notification(f'{url} is no longer out of stock!')

  def grab_html(self):
    page_by_url = {}
    for url in self.urls:
      page_by_url[url] = requests.get(url)
    return page_by_url

  def parse_html(self, page_by_url:dict):
    outputs = []
    for url, page in page_by_url.items():
      soup = BeautifulSoup(page.content, 'html.parser')
      if not self.is_sold_out(soup):
         outputs.append(url)
    return outputs

  def is_sold_out(self, soup):
    sold_out_spans = soup.find_all('span', class_='productlabel soldout')
    return bool(sold_out_spans)

if __name__ == '__main__':
  args = parser.parse_args()
  scraper = Scraper(args.urls)
  scraper.check_urls()