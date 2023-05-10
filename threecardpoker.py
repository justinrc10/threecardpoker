import random

class card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class player:
    def __init__(self, funds, settleAmount, idealAnte, idealPairPlus):
        self.funds = funds
        self.settleAmount = settleAmount
        self.idealAnte = idealAnte
        self.ante = 0
        self.idealPairPlus = idealPairPlus
        self.pairPlus = 0
        self.hand = []
        self.handType = []
        self.play = False

class dealer:
    def __init__(self):
        self.deck = []
        self.hand = []
        self.handType = []
        self.play = False

class statistics:
    def __init__(self):
        self.currentMatchOutcome = ""
        self.totalSettles = 0
        self.totalBusts = 0
        self.maxCash = 0
        self.minCash = 0
        self.maxMaxCash = 0
        self.minMinCash = 9999999999999999
        self.isBust = False

def placeBets(player):
    if player.funds >= (2 * player.idealAnte) + player.idealPairPlus:
        player.ante = player.idealAnte
        player.pairPlus = player.idealPairPlus
    elif (2 * player.idealAnte) <= player.funds < (2 * player.idealAnte) + player.idealPairPlus:
        player.ante = player.idealAnte
        player.pairPlus = player.funds - (2 * player.idealAnte)
    elif player.funds == 1:
        player.ante = 0
        player.pairPlus = 0
    else:
        player.ante = int(player.funds / 2)
        player.pairPlus = 0

def newDeck():
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
   
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(card(rank,suit))
    random.shuffle(deck)

    return deck

def drawCard(deck):
    card = deck[-1]
    deck.pop()
    return card

def dealHand(deck):
    hand = []
    for i in range(3):
        hand.append(drawCard(deck))
    return hand

def dealHands(player, dealer):
    dealer.deck = newDeck()
    player.hand = dealHand(dealer.deck)
    dealer.hand = dealHand(dealer.deck)

# Ranking index:    hand types: {"high" = 1, "pair" = 2, "flush" = 3, "straight" = 4, "threeOfAKind" = 5, "straightFlush" = 6}
#                   high cards: {"2" = 2, "3" = 3, ..., "10" = 10, "Jack" = 11, "Queen" = 12, "King" = 13, "Ace" = 14}
highCardIndex = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "Jack" : 11, "Queen" : 12, "King" : 13, "Ace" : 14}

def checkHigh(hand):
    handType = [highCardIndex[hand[0].rank], highCardIndex[hand[1].rank], highCardIndex[hand[2].rank]]
    handType.sort(reverse = True)
    handType.insert(0,1)
    return handType

def checkPair(hand):
    handType = [highCardIndex[hand[0].rank], highCardIndex[hand[1].rank], highCardIndex[hand[2].rank]]
    handType.sort(reverse = True)
    if handType[0] == handType[1]:
        return [2, handType[1], handType[2]]
    elif handType [1] == handType[2]:
        return [2, handType[1], handType[0]]
    else:
        return False

def checkFlush(hand):
    if hand[0].suit == hand[1].suit == hand[2].suit:
        handType = [highCardIndex[hand[0].rank], highCardIndex[hand[1].rank], highCardIndex[hand[2].rank]]
        handType.sort(reverse = True)
        handType.insert(0,3)
        return handType
    else:
        return False

def checkStraight(hand):
    handType = [highCardIndex[hand[0].rank], highCardIndex[hand[1].rank], highCardIndex[hand[2].rank]]
    handType.sort()
    if handType[0] + 2 == handType[1] + 1 == handType[2] or (handType[0] == 2 and handType[1] == 3 and handType[2] == 14):
        if handType[2] == 14:
            return [4, 3]
        else:
            return [4, handType[2]]
    else:
        return False

def checkThreeOfAKind(hand):
    if hand[0].rank == hand[1].rank == hand[2].rank:
        return [5, highCardIndex[hand[0].rank]]
    else:
        return False

def checkStraightFlush(hand):
    handType = checkStraight(hand)
    if handType and checkFlush(hand):
        return [6, handType[1]]
    else:
        return False

def checkHandType(hand):
    pair = checkPair(hand)
    flush = checkFlush(hand)
    straight = checkStraight(hand)
    threeOfAKind = checkThreeOfAKind(hand)
    straightFlush = checkStraightFlush(hand)

    if straightFlush:
        return straightFlush
    elif straight:
        return straight
    elif flush:
        return flush
    elif threeOfAKind:
        return threeOfAKind
    elif pair:
        return pair
    else:
        return checkHigh(hand)

def checkIfPlaying(player, dealer):
    if player.handType[0] > 1 or player.handType[1] > 12 or (player.handType[1] == 12 and player.handType[2] > 6) or (player.handType[1] == 12 and player.handType[2] == 6 and player.handType[3] > 3):
        player.play = True
    else:
        player.play = False
    
    if dealer.handType[0] > 1 or dealer.handType[1] > 11:
        dealer.play = True
    else:
        dealer.play = False

def checkOutcome(player, dealer):
    player.handType = checkHandType(player.hand)
    dealer.handType = checkHandType(dealer.hand)

    checkIfPlaying(player, dealer)

    if player.play == True:
        if player.handType[0] > dealer.handType[0]:
            return "Win"
        elif player.handType[0] < dealer.handType[0]:
            return "Lose"
        elif player.handType[0] == dealer.handType[0] == 1 or player.handType[0] == dealer.handType[0] == 3:
            if player.handType[1] > dealer.handType[1]:
                return "Win"
            elif player.handType[1] < dealer.handType[1]:
                return "Lose"
            elif player.handType[1] == dealer.handType[1]:
                if player.handType[2] > dealer.handType[2]:
                    return "Win"
                elif player.handType[2] < dealer.handType[2]:
                    return "Lose"
                elif player.handType[2] == dealer.handType[2]:
                    if player.handType[3] > dealer.handType[3]:
                        return "Win"
                    elif player.handType[3] < dealer.handType[3]:
                        return "Lose"
                    elif player.handType[3] == dealer.handType[3]:
                        return "Tie"
        elif player.handType[0] == dealer.handType[0] == 2:
            if player.handType[1] > dealer.handType[1]:
                return "Win"
            elif player.handType[1] < dealer.handType[1]:
                return "Lose"
            elif player.handType[1] == dealer.handType[1]:
                if player.handType[2] > dealer.handType[2]:
                    return "Win"
                elif player.handType[2] < dealer.handType[2]:
                    return "Lose"
                elif player.handType[2] == dealer.handType[2]:
                    return "Tie"
        elif player.handType[0] == dealer.handType[0] == 4 or player.handType[0] == dealer.handType[0] == 5 or player.handType[0] == dealer.handType[0] == 6:
            if player.handType[1] > dealer.handType[1]:
                return "Win"
            elif player.handType[1] < dealer.handType[1]:
                return "Lose"
            elif player.handType[1] == dealer.handType[1]:
                return "Tie"
    else:
        return "Lose"

def payoutAnte(player, dealer, statistics):
    if statistics.currentMatchOutcome == "Win":
        if dealer.play == False:
            player.funds = player.funds + player.ante
        else:
            player.funds = player.funds + (2 * player.ante)
        if player.handType == 4:
            player.funds = player.funds + player.ante
        elif player.handType == 5:
            player.funds = player.funds + (3 * player.ante)
        elif player.handType == 6:
            player.funds = player.funds + (5 * player.ante)
    elif statistics.currentMatchOutcome == "Lose":
        player.funds = player.funds - (2 * player.ante)

def payoutPairPlus(player):
    if player.handType == 2:
        player.funds = player.funds + player.pairPlus
    elif player.handType == 3:
        player.funds = player.funds + (4 * player.pairPlus)
    elif player.handType == 4:
        player.funds = player.funds + (5 * player.pairPlus)
    elif player.handType == 5:
        player.funds = player.funds + (30 * player.pairPlus)
    elif player.handType == 6:
        player.funds = player.funds + (40 * player.pairPlus)
    else:
        player.funds = player.funds - player.pairPlus

def payout(player, dealer, statistics):
    if player.play == True:
        payoutAnte(player, dealer, statistics)
        payoutPairPlus(player)
    else:
        player.funds = player.funds - player.ante - player.pairPlus

def isTerminate(player, statistics):
    if player.funds <= 1:
        statistics.isBust = True
        statistics.totalBusts = statistics.totalBusts + 1
        return True
    elif player.funds >= player.settleAmount:
        statistics.isBust = False
        statistics.totalSettles = statistics.totalSettles + 1
        return True
    else:
        return False

def updateStatistics(statistics, player):
    statistics.maxCash = max([statistics.maxCash, player.funds])
    statistics.minCash = min([statistics.minCash, player.funds])

def printStatistics(statistics, i):
    if statistics.isBust == True:
        print(str(i+1) + ": Bust; Max cash: " + str(statistics.maxCash))
        statistics.maxMaxCash = max([statistics.maxMaxCash, statistics.maxCash])
    else:
        print(str(i+1) + ": Settle; Min cash: " + str(statistics.minCash))
        statistics.minMinCash = min([statistics.minMinCash, statistics.minCash])

def test():
    funds = int(input("How much money are you starting with?\n$"))
    settleAmount = int(input("How much money would you settle with?\n$"))
    idealAnte = int(input("If you had the available funds, how much money would you put into your ante bet?\n$"))
    idealPairPlus = int(input("If you had the available funds, how much money would you put into your pair plus bet?\n$"))
    numSimulations = int(input("How many simulations would you like to run?\n"))
    Statistics = statistics()
    for i in range(numSimulations):
        Player = player(funds, settleAmount, idealAnte, idealPairPlus)
        Dealer = dealer()
        Statistics.maxCash = funds
        Statistics.minCash = funds
        while isTerminate(Player, Statistics) == False:
            placeBets(Player)
            dealHands(Player, Dealer)
            Statistics.currentMatchOutcome = checkOutcome(Player, Dealer)
            payout(Player, Dealer, Statistics)
            updateStatistics(Statistics, Player)
        del(Player)
        del(Dealer)
        printStatistics(Statistics, i)
    print("Total busts: " + str(Statistics.totalBusts) + "; Total settles: " + str(Statistics.totalSettles))
    print("Closest bust: " + str(Statistics.minMinCash) + "; Closest settle: " + str(Statistics.maxMaxCash))

test()