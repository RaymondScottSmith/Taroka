from DeckFactory import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import PIL
from PIL import Image, ImageTk
import random

#Setting up Cardbacks
MinorBack = MinorCard(None, None, "Cardback", "Back of a Taroka card",'CardBack.png')
MajorBack = MajorCard("Cardback", "Back of a Taroka card", "Back of a Taroka card", None,'CardBack.png')

#Setting up the point of each card in the cross
TopCardDesc="This card tells of a powerful force for good and protection, a holy symbol of great hope."
LeftCardDesc="This card tells of history. Knowledge of the ancient will help you better understand your enemy."
RightCardDesc="This is a card of power and strength. It tells of a weapon of vengeance: a sword of sunlight."
MiddleCardDesc="Your enemy is a creature of darkness, whose powers are beyond mortality. \nThis card will lead you to him!"
BottomCardDesc="This card sheds light on one who will help you greatly in the battle against the darkness."

class FortuneTeller:

    def __init__(self, master):
        #Needs refactoring
        master.title('Taroka Deck Reading')
        master.resizable(False, False)
        filler2 = Frame(master, height=20)
        filler2.pack(side=TOP)

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        f = Frame(master, width=10000)
        f.pack(side=LEFT)
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        filler = Frame(master, height = 20)
        filler.pack(side=BOTTOM)

        image = Image.open('Images/CardBack.png')
        image = image.resize((180, 252), Image.ANTIALIAS)
        self.cardBack = ImageTk.PhotoImage(image)

        ttk.Label(self.frame_content, wraplength= 180, justify = 'center',
                  text = TopCardDesc).grid(row=1, column=3, padx=5)



        self.topCard = ttk.Label(self.frame_content, image = self.cardBack)
        global TopCard
        TopCard = MinorBack
        self.topCard.grid(row=0, column=3, padx=20)



        ttk.Label(self.frame_content, wraplength=180, justify='center',
                  text=LeftCardDesc).grid(row=3, column=2, padx=5)

        ttk.Label(self.frame_content, wraplength=180, justify='center',
                  text=RightCardDesc).grid(row=3, column=4, padx=5)

        self.leftCard = ttk.Label(self.frame_content, image = self.cardBack)
        self.leftCard.grid(row=2, column=2, padx=20)
        global LeftCard
        LeftCard = MinorBack

        self.midCard = ttk.Label(self.frame_content, image = self.cardBack)
        self.midCard.grid(row=2, column=3, padx=20)
        global MiddleCard
        MiddleCard = MajorBack
        ttk.Label(self.frame_content, wraplength=180, justify='center',
                  text=MiddleCardDesc).grid(row=3, column=3, padx=5)

        self.rightCard = ttk.Label(self.frame_content, image = self.cardBack)
        self.rightCard.grid(row=2, column=4, padx=20)
        global RightCard
        RightCard = MinorBack

        self.bottomCard = ttk.Label(self.frame_content, image = self.cardBack)
        self.bottomCard.grid(row=4, column=3, padx=20)
        global BottomCard
        BottomCard = MajorBack

        ttk.Label(self.frame_content, wraplength=180, justify='center',
                  text=BottomCardDesc).grid(row=5, column=3, padx=5)



        ttk.Button(f, text='Draw',
                   command=self.draw).pack(pady=10, padx=30)

        ttk.Button(f, text='Clear',
                   command=self.clear).pack(pady=10, padx=30)

        #Binding clicking on cards
        self.topCard.bind('<ButtonPress>', click_top)
        self.midCard.bind('<ButtonPress>', click_mid)
        self.leftCard.bind('<ButtonPress>', click_left)
        self.rightCard.bind('<ButtonPress>', click_right)
        self.bottomCard.bind('<ButtonPress>', click_bottom)


    def draw(self):
        #Building Decks of Major and Minor cards
        deck = BuildMinorDeck()
        deck2 = BuildMajorDeck()

        #Shuffling the decks and drawing top 3 and 2 cards
        random.shuffle(deck)
        random.shuffle(deck2)
        self.card1 = deck[0]
        self.card2 = deck[1]
        self.card3 = deck[2]
        self.card4 = deck2[0]
        self.card5 = deck2[1]

        #Changing the card numbers to Master instead of 10
        #Possibly remove. Holdover from previous iteration of concept
        if self.card1.number == 10:
            self.card1.number = "Master of"
        if self.card2.number == 10:
            self.card2.number = "Master of"
        if self.card3.number == 10:
            self.card3.number = "Master of"

        #Refactor below. There's probably a simpler way
        #Set the info of the top card
        image1 = Image.open('Images/'+ self.card1.img)
        image1 = image1.resize((180, 252), Image.ANTIALIAS)
        photoImg = ImageTk.PhotoImage(image1)
        self.topCard.configure(image = photoImg)
        self.topCard.image = photoImg
        global TopCard
        TopCard = self.card1

        #Set the info of the left card
        image2 = Image.open('Images/' + self.card2.img)
        image2 = image2.resize((180, 252), Image.ANTIALIAS)
        photoImg = ImageTk.PhotoImage(image2)
        self.leftCard.configure(image=photoImg)
        self.leftCard.image = photoImg
        global LeftCard
        LeftCard = self.card2

        #Set the info of the right card
        image3 = Image.open('Images/' + self.card3.img)
        image3 = image3.resize((180, 252), Image.ANTIALIAS)
        photoImg = ImageTk.PhotoImage(image3)
        self.rightCard.configure(image=photoImg)
        self.rightCard.image = photoImg
        global RightCard
        RightCard = self.card3

        #Set the info of the bottom card
        image4 = Image.open('Images/' + self.card4.img)
        image4 = image4.resize((180, 252), Image.ANTIALIAS)
        photoImg = ImageTk.PhotoImage(image4)
        self.bottomCard.configure(image=photoImg)
        self.bottomCard.image = photoImg
        global BottomCard
        BottomCard = self.card4

        #Set the info of the middle card
        image5 = Image.open('Images/' + self.card5.img)
        image5 = image5.resize((180, 252), Image.ANTIALIAS)
        photoImg = ImageTk.PhotoImage(image5)
        self.midCard.configure(image=photoImg)
        self.midCard.image = photoImg
        global MiddleCard
        MiddleCard = self.card5


    def clear(self):
        #prepare cardback image
        image = Image.open('Images/CardBack.png')
        image = image.resize((180, 252), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)

        #Reset the cards to show cardbacks and have the cardback info associated
        self.midCard.configure(image=image)
        self.midCard.image = image
        global MiddleCard
        MiddleCard = MajorBack
        self.topCard.configure(image=image)
        self.topCard.image = image
        global TopCard
        TopCard = MinorBack
        self.rightCard.configure(image=image)
        self.rightCard.image = image
        global RightCard
        RightCard = MinorBack
        self.leftCard.configure(image=image)
        self.leftCard.image = image
        global LeftCard
        LeftCard = MinorBack
        self.bottomCard.configure(image=image)
        self.bottomCard.image = image
        global BottomCard
        BottomCard = MajorBack

def openNewWindow(position, card, fortune):
    #Window that opens when clicking on card
    newWindow = Toplevel()
    newWindow.title("The " + card.name)

    f1 = ttk.Frame(newWindow)
    f1.pack()

    #Possibly revisit to adjust fonts and font size
    image = Image.open('Images/' + card.img)
    image = image.resize((400, 560), Image.ANTIALIAS)
    photoImg = ImageTk.PhotoImage(image)
    Label(f1, text=position, wraplength=350, font=('Times New Roman', 15, 'italic'), pady=10).pack()
    Label(f1, image = photoImg, padx=10).pack()
    Label(f1, text=fortune, wraplength=350, font=('Times New Roman', 15, 'bold italic'), pady=10).pack()
    newWindow.mainloop()


#Click events for each card
def click_top(event):
    openNewWindow(TopCardDesc, TopCard, TopCard.description)

def click_left(event):
    openNewWindow(LeftCardDesc, LeftCard, LeftCard.description)

def click_mid(event):
    openNewWindow(MiddleCardDesc, MiddleCard, MiddleCard.location)

def click_right(event):
    openNewWindow(RightCardDesc, RightCard, RightCard.description)

def click_bottom(event):
    openNewWindow(BottomCardDesc, BottomCard, BottomCard.ally)

def main():
    root = Tk()
    ft = FortuneTeller(root)
    root.mainloop()

if __name__ == "__main__": main()