from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
class SeleniumInterfaceTest():
   def CreateConnection():
      options = webdriver.ChromeOptions()
      options.add_experimental_option("excludeSwitches", ["enable-logging"])
      options.add_experimental_option("detach", True)
      driver = webdriver.Chrome(options=options)
      return driver
   def CloseCinnection(self,connection):
      return connection.close()
   



def fastBattleTest(driver):
   try:
      driver.get("http://127.0.0.1:8000/")
      input_element = driver.find_element(By.ID,"fast_battle")
      if input_element:
         print(f"Элемент найден -> {input_element}")
         click_input_element = input_element.click()
         email_find = driver.find_element(By.ID, "TITLE")
         if (email_find):
            print(f"Найдена строка email -> {email_find}")
            email_find.send_keys("wastellplays@mail.ru")
            input_element = driver.find_element(By.ID,"submit-email").click()
      else:
         print("Элемент не найден")
   except Exception as Ex:
      print(f"Должно быть ошибка.. {Ex}")

def search_and_commentsTest(driver):
   try:
      driver.get("http://127.0.0.1:8000/")
      driver.find_element(By.ID,"site-search").send_keys("pikachu")
      driver.find_element(By.ID,"btn-search").click()
      driver.find_element(By.TAG_NAME,"a").click()
      driver.find_element(By.ID,"rating4").click()
      driver.find_element(By.ID,"email").send_keys('test@gmail.com')
      driver.find_element(By.ID,"TITLE").send_keys('Крутой покемон! Молния!')
      driver.find_element(By.ID,"btn-submt-comm").click()
   except Exception as Ex:
      print(f"Должно быть ошибка.. {Ex}")


def battleTest(driver):
   try:
      driver.get("http://127.0.0.1:8000/")
      driver.find_element(By.ID,"site-search").send_keys("slowpoke")
      driver.find_element(By.ID,"battle").click()
      driver.find_element(By.ID,"site-search").send_keys("2")
      driver.find_element(By.ID,"submit-battle-btn").click()
      sleep(10)
   except Exception as Ex:
      print(f"Должно быть ошибка.. {Ex}")

from selenium.webdriver.chrome.options import Options

driver = SeleniumInterfaceTest.CreateConnection()
#fastBattleTest(driver)
#search_and_commentsTest(driver)
battleTest(driver)
driver.close()