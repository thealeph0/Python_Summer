class Pet:

    def __init__(self,name,type,age):
        self.__name = name
        self.__animal_type = type
        self.__age = age

    def set_name(self,name):
        self.__name = name
    
    def set_animal_type(self,type):
        self.__animal_type = type
    
    def set_age(self,age):
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age

def main():
    name = input('What is the name?')
    type = input('What is the type of pet?')
    age = int(input('What is the age of your pet?'))

    pet1 = Pet(name,type,age)

    print('Your pet\'s name is: ', pet1.get_name())
    print('Your pet\'s is a: ', pet1.get_animal_type())
    print('Your pet\'s age is: ', pet1.get_age())

main()
