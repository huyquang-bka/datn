from typing import final


class Person():
    def __init__(self):
        self.a = "1"
        
class Person2():
    def __init__(self):
        self.b = "2"
        
class Person3():
    def __init__(self):
        self.c = "3"
        
class Final(Person, Person2, Person3):
    def __init__(self):
        super().__init__()
        

final = Final()
print(final.a, final.b, final.c)