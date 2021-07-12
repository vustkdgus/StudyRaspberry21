class Pereson(object):

    total = 0

    def __init__(self, name, age): # 추가생성자 (selft) / overloading
        self.name = name
        self.age = age
    
    def getAge(self):
        return self.age

