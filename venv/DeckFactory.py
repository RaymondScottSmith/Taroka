from MinorCard import MinorCard
from MajorCard import MajorCard


def BuildMajorDeck():
    deck = []
    f = open("MajorDeck.txt", "r")
    for _ in range(14):
        line = f.readline()
        hold = line.split("/")
        deck.append(MajorCard(hold[0],hold[1],hold[2],None,hold[3].rstrip()))
    return deck
        
        

def BuildMinorDeck():
    deck = []
    f = open("MinorDeck.txt", "r")
    suits = ["Swords", "Stars", "Coins", "Glyphs"] #"Swords", "Stars", "Coins", "Glyphs"]
    for suit in suits:
        for i in range(10):
            line = f.readline()
            hold = line.split("/")
            deck.append(MinorCard(suit, i+1, hold[0], hold[1], hold[2].rstrip()))
    return deck





