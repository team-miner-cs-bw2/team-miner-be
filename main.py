import time
import requests
import os


API_KEY = os.getenv("API_KEY")
MAIN_URL = os.getenv("URL")
NAME = os.getenv("NAME")
NEW_LOCATION = os.getenv("NEW_LOCATION")
ROOM_SPECIAL= os.getenv("ROOM_SPECIAL")

# testing .env if it's working
print('this is the API key', API_KEY);
print('this is the main url', MAIN_URL);
print('this is my name', NAME)
print('this is my new location', NEW_LOCATION)