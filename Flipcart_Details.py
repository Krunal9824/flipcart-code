from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def information():
    driver=webdriver.Chrome("G:\driver\chromedriver.exe")
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    sleep(7)

    username=driver.find_element_by_xpath("//input[@class='_2zrpKA _1dBPDZ']")
    username.send_keys(9824039177)
    sleep(3)
    password=driver.find_element_by_xpath("//input[@class='_2zrpKA _3v41xv _1dBPDZ']")
    password.send_keys("kru@1490")
    sleep(3)

    login=driver.find_element_by_xpath(" //button[@class='_2AkmmA _1LctnI _7UHT_c']").click()

    sleep(3)


    actions=ActionChains(driver);

    electronics=driver.find_element_by_xpath("//span[text()='Electronics']")
    actions.move_to_element(electronics).perform()

    sleep(3)

    samsung=driver.find_element_by_xpath("(//a[@title='Samsung'])[1]") #(//a[@title='Samsung'])[1]
    actions.move_to_element(samsung).click().perform()

    sleep (3)

    link=driver.find_element_by_xpath("//a[contains(text(),'Samsung S9')]").click()
    sleep(3)

    title=driver.find_element_by_xpath("//span[@class='_35KyD6']")
    ratings=driver.find_element_by_xpath("//div[@class='hGSR34']")
    price=driver.find_element_by_xpath("//div[@class='_1vC4OE _3qQ9m1']")

    print(title.text)
    print(ratings.text)
    print(price.text)

    sleep(5)
  
information()