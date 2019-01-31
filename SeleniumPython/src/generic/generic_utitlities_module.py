'''
Created on 31-Jan-2019
@author: Ivavsys
'''

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException,\
    ElementNotSelectableException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class Pojo:
    '''This class contains getters setters for required classes'''    
    def __init__(self):
        pass    

    def set_web_Driver(self,driver):
        self.driver=driver
    
    def get_web_driver(self):
        return self.driver
    
    def set_web_driver_wait(self,wait):
        self.wed_driver_wait=wait
    
    def get_web_driver_wait(self):
        return self.wed_driver_wait
    
    def set_wrappeer_function(self,obj_wrapper_function):
        self.obj_wrapper_function=obj_wrapper_function
    
    def get_wrapper_function(self):
        return self.obj_wrapper_function
        
class BaseTest(Pojo):
    '''This class is for initialization and termination of web driver'''
    def initialize_web_environment(self):
        '''This method is used for initialization of web driver'''
        self.obj_init_tear_down=initialize_tear_down_environment()
        self.driver=self.obj_init_tear_down.initialize_web_environment()
        self.set_web_Driver(self.driver)
        obj_wrapper_function=WrapperFunctions(self)
        self.set_wrappeer_function(obj_wrapper_function)
    def tear_down_web_environment(self):
        '''This method is used for termination of web driver and releasing all the resources'''
        self.driver.quit()
                
class WrapperFunctions:
    '''This class contains all the common methods required for web/application interaction eg.click'''
    def __init__(self,obj_pojo):
        self.obj_pojo=obj_pojo
    
    def click(self,locator):
        '''This method is used to click the element for provided locator'''
        try:
            element=self.get_element(locator)
            element.click()
        except Exception as exception:
            print("Caught An Exception for get element",exception)
        
    def get_element(self,locator):
        try:
            wait=WebDriverWait(self.obj_pojo.driver,30,poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,ElementNotInteractableException])
            element=wait.until(expected_conditions.presence_of_element_located((By.XPATH,locator)))
        except Exception as exception:
            print("Caught An Exception for get element",exception)
        return element
    
class initialize_tear_down_environment:
    
    def initialize_web_environment(self):
        '''This method initializes web driver and opens an instance of given web browser'''
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.seleniumeasy.com/test/')
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
        return self.driver

