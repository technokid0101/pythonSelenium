'''
Created on 29-Jan-2019

@author: Ivavsys
'''
from generic import test_cases

obj_test=test_cases.TestCases()
obj_test._setup_()

print("-----TEST CASE:"+obj_test.verify_homapge_displayed.__doc__)
obj_test.verify_homapge_displayed()
print("-----TEST CASE:"+obj_test.verify_message_functionality.__doc__)
obj_test.verify_message_functionality()
print("-----TEST CASE:"+obj_test.verify_selected_day.__doc__)
obj_test.verify_selected_day()

obj_test._tearDown_()