class Animal:
    def __init__(self,name,age,health,happiness):
        self.name=name
        self.age=age
        self.health=health
        self.happiness=happiness
    def display_info(self):
        print(f"Name: {self.name}, Health: {self.health}, Happiness: {self.happiness}")
    def feed(self):
        self.health+=10
        self.happiness+=10
        

class Lions(Animal):
    def __init__(self,name,age,health=50,happiness=10):
        super().__init__(name,age,health,happiness)
    def feed(self):
        self.health+=5
        if self.health+5>100:
            self.health=100
        self.happiness+=5
        if self.happiness+5>100:
            self.happiness=100

class Tigers(Animal):
    def __init__(self,name,age,health=90,happiness=90):
        super().__init__(name,age,health,happiness)
    def feed(self):
        self.health+=20
        if self.health+20>100:
            self.health=100
        self.happiness+=20
        if self.happiness+20>100:
            self.happiness=100

class Bears(Animal):
    def __init__(self,name,age,color,health=80,happiness=50):
        super().__init__(name,age,health,happiness)
        self.color=color
    def feed(self):
        self.health+=15
        if self.health+155>100:
            self.health=100
        self.happiness+=5
        if self.happiness+5>100:
            self.happiness=100


bear1=Bears("bear1",5,"brown")
bear1.display_info()
bear1.feed()
bear1.display_info()

lion1=Lions("lion1",3)
lion1.display_info()
lion1.feed()
lion1.display_info()

tiger1=Tigers("tiger1",2)
tiger1.display_info()
tiger1.feed()
tiger1.display_info()

tiger2=Tigers("tiger2",4,happiness=8)
tiger2.display_info()
tiger2.feed()
tiger2.display_info()

tiger3=Tigers("tiger3",1,75,0)
tiger3.display_info()
tiger3.feed()
tiger3.display_info()
tiger3.feed()
tiger3.feed()
tiger3.feed()
tiger3.display_info()

