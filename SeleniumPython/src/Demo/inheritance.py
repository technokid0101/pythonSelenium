class Human(object):
    parent_='Human'
    height_=0
    wieght_=0
    def __init__(self):
        print("---------Human is a parent Class")
    
    def print_human_properties(self):
        pass

class Sushil(Human):
    def __init__(self):
        self.height_=5.2
        self.wieght_=50
        print("Sushil is also",self.parent_)

    def print_human_properties(self):
        print("Name : Sushil")
        print("Height :",str(self.height_)+" ft")
        print("Weight :",str(self.wieght_)+" kg")
        
class Rahul(Human):
    def __init__(self):
        self.height_=5.3
        self.wieght_=70
        print("Rahul is also",self.parent_)

    def print_human_properties(self):
        print("Name : Rahul")
        print("Height :",str(self.height_)+" ft")
        print("Weight :",str(self.wieght_)+" kg")

human_ins_parent=Human()
human_ins=Sushil()
human_ins.print_human_properties()
human_ins=Rahul()
human_ins.print_human_properties()

 

    
