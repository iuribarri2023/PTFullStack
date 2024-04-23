import math
my_list= ['Germany','France','Portugal','Italy','Spain']
my_tuple = ("Maries Curie","Albert Einstein","Isaac Newton","Charles Darwin","Nikola Tesla")
my_float= 10.554
my_integer= 4
my_decimal_= 1/3
my_dictionary =  {
    "name": "Eustaquio",
    "age": 30,
    "city": "Bilbao",
    "occupation": "Software engineer",
    "hobbies":["reading","eating","sleeping"]
}
#2.Round the float up
math.ceil(my_float)
#3.Get the square root of the float
math.sqrt(my_float)
#4.Select the first element from your dictionary
my_dictionary["name"]
#5.Select the second element from your tuple
my_tuple[1]
#6. Add an element to the end of your list
my_list.append("Belgium")
#7. Replace the first element in your list.
my_list[0]="Finland"
#8 Sort your list alphabetically.
new_list= sorted(my_list)
print(new_list)
#9 Use reasignment to add an element to your tuple
my_tuple2= my_tuple + ("Leonardo Da Vinci",)
print(my_tuple2)
