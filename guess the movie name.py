import random
score = 0
permission =input("You wanna play? ").lower()
while permission == "yes":
    movie = ["interstellar","oppenheimer","inception","top gun ", "the batman","the dark knight","joker"]
    len_movie = len(movie)
    randMovie = random.randint(0,len_movie -1)

    movie_name = input("Enter your guess: " ).lower()
    if(movie_name == movie[randMovie]):
        print("your guess was correct")
        score +=1
    elif(movie_name not in movie):
        print("Please fuck off")
    else:
        print("your guess was incorrect\nthe correct answer was:",movie[randMovie])

else:
    print("fook off")