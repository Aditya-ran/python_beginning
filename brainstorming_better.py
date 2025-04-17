from random import choice


stuff = {
"bored" : ["You should go for a walk!" , "You can go and help your mother", "you can learn a new skill" , "you can focus on your fitness", "you can complete your incomplete assignments"],
"study": ["you can study maths","you can study english","you can study science","you can study sst","you can do coding"],
"eat" : ["chicken biryani","butter chicken masala","mutton korma","mutton biryani","chicken korma","chicken kaali mirch"],
"ideas_visit" : ["Jaipur","Tokyo","Kyoto","New York","Los Angeles","Beijing","Berlin","Miami","Riyadh","Dubai","Jammu","Srinagar","Shimla","Manali","Haldwani","Paras Nath Hills","Amsterdam"],
"ideas_wear" : ["Jeans","Pants","shorts","Football kit","Party attire"]
}

random = {1:"ideas_bored",2:"ideas_study",3:"ideas_eat",4:"ideas_visit",5:"ideas_wear"}
user_input = input(">>").lower()
if user_input in stuff.keys():
    print(choice(stuff[user_input]))