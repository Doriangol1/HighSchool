#Dorian 9/30/2020
import random

#define a function
def greet_user():
    
    greet_user = "Hello, what is your name?"
    #asks for the user's name
    user_name = input(greet_user)
    Nickname = user_name[0]
    print("Hello " + user_name + ", I think I'll just call you " + Nickname)
    #creats the user a nickname
    return user_name
def discuss_weather(): 
    prompt = "What is the weather like today? "
    #asking the user a question about the weather
    user_input = input(prompt)
    #The user's response
    Sunny_day = "Get some Vitamin D!"
    Rainy_day= "Do you like rain?"
    Snowy_day= "You should go skiing today!"
    Cloudy_day= "Do you like cloudy days?"
    Thunderstorm_day= "Oh no! hopefully tomorrow will be better"
    #assigning values to variables
    if "sunny" in user_input or "hot" in user_input:
      r = input(Sunny_day)
    if "rainy" in user_input:
      r=input(Rainy_day)
    if "snowy" in user_input:
      r=input(Snowy_day)  
    if "cloudy" in user_input:
      r=input(Cloudy_day)
    if "thunderstorming" in user_input or "cold" in user_input:
      r=input(Thunderstorm_day)
    #Different response based on the user response using the variables.
    Question = "Do you like this type of weather? "
    #continues the converstaion about weather
    Answer = input(Question)
    if Answer == "yes":
        print("good for you!")
    if Answer == "no":
        print("Better days will come")
    #Responds depends on the yes or no answer

    Second_Q = "what types of weather do you like?"
    hot_list = ["hot", "sunny", "warm"]
    cold_list = ["cold", "rain", "snow", "cloudy", "thunderstorm"]
    #asks another question and creates two lists of possible answers.
    Second_A = input(Second_Q)
    if Second_A in hot_list:
      print("I'm assuming that your favorite season is the summer")
    if Second_A in cold_list:
      print("I'm assuming that you like the winter")
    #responds to the user based on which list the answer is inside of.

#creates a new  therapist function
def therapist():
    FR_list = ["Why are you feeling this way?", "what makes you sad?", "I'm glad you are feeling happy", "why are you depressed?", "we all need to relax sometime", "please tell me, what are you worried about?", "Good, what are you excited for?", "Do you believe it is normal to feel unsure?"]
    #creates a list of possible responses(FR = feeling response)
    Index = 0
    prompt="how are you feeling today?"
    Feeling = input(prompt)
    Feeling = Feeling.lower()
   
    #finds the "I am" and adds 5 to find the actual feeling"
  
    if "sad" in Feeling:
        Index = 1
        user_response = input(FR_list[Index])
        print("I am sorry to hear that.") 
    if "happy" in Feeling:
        Index = 2
        print(FR_list[Index])
    if "depressed" in Feeling:
        Index = 3
        user_response = input(FR_list[Index])
        print("I am sorry to hear that.") 
    if "relaxed" in Feeling:
        Index = 4
        print(FR_list[Index])
    if "worried" in Feeling:
        Index = 5
        user_response = input(FR_list[Index])
        print("I am sorry to hear that.") 
    if "excited" in Feeling:
        Index = 6
        user_response = input(FR_list[Index])
        print("Good for you!")
    if "unsure" in Feeling:
        Index = 7
        user_response = input(FR_list[Index])
        print("I am sorry to hear that.") 
   
    #gets a different response from the list based on the user's answer.

def favorite_movie():
  #asks the user what's his/her favorite movie
  
  prompt = "what is your favorite movie?"
  user_input = input(prompt)
  response = user_input + " is a great movie"
  print(response)

def favorite_sport():
  #asks the user what's his/her favorite sport
  
  prompt = "what is your favorite sport?"
  sport_input = input(prompt)
  sport_response = sport_input + " is a great sport"
  print(sport_response)

def discuss_music(user_name):
    #establish list of artists to discuss
    artist_list = ["Demi Lovato", "Ed Sheeran", "Ariana Grande ", "Kanye West", "Future" ]
    print("Let's talk about music.")

    #iterate through each artist in the list 
    #this is the start of the loop 
    for artist in artist_list: 
        #all of these indented steps will be done repeatedly
        #use the target variable to create a statement
        print("Hey, " + user_name + ", " + artist + " is great!")
    #the loop has now finished
    #make a statement after going through the list

def roll_credits():
    credits_list = ["Main Developer - Dorian","First Partner - James", "Second Partner - Daniel", "Third Partner - Mark"]
    print("Here are some credits for developers and helpers: ")

    for credit in credits_list:
        print(credit)
        #The above line will repeat
    
    print("Thank You!")

  

def main():
  chat = True
  
  #calls all functions
  
  greet_user()
  favorite_movie()
  favorite_sport()
  #discuss_music(user_name)
 
  discuss_weather()

  while chat == True:
    therapist() 
      #the user still wants to chat, so it will keep asking questions.
    stop = input("Do you still want to talk?")
    if stop=="no":
      print("It was nice chatting with you, goodbye")
      chat = False
    
        
    
    

  
  
main()