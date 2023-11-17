from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/.../.../chromedriver.exe')
driver.get("http://127.0.0.1:8000/")
input_username = driver.find_element_by_id("user-name")
if input_username is None:
   print("Элемент не найден")
else:
   print("Элемент найден")