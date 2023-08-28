#Dorian Benhamou Goldfajn 11/4/2020
import random

def main():
    #get user's name
    user_name = get_user_name()
    #greets user
    greet_user(user_name)
    
    
    #initialize boolean variable
    user_wants_to_play = True
    #set default value for scores
    bot_1_score = 0
    bot_2_score = 0
    bot_3_score = 0
    user_score = 0


    #repeat for as long as the user wants to play
    while user_wants_to_play:
        #creates a list of all possible cards(taking into considartion numbers and colors)
        all_cards = ['Red: 0', 'Red: 1', 'Red: 1', 'Red: 2', 'Red: 2', 'Red: 3', 'Red: 3', 'Red: 4', 'Red: 4', 'Red: 5', 'Red: 5', 'Red: 6', 'Red: 6', 'Red: 7', 'Red: 7', 'Red: 8', 'Red: 8', 'Red: 9', 'Red: 9', 'Yellow: 0', 'Yellow: 1', 'Yellow: 1', 'Yellow: 2', 'Yellow: 2', 'Yellow: 3', 'Yellow: 3', 'Yellow: 4', 'Yellow: 4', 'Yellow: 5', 'Yellow: 5', 'Yellow: 6', 'Yellow: 6', 'Yellow: 7', 'Yellow: 7', 'Yellow: 8', 'Yellow: 8', 'Yellow: 9', 'Yellow: 9', 'Green: 0', 'Green: 1', 'Green: 1', 'Green: 2', 'Green: 2', 'Green: 3', 'Green: 3', 'Green: 4', 'Green: 4', 'Green: 5', 'Green: 5', 'Green: 6', 'Green: 6', 'Green: 7', 'Green: 7', 'Green: 8', 'Green: 8', 'Green: 9', 'Green: 9', 'Blue: 0', 'Blue: 1', 'Blue: 1', 'Blue: 2', 'Blue: 2', 'Blue: 3', 'Blue: 3', 'Blue: 4', 'Blue: 4', 'Blue: 5', 'Blue: 5', 'Blue: 6', 'Blue: 6', 'Blue: 7', 'Blue: 7', 'Blue: 8', 'Blue: 8', 'Blue: 9', 'Blue: 9']
        #set the default for the players' cards
        bot_1_cards = []
        bot_2_cards = []
        bot_3_cards = []
        user_cards = []
        #set the default value for the winner variable
        winner = "unknown"
        #randomly select 7 cards from the list for bot 1 and taking these cards away from the list
        bot_1_cards, all_cards = get_bot_1_cards(all_cards, bot_1_cards)
        #randomly select 7 cards from the list for bot 2 and taking these cards away from the list
        bot_2_cards, all_cards = get_bot_2_cards(all_cards, bot_2_cards)
        #randomly select 7 cards from the list for bot 3 and taking these cards away from the list
        bot_3_cards, all_cards = get_bot_3_cards(all_cards, bot_3_cards)
        #randomly select 7 cards from the list for the user and taking these card away from the lists
        user_cards, all_cards = get_user_cards(all_cards, user_cards)
        #tell the user his/her cards
        print(user_name, ", your cards are: ", user_cards)
        #randomly select one card from the list(it will serve as the opener card) and display it
        top_card, top_card_color, top_card_number, all_cards = get_top_card(all_cards)
        print("The opener card is: ", top_card)
        #the remaining cards in the list are put into a pile (which the players will have to draw from if they do not have a matching card)
        cards_pile = make_pile(all_cards)
        #make a boolean variable
        no_winner = True
        #repeats until there is a winner(when someone does not have any cards left)
        while no_winner:
            #bot 1 turn
            matching_cards, bot_1_play, top_card_color, top_card_number, bot_1_cards, cards_pile, no_winner, winner, user_wants_to_play, top_card = bot_1_turn(top_card, top_card_color, top_card_number, cards_pile, bot_1_cards, no_winner, winner, user_wants_to_play)
            #display bot 1's play and the current top card
            print("Bot 1 play: ", bot_1_play)
            print("The current top card is: ", top_card)
            #check how many cards are left for bot 1
            #if bot 1 has 0 cards, end the loop and set the winner
            if len(bot_1_cards) == 0:
                no_winner = False
                winner = "bot 1"

            #bot 2 turn
            matching_cards, bot_2_play, top_card_color, top_card_number, bot_2_cards, cards_pile, no_winner, winner , user_wants_to_play, top_card = bot_2_turn(top_card, top_card_color, top_card_number, cards_pile, no_winner, winner, user_wants_to_play, bot_2_cards)
            #display bot 2's play and the current top card
            print("Bot 2 play: ", bot_2_play)
            print("The current top card is: ", top_card)
            #check how many cards are left for bot 2
            #if bot 2 has 0 cards, end the loop and set the winner
            if len(bot_2_cards) == 0 and winner != "bot 1":
                no_winner = False
                winner = "bot 2"
            #bot 3 turn
            matching_cards, bot_3_play, top_card_color, top_card_number, bot_3_cards, cards_pile, no_winner, winner , user_wants_to_play, top_card = bot_3_turn(top_card, top_card_color, top_card_number, cards_pile, bot_3_cards, no_winner, winner, user_wants_to_play)
            #display bot 3's play and the current top card
            print("Bot 3 play: ", bot_3_play)
            print("The current top card is: ", top_card)
            #check how many cards are left for bot 3
            #if bot 3 has 0 cards, end the loop and set the winner
            if len(bot_3_cards) == 0 and winner != "bot 1" and winner!= "bot 2":
                no_winner = False
                winner = "bot 3"
            #user turn
            matching_cards, user_play, top_card_color, top_card_number, cards_pile, no_winner, winner , user_wants_to_play, user_cards, top_card = user_turn(top_card, top_card_color, top_card_number, cards_pile, user_cards, no_winner, winner, user_wants_to_play, user_name)
            #display the user's play and the user's remaining cards
            print("You chose: ", user_play)
            print(user_name , ", your remaining cards are: ", user_cards)
            #make sure the user follows and agrees(otherwise the code will run really fast)
            stop = "Please press enter to continue - "
            response = input(stop)
            #display the current top card
            print("The current top card is: ", top_card)
            #check how many cards are left for the user
            #if the user has 0 cards, end the loop and set the winner
            if len(user_cards) == 0 and winner != "bot 1" and winner != "bot 2" and winner != "bot 3":
                no_winner = False
                winner = "user"

        #announce winner
        announce_winner(winner, user_name)
        #keep track of the score
        bot_1_score, bot_2_score, bot_3_score, user_score = track_score(user_name, winner, bot_1_score, bot_2_score, bot_3_score, user_score)
        #ask user to replay
        user_wants_to_play = ask_replay(user_name, user_wants_to_play)
        
    
    #announce final results
    announce_final_results(user_name, bot_1_score, bot_2_score, bot_3_score, user_score)

    
def get_user_name():
    #asks for the user's name
    prompt = "Hello, what is your name?"
    user_name = input(prompt)
    #return value which is the user name
    return user_name

def greet_user(user_name):
    #gets the user_name from the previous function
    #code to greet the user goes here
    greet_user = "Hello " + user_name + ", How are you today? "
    user_mood = input(greet_user)

def get_bot_1_cards(all_cards, bot_1_cards):
    #code to select 7 random cards from the list
    for i in range(7):
        #get a random number that will be used as an index
        number_of_cards = len(all_cards) - 1
        index_1 = random.randint(0, number_of_cards)
        #make a list of bot 1 cards
        bot_1_cards.append (all_cards[index_1])
        #remove those cards from the originial list(called all_cards)
        all_cards.remove(all_cards[index_1])
        number_of_cards = len(all_cards)
    #return the bot 1 cards and the updated list(which is the original list without the 7 cards)
    return bot_1_cards, all_cards

def get_bot_2_cards(all_cards, bot_2_cards):
    #code to select 7 random cards from the list
    for i in range(7):
        #get a random number that will be used as an index
        number_of_cards = len(all_cards) - 1
        index_2 = random.randint(0, number_of_cards)
        #make a list of bot 2 cards
        bot_2_cards.append (all_cards[index_2])
        #remove those cards from the originial list(called all_cards)
        all_cards.remove(all_cards[index_2])
        number_of_cards = len(all_cards)
    #return the bot 2 cards and the updated all_cards list
    return bot_2_cards, all_cards

def get_bot_3_cards(all_cards, bot_3_cards):
    #code to select 7 random cards from the list
    for i in range(7):
        #get a random number that will be used as an index
        number_of_cards = len(all_cards) - 1
        index_3 = random.randint(0, number_of_cards)
        #make a list of bot 3 cards
        bot_3_cards.append (all_cards[index_3])
        #remove those cards from the originial list(called all_cards)
        all_cards.remove(all_cards[index_3])
        number_of_cards = len(all_cards)
    #return the bot 3 cards and the updated all_cards list
    return bot_3_cards, all_cards


def get_user_cards(all_cards, user_cards):
    #code to select 7 random cards from the list
    for i in range(7):
        #get a random number that will be used as an index
        number_of_cards = len(all_cards) - 1
        index_4 = random.randint(0, number_of_cards)
        #make a list of the user cards
        user_cards.append (all_cards[index_4])
        #remove those cards from the originial list(called all_cards)
        all_cards.remove(all_cards[index_4])
        number_of_cards = len(all_cards)
    #return the user's cards and the updated all_cards list
    return user_cards, all_cards


def get_top_card(all_cards):
    #code to select 1 random card from the list.
    #get a random number that will be used as an index
    number_of_cards = len(all_cards) - 1
    index_top = random.randint(0, number_of_cards)
    #assign a variable called top_card to the random card selected.
    top_card = (all_cards[index_top])
    #remove this card from the all_cards list.
    all_cards.remove(all_cards[index_top])
    #find top card's color and number
    find_color_number = top_card.split(":")
    top_card_color = find_color_number[0]
    top_card_number = find_color_number[1]
    #return the top_card, top_card's color, top_card's number, and the updated all_cards list
    return top_card, top_card_color, top_card_number, all_cards

def make_pile(all_cards):
    #make the pile equal to the remaining cards in the all_cards list
    #this isn't necessary but it will make the code look better
    cards_pile = all_cards
    #return the pile
    return cards_pile

def bot_1_turn(top_card, top_card_color, top_card_number, cards_pile, bot_1_cards, no_winner, winner, user_wants_to_play):
    #get these previously defined values
    #initialize variables
    matching_cards = []
    bot_1_play = "drew a card from the pile"
    matching_card = False
    #check for matching cards
    for card in bot_1_cards:
        if top_card_color in card:
            matching_cards.append(card)
            matching_card = True
        if top_card_number in card:
            matching_cards.append(card)
            matching_card = True
    #make a play based on the top card
    #if there is a matching card:
    if matching_card is True:
        bot_index = random.randint(0, (len(matching_cards)-1))
        #choose a random card from the matching cards
        bot_1_play = matching_cards[bot_index]
        #set the new value for the top_card 
        top_card = bot_1_play
        #find the top card color and number
        find_color_number = top_card.split(":")
        top_card_color = find_color_number[0]
        top_card_number = find_color_number[1]
        #update bot_1_cards
        bot_1_cards.remove(bot_1_play)
    #if there isn't a matching card:
    else:
        #get a random card from the pile
        number_of_cards = len(cards_pile) - 1
        index_pile = random.randint(0, number_of_cards)
        card_from_pile = cards_pile[index_pile]
        #update bot_1_cards
        bot_1_cards.append(card_from_pile)
        #update the cards_pile list
        cards_pile.remove(card_from_pile)
    
    
    #return these values:
    return matching_cards, bot_1_play, top_card_color, top_card_number, bot_1_cards, cards_pile, no_winner, winner , user_wants_to_play, top_card
    

def bot_2_turn(top_card, top_card_color, top_card_number, cards_pile, no_winner, winner, user_wants_to_play, bot_2_cards):
    #get these variables
    #initialize variables for bot 2
    matching_cards = []
    bot_2_play = "drew a card from the pile"
    matching_card = False
    #check for matching cards
    for card in bot_2_cards:
        if top_card_color in card:
            matching_cards.append(card)
            matching_card = True
        if top_card_number in card:
            matching_cards.append(card)
            matching_card = True
    #make a play based on the top card
    #if there is a matching card:
    if matching_card is True:
        #choose a random card from the matching cards
        bot_index = random.randint(0, (len(matching_cards)-1))
        bot_2_play = matching_cards[bot_index]
        #set the new value for the top_card 
        top_card = bot_2_play
        #find the top card color and number
        find_color_number = top_card.split(":")
        top_card_color = find_color_number[0]
        top_card_number = find_color_number[1]
        #update bot_2_cards
        bot_2_cards.remove(bot_2_play)
    #if there isn't a matching card:
    else:
        #get a random card from the pile
        number_of_cards = len(cards_pile) - 1
        index_pile = random.randint(0, number_of_cards)
        card_from_pile = cards_pile[index_pile]
        #update bot_2_cards
        bot_2_cards.append(card_from_pile)
        #update the cards_pile list
        cards_pile.remove(card_from_pile)
    
    #return these values:
    return matching_cards, bot_2_play, top_card_color, top_card_number, bot_2_cards, cards_pile, no_winner, winner , user_wants_to_play, top_card

def bot_3_turn(top_card, top_card_color, top_card_number, cards_pile, bot_3_cards, no_winner, winner, user_wants_to_play):
    #get these variables and values
    #initialize variables for bot 3
    matching_cards = []
    bot_3_play = "drew a card from the pile"
    matching_card = False
    #check for matching cards
    for card in bot_3_cards:
        if top_card_color in card:
            matching_cards.append(card)
            matching_card = True
        if top_card_number in card:
            matching_cards.append(card)
            matching_card = True
    #make a play based on the top card
    #if there is a matching card
    if matching_card is True:
        #choose a random card from the matching cards
        bot_index = random.randint(0, (len(matching_cards)-1))
        bot_3_play = matching_cards[bot_index]
        #set the new value for the top_card 
        top_card = bot_3_play
        #find the top card color and number
        find_color_number = top_card.split(":")
        top_card_color = find_color_number[0]
        top_card_number = find_color_number[1]
        #update bot_3_cards
        bot_3_cards.remove(bot_3_play)
    #if there isn't a matching card
    else:
        #get a random card from the pile.
        number_of_cards = len(cards_pile) - 1
        index_pile = random.randint(0, number_of_cards)
        card_from_pile = cards_pile[index_pile]
        #update bot_3_cards
        bot_3_cards.append(card_from_pile)
        #update the cards_pile list
        cards_pile.remove(card_from_pile)
    #return these values:
    return matching_cards, bot_3_play, top_card_color, top_card_number, bot_3_cards, cards_pile, no_winner, winner , user_wants_to_play, top_card

def user_turn(top_card, top_card_color, top_card_number, cards_pile, user_cards, no_winner, winner, user_wants_to_play, user_name):
    #get these values and variables for the user
    #set the default values for these variables
    matching_cards = []
    user_play = "draw a card from the pile"
    matching_card = False
    #check for matching cards
    for card in user_cards:
        if top_card_color in card:
            matching_cards.append(card)
            matching_card = True
        if top_card_number in card:
            matching_cards.append(card)
            matching_card = True
    #make a play based on the top card
    #if there is a matching card:
    if matching_card is True:
        #display the matching cards
        print(user_name , ", these are your matching cards: " , matching_cards)
        #make the user choose one of the cards by typing the index number of the card
        prompt = "Please type the index number of the card you would like to pick - "
        user_input = int((input(prompt)))
        user_index = user_input - 1
        user_play = matching_cards[user_index]
        #set the new value for the top_card
        top_card = user_play
        #find the top card color and number
        find_color_number = top_card.split(":")
        top_card_color = find_color_number[0]
        top_card_number = find_color_number[1]
        #update user_cards
        user_cards.remove(user_play)
    #if there isn't a matching card
    else:
        #get a random card from the pile
        number_of_cards = len(cards_pile) - 1
        index_pile = random.randint(0, number_of_cards)
        card_from_pile = cards_pile[index_pile]
        #update user_cards
        user_cards.append(card_from_pile)
        #update the cards_pile list
        cards_pile.remove(card_from_pile)
    

    #return these values:
    return matching_cards, user_play, top_card_color, top_card_number, cards_pile, no_winner, winner , user_wants_to_play, user_cards, top_card

def announce_winner(winner, user_name):
    #code to announce the winner based on who won
    if winner == "bot 1":
        print("bot 1 won")
    if winner == "bot 2":
        print("bot 2 won")
    if winner == "bot 3":
        print("bot 3 won")
    if winner == "user":
        print(user_name, " won")

def track_score(user_name, winner, bot_1_score, bot_2_score, bot_3_score, user_score):
    #code to keep track of of the wins of each player
    if winner == "bot 1":
        bot_1_score = bot_1_score + 1
    if winner == "bot 2":
        bot_2_score = bot_2_score + 1
    if winner == "bot 3":
        bot_3_score = bot_3_score + 1
    if winner == "user":
        user_score = user_score + 1
    #return the # of wins of each player
    return bot_1_score, bot_2_score, bot_3_score, user_score

def ask_replay(user_name, user_wants_to_play):
    #code to ask the user to keep playing or stop
    ask_play = "Would you like to play again? "
    user_response = input(ask_play)
    user_response = user_response.lower()
    #set the user_wants_to_play boolean variable based on the answer
    if user_response == "no":
        user_wants_to_play = False
    #return whether the user wants to keep playing or stop
    return user_wants_to_play

def announce_final_results(user_name, bot_1_score, bot_2_score, bot_3_score, user_score):
    #code to announce how many wins each player has
    print("Bot 1 has ", bot_1_score, " wins")
    print("Bot 2 has ", bot_2_score, " wins")
    print("Bot 3 has ", bot_3_score, " wins")
    print(user_name, " has ", user_score, " wins")




main()