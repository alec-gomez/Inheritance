class Person:
    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    def print_person(self, name, address, telephone):
        print(self.__name)
        print(self.__address)
        print(self.__telephone)


class Customer(Person):
    def __init__(self, cust_num, mail_list):
        self.__cust_num = cust_num
        self.__mail_list = mail_list
