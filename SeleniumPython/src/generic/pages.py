from selenium.webdriver.support.select import Select

class HomePage(object):        
    
    
    ''' Locators here'''
    
    txt_input_forms="(//a[@class='dropdown-toggle'])[1]"
    txt_simple_form_demo="(//a[text()='Simple Form Demo'])[1]"
    hdr_homepage="(//a[@title='Home'])[2]"
    inp_message="//input[@id='user-message']"
    btn_show_message="//button[text()='Show Message']"
    txt_message="//span[@id='display']"
    txt_select_day="(//a[text()='Select Dropdown List'])[1]"
    drp_select_days='select-demo'
    txt_selected_day="//p[@class='selected-value']"
    
    def __init__(self,driver):
        self.driver=driver
    
    def is_homepage_header_displayed(self):
        element=self.driver.find_element_by_xpath(self.hdr_homepage)
        if element.is_displayed():
            return True
        else:
            return False
    
    def set_text_to_messagebox(self,text):
        elment=self.driver.find_element_by_xpath(self.inp_message)
        elment.send_keys(text)
    
    def click_input_form_demo(self):
        element=self.driver.find_element_by_xpath(self.txt_input_forms)
        element.click()
    
    def click_simple_form_demo(self):
        element=self.driver.find_element_by_xpath(self.txt_simple_form_demo)
        element.click()
        
    def click_show_message_button(self):
        element=self.driver.find_element_by_xpath(self.btn_show_message)
        element.click()
        
    def get_text_of_txt_message(self):
        element=self.driver.find_element_by_xpath(self.txt_message)
        return element.text
    
    def select_day_from_drop_down(self,index):
        select=Select(self.driver.find_element_by_id(self.drp_select_days))
        select.select_by_index(index)
        element=self.driver.find_element_by_xpath(self.txt_selected_day)
        return element.text
    
    def click_select_dropdown_list(self):
        element=self.driver.find_element_by_xpath(self.txt_select_day)
        element.click()
    