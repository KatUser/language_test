import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_language_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    cart_button = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#add_to_basket_form > button')))
    assert browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form > button').size != 0, f'No cart found'


