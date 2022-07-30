import requests
from requests.exceptions import HTTPError


# class Scraper:
#     def __init__():
#         self.url = ""
    
#     def get_response():



response = requests.get('https://realpython.com/python-requests/')
print(response.text)