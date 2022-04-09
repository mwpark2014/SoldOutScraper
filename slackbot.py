from datetime import datetime
import logging
import json
import os
import requests

SLACK_WRITE_ENDPOINT = 'https://slack.com/api/chat.postMessage'

class SlackBot:
  def __init__(self):
    logging.basicConfig(filename='errors.log', level=logging.ERROR)
    if os.path.exists('subscribed_users.txt'):
      with open('subscribed_users.txt', 'r') as file:
        self.subscribed_users = set(file.readline().split(','))
    else:
      self.subscribed_users = set()

  def add_subscriber(self, user_id):
    self.subscribed_users.add(user_id)
    with open('subscribed_users.txt', 'w') as file:
      file.write(','.join(self.subscribed_users))
  
  def send_notification(self, message):
    BEARER_TOKEN = os.environ.get('SLACK_TOKEN')
    for user_id in self.subscribed_users:
      data = { 'text': message, 'channel': user_id}
      headers = { 'Authorization': f"Bearer {BEARER_TOKEN}" }
      response = requests.post(SLACK_WRITE_ENDPOINT, headers=headers, data=data)
      response_json = response.json()
      if response_json.get('error'):
        logging.error(f"[{datetime.now()}] Error encountered. Error message: {response_json['error']}, User_ID: {user_id}, Message: {message}")
    
