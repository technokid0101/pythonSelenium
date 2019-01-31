"""
Created on 31-Jan-2019

@author: Ivavsys
"""
import SeleniumPython.src.pageFactory.locators_module


class HomePage:

    def __init__(self,obj_pojo):
        self.obj_pojo=obj_pojo
        self.obj_home_page_locators=SeleniumPython.src.pageFactory.locators_module.HomePageLocators()

    def click_input_text_forms(self):
        obj_wrapper_function=self.obj_pojo.get_wrapper_function()
        text=obj_wrapper_function.click(self.obj_home_page_locators.txt_input_forms)
        print(text)