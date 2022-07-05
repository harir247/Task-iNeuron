#Questions

#l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
#1 . Try to reverse a list
#2. try to access 234 out of this list
#3 . try to access 456
#4 . Try to extract only a list collection form list l
#5 . Try to extract "sudh"
#6 . Try to list all the key in dict element avaible in list
#7 . Try to extract all the value element form dict available in list


import logging
logging.basicConfig(filename="Task2.log",level=logging.INFO)

q= [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]

class List_ext:
    def __init__(self,l):
        self.l=l

    def lst_items(self):
        l1=[]
        try:
            logging.info("Collecting all list items from input")
            for i in self.l:
                if type(i)==list:
                    l1.append(i)
                elif type(i)==dict:
                      for k,v in i.items():
                        if type(k)==list:
                            l1.append(k)
                        elif type(v)==list:
                             l1.append(v)
                             logging.info("The all list elements from the question are : %s",l1)
                             return l1
            logging.info(l1)


        except Exception as e:
            logging.exception(e)

l2 =List_ext(q)

class Reverse_list:
    def __init__(self,l):
        self.l =l

    def reversed_lists(self):
        try:
            logging.info("Reversing the list")
            rev_list = self.l[::-1]
            logging.info("The reversed list is: %s",rev_list)
            return rev_list

        except Exception as e:
            logging.exception(e)
l3 = Reverse_list(q)

class Find:
    def __init__(self,l):
        self.l =l

    def search(self):
        try:
            logging.info("Searching the elememt 234")
            for i in self.l:
                if type(i)== tuple:
                    for j in i:
                     if j==234:
                        logging.info("The element found: %s",j)
                        return j
        except Exception as e:
            logging.exception(e)
l4 =Find(q)

class Dict_elements:
    def __init__(self,l):
        self.l =l

    def key_elemets(self):
        try:
            logging.info("Sorting the dictionary elements")
            key=[]
            value=[]
            for i in self.l:
                if type(i)==dict:
                    for k,v in i.items():
                        key.append(k)
                        value.append(v)
                    logging.info("key elements: %s",key)
                    logging.info("value elements: %s", value)
                    print("key elements: ",key)
                    print("value elements: %s ",value)

        except Exception as e:
            logging.exception(e)

l5 = Dict_elements(q)

class List_collection:
    def __init__(self,l):
        self.l =l

    def list_collections(self):
        try:
            logging.info("Sorting the list from dictionary elements")
            lst_collect =[]
            for i in self.l:
                if type(i)==list:
                    lst_collect.append(i)
                elif type(i)==dict:
                    for k,v in i.items():
                        if type(k)==list:
                            lst_collect.append(k)
                        if type(v)==list:
                            lst_collect.append(v)
                            logging.info("The list elements fro dictionary %s",lst_collect)
                            return lst_collect
        except Exception as e:
            logging.exception(e)

l6 = List_collection(q)


print(l2.lst_items())
print(l3.reversed_lists())
print(l4.search())
l5.key_elemets()
print(l6.list_collections())