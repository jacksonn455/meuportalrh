# Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# Intra-imports
from driver import driver
from Ponto import Ponto

def start(driver):
    step = Ponto(driver)
    driver = step.getDriver()

start(driver)