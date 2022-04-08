from bs4 import BeautifulSoup
import requests
import argparse

class Scraper:
  def __init__(self, urls):
    self.urls = urls

  def grab_html():
    pass

  def parse_html():
    # soup = BeautifulSoup(fp, 'html.parser')
    pass

  def is_sold_out():
    pass

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Sold Out Scraper')
  parser.add_argument("-u", "--urls", nargs='+', help="URLs to scrape")
  scraper = Scraper()