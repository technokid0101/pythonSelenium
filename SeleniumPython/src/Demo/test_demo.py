# li=list(x for x in range(1,11))
# print(li)
# filter_=list(filter(lambda x:x%2==0,li))
# print("Filtered Even Numbers:-",filter_)
# filter_=list(filter(lambda  x:x%2!=0,li))
# print("Filtered Odd Numbers:-",filter_)
#
# test_list=['Sushil','Shubham','Abasaheb','Rahul','Gajanan']
# string_test1="SILENT"
# string_test2="LISTEN"
# print("".join(sorted(string_test1)))
# print("".join(sorted(string_test2)))
# print(sorted(test_list))
#
# g=(lambda x:list(i for i in range(x)))
# print(g(10))

dict_demo={'Name':'Sushil','Address':'Ahmednagar','Age':30,'Married':False}

for key,value in dict_demo.items():
    print(key,":",value)
