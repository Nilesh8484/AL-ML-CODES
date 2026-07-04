# class Students:
#     name = "nileshh"            #classs
#     college = "gec bvn"
#     city = "bhavnagar"

# stud = Students();
# print(stud.name);                   #objects





# init constuctor.....................



# class Student:

#     college_name = "gec bvn";
#     def __init__(self,name,cgpa):
#         self.name =name; 
#         self.cgpa=cgpa;

#     def get_cgpa(self):             #dedult parameter that why self perameters
#         return self.cgpa;

# stud = Student("nilesh",9.4);
# stud2 = Student("kalpesh",8.3);
# stud3 = Student("jenish",7.6);


# print(stud.get_cgpa());
# print(stud.college_name);
# print(stud.name);
# print(stud2.name);
# print(stud3.name);




# class Laptop:
#     storage_type = "ssd";                              # cladd attribute 

#     def __init__ (self,ram,storage):
#         self.ram=ram;
#         self.storage=storage;

#     def get_info(self):
#         print(self.ram,self.storage, self.storage_type);

#     @classmethod              # class method
#     def get_storage_type(cls):
#         print(cls.storage_type);

#     @staticmethod              # static method
#     def get_discount(price,discount):
#         final_price= price - (discount*price/100);
#         print(final_price);


# l1 = Laptop("16gb","512gb");
# l2 = Laptop("8gb","256gb");


# l1.get_discount(40000,10);


# ans=l2.get_storage_type();
# print(ans);

# print(l2.get_info());





# # practice problem_______________



# class OnlineStore:

#     count=0;


#     def __init__(self,name,price):
#         self.name=name;
#         self.price=price;
#         OnlineStore.count +=1;
        

#     def get_info(self):
#         print(self.name,self.price);

#     @classmethod
#     def tot_count(cls):
#         print(cls.count);

#     @staticmethod
#     def get_discount(price,percentage):
#         print(price-(price*percentage/100));




# p1 = OnlineStore("laptop",40000);
# p2 = OnlineStore("tv",10000);
# p3 = OnlineStore("mobile",7000);
# p4 = OnlineStore("pen",20);

# p1.get_info();
# p2.get_info();
# p3.get_info();
# p4.get_info();

# OnlineStore.tot_count();
# p1.get_discount(p1.price,10);



# encapsulatiom concept_____________________


# class BankAccount:

#     def __init__ (self,username,balance):
#         self.username= username;
#         self.__balance=balance;       <-            #that make to private attributes for double undersocre


#     def get_balance(self):
#         return self.__balance;                


#     def set_balance(self,newbalance):
#         self.__balance=newbalance;


# a1=BankAccount("nilesh",10000);
# # a1.set_balance(393323);
# # print(a1.username,a1.get_balance());
# # print(a1._BankAccount__balance)



# class Employee:
#     start="3pm";
#     end= "2am";

# class admin(Employee):
#     def __init__ (self,role):
        
#         self.role=role;

# class accountant(admin):
#     def __init__(self,salary,role):
#         super().__init__(role)
#         self.salary=salary;


# acc1 = accountant(223323,"ca");

# print(acc1.role)




# abstaction +________________________


# from abc import ABC,abstractmethod


# class animal:
#     @abstractmethod
#     def make_sound(self):
#         pass


# class lion(animal):
#     def make_sound(self):
#         print("riorrr!!!");


# l1 = lion();
# l1.make_sound();




# duck typing _______________


# class teacher:

#     def destiny(self):
#         print("call techear");

        

# class account:

#     def destiny(self):
#         print("call account");


# t1=teacher()
# t1.destiny();


# a1=account();
# a1.destiny();