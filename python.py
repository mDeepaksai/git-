# strings
from turtle import update


string = "Hello, World!"
name="ChatGPT"
new=f"{string} I am {name}."
print(new)
print(new.replace("ChatGPT", "Deepak sai"))
# lists
my_list = [1, 2, 3, 4, 5,5,"smiriti","my love"]
print(my_list[6:])
# tuples
my_tuple = (10, 20, 30, 40, 50)
# dictionarys
my_dict = {
    "name": "Alice",
    "age": 30, 
    "city": "New York"
    }
print(my_dict["name"])
my_dict1={
    "name":"Deepak sai",
    "age":22,
    "collage":"kit",
    "subjects":{
        "sub1":"maths",
        "sub2":"python",
        "sub3":"web development"
    }
}
print(my_dict1.get("collage"))
my_dict1.update({"hobby":"coding"})
print(my_dict1)