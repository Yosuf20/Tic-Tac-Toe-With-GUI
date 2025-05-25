from tkinter import *

root = Tk()
root.title("Tic Tac Toe")
root.geometry("700x600")

turn = 0

board = {1:" ", 2:" ", 3:" ",
         4:" ", 5:" ", 6:" ",
         7:" ", 8:" ", 9:" "}




def checkwin():
    wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for i in wins:
        if (board[i[0]] == board[i[1]] == board[i[2]] == "X"):
            print("X Wins")
            disable_all_buttons()
            return True
        elif (board[i[0]] == board[i[1]] == board[i[2]] == "O"):
            print("O Wins")
            disable_all_buttons()
            return True
           
    if all(value != " " for value in board.values()):
        print("It's a Draw")



def play(event):
    global turn

    button = event.widget
    buttonstr = (str(button))
    buttonindex = buttonstr[-1]


    if buttonindex == "n":
        buttonindex = 1
    else:
        buttonindex = (int(buttonindex))

    print(buttonindex)

    if button["text"] == "":
        if turn == 0:
            button["text"] = "X"
            board[buttonindex] = "X"
            
            if checkwin():
                winninglabel = Label(frame2, text="X won", bg="Grey", font=("bold 25"), height=1)
                winninglabel.grid(row=3, column=1)
            turn = 1   
        else:
            button["text"] = "O"
            board[buttonindex] = "O"
            
            if checkwin():
                winninglabel = Label(frame2, text="O won", bg="grey", font=("bold 25"), height=1)
                winninglabel.grid(row=3, column=1)
            turn = 0
                
            
    
    print(board)



frame1 = Frame(root)
frame1.pack()
gametitle = Label(text="Tic Tac Toe", font=("bold 25"), bg="black", fg="white", height=2)
gametitle.pack(fill='x')

frame2 = Frame(root)
frame2.pack()

# first row
Button1 = Button(frame2, text="", bg="yellow", width=6, height=2, font=("Arial, 35"))
Button1.grid(row=0, column=0)
Button1.bind('<Button-1>',play)

Button2 = Button(frame2, text="", bg="yellow", width=6, height=2, font=("Arial, 35"))
Button2.grid(row=0, column=1)
Button2.bind('<Button-1>',play)

Button3 = Button(frame2, text="", bg="yellow", width=6, height=2, font=("Arial, 35"))
Button3.grid(row=0, column=2)
Button3.bind('<Button-1>',play)

# second row
Button4 = Button(frame2, text="", bg="yellow", width=6, height=2, font=("Arial, 35"))
Button4.grid(row=1, column=0)
Button4.bind('<Button-1>',play)

Button5 = Button(frame2, text="", bg="yellow", width=6, height=2, font=("Arial, 35"))
Button5.grid(row=1, column=1)
Button5.bind('<Button-1>',play)

Button6 = Button(frame2, text="", bg="yellow", width=6, height=2, font=("Arial, 35"))
Button6.grid(row=1, column=2)
Button6.bind('<Button-1>',play)

# third row
Button7 = Button(frame2, text="", bg="yellow", width=6, height=2, font=("Arial, 35"))
Button7.grid(row=2, column=0)
Button7.bind('<Button-1>',play)

Button8 = Button(frame2, text="", bg="yellow", width=6, height=2, font=("Arial, 35"))
Button8.grid(row=2, column=1)
Button8.bind('<Button-1>',play)

Button9 = Button(frame2, text="", bg="yellow", width=6, height=2, font=("Arial, 35"))
Button9.grid(row=2, column=2)
Button9.bind('<Button-1>',play)



buttons = {
    1: Button1, 2: Button2, 3: Button3,
    4: Button4, 5: Button5, 6: Button6,
    7: Button7, 8: Button8, 9: Button9
}

def disable_all_buttons():
    for btn in buttons.values():
        btn.config(state="disabled")




root.mainloop()