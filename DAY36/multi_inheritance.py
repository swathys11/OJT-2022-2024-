class g_father:# parent class 
    def g_father_name(self): 
        print("my father name is xyz") 

class father(g_father): # child class 
    def father_name(self): 
        print("my father name is abc") 

class son(father): # child class 
    def son_name(self): 
        print("my name is SSS") 
 
obj_g_father= father() # object for g_father class. 
obj_father= father() # object for father class. 
obj_son=son() # object for son class. 
obj_son.g_father_name() # you access son class to g_father class. obj_son.father_name() # you access son class to father class. 
obj_son.son_name() # you access same class.


#Multiple_inheritance
class father: # parent class 
    def father_name(self): 
        print("my father name is xvz") 
class mother: # parent class 
    def mother_name(self): 
        print("my father name is abcd") 
 
class son(mother,father): # child class 
    pass  
obj_father= father() # object for father class. 
obj_mother=mother() # object for mother class. obj_son=son() # object for son class. 
obj_son.father_name() # you access son class to father class. 
obj_son=son() #
obj_son.mother_name() # you access son class to mother class. 