import tkinter as tk
pad = 2
root = tk.Tk()
canvas = tk.Canvas(root,width=350 + pad* 2,height=350 + pad * 2) #Defines size of Canvas widget
canvas.pack() #adds widget to window
rows = [0,1,2,3,4,5,6]
cols = [0,1,2,3,4,5,6]
for row in rows: #Loop creates 7x7 grid of squares of size '50'
    for col in cols:
        canvas.create_rectangle(col * 50 + pad, row * 50 + pad, (col * 50) + 50 + pad, (row * 50) + 50 + pad, fill="")

def on_click(event):
    """
    A function that returns the 'square' coordinate when clicked
    """
    coll_coord = (event.x - pad) // 50 #Determines the column coordinate in grid
    row_coord = (event.y - pad) // 50 #Determines the row coordinate in grid
    if not -1 < coll_coord < 7 and -1 < row_coord < 7: #Ensures click is not out of range of grid
        return
    new_x =  chr(ord('A')+ coll_coord)#Assigns A-G to column depending on range of click
    new_y = row_coord + 1 #Assigns 1-7 to row depending on range of click
    new_x_y= new_x + str(new_y)
    return print(new_x_y)

canvas.bind("<Button-1>",on_click) #Button-1 == left click, so on left click call def
root.mainloop()
