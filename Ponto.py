# -*- encoding: utf-8 -*-
# Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Intra-imports
from driver import driver


username = ''
password = ''

class Ponto:
    def __init__(self, driver):
        self.driver = driver
        self.start()

    def __str__(self):
        return self.driver

    def start(self):
        self.paginaInicial()
        self.dashBoard()
        pass

    def paginaInicial(self):
        # Acessar painel de login
        print('PAGINA INICIAL')
        self.driver.get('https://meuportalrh.superbid.net/web/app/RH/PortalMeuRH/#/login')
       
        print('     Inserindo usuario e senha')
        # Insere user
        self.driver.waitForSelector(
            'body > app-root > div > div > app-login > div.po-sm-12.po-md-6.po-lg-6.po-xl-6.login-container > div.input.login-form > form > po-input > po-field-container > div > div.po-field-container-content > input').send_keys(username)
        
        # Insere senha
        self.driver.waitForSelector(
            'body > app-root > div > div > app-login > div.po-sm-12.po-md-6.po-lg-6.po-xl-6.login-container > div.input.login-form > form > po-password > po-field-container > div > div.po-field-container-content > input').send_keys(password)
        
        # Clica no botao de logon
        print('     Clicando no botao para logar')
        self.driver.waitForSelector('body > app-root > div > div > app-login > div.po-sm-12.po-md-6.po-lg-6.po-xl-6.login-container > div.input.login-form > form > po-button > button > span').click()
      
    pass

    def dashBoard(self):
        import time
        time.sleep(25)
        print('     Clicando no ponto')
        self.driver.waitForSelector('body > app-root > div > div > div.po-wrapper > po-menu > div.po-menu > nav > div > div > div:nth-child(3) > po-menu-item > div > div.po-menu-item.po-menu-icon-container.po-menu-item-grouper-down').click()
        time.sleep(1)
        print('     Clicando no relogio')
        self.driver.waitForSelector('body > app-root > div > div > div.po-wrapper > po-menu > div.po-menu > nav > div > div > div:nth-child(3) > po-menu-item > div > div.po-menu-sub-items > div:nth-child(3) > po-menu-item > a > div > div').click()
        time.sleep(1)
        
        print('     Clicando na circunferencia do ponto')
        drag = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#div-swipeButtonTextTip")))
        drop = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > div > div > div.po-wrapper > po-page-default > po-page > div > po-page-content > div > app-clocking-geo-register > div > div.div-clock.po-sm-12.po-md-12.po-lg-12.po-xl-12 > span.clock.po-sm-12.po-md-12.po-lg-12.po-xl-12")))
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()
        time.sleep(3)
        self.driver.close()
    pass