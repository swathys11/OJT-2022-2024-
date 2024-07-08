class father:
    def father_name(self):
        print("My father name is ABCD")
        
class son(father):
    pass


obj_father = father()
obj_son = son()

obj_son.father_name()
