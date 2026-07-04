# username = input("enter the username:-");
# password =int(input("enter the password:-"));


# if (username == "nilesh" and password == 123):
#     print("login is successfully");
# elif(username != "nilesh"):
#     print("username is wrong");
# else:
#     print("passwoed is invalid");


#match case-------------------

"""
color = input("enter taffic color: ");
match (color):
    case ("green"):
        print("gooo");
    case ("yellow"):
        print("look");
    case ("red"):
        print("stoppp");
    case _:
        print("invalid color !!");"""     #default case_________________________


#while loop__________________\


# n = int(input("enter number"));

# i = 1;

# while(i<=10):
#     print(n*i);
#     i +=1;


    # break keyworks__________________


# i = 0;

# while(i<10):
#     i+=1;
#     if(i%3==0):
#         continue;
        
#     print(i);
  

# string = "nilesh";

# if "e" in string:
#     print ("successfull");


# word ="artificial intelligence";
# count=0;
# for i in word:
#     if (i=="i"):
#         count+=1;
# print(count);




# word = "artificial intelligence";

# count = 0;

# for i in word:
#     if (i == "a"or i== "e"or i=="o"or i=="u"or i=="i"):
#         count+=1;
#         print(i,count);
# print(count);


# number = int(input("enter the number"));
# sum=0;
# for i in range(number+1):
#     sum +=i;

# print(sum);



#funcation _________________________


# def avg(a ,b,c):
#     s = (a+b+c)/3;
#     return s;

# ans=avg(3,5,1);
# print(ans);


#lambda function ____________


# avg = lambda a,b,c : (a+b+c)/3;
# print(avg(2,2,2));

# def findfact(number):
#     fact=1;
#     for i in range(1,number+1):
#         fact*=i;
#     return fact;

# n = int(input("enter the number"));
# print(findfact(n));