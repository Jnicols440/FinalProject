import random
import time

def shuffleDeck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suits = ['♠', '♦', '♥', '♣']
    deck = [(rank + suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def dealHands(deck):
    for i in range(0,52,4):
        player.append(deck[i])
        comp1.append(deck[i+1])
        comp2.append(deck[i+2])
        comp3.append(deck[i+3])
                    

def printHand(hand):
    time.sleep(1)
    print("\nYour Hand:")
    for card in hand:
        print(',-----.',end=' ')
    print()
    for card in hand:
        rank = card[0]
        print(f'|{rank}    |',end=' ')
    print()
    for card in hand:
        print(f'|  {card[-1]}  |',end=' ')
    print()
    for card in hand:
        rank = card[0]
        print(f'|    {rank}|',end=' ')
    print()
    for card in hand:
        print('`-----\'',end=' ')
    print()

def sortHand(hand):
    c_list = []
    d_list = []
    s_list = []
    h_list = []
    for card in hand:
        if '♣' in card:
            c_list.append(card)
        elif '♦' in card:
            d_list.append(card)
        elif '♠' in card:
            s_list.append(card)
        elif '♥' in card:
            h_list.append(card)
    hand.clear()
    hand.extend(c_list + s_list + d_list + h_list)

def playerTurn(suit):
    turn = True
    printHand(player)
    place = input("Which card would you like to place down?\n")
    place = place.upper()
    if len(player) == 13:
        while place == 'QS':
            print('You cannot place the Queen of Spades on the first turn')
            place = input("Which card would you like to place down?\n")
            place = place.upper()
    while turn:
        if place[-1] == 'S':
            place = place[0] + '♠'
        elif place[-1] == 'D':
            place = place[0] + '♦'
        elif place[-1] == 'C':
            place = place[0] + '♣'
        elif place[-1] == 'H':
            place = place[0] + '♥'
        if place not in player:
            print('You must pick a card from your hand')
            place = input("Which card would you like to place down?\n")
        elif suit not in place and any(suit in card for card in player):
            print("You must place a card matching the suit of the first player")
            place = input(("Which card would you like to place down?\n"))
        else:
            turn = False
    time.sleep(1)
    print(f"""
{name}:
,-----.
|{place[0]}    |
|  {place[-1]}  |
|    {place[0]}|
`-----'""", end='')

    player.remove(place)

    return place

def round1():
    if '2♣' in player:
        return playerFirst()
    elif '2♣' in comp1:
        return comp1First()
    elif '2♣' in comp2:
        return comp2First()
    elif '2♣' in comp3:
        return comp3First()

def winningTrick(trick, suit):
    suited = []
    numbers = []

    for cards in trick:
        if suit in cards:
            suited.append(cards)

    for cards in suited:
        if 'T' in cards:
            numbers.append(10)
        elif 'J' in cards:
            numbers.append(11)
        elif 'Q' in cards:
            numbers.append(12)
        elif 'K' in cards:
            numbers.append(13)
        elif 'A' in cards:
            numbers.append(14)
        else:
            numbers.append(int(cards[0]))

    winner = max(numbers)

    if winner == 10:
        winner = 'T'
    elif winner == 11:
        winner = 'J'
    elif winner == 12:
        winner = 'Q'
    elif winner == 13:
        winner = 'K'
    elif winner == 14:
        winner = 'A'
    else:
        winner = str(winner)

    return winner + suit

def computerTurn(comp, suit):
    comp_choices = []
    

    for i in comp:
        if suit in i:
            comp_choices.append(i)

    if comp_choices == []:
        place = random.choice(comp)
        if len(comp) == 13:
            while place == 'Q♠':
                place = random.choice(comp)
    else:
        place = random.choice(comp_choices)

    if comp == comp1:
        opponent = 'George'
    elif comp == comp2:
        opponent = 'Pablo'
    elif comp == comp3:
        opponent = 'Roman'

    time.sleep(1)
    print(f"""
{opponent}:
,-----.
|{place[0]}    |
|  {place[-1]}  |
|    {place[0]}|
`-----'""", end='')

    comp.remove(place)

    return place

def computerFirst(comp):
    if '2♣' in comp:
        place = '2♣'

    else:
        has = False
        for card in comp:
                if '♥' not in card:
                    has = True
        if '♥' in hearts or has != True:
            place = random.choice(comp)

        else:
            place = random.choice(comp)
            while '♥' in place:
                place = random.choice(comp)
    if comp == comp1:
        opponent = 'George'
    elif comp == comp2:
        opponent = 'Pablo'
    elif comp == comp3:
        opponent = 'Roman'

    time.sleep(1)
    print(f"""
{opponent}:
,-----.
|{place[0]}    |
|  {place[-1]}  |
|    {place[0]}|
`-----'""", end='')

    comp.remove(place)

    return place

def comp1First():
    place1 = computerFirst(comp1)

    place2 = computerTurn(comp2, place1[1])

    place3 = computerTurn(comp3, place1[1])

    place4 = playerTurn(place1[1])

    trick = [place1, place2, place3, place4]

    winner = winningTrick(trick, place1[1])

    first = pickUpTrick(winner, place1, place2, place3, place4)

    return first

def comp2First():
    place2 = computerFirst(comp2)

    place3 = computerTurn(comp3, place2[1])

    place4 = playerTurn(place2[1])

    place1 = computerTurn(comp1, place2[1])

    trick = [place1, place2, place3, place4]

    winner = winningTrick(trick, place2[1])

    first = pickUpTrick(winner, place1, place2, place3, place4)

    return first

def comp3First():
    place3 = computerFirst(comp3)

    place4 = playerTurn(place3[1])

    place1 = computerTurn(comp1, place3[1])

    place2 = computerTurn(comp2, place3[1])

    trick = [place1, place2, place3, place4]

    winner = winningTrick(trick, place3[1])

    first = pickUpTrick(winner, place1, place2, place3, place4)

    return first

def playerFirst():
    if '2♣' in player:
        place4 = '2♣'
    else:
        printHand(player)
        while True:
            place4 = input('Which card would you like to place down?\n')
            place4 = place4.upper()
            if place4[-1] == 'S':
                place4 = place4[0] + '♠'
            elif place4[-1] == 'D':
                place4 = place4[0] + '♦'
            elif place4[-1] == 'C':
                place4 = place4[0] + '♣'
            elif place4[-1] == 'H':
                place4 = place4[0] + '♥'
            if place4 not in player:
                print('You must place a card from your hand')
            elif '♥' in place4 and ('♥' not in hearts or not any('♥' in card for card in player)):
                print('Hearts are not broken, you cannot yet place a heart first')
            else:
                break

    time.sleep(1)
    print(f"""
{name}:
,-----.
|{place4[0]}    |
|  {place4[-1]}  |
|    {place4[0]}|
`-----'""", end='')

    player.remove(place4)
    
    place1 = computerTurn(comp1, place4[1])
    place2 = computerTurn(comp2, place4[1])
    place3 = computerTurn(comp3, place4[1])

    trick = [place1, place2, place3, place4]
    winner = winningTrick(trick, place4[1])

    first = pickUpTrick(winner, place1, place2, place3, place4)

    return first

def pickUpTrick(winner, place1, place2, place3, place4):
    has = True
    time.sleep(1)
    for cards in hearts:
        if '♥' in cards:
            has = False
    if has:
        hearts.append(place1[1])
        hearts.append(place2[1])
        hearts.append(place3[1])
        hearts.append(place4[1])
        for cards in hearts:
            if '♥' in cards:
                print('\nHEARTS ARE BROKEN')
                break

    if winner == place1:
        winnings1.append(place1)
        winnings1.append(place2)
        winnings1.append(place3)
        winnings1.append(place4)
        print('\nGeorge picked up the trick')
        return 1

    elif winner == place2:
        winnings2.append(place1)
        winnings2.append(place2)
        winnings2.append(place3)
        winnings2.append(place4)
        print('\nPablo picked up the trick')
        return 2

    elif winner == place3:
        winnings3.append(place1)
        winnings3.append(place2)
        winnings3.append(place3)
        winnings3.append(place4)
        print('\nRoman picked up the trick')
        return 3

    elif winner == place4:
        winningsP.append(place1)
        winningsP.append(place2)
        winningsP.append(place3)
        winningsP.append(place4)
        print('\nYou picked up the trick')
        return 4
        
def scoreBoard(winningsP, winnings1, winnings2, winnings3):
    scoreP = 0
    score1 = 0
    score2 = 0
    score3 = 0
    for cards in winningsP:
        if '♥' in cards:
            scoreP += 1
        elif cards == 'Q♠':
            scoreP += 13
    

        
    for cards in winnings1:
        if '♥' in cards:
            score1 += 1
        elif cards == 'Q♠':
            score1 += 13


    for cards in winnings2:
        if '♥' in cards:
            score2 += 1
        elif cards == 'Q♠':
            score2 += 13


    for cards in winnings3:
        if '♥' in cards:
            score3 += 1
        elif cards == 'Q♠':
            score3 += 13

    if scoreP == 26:
        print('You Shot The Moon!')
        scoreP = 0
        score1 = 26
        score2 = 26
        score3 = 26
    elif scoreP == 26:
        print(f'{George} Shot The Moon!')
        scoreP = 26
        score1 = 0
        score2 = 26
        score3 = 26
    elif scoreP == 26:
        print(f'{Pablo} Shot The Moon!')
        scoreP = 26
        score1 = 26
        score2 = 0
        score3 = 26
    elif scoreP == 26:
        print(f'{Roman} Shot The Moon!')
        scoreP = 26
        score1 = 26
        score2 = 26
        score3 = 0

    if 'J♦' in winningsP:
        scoreP -= 10
    elif 'J♦' in winnings1:
        score1 -= 10
    elif 'J♦' in winnings2:
        score2 -= 10
    elif 'J♦' in winnings3:
        score3 -= 10
    

    print(f'{name} gained: {scoreP} points')
    print(f'George gained: {score1} points')
    print(f'Pablo gained: {score2} points')
    print(f'Roman gained: {score3} points')
    return scoreP, score1, score2, score3

input('Welcome to Hearts\nPress Enter to Play!')
maxScore = 0
name = input("What is your name?\n")
print("""
INSTRUCTIONS:

WHAT IS THE HEARTS CARD GAME:
    Hearts is a classic “trick taking” card game
    Where players try to avoid collecting points.

OBJECTIVE:
    To have the lowest score at the end of the game.
    
PLAYERS:
    The game is played with 4 players
    Each holding 13 cards of a standard 52 card deck

HOW TO PLAY->
PLAY THE FIRST CARD OF THE FIRST TRICK:
    The two of clubs is always the “leading” card and suit, so whoever has it plays it to start the first trick.

    Two place a card first type its rank and then first letter of suit
    For example the two of clubs would be inputted as: 2C
    For this I recommend keeping caps lock on

CONTINUE AND COMPLETE THE TRICK:
    After the 2 of clubs is played, play continues clockwise until all four players have each played a card.
    Whoever has the highest rank of the leading suit (in this case clubs) takes the trick.
    In hearts, Twos are the lowest card rank and Aces is the highest card rank.

THERE ARE THREE IMPORTANT RULES HERE:
    If a player has a card that matches the lead suit, they must play it.

    In the first trick, if a player doesn’t have a club, they can “slough” (or play a card of another suit),
    But it can only be any non-point-scoring card (anything but hearts and the queen of spades).
    In subsequent rounds, any card can be played during a slough.

    The “lead suit” always outranks any other suits played on it.
    So if the first hand was: 2 of clubs, queen of diamond, 9 of diamonds, 8 of clubs…
    The 8 of clubs takes the hand because it is the highest card in the lead suit.

PLAY THE NEXT TRICK:
    The player that took the previous trick goes first in the next trick.
    They can lead with any card except for hearts, which first needs to be “broken.”

    Play continues clockwise again,
    Following the same general rules as the first trick with two exceptions.

    If a player doesn’t have a card of the same suit as the lead card,
    In addition to to be able to “slough” or play non-scoring cards, they also play scoring cards:
        The Queen of Spades
        Any Heart (and hearts will then be broken)
        
CONTINUE PLAY UNTIL NO MORE CARDS LEFT:
    Play continues the same way as the second trick.
    However, once the first heart has been played, hearts are “broken,” and players can then lead with hearts.

SCORE THE HAND
    Once all 13 tricks have been taken, players will count the points that they’ve taken.
    Point scoring is as follows:
        1 point for each heart
        13 points for Queen of Spades
        -10 points for the Jack of Diamonds
        
    A player who is able to take all the point scoring cards (all 13 hearts and the queen of spades) has “shot the moon.”
    A player who shoots the moon scores zero points, and also sends 26 points to all three of their opponents!

PLAY THE NEXT HAND:
    Players continue to play more hands in a similar fashion.

CONTINUE MORE HANDS UNTIL DESIRED POINTS ARE REACHED:
    Play continues until one player reaches an agreed upon total,
    Which is usually 100 points.
    Once any player (or players) reach or exceed that point total,the game is over.

DECLARE A WINNER:
    Once any player has reached or exceeded desired points,
    All players tally their scores and the player with the lowest score wins!""")


while maxScore <= 0:
    maxScore = int(input('\nWhat would you like to play to?\n'))
totalP = 0
total1 = 0
total2 = 0
total3 = 0

while totalP < maxScore and total1 < maxScore and total2 < maxScore and total3 < maxScore:
    player = []
    comp1 = []
    comp2 = []
    comp3 = []
    winningsP = []
    winnings1 = []
    winnings2 = []
    winnings3 = []
    hearts = []
    first = 0

    dealHands(shuffleDeck())
    sortHand(player)
    first = round1()
    while player != []:
        if first == 1:
            first = comp1First()
        elif first == 2:
            first = comp2First()
        elif first == 3:
            first = comp3First()
        elif first == 4:
            first = playerFirst()
        print()
    score_player, score_george, score_pablo, score_roman = scoreBoard(winningsP, winnings1, winnings2, winnings3)
    totalP += score_player
    total1 += score_george
    total2 += score_pablo
    total3 += score_roman
    play = 'Y'
    if totalP < maxScore and total1 < maxScore and total2 < maxScore and total3 < maxScore:
        play = input('Start next round?Y/N\n')
    if play == 'N':
        break
    
my_dict = {totalP: name, total1: 'George', total2: 'Pablo', total3: 'Roman'}
print(f'THE WINNER IS: {my_dict[min(my_dict)]}!')
print('Thanks For Playing!')
print("""Credits->
Instructions from:
https://gameonfamily.com/how-to-play-hearts-card-game/""")
input()
