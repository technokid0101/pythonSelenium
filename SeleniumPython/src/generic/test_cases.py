'''
Created on 29-Jan-2019

@author: Ivavsys
'''
from generic import pages
from selenium import webdriver
import unittest
import time

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
    
    def verify_mutli_select_list(self):
        '''Muilti Select List'''
        li=['California','Florida']
        self.obj_home_page.click_input_form_demo()
        self.obj_home_page.click_select_dropdown_list()
        self.obj_home_page.multi_select_list_demo(li)
    
    def verify_bootstrap_date_picker(self):
        self.obj_home_page.click_date_picker_link()
        self.obj_home_page.click_bootstrap_date_picker()
        self.obj_home_page.click_date_picker()
        self.obj_home_page.verify_bootstrap_date_picker('2019-01-29')
        
    def verify_table_filter_search(self):
        '''Handling Dynamic Table'''
        time.sleep(3) 
        self.obj_home_page.click_table_link()
        self.obj_home_page.click_table_search_link()
        li=["Wireframes","Landing Page"]
        for x in li:
            self.obj_home_page.set_table_filter_text(x)
            time.sleep(3)
            actual_text=self.obj_home_page.get_table_data(1, 2)
            print(x+"   "+actual_text)
            if x in actual_text:
                print("PASS")
            else:
                print("FAIL")
            self.driver.refresh()
        
    def _tearDown_(self):
        self.driver.quit()
        
    