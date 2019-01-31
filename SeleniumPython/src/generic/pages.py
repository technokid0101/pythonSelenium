from selenium.webdriver.support.select import Select

class HomePage(object):        
    ''' Locators here'''
    txt_input_forms = "(//a[@class='dropdown-toggle'])[1]"
    txt_simple_form_demo = "(//a[text()='Simple Form Demo'])[1]"
    hdr_homepage = "(//a[@title='Home'])[2]"
    inp_message = "//input[@id='user-message']"
    btn_show_message = "//button[text()='Show Message']"
    txt_message = "//span[@id='display']"
    txt_select_day = "(//a[text()='Select Dropdown List'])[1]"
    drp_select_days = 'select-demo'
    txt_selected_day = "//p[@class='selected-value']"
    drp_multi_select = 'multi-select'
    btn_get_all_selected = 'printAll'
    txt_get_all_selected = 'getall-selected'
    
    lnk_date_pickers = "(//a[@class='dropdown-toggle'])[2]"
    lnk_bootstrap_date_picker = "(((//a[@class='dropdown-toggle'])[2]/following::ul)[1]//li)[1]"
    inp_bootstrap_date = "(//h4[text()=' Select Date']//following::input)[1]"
    btn_bootstrap_date = "(//span[@class='input-group-addon'])[1]"
    btn_switch = "//div[@class='datepicker-days']//th[@class='datepicker-switch']"
    btn_year = "//div[@class='datepicker-months']//th[@class='datepicker-switch']"
    btn_years = "//div[@class='datepicker-years']//td"
    btn_months = "//div[@class='datepicker-months']//td"
    btn_days = "//div[@class='datepicker-days']//table//tbody"
    
    lnk_table="(//a[@class='dropdown-toggle'])[3]"
    lnk_table_data_search="(//ul[@class='dropdown-menu'])[3]//li[2]"
    input_table_filter="//input[@id='task-table-filter']"
    
    
    def __init__(self, driver):
        self.driver = driver
    
    def is_homepage_header_displayed(self):
        element = self.driver.find_element_by_xpath(self.hdr_homepage)
        if element.is_displayed():
            return True
        else:
            return False
    
    def set_text_to_messagebox(self, text):
        elment = self.driver.find_element_by_xpath(self.inp_message)
        elment.send_keys(text)
    
    def click_input_form_demo(self):
        element = self.driver.find_element_by_xpath(self.txt_input_forms)
        element.click()
    
    def click_simple_form_demo(self):
        element = self.driver.find_element_by_xpath(self.txt_simple_form_demo)
        element.click()
        
    def click_show_message_button(self):
        element = self.driver.find_element_by_xpath(self.btn_show_message)
        element.click()
        
    def get_text_of_txt_message(self):
        element = self.driver.find_element_by_xpath(self.txt_message)
        return element.text
    
    def select_day_from_drop_down(self, index):
        select = Select(self.driver.find_element_by_id(self.drp_select_days))
        select.select_by_index(index)
        element = self.driver.find_element_by_xpath(self.txt_selected_day)
        return element.text
    
    def click_select_dropdown_list(self):
        element = self.driver.find_element_by_xpath(self.txt_select_day)
        element.click()
    
    def click_date_picker_link(self):
        element = self.driver.find_element_by_xpath(self.lnk_date_pickers)
        element.click()
    
    def click_bootstrap_date_picker(self):
        element = self.driver.find_element_by_xpath(self.lnk_bootstrap_date_picker)
        element.click()
    
    def click_date_picker(self):
        element = self.driver.find_element_by_xpath(self.btn_bootstrap_date)
        element.click()
    
    def multi_select_list_demo(self, li):
        '''Yet to be covered fully'''
        select = Select(self.driver.find_element_by_id(self.drp_multi_select))
        # element=self.driver.find_element_by_id(self.drp_multi_select)
        for x in li:
            select.select_by_value(x)

        element = self.driver.find_element_by_id(self.btn_get_all_selected)
        element.click()
        element = self.driver.find_element_by_class_name(self.txt_get_all_selected)
        text = element.text
        li = list(text.split(':'))
        print("Selected Options : ", li)
        
    def verify_bootstrap_date_picker(self, date):
        pass
    
    def get_table_data(self,row_index,column_index):
        table_locator="//table[@id='task-table']//tbody//tr["+str(row_index)+"]//td["+str(column_index)+"]"
        element=self.driver.find_element_by_xpath(table_locator)
        return element.text

    def click_table_link(self):
        element=self.driver.find_element_by_xpath(self.lnk_table)
        element.click()
    
    def click_table_search_link(self):
        element=self.driver.find_element_by_xpath(self.lnk_table_data_search)
        element.click()
        
    def set_table_filter_text(self,text):
        element=self.driver.find_element_by_xpath(self.input_table_filter)
        element.send_keys(text)
    
    
        