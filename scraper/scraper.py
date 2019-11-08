import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# URL link for NYC zoning
url = 'https://www1.nyc.gov/site/planning/zoning/access-text.page'
response = requests.get(url)
