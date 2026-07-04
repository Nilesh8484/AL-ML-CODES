#slicing____________________


# word = "python";

# print(word[-4:-2]);  # also allow fo negative index


# a =5;
# b=4;
# sum =a+b;

# print(f"sum of {a} amd {b} is = {sum}");



# list__________________


# mark = [23,4,24,232,13,213,23.3];   #mutable
#                         #silicing a working
# mark.append(4);
# mark.insert(3,585.45);
# mark.reverse();
# mark.sort();
# print(mark);


# mark= [1,2,3,10,4];
# inx =0;
# for i in mark:
#     if(i==10):
#         print(f"number is {i} then index is : {inx}");
#         break;
#     inx+=1;
        


        #tuples______________________________

# number = (1,2,2,3,4,2,5,6,2);
# print(number)
# print(number.index(2));
# print(number.count(2));


#dictionary __________________

# info= {
#     "name":"nilesh",
#     "cgpa":7.4,
#     "subject":["math","english","python"],
#     "pi":3.24
# }


# print(info.keys());
# print(info.values());
# print(info.items());

# print(info.update({"address":"bhavnagar"}));
# print(info.get("address"));
# print(info);



#sets-____________________

# number1 = {1,2,2,3,3,4,4,5,6,7,7,8,9,9};
# number2 = {1,2,2,3,3,5,11,23,34};
# print(number1.add(10));
# number1.remove(3);
# number1.pop();
# ans =number1.intersection(number2);
# ans2=number1.clear();

# print(number1);




#quastion __________________________

# info = [
# ("Alice", "Math"),
# ("Bob", "Science"),
# ("Alice", "Science"),
# ("Charlie", "Math"),
# ("Bob", "Math"),
# ("Alice", "English"),
# ("Charlie", "English"),
#  ]
# uniq= set();
# for tup in info:
#     uniq.add(tup[1]);
# print(uniq);



# for tup in info:
#     if (tup[1] == "English"):
#         print(tup[0]);


    
# dict={};

# for name,course in info:
#     if(dict.get(name)==None):
#         dict.update({name:set()});
#         dict[name].add(course);
#     else:
#         dict[name].add(course);
# print(dict);