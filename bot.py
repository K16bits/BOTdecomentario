from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

from user import nick,password

class BOT:
    def __init__(self,username,password,post='',comments=''):
        self.username = username
        self.password = password
        self.post = post
        self.comments = comments
        self.pathdrive = os.getcwd()+"\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path = self.pathdrive)

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
    
    def comment(self):
        driver = self.driver
        driver.get(self.post)
        driver.find_element_by_class_name("Ypffh").click()
        campo_comentar = driver.find_element_by_class_name("Ypffh")

        for i in range(4): ##Tamanho 
            campo_comentar.clear()
            campo_comentar.send_keys(self.comments)
            driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
            time.sleep(3)
    
    def logOff(self):
        drive = self.driver
        drive.get("https://www.instagram.com/"+self.username)
        time.sleep(1)
        clickPerfil = drive.find_element_by_class_name("_6q-tv")
        clickPerfil.click()
        # time.sleep(1)
        # clickSair = drive.find_element_by_xpath(r"//div[contains(text(),'Sair')]")
        # clickSair.click()


bot = BOT(nick,password,'','uou')
bot.login()
#bot.comment()
bot.logOff()
