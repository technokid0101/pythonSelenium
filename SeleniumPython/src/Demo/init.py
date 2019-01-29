'''
Created on 28-Jan-2019

@author: Ivavsys
'''
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/')

if 'Selenium Easy' in driver.title:
        print("Pass")
        input_forms=driver.find_element_by_xpath("(//a[@class='dropdown-toggle'])[1]")
        input_forms.click()
        simple_form_demo=driver.find_element_by_xpath("(//a[text()='Simple Form Demo'])[1]")
        simple_form_demo.click()
        enter_message=driver.find_element_by_xpath("//input[@id='user-message']")
        enter_message.send_keys('test')
        show_message_button=driver.find_element_by_xpath("//button[text()='Show Message']")
        show_message_button.click()
        message=driver.find_element_by_xpath("//span[@id='display']")
        print('test' in message.text)
else:
        print("Fail")
        
driver.quit()



