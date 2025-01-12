import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import service as chromeService
from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(service=ChromeDriverManager().install())

def test_Prueba():
    driver.get('https://www.youtube.com/watch?v=yC-t-LX7Hvs')
    titulo = driver.title
    assert titulo == 'ghsjsj'
