'''
Created on 31-Jan-2019

@author: Ivavsys
'''
   
''' Home Page Locators Here '''
class HomePageLocators:
    '''Home Page Locators here'''
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

class LoginPageLocators:
    '''Login Page Locators Here '''