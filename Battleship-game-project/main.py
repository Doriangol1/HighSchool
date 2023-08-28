
import random
import os
import time

class Battleship:
    def __init__(self, player):
        #coordinate_selection are the ship spot selections
        self.coordinate_selection = []
        #selection_list is the coordinates available to select on attacks
        self.selection_list = []
        self.player = player
        self.select = 0
       
    
    def user_select_coordinate(self):
        #user selects coordinates to attack the bot
        waiting_for_coordinate_correct = True
        while waiting_for_coordinate_correct:
            print("")
            self.select = input("Please select one of those coordinates to attack on the bot. ")
            if self.select in self.selection_list:
                print("")
                print("You selected " + self.select)
                waiting_for_coordinate_correct = False
                time.sleep(2)
                os.system('clear')
            if self.select not in self.selection_list:
                print("That is not one of the coordinates you can select! ")
            
            
        
    def bot_select_coordinate(self):
        #bot randomly selects a coordinate from their selection list to attack the user
        self.select = random.choice(self.selection_list)
    
        print("The bot attacked the user with the coordinate " + self.select)
        

class Coordinate:
    def __init__(self):
        #intializes attribute for coordinates list
        self.coordinate_list = []
    
    def create_list(self):
        #a list of all possible coordinates is made
        for x in range(5):
            #^^^^we can adjust the numbers from 5 to 2-3 to make the rounds go a lot faster so we can test the code at the end of the round.
            x = x + 1
            for y in range(5):
                y = y + 1
                blank = str(x) + "," + str(y)
                self.coordinate_list.append(blank)

class Score:
    def __init__(self):
        self.score = 0
    
        
def get_user_name():
    #asks for the user's name
    prompt = "Hello, what's your name? "
    user_name = input(prompt)
    #return value which is the user name
    return user_name

def instructions(user_name):
    #asks the user if they know how to play Battleships
    prompt = "Do you know how to play Battleship? Please respond with no or yes. "
    user_answer = input(prompt)
    user_answer = user_answer.lower()
    #if not, instructions and rules will be shown.
    if user_answer == "no":
        print("Hello " + user_name + ", these are the instructions and rules for Battleship: There is a 10 by 10 grid divided into 2. One half is for the bot's ships and the other is for your ships. At the beginning, both players have to select 5 coordinates within their 5 by 5 half, which will be the coordinates for their 5 ships. After both players finished selecting their ships' coordinates, the players take turns in guessing the opponent's ships' coordinates. If they guess correctly, they destroy the opponent's ship and get a point. The first player to destroy the opponent's ships wins.")
        time.sleep(5)
        print("")
        ready = input("If you are done reading, press enter to continue. ")
    if user_answer == "yes":
        print("Great!")
        time.sleep(2)
    os.system('clear')
    

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
   

def announce_winner(final_user_score, final_bot_score, winner, user_name):
    #code to announce the winner
    if winner == "tie":
        print(user_name + " and the bot destroyed each others ships in the same amount of turns.")
    if winner == 0:
        print(user_name + " destroyed the bot's ships")
        #adds a point to the users total score
        final_user_score.score = final_user_score.score + 1
    if winner == 1:
        print("The bot destroyed " + user_name + "'s ships")
        #adds a point to the bots total score
        final_bot_score.score = final_bot_score.score + 1
    
    return final_user_score, final_bot_score
        
    

    
def announce_final_results(user_name, final_user_score, final_bot_score):
    os.system('clear')
    #code to announce how many wins each player had
    print(user_name + " has " , final_user_score.score , " wins!")
    print("")
    print("The bot has " , final_bot_score.score , " wins!")
    print("")
    print("Thank you for playing my version of Battelships. I hope the game was succesfull in being informative on some of the harms of cannabis and establishing the position that cannabis comes with a variety of both short and long term consequences.")
    print("")
    time.sleep(3)
    print("Reference List: ")
    print("")
    print("Andriot, T., Ohnmacht, P., Vuilleumier, P., Thorens, G., Khazaal, Y., Ginovart, N., & Ros, T. (2022) Electrophysiological and behavioral correlates of cannabis use disorder. Cognitive, Affective, & Behavioral Neuroscience, 22(6), 1421-1431.")
    print("")
    print("Coughlin, L. N., Ilgen, M. A., Jannausch, M., Walton, M. A., & Bohnert, K. M. (2021). Progression of cannabis withdrawal symptoms in people using medical cannabis for chronic pain. Addiction, 116(8), 2067-2075.")
    print("")
    print("Gilman, J. M., Kuster, J. K., Lee, S., Lee, M. J., Kim, B. W., Makris, N., ... & Breiter, H. C. (2014). Cannabis use is quantitatively associated with nucleus accumbens and amygdala abnormalities in young adult recreational users. Journal of Neuroscience, 34(16), 5529-5538.")
    print("")
    print("Greaves, L., & Hemsing, N. (2020). Sex and gender interactions on the use and impact of recreational cannabis. International journal of environmental research and public health, 17(2), 509.")
    print("")
    print("Herrmann, E. S., Weerts, E. M., & Vandrey, R. (2015). Sex differences in cannabis withdrawal symptoms among treatment-seeking cannabis users. Experimental and clinical psychopharmacology, 23(6), 415.")
    print("")
    print("Panlilio, L., Goldberg, S. and Justinova, Z. (2015), Cannabinoid abuse and addiction: Clinical and preclinical findings. Clin. Pharmacol. Ther., 97: 616-627.")
    print("")
    print("Battistella G, Fornari E, Thomas A, Mall JF, Chtioui H, et al. (2013) Weed or Wheel! fMRI, Behavioural, and Toxicological Investigations of How Cannabis Smoking Affects Skills Necessary for Driving. PLOS ONE 8(1): e52545.")
    print("")
    print("Compton, Michael T., et al. “Association of Pre-Onset Cannabis, Alcohol, and Tobacco Use With Age at Onset of Prodrome and Age at Onset of Psychosis in First-Episode Patients.” American Journal of Psychiatry, vol. 166, no. 11, American Psychiatric Association, Nov. 2009, pp. 1251–57.")
    print("")
    print("Ramaekers, J.G., Mason, N.L., Toennes, S.W. et al. Functional brain connectomes reflect acute and chronic cannabis use. Sci Rep 12, 2449 (2022). ")
    print("")
    print("Joel, Daphna, et al. “Sex Beyond the Genitalia: The Human Brain Mosaic.” Proceedings of the National Academy of Sciences of the United States of America, vol. 112, no. 50, National Academy of Sciences, Dec. 2015, pp. 15468–73.")
def create_lists():
    #Code to instantiate 2 objects using class Coordinate and create coordinates list for the bot and the user
    coordinate1 = Coordinate()
    coordinate1.create_list()
    coordinate2 = Coordinate()
    coordinate2.create_list()
    bot_coordinate = Coordinate()
    bot_coordinate.create_list()
    user_coordinate = Coordinate()
    user_coordinate.create_list()
    #instantiate objects using class battleship to the user and bot
    user = Battleship("User")
    bot = Battleship("Bot")
    bot.selection_list = coordinate1.coordinate_list
    user.selection_list = coordinate2.coordinate_list
    #return the coordinates lists and battleships
    return coordinate1, coordinate2, bot_coordinate, user_coordinate, bot, user

def main():
    #get user's name
    user_name = get_user_name()
    #gets instructions
    print('\n' + "Hey " + user_name + ", here is some info about the project: " + '\n' + '\n' + "This project involves a computer game version of the board game Battleships, which used to be one my favorite games to play as a kid. In this game, however, every time a ship is destroyed, information on some of the harmful impacts of cannabis consumption pops up. I've decided to research cannabis dependence and effects as a bunch of my friends are heavy, chronic marijuana users. I looked at both medical and recreational use since my friends fit into both categories. I chose this game specifically because it does not require a lot of attention, which I've come to learn is something most marijuana users tend to lack. There is a common misconception that weed is harmless, and so I hope this game teaches you otherwise.")
    print("")
    time.sleep(2)
    instructions(user_name)
    #initialize final scores
    final_user_score = Score()
    final_bot_score = Score()
    #initialize boolean variable
    user_wants_to_play = True
    faxList = ["Relative alpha power in the brain was found to be higher in Cannabis Use Disorder patients, and increased alpha power was associated with worse performance in activities requiring attention. While attentional deficits are widely experienced during cannabis intoxication, research findings show that this effect may persist beyond, posing a long-term risk. "+ '\n' + '\n' + "ref: Andriot, T., Ohnmacht, P., Vuilleumier, P., Thorens, G., Khazaal, Y., Ginovart, N., & Ros, T. (2022) Electrophysiological and behavioral correlates of cannabis use disorder. Cognitive, Affective, & Behavioral Neuroscience, 22(6), 1421-1431.", "The most common cannabis withdrawal symptoms include anxiety, sleep difficulties, decreased appetite, restlessness, mood shifts, and irritability. "+ '\n' + '\n' +  "ref: Coughlin, L. N., Ilgen, M. A., Jannausch, M., Walton, M. A., & Bohnert, K. M. (2021). Progression of cannabis withdrawal symptoms in people using medical cannabis for chronic pain. Addiction, 116(8), 2067-2075.", "Generally, younger people with severe withdrawal symptoms were found to be at a greater risk for cannabis-related problems, used cannabis more often and at larger quantities, and were more likely to smoke cannabis as opposed to other consumption methods. "+ '\n' +  '\n' + "ref: Coughlin, L. N., Ilgen, M. A., Jannausch, M., Walton, M. A., & Bohnert, K. M. (2021). Progression of cannabis withdrawal symptoms in people using medical cannabis for chronic pain. Addiction, 116(8), 2067-2075.", "Combined findings from past studies suggest that younger individuals with greater mental health issues might be at risk of greater consequences from use, having a harder time stopping use, and increased susceptibility to relapse due to more acute and longer-lasting withdrawal symptoms. " + '\n' + '\n' +  "ref: Coughlin, L. N., Ilgen, M. A., Jannausch, M., Walton, M. A., & Bohnert, K. M. (2021). Progression of cannabis withdrawal symptoms in people using medical cannabis for chronic pain. Addiction, 116(8), 2067-2075.", "Even in young, nondependent cannabis users, there are observable abnormalities in the brain compared with non-users. "+ '\n' +  '\n' + "ref: Gilman, J. M., Kuster, J. K., Lee, S., Lee, M. J., Kim, B. W., Makris, N., ... & Breiter, H. C. (2014). Cannabis use is quantitatively associated with nucleus accumbens and amygdala abnormalities in young adult recreational users. Journal of Neuroscience, 34(16), 5529-5538.", "Similar brain abnormalities are apparent in cannabis users and patients with schizophrenia, obsessive-compulsive disorders, Parkinson’s disease, and Tourette’s syndrome, suggesting potential correlations. "+ '\n' +  '\n' + "ref: Gilman, J. M., Kuster, J. K., Lee, S., Lee, M. J., Kim, B. W., Makris, N., ... & Breiter, H. C. (2014). Cannabis use is quantitatively associated with nucleus accumbens and amygdala abnormalities in young adult recreational users. Journal of Neuroscience, 34(16), 5529-5538.", "Density increase of a large area, as appears in the amygdala region of the brain among cannabis users, represents a factor that is usually implicated in addiction, potentially playing an important role in drug craving. "+ '\n' +  '\n' + "ref: Gilman, J. M., Kuster, J. K., Lee, S., Lee, M. J., Kim, B. W., Makris, N., ... & Breiter, H. C. (2014). ", "Density changes in the prefrontal cortex of the brain, as observed in cannabis users, is related to decision-making abnormalities when it comes to addiction, although more research is necessary. "+ '\n' +  '\n' + "ref: Gilman, J. M., Kuster, J. K., Lee, S., Lee, M. J., Kim, B. W., Makris, N., ... & Breiter, H. C. (2014).", " Cannabis Use Disorder (CUD) affects about 10% of marijuana users. "+ '\n' +  '\n' + "ref: Greaves, L., & Hemsing, N. (2020). Sex and gender interactions on the use and impact of recreational cannabis. International journal of environmental research and public health, 17(2), 509.", "On average, males report greater and more frequent cannabis use than females, but females were found to develop Cannabis Use Disorder quicker, a phenomenon termed 'telescoping'. "+ '\n' +  '\n' + "ref: Greaves, L., & Hemsing, N. (2020). Sex and gender interactions on the use and impact of recreational cannabis. International journal of environmental research and public health, 17(2), 509. ", "Females report stronger effects at lower doses of cannabis and experience greater Cannabis Use Disorder and withdrawal symptoms intensity. "+ '\n' +  '\n' + "ref: Greaves, L., & Hemsing, N. (2020). Sex and gender interactions on the use and impact of recreational cannabis. International journal of environmental research and public health, 17(2), 509.", "Sex differences in Cannabis Use Disorder severity and development may be influenced by genetic differences (as was seen in rats) and/or as a result of women experiencing worse stigma, discrimination, shame, and blame regarding substance use, receiving less social support than men. "+ '\n' +  '\n' + "ref: Greaves, L., & Hemsing, N. (2020). Sex and gender interactions on the use and impact of recreational cannabis. International journal of environmental research and public health, 17(2), 509. ", "Men tend to have more access to substances relative to women as it is more socially acceptable, and so riskier patterns of use and susceptibility to cannabis dependence occur as a consequence, such as higher rates of impaired driving. "+ '\n' +  '\n' + "ref: Greaves, L., & Hemsing, N. (2020). Sex and gender interactions on the use and impact of recreational cannabis. International journal of environmental research and public health, 17(2), 509.", "Women were found to experience a wider range of mood related cannabis withdrawal symptoms, and experience anxiety, restlessness, and increased aggression more severely than men. The research suggests this to be due to a genetic difference. "+ '\n' +  '\n' + "ref: Herrmann, E. S., Weerts, E. M., & Vandrey, R. (2015). Sex differences in cannabis withdrawal symptoms among treatment-seeking cannabis users. Experimental and clinical psychopharmacology, 23(6), 415.", "During intoxication, effects could be 'desirable', like euphoria, ease of laughter, talkativeness and/or 'undesirable', such as dysphoria, anxiety, panic, paranoia, dry mouth, and blood pressure increase, the magnitude and frequency of which may be determined by the individual’s experience with cannabis, personality traits, and amount of cannabis consumed. The dose-effect relationship follows an inverted U shape (which is typical of abused drugs). "+ '\n' +  '\n' + "ref: Panlilio, L., Goldberg, S. and Justinova, Z. (2015), Cannabinoid abuse and addiction: Clinical and preclinical findings. Clin. Pharmacol. Ther., 97: 616-627. ", "Regular cannabis use was associated with addiction, cognitive impairment such as lower IQ, poor educational outcome, diminished life satisfaction, and increased vulnerability to psychotic disorders. "+ '\n' +  '\n' + "ref: Panlilio, L., Goldberg, S. and Justinova, Z. (2015), Cannabinoid abuse and addiction: Clinical and preclinical findings. Clin. Pharmacol. Ther., 97: 616-627. ", "Adolescents are more vulnerable to long term effects as the brain and the endocannabinoid undergo developmental changes. "+ '\n' +  '\n' + "ref: Panlilio, L., Goldberg, S. and Justinova, Z. (2015), Cannabinoid abuse and addiction: Clinical and preclinical findings. Clin. Pharmacol. Ther., 97: 616-627. ", "Risk for cannabis dependence is measured to be around 9%; 16% among adolescents. Addiction to cannabis is determined by both environmental and genetic factors, and relapse rates for Cannabis Use Disorder are similar to other drugs. "+ '\n' +  '\n' + "ref: Panlilio, L., Goldberg, S. and Justinova, Z. (2015), Cannabinoid abuse and addiction: Clinical and preclinical findings. Clin. Pharmacol. Ther., 97: 616-627. ", "There are high rates of comorbidity between Cannabis Use Disorder and psychiatric disorders such as schizophrenia, depression, bipolar disorders, anxiety disorders, and others. "+ '\n' +  '\n' + "ref: Panlilio, L., Goldberg, S. and Justinova, Z. (2015), Cannabinoid abuse and addiction: Clinical and preclinical findings. Clin. Pharmacol. Ther., 97: 616-627. ", "Heavy cannabis use can cause neurocognitive deficits that last for several days or weeks post consumption. Memory and attention impairments may also persist. "+ '\n' +  '\n' + "ref: Panlilio, L., Goldberg, S. and Justinova, Z. (2015), Cannabinoid abuse and addiction: Clinical and preclinical findings. Clin. Pharmacol. Ther., 97: 616-627. ", "So far, the most successful treatment models for cannabis use disorder are cognitive-behavioral therapies, motivational enhancement therapies, contingency management, and family-based therapies. "+ '\n' +  '\n' + "ref: Panlilio, L., Goldberg, S. and Justinova, Z. (2015), Cannabinoid abuse and addiction: Clinical and preclinical findings. Clin. Pharmacol. Ther., 97: 616-627. ", "The most successful medication tested for Cannabis Use Disorder is replacement therapy with synthetic THC, which displayed a reduction of withdrawal symptoms but no effect on administration or relapse. "+ '\n' +  '\n' + "ref: Panlilio, L., Goldberg, S. and Justinova, Z. (2015), Cannabinoid abuse and addiction: Clinical and preclinical findings. Clin. Pharmacol. Ther., 97: 616-627. ", "Given the findings that the opioid and cannabinoid systems can influence each other, opioid treatment practices may potentially be effective for Cannabis Use Disorder as well. "+ '\n' +  '\n' + "ref: Panlilio, L., Goldberg, S. and Justinova, Z. (2015), Cannabinoid abuse and addiction: Clinical and preclinical findings. Clin. Pharmacol. Ther., 97: 616-627. ", "Drug discrimination procedures in rats indicate that nicotine and morphine potentiate the effects of THC. "+ '\n' +  '\n' + "ref: Panlilio, L., Goldberg, S. and Justinova, Z. (2015), Cannabinoid abuse and addiction: Clinical and preclinical findings. Clin. Pharmacol. Ther., 97: 616-627. ", " THC increases dopamine neurons, but these cells can develop tolerance after repeated exposure. "+ '\n' +  '\n' + "ref: Panlilio, L., Goldberg, S. and Justinova, Z. (2015), Cannabinoid abuse and addiction: Clinical and preclinical findings. Clin. Pharmacol. Ther., 97: 616-627. ", "In rats, tolerance to and dependence on cannabis developed after daily exposure for 3-14 days. "+ '\n' +  '\n' + "ref: Panlilio, L., Goldberg, S. and Justinova, Z. (2015), Cannabinoid abuse and addiction: Clinical and preclinical findings. Clin. Pharmacol. Ther., 97: 616-627. ", "More research is needed on the mechanisms behind  a common gateway progression from alcohol use to cannabis use to drugs such as cocaine and heroin. "+ '\n' +  '\n' + "ref: Panlilio, L., Goldberg, S. and Justinova, Z. (2015), Cannabinoid abuse and addiction: Clinical and preclinical findings. Clin. Pharmacol. Ther., 97: 616-627. ", "Certain antagonists have been proven successful in lowering THC consumption and showing resistance in individuals motivated to quit and comply with antagonist treatment (but not in those who don’t!). "+ '\n' +  '\n' + "ref: Panlilio, L., Goldberg, S. and Justinova, Z. (2015), Cannabinoid abuse and addiction: Clinical and preclinical findings. Clin. Pharmacol. Ther., 97: 616-627. ", "Non-chronic cannabis users that consumed a joint of marijuana experienced feelings of intoxication, confusion, 'high', or environment changes, and those feelings persisted even 3 hours after the peak of THC (the component in cannabis that gets you 'high') concentration in the blood stream. "+ '\n' +  '\n' + "ref: Battistella G, Fornari E, Thomas A, Mall JF, Chtioui H, et al. (2013) Weed or Wheel! fMRI, Behavioural, and Toxicological Investigations of How Cannabis Smoking Affects Skills Necessary for Driving. PLOS ONE 8(1): e52545.", "Cannabis significantly decreases psychomotor skills by altering the main brain networks involved in cognition and resulting in lack of recruitment of attention, making it extremely dangerous to drive post THC consumption. "+ '\n' +  '\n' + "ref: Battistella G, Fornari E, Thomas A, Mall JF, Chtioui H, et al. (2013) Weed or Wheel! fMRI, Behavioural, and Toxicological Investigations of How Cannabis Smoking Affects Skills Necessary for Driving. PLOS ONE 8(1): e52545.", "Risk of onset of psychosis was not associated with magnitude of marijuana consumption, but rather progression of use frequency. Progression to daily cannabis use and/or daily tobacco use showed an increased risk of onset of psychosis. In addition, progression to daily use increased the risk of onset of psychosis more in females than in males. "+ '\n' +  '\n' + "ref: Compton, Michael T., et al. “Association of Pre-Onset Cannabis, Alcohol, and Tobacco Use With Age at Onset of Prodrome and Age at Onset of Psychosis in First-Episode Patients.” American Journal of Psychiatry, vol. 166, no. 11, American Psychiatric Association, Nov. 2009, pp. 1251–57. ", "Researchers suggest that early treatment of cannabis use may delay onset of psychosis. Earlier onset is generally a cause for greater cognitive impairments, increased severity of disabilities and symptoms, decreased responsiveness to antipsychotics, and greater likelihood of rehospitalization, and for such, delaying onset by reducing adolescent substance use is of significant importance. "+ '\n' +  '\n' + "ref: Compton, Michael T., et al. “Association of Pre-Onset Cannabis, Alcohol, and Tobacco Use With Age at Onset of Prodrome and Age at Onset of Psychosis in First-Episode Patients.” American Journal of Psychiatry, vol. 166, no. 11, American Psychiatric Association, Nov. 2009, pp. 1251–57.", "Results from MRI scans analyses suggest a state of hyperconnectivity in chronic cannabis users as compared to occasional users. Analyses also show that in chronic cannabis users, increments in connectivity within a network were matched by decrements in connectivity between networks, highlighting that consistent history of cannabis use may be more impactful than previously thought. "+ '\n' +  '\n' + "ref: Ramaekers, J.G., Mason, N.L., Toennes, S.W. et al. Functional brain connectomes reflect acute and chronic cannabis use. Sci Rep 12, 2449 (2022). ", "Findings suggest a reduction of top-down attention control and motor coordination as well as increased “internalization of attention directed at monitoring of mind wandering or spontaneous cognition” during cannabis intoxication. "+ '\n' +  '\n' + "ref: Ramaekers, J.G., Mason, N.L., Toennes, S.W. et al. Functional brain connectomes reflect acute and chronic cannabis use. Sci Rep 12, 2449 (2022). ", "Hyperconnectivity WITHIN ALL brain networks was found to be a significant differentiator between chronic and occasional users, suggesting that, specifically in chronic cannabis users, functional hyperconnectivity is not restricted to local brain regions. "+ '\n' +  '\n' + "ref: Ramaekers, J.G., Mason, N.L., Toennes, S.W. et al. Functional brain connectomes reflect acute and chronic cannabis use. Sci Rep 12, 2449 (2022).","Research findings show that exclusively chronic effects might reflect an additional response to repeated cannabis use, in line with previous findings that chronic cannabis users can develop partial tolerance to the impairing effects of cannabis. "+ '\n' + '\n' +  '\n' + "ref:Ramaekers, J.G., Mason, N.L., Toennes, S.W. et al. Functional brain connectomes reflect acute and chronic cannabis use. Sci Rep 12, 2449 (2022). ", "Regardless of the type of imaging, analysis, or sample, consistency among “male” and “female” traits are uncommon, showing that human brains cannot be categorized into “male brain” or “female brain”. Furthermore, the magnitude of consistency in regions of the brain varied between data sets, suggesting a dependence on environmental factors. "+ '\n' +  '\n' + "ref: Joel, Daphna, et al. “Sex Beyond the Genitalia: The Human Brain Mosaic.” Proceedings of the National Academy of Sciences of the United States of America, vol. 112, no. 50, National Academy of Sciences, Dec. 2015, pp. 15468–73."]
    while user_wants_to_play: 
        #creates coordinates list
        coordinate1, coordinate2, bot_coordinate, user_coordinate, bot, user = create_lists()
        #initalizes variable for number of coordinates selected
        check_select = 0
        #creates boolean variable
        number = 0
        waiting_for_user_selection = True
        #repeats until the user selects 3 coordinates.
        print(coordinate1.coordinate_list)
        while waiting_for_user_selection:
            number = number + 1
            #asks user for ship coordinates
            user_choice = input("Please select a coordinate from the coordinate list for your number " + str(number) + " ship. ")
            if user_choice not in user_coordinate.coordinate_list:
                #if the user doesn't select a coordinate properly this code will run
                print("that is not one of the coordinates you can select.")
                number = number - 1
            else:
                #if the user select a valid coordinate, it will be added to a new list
                check_select = check_select + 1
                user.coordinate_selection.append(user_choice)
                user_coordinate.coordinate_list.remove(user_choice)
                if check_select == 5:
                    os.system('clear')
                    print("Your ships are placed on the spots: " + str(user.coordinate_selection))
                    time.sleep(1.5)
                    print("")
                    line_enter = input("Press enter to continue onto the game. ")
                    waiting_for_user_selection = False
        bot_check = 0
        waiting_for_bot_selection = True
        #repeat until the bot selects 5 battleships coordinates
        while waiting_for_bot_selection:
            bot_check = bot_check + 1
            if bot_check == 5:
                waiting_for_bot_selection = False
            #the bot will randomly select a coordinate from its selection list
            index = random.choice(bot_coordinate.coordinate_list)
            bot.coordinate_selection.append(index)
            bot_coordinate.coordinate_list.remove(index)
        os.system('clear')
        #set default for round score
        user_score = 0
        bot_score = 0
        user_plays_battleship = True
        #repeat until the game is over(when someone destroys the opponents ships)
        while user_plays_battleship:
            print("Your ships are placed on the spots: " + str(user.coordinate_selection))
            print(" ")
            print(user.selection_list)
            #user selects coordinates to attack the bot
            user.user_select_coordinate()  
            user.selection_list.remove(user.select)
            #if the user selects a coordinate on one of the bots ships
            if user.select in bot.coordinate_selection:
                user_score = user_score + 1
                bot.coordinate_selection.remove(user.select)
                print("The user hit the bots ship on the coordinate " + user.select)
                print(" ")
                print("The bot now has " + str(len(bot.coordinate_selection)) + " ships left.")
                time.sleep(4)
                os.system('clear')
                print("DID YOU KNOW? ")
                print("")
                randomchoice = random.choice(faxList)
                print(randomchoice)
                faxList.remove(randomchoice)
                time.sleep(4)
                print(" ")
                input("press enter to continue")
            #if the user misses
            else:
                print("The user did not hit any of the bots ships.")
                time.sleep(3)
            os.system('clear')
            #bot slects coordinates to attack the user
            bot.bot_select_coordinate()
            bot.selection_list.remove(bot.select)
            print("")
            time.sleep(1)
            #if the bot selects a coordinate on one of the users ships
            if bot.select in user.coordinate_selection:
                bot_score = bot_score + 1
                user.coordinate_selection.remove(bot.select)
                print("The bot hit the users ship on the coordinate " + bot.select)
                print(" ")
                print("The user now has " + str(len(user.coordinate_selection)) + " ships left.")
                time.sleep(4)
                os.system('clear')
                print("DID YOU KNOW? ")
                print("")
                randomchoice = random.choice(faxList)
                print(randomchoice)
                faxList.remove(randomchoice)
                time.sleep(5)
                print(" ")
           #if the bot misses     
            else:
                print("The bot did not hit any of the users ships.")
            time.sleep(1)
            print("")
            l1n3 = input("Please press enter to continue")
            os.system('clear')
            #display round score
            score = str(user_score) + "-" + str(bot_score)
            print("The score is now " + score)
            time.sleep(2)
            os.system('clear')
            #check for winner
            if "5-5" in score:
                user_plays_battleship = False
                winner = "tie"    
            else:
                #if the user won:
                if user_score == 5:
                    user_plays_battleship = False
                    winner = 0
                #if the bot won:
                if bot_score == 5:
                    user_plays_battleship = False
                    winner = 1
                    

        #announce winner
        announce_winner(final_user_score, final_bot_score, winner, user_name)
       
        #ask user to replay
        user_wants_to_play = ask_replay(user_name, user_wants_to_play)
    
      
    
    
    #announce final results
    announce_final_results(user_name, final_user_score, final_bot_score)
  
        


main()