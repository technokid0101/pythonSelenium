'''
Created on 31-Jan-2019

@author: Ivavsys
'''
from  SeleniumPython.src.pageFactory.locators_module import HomePageLocators

class HomePage:

    def __init__(self,obj_pojo):
        self.obj_pojo=obj_pojo
        self.obj_home_page_locators=HomePageLocators()

    def click_input_text_forms(self):
        obj_wrapper_function=self.obj_pojo.get_wrapper_function()
        text=obj_wrapper_function.click(self.obj_home_page_locators.txt_input_forms)
        flag=text.__contains__('Input Forms')

        if(flag):
            print("PASS")
        else:
            print("FAIL")