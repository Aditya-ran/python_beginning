import random

#this will be for when  i am bored and can't think of what to do ! 
def whattodo():
    ideas_bored = ["You should go for a walk!" , "You can go and help your mother", "you can learn a new skill" , "you can focus on your fitness", "you can complete your incomplete assignments"]
    len_ideas = len(ideas_bored)
    randInt = random.randint(0,len_ideas - 1 )
    print(ideas_bored[randInt])


#this is for when i can't figure out what subject to study ! 
def whattostudy():
    ideas_study = ["you can study maths","you can study english","you can study science","you can study sst","you can do coding"]
    len_ideas_study = len(ideas_study)
    studyInt = random.randint(0,len_ideas_study -1)
    print(ideas_study[studyInt])


#this is for when i can't decide what to eat today ! 
def whattoeat():
    ideas_eat = ["chicken biryani","butter chicken masala","mutton korma","mutton biryani","chicken korma","chicken kaali mirch"]
    len_eat = len(ideas_eat)
    randEat = random.randint(0,len_eat - 1)
    print(ideas_eat[randEat])


#this is for me when i can't decide which place to visit
def wheretogo():
    ideas_visit = ["Jaipur","Tokyo","Kyoto","New York","Los Angeles","Beijing","Berlin","Miami","Riyadh","Dubai","Jammu","Srinagar","Shimla","Manali","Haldwani","Paras Nath Hills","Amsterdam"]
    len_visit = len(ideas_visit)
    randVisit = random.randint(0,len_visit - 1 )
    print(ideas_visit[randVisit])

def whattowear():
    ideas_wear = ["Jeans","Pants","shorts","Football kit","Party attire"]
    len_wear = len(ideas_wear)
    randWear = random.randint(0,len_wear -1)
    print(ideas_wear[randWear])

user_input = input(">>").lower()

match user_input:
    case "bored":
        whattodo()
    case "study":
        whattostudy()
    case "eat":
        whattoeat()
    case "visit":
        wheretogo()
    case "clothes":
        whattowear()

