'''
Created on 29-Jan-2019

@author: Ivavsys
'''
from generic import pages
from selenium import webdriver
import unittest

class TestCases(unittest.TestCase):
       
    def _setup_(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.seleniumeasy.com/test/')
        self.driver.maximize_window()
        self.obj_home_page=pages.HomePage(self.driver)
        
    def verify_homapge_displayed(self):
        '''Home Page Verification Test'''
        if self.obj_home_page.is_homepage_header_displayed():
            print("PASS")
        else:
            print("FAIL") 
    
    def verify_message_functionality(self):
        '''Message Functionality Test'''
        text="test"
        self.obj_home_page.click_input_form_demo()
        self.obj_home_page.click_simple_form_demo()
        self.driver.implicitly_wait(3)
        self.obj_home_page.set_text_to_messagebox(text)
        self.obj_home_page.click_show_message_button()
        if text in self.obj_home_page.get_text_of_txt_message():
            print("PASS")
        else:
            print("FAIL")
                
    def verify_selected_day(self):
        '''Drop down test'''
        text='Sunday'
        index=1
        self.obj_home_page.click_input_form_demo()
        self.obj_home_page.click_select_dropdown_list()
        if text in self.obj_home_page.select_day_from_drop_down(index):
            print("PASS")
        else:
            print("FAIL")
        

    def _tearDown_(self):
        self.driver.quit()
        
    