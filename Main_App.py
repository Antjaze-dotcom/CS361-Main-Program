import tkinter as tk
from tkinter import PhotoImage, Label
from App_Controller import GameSession

from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fantasy Battle")
        self.geometry('720x480')
        self.session = GameSession()

        container = tk.Frame(self)
        container.pack(fill='both', expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.pages = {}

        for PageClass in (MainMenu,HowTo,SetUp,Game):
            page = PageClass(parent=container, controller=self)
            self.pages[PageClass.__name__] = page
            page.grid(row = 0, column = 0, sticky = 'nsew')

        self.show_page("MainMenu")

    def show_page(self, page_name:str):
        """Displays chosen page"""
        page = self.pages[page_name]
        page.tkraise()



class MainMenu(tk.Frame):
    def __init__(self,parent,controller:App):
        super().__init__(parent)

        #Displays label as background
        self.image = Image.open('Backgrounds/Fantasy Battle(Main Menu) - Copy.PNG')
        self.img = self.image.resize((720,480))
        self.bg_img = ImageTk.PhotoImage(self.img)
        self.label_bg = Label( self, image = self.bg_img)
        self.label_bg.place(x=0, y=0, relwidth=1, relheight=1)

        #Creates 'How To Play' button
        self.rules_image = Image.open('Buttons/Rules Button - Copy.PNG')
        self.rules_image = self.rules_image.resize((132,52))
        self.rules_button = ImageTk.PhotoImage(self.rules_image)
        Go_To_Rules = tk.Button(self, image=self.rules_button, text='How To Fight',
                                command=lambda: controller.show_page('HowTo')).place(x=25,y=370)
        #Creates 'Begin' button
        self.begin_image = Image.open('Buttons/Begin Button - Copy.PNG')
        self.begin_image = self.begin_image.resize((132,52))
        self.begin_button = ImageTk.PhotoImage(self.begin_image)
        Go_To_Setup = tk.Button(self, image=self.begin_button, text='Begin',
                                command=lambda: controller.show_page('SetUp')).place(x=550,y=370)


class HowTo(tk.Frame):
    def __init__(self,parent,controller:App):
        super().__init__(parent)

        #Displays label as background
        self.image = Image.open('Backgrounds/Fantasy Battle(Rules) - Copy.PNG')
        self.img = self.image.resize((720, 480))
        self.bg_img = ImageTk.PhotoImage(self.img)
        self.label_bg = Label(self, image=self.bg_img)
        self.label_bg.place(x=0, y=0, relwidth=1, relheight=1)


        #Creates 'Return' button
        self.Main_image = Image.open('Buttons/Return Button - Copy.PNG')
        self.Main_image = self.Main_image.resize((132,52))
        self.Main_button = ImageTk.PhotoImage(self.Main_image)
        Go_To_Setup = tk.Button(self, image=self.Main_button, text='Begin',
                                command=lambda: controller.show_page('MainMenu')).place(x=550,y=30)


class SetUp(tk.Frame):
    def __init__(self,parent,controller:App):
        super().__init__(parent)

        #Displays label as background
        self.image = Image.open('Backgrounds/Fantasy Battle (Set Up) - Copy.PNG')
        self.img = self.image.resize((720, 480))
        self.bg_img = ImageTk.PhotoImage(self.img)
        self.label_bg = Label(self, image=self.bg_img)
        self.label_bg.place(x=0, y=0, relwidth=1, relheight=1)

        #Creates 'Return' button
        self.Main_image = Image.open('Buttons/Return Button - Copy.PNG')
        self.Main_image = self.Main_image.resize((132,52))
        self.Main_button = ImageTk.PhotoImage(self.Main_image)
        Go_To_Setup = tk.Button(self, image=self.Main_button, text='Return',
                                command=lambda: controller.show_page('MainMenu')).place(x=550,y=370)
        #Creates 'Autoset' button
        self.Auto_image = Image.open('Buttons/Autoset Pawns Button - Copy.PNG')
        self.Auto_image = self.Auto_image.resize((132, 52))
        self.Auto_button = ImageTk.PhotoImage(self.Auto_image)
        Go_To_Setup = tk.Button(self, image=self.Auto_button, text='Autoset My Pawns',
                                command=lambda: controller.session.autoset()).place(x=25, y=370) #Place holder command
        #Creates 'Ready' button
        self.Ready_image = Image.open('Buttons/Ready Button - Copy.PNG')
        self.Ready_image = self.Ready_image.resize((132, 52))
        self.Ready_button = ImageTk.PhotoImage(self.Ready_image)
        Go_To_Setup = tk.Button(self, image=self.Ready_button, text='Autoset My Pawns',
                                command=lambda: controller.show_page('Game')).place(x=295, y=370)

        #Initilaizes a game board via Canvas
        pad = 2
        cell = 45
        self.board_pad = pad
        self.board_cell = cell
        self.canvas = tk.Canvas(self, width=315 + pad * 2, height=315 + pad * 2)  # Defines size of Canvas widget
        self.canvas.place(x=205, y=30)  # adds widget to window
        rows = [0, 1, 2, 3, 4, 5, 6]
        cols = [0, 1, 2, 3, 4, 5, 6]
        for row in rows:  # Loop creates 7x7 grid of squares of size '50'
            for col in cols:
                self.canvas.create_rectangle(col * cell + pad, row * cell + pad, (col * cell) + cell + pad, (row * cell) + cell + pad,fill="")
        self.canvas.bind("<Button-1>", self.on_click)  # Button-1 == left click, so on left click call def


        # Initializes Drop down menu for Canvas board
        self.pending_grid_coord = None
        self.pawn_choose = tk.StringVar(value="Choose value") # StringVar creates a readable/ writable string for Tk.OptionMenu
        pawn_types = ["Dragon","Troll","Centaur","Minotaur","Warlock","Unicorn","Fay"]
        self.pawn_menu = tk.OptionMenu(self, self.pawn_choose, *pawn_types,command=self.pawn_chosen) #Creates drop down menu, * expands list, pawn_chosen called only when pawn_type selected
        self.pawn_menu.place_forget() #Hides drop down menu until square is clicked

        self.board_x = 205
        self.board_y = 30

        #Stores pawn Images using PIL
        self.pawn_imgs = {} # Creates dict that stores each pawn's img
        for pawn in pawn_types: # Loop creates img path for each image per player
            for player in ("PlayerOne","PlayerTwo"):
                path = f'Pawns/{pawn}_{player} - Copy.PNG'
                img = Image.open(path)
                img = img.resize((cell-6,cell-6)) # resizes to fit 45x45 square
                self.pawn_imgs[(pawn,player)] = ImageTk.PhotoImage(img) # Inserts tuple as key in dict and corresponding img as value

    def on_click(self,event):
        """
        A function that returns the 'square' coordinate when clicked
        """
        pad = self.board_pad
        cell = self.board_cell

        coll_coord = (event.x - pad) // cell  # Determines the column coordinate in grid
        row_coord = (event.y - pad) // cell  # Determines the row coordinate in grid
        if not (-1 < coll_coord < 7 and -1 < row_coord < 7):  # Ensures click is not out of range of grid
            return

        final_coord = f"{chr(ord('A') + coll_coord)}{row_coord + 1}" # Assigns A-G to column and 1-7 to row depending on click range
        self.handle_pawn_place(final_coord)
        return

    def handle_pawn_place(self,coord):
        """
        Handles placing a single pawn on game board
        """
        valid_coord_list = ["A1","A2","A3","A4","A5","A6","A7","G1","G2","G3","G4","G5","G6","G7"]
        if coord not in valid_coord_list:
            return

        self.pending_grid_coord = coord # Saves Grid coord value for future use
        col = ord(coord[0]) - ord('A') #reverts 'A1' grid coordinate to pixel coordinate
        row = int(coord[1]) - 1

        x = self.board_x + self.board_pad + (self.board_cell * col) #sets coordinates in Board for menu
        y = self.board_y + self.board_pad + (self.board_cell * row)

        self.pawn_choose.set("Choose Pawn") #Resets drop down everytime it is called
        self.pawn_menu.place(x=x,y=y,)


    def set_pawns(self):
        self.GameSession = GameSession()
        pawn_list = self.GameSession.autoset()

    def pawn_chosen(self,pawn_type):
        """
        Inserts image of pawn_type in grid square
        """
        pad = self.board_pad
        cell = self.board_cell

        col = ord(self.pending_grid_coord[0]) - ord('A') #reverts 'A1' grid coordinate to pixel coordinate
        row = int(self.pending_grid_coord[1]) - 1

        x = pad + col * cell + cell // 2 #Find coordinates for center of grid square
        y = pad + row * cell + cell // 2

        if self.pending_grid_coord[0] == "A":
            img = self.pawn_imgs[(pawn_type,"PlayerOne")]
            self.canvas.create_image(x,y, image=img ,anchor="center")
        else:
            img = self.pawn_imgs[(pawn_type,"PlayerTwo")]
            self.canvas.create_image(x, y, image=img, anchor="center")
        return


class Game(tk.Frame):
    def __init__(self,parent,controller:App):
        super().__init__(parent)

        #Displays label as background
        self.image = Image.open('Backgrounds/Fantasy Battle (Board) - Copy.PNG')
        self.img = self.image.resize((720, 480))
        self.bg_img = ImageTk.PhotoImage(self.img)
        self.label_bg = Label(self, image=self.bg_img)
        self.label_bg.place(x=0, y=0, relwidth=1, relheight=1)

        #Creates 'Main Menu' Button
        self.Main_image = Image.open('Buttons/Main Menu Button - Copy.PNG')
        self.Main_image = self.Main_image.resize((132,52))
        self.Main_button = ImageTk.PhotoImage(self.Main_image)
        Go_To_Setup = tk.Button(self, image=self.Main_button, text='Return',
                                command=lambda: controller.show_page('MainMenu')).place(x=550,y=370)
        #Creates 'End Turn' Button
        self.End_image = Image.open('Buttons/End Turn Button - Copy.PNG')
        self.End_image = self.End_image.resize((132, 52))
        self.End_button = ImageTk.PhotoImage(self.End_image)
        Go_To_Setup = tk.Button(self, image=self.End_button, text='End Turn',
                                command=lambda: controller.show_page('MainMenu')).place(x=25, y=370) #Place holder command

class BoardView(tk.Frame):
    def __init__(self,parent,controller:App,length,width,):
        super().__init__(parent)


if __name__=="__main__":
    app = App()
    app.mainloop()

