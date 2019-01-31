'''
Created on 31-Jan-2019

@author: Ivavsys
'''
from generic.generic_utitlities_module import BaseTest
from generic.pages_module import HomePage

class Test(BaseTest):

    def __init__(self):
        self.initialize_web_environment()
        self.obj_home_page=HomePage(self)
        
    def test101(self):
        self.obj_home_page.click_input_text_forms()
    
    def tear_down(self):
        self.get_web_driver().quit()
        pass