class person:
    def __init__(self,id,name,age,number):
        self.id=id
        self.name=name
        self.age=age 
        self.number=number
    
    def info(self):
        print("Person's information:")
        print(f"Id is:{self.id}\n Name is:{self.name}\n Age is:{self.age}\n Number is:{self.number}")

p1=person(11,"Neha Bhadoriya",27,123456)
p2=person(12,"Nidhi Bhadouriya",25,234567)

p1.info()
p2.info()



