from bs4 import BeautifulSoup
import requests


def set_up():
    
    site = requests.get("http://127.0.0.1:8000/").text
    soup = BeautifulSoup(site,"html.parser")
    return soup