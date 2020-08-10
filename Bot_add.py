from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class BOT:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path = r"C:\ O diretorio\geckodriver.exe") # Colocar o diretorio do geckordriver

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        campo_user = driver.find_element_by_xpath(r"//input[@name='username']")
        campo_user.click()
        campo_user.send_keys(self.username)

        campo_pass = driver.find_element_by_xpath(r"//input[@name='password']")
        campo_pass.click()
        campo_pass.clear()
        campo_pass.send_keys(self.password)
        campo_pass.send_keys(Keys.RETURN)
        time.sleep(3)

        driver.get("")  # o link da publicação 
        driver.find_element_by_class_name("Ypffh").click()
        campo_comentar = driver.find_element_by_class_name("Ypffh")

        for i in range(4): ##Tamanho 
            campo_comentar.clear()
            campo_comentar.send_keys("Comentario")  ##Comentario a ser escrito 
            driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
            time.sleep(3)
    
kana = BOT("","") ## Usuario | senha 
kana.login()