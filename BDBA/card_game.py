'''
Card Game in Python
Game Mechanics: The game is a card game between two entities. The game can be played between two humans or a human and a machine. Choose a set of characters(fictional or real) and their characteristics. Characteristics are represented by a specific numeric value indicating the strength of the characteristic (strenghts may be indicated by negative or positive numeric value). Each card contains only one character and its characteristics.
Characteristics must be same across all characters but can vary in strength. No characteristic across characters can share the same value.
The two entities will be called Player 1 and Player 2 hence.
Distribute the cards equally among player 1 and player 2 face down such that the players cannot see the characters they have been given. Simulate a dice throw by both player 1 and player 2 where the highest number starts first.
Constraints: Each player gets two special spells (God and Resurrect) . These spells are not associated to the characters but is assoicated to the player itself.
Each round is played as below:
Player 1 : chooses the first card from the deck and can: play a charactertistic he wishes to challenge player 2 with . Player 2 chooses the first card in his deck and compares the charactertistic. The round is won by the Player whose characteristic weighs more and gets 1 point. The 2 cards are then kept faced down on a different deck called ‘outdated'(the cards go in the outdated deck in a random order). In round 2 , The player who won the previous round begins by choosing the next card in his deck and the round proceeds as above.
Spells:
In each round a player can decide to play the God spell or the Resurrect spell along with challenging with a characteristic. God Spell: After choosing the next card and characteristic on his deck, player 1 can play the God spell allowing the player to force a card number to be played by the Player 2. Player 1 can choose any card number he wants and player 2 should then compare the charactestic on the choosen card.
Resurrect Spell: Before choosing the next card and characteristic, player 1 can choose Resurrect spell. Choosing Resurrect will create a random number and the card at the that random number position from the ‘outdated’ deck will be choosen. The card present at the random number at the ‘outdated’ deck will be added back to the top of the player deck. The player must then play this card.
When Player 1 plays the God spell , Player 2 cannot play the God spell as he is forced to choose the card , however player 2 can play the Resurrect spell and add a new card to the top of his deck. Player 1 can then force the resurrected card to be choosen or can go with his earlier choice.
God and Resurrect spell can only be played once by each Player. 
The Game ends when all cards of one / both players have been played.
The game is won by the player with maximum points. 
'''

import random
import time
from IPython.display import clear_output

#Dice roll Logic
def dice():
#    clear_output()

    while True:
        dicep1 = input("Player 1: Enter 'Y' to roll dice.")
        if valid4(dicep1): break
    if dicep1 == 'Y':
        dicep1value = random.randint(1,6)
        print(f"Player 1 dice value is: {dicep1value}")
    while True:
        dicep2 = input("Player 2: Enter 'Y' to roll dice.")
        if valid4(dicep2): break
    if dicep2 == 'Y':
        dicep2value = random.randint(1,6)
        print(f"Player 2 dice value is: {dicep2value}")
    if dicep1value > dicep2value:
        time.sleep(2)
#        clear_output()
        print("Player 1 play first")
        time.sleep(2)
#        clear_output()
        playfirst = 1
        return playfirst
    elif dicep1value < dicep2value:
        time.sleep(2)
#        clear_output()
        print("Player 2 play first")
        time.sleep(2)
#        clear_output()
        playfirst = 2
        return playfirst
    else:
        print("Player 1 and Player 2 received same number. Roll Dice again!")
        time.sleep(5)
        dice()
    

def share():
    cards =[["Goblins",100,190],["Bats",110,180],["Bomber",120,170],["Knight",130,160],["Fireball",140,150],
            ["Valkyrie",150,140],["Witch",160,130],["Tower",170,120],["Dragon",180,110],["Prince",190,100]]
    total = []
    cardsp1 = []
    cardsp2 = []
    for i in range(0,5):
        c1 = False
        while(c1 == False):
            x = random.randint(0,9)
            if x not in total:
                cardsp1.append(cards[x])
                total.append(x)
                c1 = True

        c2 = False
        while(c2 == False):
            x = random.randint(0,9)
            if x not in total:
                cardsp2.append(cards[x])
                total.append(x)
                c2 = True
    return cardsp1, cardsp2

def valid1(inp):
    if ((inp == 'N') or (inp == 'Y')):
        return True
    return False

def valid2(inp):
    if ((inp == 1) or (inp == 2)):
        return True
    return False
def valid3(inp):
    if ((inp == 'E') or (inp == 'R')):
        return True
    return False
def valid4(inp):
    if (inp == 'Y'):
        return True
    return False
def valid5(inp,rang):
    if inp in range(0,rang):
        return True
    return False

#Home Page design
def home():
       
#    clear_output()
    print("Welcome to 'Clash Royale' Game !!!")
    print("\nCharacter Life   Power")
    print("------------------------------")
    print('Goblins:  100    190\nBats:     110    180\nBomber:   120    170\nKnight:   130    160\nFireball: 140    150' +
          '\nValkyrie: 150    140\nWitch:    160    130\nTower:    170    120\nDragon:   180    110\nPrince:   190    100')
    time.sleep(2)
    game = (input("Enter 'Y' to start the Game.") == 'Y')     
    return game

def classroyale():
    cardsp1, cardsp2 = share()
    game = home()
    if game:
        playfirst = dice()
        
        firstround = True
        rounds = 1
        outdated = []
        godp1 = True
        godp2 = True
        resp1 = True
        resp2 = True
        char  = 0
        
        wonp1 = 0
        wonp2 = 0

        while((len(cardsp1) > 0) and (len(cardsp2) > 0)):
            print(f"Round:'{rounds}' ")
            rounds += 1 
       
            if playfirst == 1:
#                clear_output()
                if firstround == False:
                    if resp1 == True:
                            
                        while True:
                            bef1p1 = input("Player 1: Do you want to use Resurrect Spell? 'Y' for Yes & 'N' for No. ")
                            if valid1(bef1p1): break
                        
                        if bef1p1 == 'Y':
                            bef2p1 = random.randint(0,(len(outdated)-1))
                            cardsp1.insert(0,outdated[bef2p1])
                            outdated.pop(bef2p1)
                            resp1 = False
                                 
                print(f"Player 1: Your first card of {len(cardsp1)} cards is: '{cardsp1[0][0]}' with Life: '{cardsp1[0][1]}' & Attack: '{cardsp1[0][2]}'")
                checkp1 = cardsp1[0]
                
                while True:
                    try:
                        char = int(input("Player 1: Select characteristic to challenge: '1' for Life & '2' for Attack: "))
                        if valid2(char): break
                    except ValueError:
                        print("Wrong input")

                if godp1 == True:
                    
                    while True:
                        zp1 = input(f"Player 1: Do you want to use God Spell? 'Y' for Yes & 'N' for No. ")
                        if valid1(zp1): break
                    if zp1 == 'Y':
                        while True:
                            try:
                                ap1 = int(input(f"Player 1: Choose Player 2 card from {len(cardsp2)} cards(0 to {len(cardsp2)-1})"))
                                if valid5(ap1,len(cardsp2)): break
                            except ValueError:
                                print("Wrong input")

                        if firstround == False:
                            if resp2 == True:
                                while True:
                                    out2p2 = input("Player 2: Do you want to use Resurrect Spell? 'Y' for Yes & 'N' for No. ")
                                    if valid1(out2p2): break
                                if out2p2 == 'Y':
                                    out1p2 = random.randint(0,(len(outdated)-1))
                                    cardsp2.insert(0,outdated[out1p2])
                                    outdated.pop(out1p2)
                                    ap1 = ap1 + 1
                                    while True:
                                        out3p1 = input("Player 1: what is your choice? 'R' for resurrected card & 'E' for Earlier card. ")
                                        if valid3(out3p1): break
                                        
                                    if out3p1 == 'R':
                                        print(f"Player 2: Your card is: '{cardsp2[0][0]}' with Life: '{cardsp2[0][1]}' & Attack: '{cardsp2[0][2]}'")
                                        checkp2 = cardsp2[0]

                                    elif out3p1 == 'E':
                                        print(f"Player 2: Your card is: '{cardsp2[ap1][0]}' with Life: '{cardsp2[ap1][1]}' & Attack: '{cardsp2[ap1][2]}'")
                                        checkp2 = cardsp2[ap1]

                                    resp2 = False
                                elif out2p2 == 'N':
                                    print(f"Player 2: Your card is: '{cardsp2[ap1][0]}' with Life: '{cardsp2[ap1][1]}' & Attack: '{cardsp2[ap1][2]}'")
                                    checkp2 = cardsp2[ap1]

                            else:
                                print(f"Player 2: Your card is: '{cardsp2[ap1][0]}' with Life: '{cardsp2[ap1][1]}' & Attack: '{cardsp2[ap1][2]}'")
                                checkp2 = cardsp2[ap1]

                        else:
                            print(f"Player 2: Your card is: '{cardsp2[ap1][0]}' with Life: '{cardsp2[ap1][1]}' & Attack: '{cardsp2[ap1][2]}'")
                            checkp2 = cardsp2[ap1]

                        godp1 = False

                    elif zp1 == 'N':
                        
                        if firstround == False: 
                            if resp2 == True:
                                while True:
                                    out2p2 = input("Player 2: Do you want to use Resurrect Spell? 'Y' for Yes & 'N' for No. ")
                                    if valid1(out2p2): break
                                if out2p2 == 'Y':
                                    out1p2 = random.randint(0,(len(outdated)-1))
                                    cardsp2.insert(0,outdated[out1p2])
                                    outdated.pop(out1p2)
                                    resp2 = False

                        print(f"Player 2: Your card is: '{cardsp2[0][0]}' with Life: '{cardsp2[0][1]}' & Attack: '{cardsp2[0][2]}'")
                        checkp2 = cardsp2[0]
                               
                else:
                    if firstround == False: 
                        if resp2 == True:

                            while True:
                                out2p2 = input("Player 2: Do you want to use Resurrect Spell? 'Y' for Yes & 'N' for No. ")
                                if valid1(out2p2): break
                            if out2p2 == 'Y':
                                out1p2 = random.randint(0,(len(outdated)-1))
                                cardsp2.insert(0,outdated[out1p2])
                                outdated.pop(out1p2)
                                resp2 = False

                    print(f"Player 2: Your card is: '{cardsp2[0][0]}' with Life: '{cardsp2[0][1]}' & Attack: '{cardsp2[0][2]}'")
                    checkp2 = cardsp2[0]

            else:

                if firstround == False:
                    if resp2 == True:
                    
                        while True:
                            bef1p2 = input("Player 2: Do you want to use Resurrect Spell? 'Y' for Yes & 'N' for No. ")
                            if valid1(bef1p2): break
                        if bef1p2 == 'Y':
                            bef2p2 = random.randint(0,(len(outdated)-1))
                            cardsp2.insert(0,outdated[bef2p2])
                            outdated.pop(bef2p2)
                            resp2 = False
                
                print(f"Player 2: Your first card of {len(cardsp2)} cards is: '{cardsp2[0][0]}' with Life: '{cardsp2[0][1]}' & Attack: '{cardsp2[0][2]}'")
                checkp2 = cardsp2[0]
  
                while True:
                    try:
                        char = int(input("Player 2: Select characteristic to challenge: '1' for Life & '2' for Attack:- "))
                        if valid2(char): break
                    except ValueError:
                        print("Wrong input")
                
                if godp2 == True:
                    while True:
                        zp2 = input(f"Player 2: Do you want to use God Spell? 'Y' for Yes & 'N' for No. ")
                        if valid1(zp2): break
                    if zp2 == 'Y':
                        while True:
                            try:
                                ap2 = int(input(f"Player 2: Choose Player 1 card from {len(cardsp1)} cards(0 to {len(cardsp1)-1})"))
                                if valid5(ap2,len(cardsp1)): break
                            except ValueError:
                                print("Wrong input")

                        if firstround == False:
                            if resp1 == True:
                                while True:
                                    out2p1 = input("Player 1: Do you want to use Resurrect Spell? 'Y' for Yes & 'N' for No. ")
                                    if valid1(out2p1): break
                                if out2p1 == 'Y':
                                    out1p1 = random.randint(0,(len(outdated)-1))
                                    cardsp1.insert(0,outdated[out1p1])
                                    outdated.pop(out1p1)
                                    ap2 = ap2 + 1
                                    while True:
                                        out3p2 = input("Player 2: what is your choice? 'R' for resurrected card & 'E' for Earlier card. ")
                                        if valid3(out3p2): break
                                    if out3p2 == 'R':
                                        print(f"Player 1: Your card is: '{cardsp1[0][0]}' with Life: '{cardsp1[0][1]}' & Attack: '{cardsp1[0][2]}'")
                                        checkp1 = cardsp1[0]

                                    elif out3p2 == 'E':
                                        print(f"Player 1: Your card is: '{cardsp1[ap2][0]}' with Life: '{cardsp1[ap2][1]}' & Attack: '{cardsp1[ap2][2]}'")
                                        checkp1 = cardsp1[ap2]

                                    resp1 = False
                                elif out2p1 == 'N':
                                    print(f"Player 1: Your card is: '{cardsp1[ap2][0]}' with Life: '{cardsp1[ap2][1]}' & Attack: '{cardsp1[ap2][2]}'")
                                    checkp1 = cardsp1[ap2]

                            else:
                                print(f"Player 1: Your card is: '{cardsp1[ap2][0]}' with Life: '{cardsp1[ap2][1]}' & Attack: '{cardsp1[ap2][2]}'")
                                checkp1 = cardsp1[ap2]

                        else:
                            print(f"Player 1: Your card is: '{cardsp1[ap2][0]}' with Life: '{cardsp1[ap2][1]}' & Attack: '{cardsp1[ap2][2]}'")
                            checkp1 = cardsp1[ap2]

                        godp2 = False

                    elif zp2 == 'N':
                        
                        if firstround == False:
                            if resp1 == True:
                                while True:
                                    out2p1 = input("Player 1: Do you want to use Resurrect Spell? 'Y' for Yes & 'N' for No. ")
                                    if valid1(out2p1): break
                                if out2p1 == 'Y':
                                    out1p1 = random.randint(0,(len(outdated)-1))
                                    cardsp1.insert(0,outdated[out1p1])
                                    outdated.pop(out1p1)
                                    resp1 = False

                        print(f"Player 1: Your card is: '{cardsp1[0][0]}' with Life: '{cardsp1[0][1]}' & Attack: '{cardsp1[0][2]}'")
                        checkp1 = cardsp1[0]
                               
                else:
                    if firstround == False:
                        if resp1 == True:
                                while True:
                                    out2p1 = input("Player 1: Do you want to use Resurrect Spell? 'Y' for Yes & 'N' for No. ")
                                    if valid1(out2p1): break
                                if out2p1 == 'Y':
                                    out1p1 = random.randint(0,(len(outdated)-1))
                                    cardsp1.insert(0,outdated[out1p1])
                                    outdated.pop(out1p1)
                                    resp1 = False

                        print(f"Player 1: Your card is: '{cardsp1[0][0]}' with Life: '{cardsp1[0][1]}' & Attack: '{cardsp1[0][2]}'")
                        checkp1 = cardsp1[0]

            if checkp1[char] > checkp2[char]:
                print("Player 1 won the point")
                wonp1 +=1
                playfirst = 1
            elif checkp1[char] < checkp2[char]:
                print("Player 2 won the point")
                wonp2 +=1
                playfirst = 2
            time.sleep(3)
            
            outdated.append(checkp1)
            cardsp1.remove(checkp1)
            outdated.append(checkp2)
            cardsp2.remove(checkp2)
                
            firstround = False
            print(f"Player 1 Points:{wonp1} & Player 2 Points:{wonp2}")
            print("++++++++++++++++++++++++++++++++++++++++++++++")        
        
        if wonp1 > wonp2:
#            clear_output()
            print(f"Player 1 won the Game with {wonp1} points")
        elif wonp1 < wonp2:
#            clear_output()
            print(f"Player 2 won the Game with {wonp2} points")
        else:
#            clear_output()
            print("Game Draw!!!")
  
    else:
#        clear_output()
        print("Come Back soon!!!")


classroyale()
