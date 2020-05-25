from tkinter import Tk, Frame, Label, Button, Entry
import tkinter.messagebox as tmsg


root = Tk()
root.title("TicTacToe")
root.iconbitmap(r'icon.ico')

main_frame = Frame(root, bg = "#000000")
main_frame.pack(fill = "both", expand = True)
board_fame = 0
current_player = "X"
push_button = 0
current_match = 0
value = 0
count_x = 0
count_o = 0
valid = False
ready = "Ready...X's turn"


#------------------Title------------------
label = Label(main_frame, text = "Tic Tac Toe", bg = "dark slate gray", fg = "white", padx = 5, pady = 5)
label.config(font = ("Arial", 18))
label.pack(fill = "x")


#------------------Screen------------------
def screen():
    global screen, ready
    screen_frame = Frame(main_frame, bg = "black")

    screen = Label(screen_frame, text = ready, bg = "white", fg = "#364d1f", padx = 10, pady = 10, font = ("Arial", 14))
    screen.pack(fill = "x", pady = (10, 5))

    screen_frame.pack(fill = "x")


#-----------------Score Board-------------
def score_board():
    global entry_match, entry_X, entry_O
    score_board = Frame(main_frame, bg = "dark slate gray")

    label_score = Label(score_board, text = "Score", font = ("Arial", 12), bg = "dark slate gray", fg = "white")
    label_X = Label(score_board, text = "X: ", font = ("Arial", 12), bg = "dark slate gray", fg = "white")
    label_O = Label(score_board, text = "O: ", font = ("Arial", 12), bg = "dark slate gray", fg = "white")
    label_match = Label(score_board, text = "Match: ", font = ("Arial", 12), bg = "dark slate gray", fg = "white")

    label_score.grid(row = 0, column = 0, sticky = "nsew")
    label_X.grid(row = 0, column = 1, sticky = "nsew")
    label_O.grid(row = 0, column = 3, sticky = "nsew")
    label_match.grid(row = 0, column = 5, sticky = "nsew")

    entry_X = Label(score_board, width = 10, text = "0", bg = "#ffffff")
    entry_O = Label(score_board, width = 10, text = "0", bg = "#ffffff")
    entry_match = Label(score_board, width = 12, text = "", bg = "#ffffff")

    entry_X.grid(row = 0, column = 2, padx = (0, 10), sticky = "nsew")
    entry_O.grid(row = 0, column = 4, padx = (0, 10), sticky = "nsew")
    entry_match.grid(row = 0, column = 6, padx = (0, 10), sticky = "nsew")

    score_board.pack(fill = "both", pady = (5, 10))

    score_board.grid_columnconfigure(0, weight = 1)
    score_board.grid_columnconfigure(2, weight = 1)
    score_board.grid_columnconfigure(4, weight = 1)
    score_board.grid_columnconfigure(6, weight = 1)


#------------------Board------------------
def frame_board():
    global board_frame, b1, b2, b3, b4, b5, b6, b7, b8, b9
    board_frame = Frame(main_frame)
    board_frame.pack(fill="both", expand=True)

    # ------------------Button------------------
    b1 = Button(board_frame, text = " ", bg = "blanched almond", fg = "black", width = 15, height = 5, command = lambda:checker(b1))
    b1.grid(row = 0, column = 0, sticky = "nsew")
    b1.bind("<Enter>", b1_enter)
    b1.bind("<Leave>", b1_leave)


    b2 = Button(board_frame, text = " ", bg = "blanched almond", fg = "black", width = 15, height = 5,command = lambda:checker(b2))
    b2.grid(row = 0, column = 1, sticky = "nsew")
    b2.bind("<Enter>", b2_enter)
    b2.bind("<Leave>", b2_leave)

    b3 = Button(board_frame, text = " ", bg = "blanched almond", fg = "black", width = 15, height = 5, command = lambda:checker(b3))
    b3.grid(row = 0, column = 2, sticky = "nsew")
    b3.bind("<Enter>", b3_enter)
    b3.bind("<Leave>", b3_leave)

    b4 = Button(board_frame, text = " ", bg = "blanched almond", fg = "black", width = 15, height = 5, command = lambda:checker(b4))
    b4.grid(row = 1, column = 0, sticky = "nsew")
    b4.bind("<Enter>", b4_enter)
    b4.bind("<Leave>", b4_leave)

    b5 = Button(board_frame, text = " ", bg = "blanched almond", fg = "black", width = 15, height = 5, command = lambda:checker(b5))
    b5.grid(row = 1, column = 1, sticky = "nsew")
    b5.bind("<Enter>", b5_enter)
    b5.bind("<Leave>", b5_leave)

    b6 = Button(board_frame, text = " ", bg = "blanched almond", fg = "black", width = 15, height = 5, command = lambda:checker(b6))
    b6.grid(row = 1, column = 2, sticky = "nsew")
    b6.bind("<Enter>", b6_enter)
    b6.bind("<Leave>", b6_leave)

    b7 = Button(board_frame, text = " ", bg = "blanched almond", fg = "black", width = 15, height = 5, command = lambda:checker(b7))
    b7.grid(row = 2, column = 0, sticky = "nsew")
    b7.bind("<Enter>", b7_enter)
    b7.bind("<Leave>", b7_leave)

    b8 = Button(board_frame, text = " ", bg = "blanched almond", fg = "black", width = 15, height = 5, command = lambda:checker(b8))
    b8.grid(row = 2, column = 1, sticky = "nsew")
    b8.bind("<Enter>", b8_enter)
    b8.bind("<Leave>", b8_leave)

    b9 = Button(board_frame, text = " ", bg = "blanched almond", fg = "black", width = 15, height = 5, command = lambda:checker(b9))
    b9.grid(row = 2, column = 2, sticky = "nsew")
    b9.bind("<Enter>", b9_enter)
    b9.bind("<Leave>", b9_leave)

    board_frame.grid_columnconfigure(0, weight = 1)
    board_frame.grid_columnconfigure(1, weight = 1)
    board_frame.grid_columnconfigure(2, weight = 1)

    board_frame.grid_rowconfigure(0, weight = 1)
    board_frame.grid_rowconfigure(1, weight = 1)
    board_frame.grid_rowconfigure(2, weight = 1)

    board_frame.grid_columnconfigure(3, weight = 1)


#------------------Side Board------------------
def board_side():
    global board_frame, submit_btn, reset_btn, help_btn, exit_btn, number_of_match_entry
    side_board = Frame(board_frame, bg = "dark slate gray", padx = 10, pady = 30)
    side_board.grid(row = 0, column = 3, rowspan = 3, sticky = "nsew")

    msg = Label(side_board, text = "Number of Match", font = ("Arial", 10), bg = "dark slate gray", fg = "white")
    msg.grid(row = 0, column = 0, sticky = "nsew")

    number_of_match_entry = Entry(side_board, width = 12, text = " ", bg = "#ffffff")
    number_of_match_entry.grid(row = 1, column = 0, padx = 15, pady = (10, 10), sticky = "nsew")

    submit_btn = Button(side_board, text = "Submit", bg = "#234d6f", fg = "white", height = 1, width = 12, command = submit_code)
    submit_btn.grid(row = 2, column = 0, sticky = "nsew", padx = 15, pady = (0, 20))
    submit_btn.bind("<Enter>", submit_enter)
    submit_btn.bind("<Leave>", submit_leave)

    reset_btn = Button(side_board, text = "Reset", height = 1, width = 12, bg = "#a8d1a9", fg = "black", command = lambda:reset_turn())
    reset_btn.grid(row = 3, column = 0, sticky = "nsew", padx = 15, pady = (5, 10))
    reset_btn.bind("<Enter>", reset_enter)
    reset_btn.bind("<Leave>", reset_leave)

    exit_btn = Button(side_board, text = "Exit", height = 1, width = 12, bg = "#af3331", fg = "white", command = exit_code)
    exit_btn.grid(row = 4, column = 0, sticky = "nsew", padx = 15, pady = (0, 10))
    exit_btn.bind("<Enter>", exit_enter)
    exit_btn.bind("<Leave>", exit_leave)

    help_btn = Button(side_board, text = "Help", height = 1, width = 12, bg = "#2d9ea1", fg = "white", command = help_code)
    help_btn.grid(row = 5, column = 0, sticky = "nsew", padx = 15, pady = (10, 0))
    help_btn.bind("<Enter>", help_enter)
    help_btn.bind("<Leave>", help_leave)

    side_board.grid_columnconfigure(0, weight = 1)

    # side_board .grid_rowconfigure(0, weight = 1)
    side_board.grid_rowconfigure(1, weight = 1)
    side_board.grid_rowconfigure(2, weight = 1)
    side_board.grid_rowconfigure(3, weight = 1)
    side_board.grid_rowconfigure(4, weight = 1)
    side_board.grid_rowconfigure(5, weight = 1)

def submit_enter(event):
    global submit_btn
    submit_btn.config(
        bg = "#35385f",
        fg = "white"
    )

def submit_leave(event):
    global submit_btn
    submit_btn.config(
        bg = "#234d6f",
        fg = "white"
    )

def reset_enter(event):
    global reset_btn
    reset_btn.config(
        bg = "#6b9933",
        fg = "white"
    )

def reset_leave(event):
    global reset_btn
    reset_btn.config(
        bg = "#a8d1a9",
        fg = "black"
    )

def exit_enter(event):
    global exit_btn
    exit_btn.config(
        bg = "#6c301e",
        fg = "white"
    )

def exit_leave(event):
    global exit_btn
    exit_btn.config(
        bg = "#af3331",
        fg = "white"
    )

def help_enter(event):
    global help_btn
    help_btn.config(
        bg = "#2accc8",
        fg = "black"
    )

def help_leave(event):
    global help_btn
    help_btn.config(
        bg = "#2d9ea1",
        fg = "white"
    )

def flipped_player():
    global current_player, screen
    if current_player == "X":
        current_player = "O"
        screen["text"] = current_player + "'s turn."
    elif current_player == "O":
        current_player = "X"
        screen["text"] = current_player + "'s turn."
    return


def checker(buttons):
    global current_player, push_button, screen, value, entry_X, entry_O, count_x, count_o, current_match, ready
    if value == 0:
        tmsg.showinfo("Warning","1st Input The Number of Match You Want To Play")
        return

    if buttons["text"] == " " and current_player == "X":
        buttons.config(
            text = current_player,
            bg = "#F2746B",
            fg = "black"
        )
        push_button = buttons
        if check_if_game_over():
            #print(current_player)
            screen["text"] = current_player + " Win."
            count_x = count_x + 1
            current_match = current_match + 1
            entry_X["text"] = count_x
            entry_match["text"] = f"{current_match} / {value}"
            #ans = tmsg.askyesno("Message", current_player + " Win.\n\n Go for next match??")
            ans = tmsg.showinfo("Message", current_player + " Win.\n\n Go for next match??")
            if ans == "ok":
                if current_match % 2 != 0:
                    current_player = "O"
                    ready = "Ready...O's turn"
                else:
                    current_player = "X"
                    ready = "Ready...X's turn"

                button_construction()
                screen["text"] = ready
                play_game()
            else:
                exit_code()

            return

        elif check_if_game_over() == None:
            screen["text"] = "Match Tie."
            current_match = current_match + 1
            entry_match["text"] = f"{current_match} / {value}"
            ans = tmsg.showinfo("Message", "Match Tie.\n\n Go for next match??")
            if ans == "ok":
                if current_match % 2 != 0:
                    current_player = "O"
                    ready = "Ready...O's turn"
                else:
                    current_player = "X"
                    ready = "Ready...X's turn"
                button_construction()
                screen["text"] = ready
                play_game()
            else:
                exit_code()
            return


        flipped_player()

    elif buttons["text"] == " " and current_player == "O":
        buttons.config(
            text = current_player,
            bg = "#118C8B",
            fg  = "white"
        )
        push_button = buttons
        if check_if_game_over():
            screen["text"] = current_player + " Win."
            count_o = count_o + 1
            current_match = current_match + 1
            entry_O["text"] = count_o
            entry_match["text"] = f"{current_match} / {value}"
            ans = tmsg.showinfo("Message", current_player + " Win.\n\n Go for next match??")
            if ans == "ok":
                if current_match % 2 != 0:
                    current_player = "O"
                    ready = "Ready...O's turn"
                else:
                    current_player = "X"
                    ready = "Ready...X's turn"
                button_construction()
                screen["text"] = ready
                play_game()
            return

        elif check_if_game_over() == None:
            screen["text"] = "Match Tie."
            current_match = current_match + 1
            entry_match["text"] = f"{current_match} / {value}"
            ans = tmsg.showinfo("Message", "Match Tie.\n\n Go for next match??")
            if ans == "ok":
                if current_match % 2 != 0:
                    current_player = "O"
                    ready = "Ready...O's turn"
                else:
                    current_player = "X"
                    ready = "Ready...X's turn"
                button_construction()
                screen["text"] = ready
                play_game()
            return

        flipped_player()


def check_for_winner():

    global screen
    global b1,b2,b3,b4,b5,b6,b7,b8,b9

    column_1 = str(b1.cget('text')) == str(b2.cget('text')) == str(b3.cget('text')) != " "
    column_2 = b4.cget('text') == b5.cget('text') == b6.cget('text') != " "
    column_3 = b7.cget('text') == b8.cget('text') == b9.cget('text') != " "
    #print(column_1)

    row_1 = b1.cget('text') == b4.cget('text') == b7.cget('text') != " "
    row_2 = b2.cget('text') == b5.cget('text') == b8.cget('text') != " "
    row_3 = b3.cget('text') == b6.cget('text') == b9.cget('text') != " "

    diagonal_1 = b1.cget('text') == b5.cget('text') == b9.cget('text') != " "
    diagonal_2 = b3.cget('text') == b5.cget('text') == b7.cget('text') != " "

    if column_1:
        return True
    elif column_2:
        return True
    elif column_3:
        return True
    elif row_1:
        return True
    elif row_2:
        return True
    elif row_3:
        return True
    elif diagonal_1:
        return True
    elif diagonal_2:
        return True

    return False

def check_for_tie():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9, screen

    if b1.cget('text') != " " and b2.cget('text') != " " and b3.cget('text') != " " and b4.cget('text') != " " and b5.cget('text') != " " and b6.cget('text') != " " and b7.cget('text') != " " and b8.cget('text') != " " and b9.cget('text') != " ":
        #print("Rajib")
        screen["text"] = "Match Tie."
        print("Match Tie")
        return True

def check_if_game_over():
    global value, current_match, entry_match, count_x, count_o, entry_O, entry_X, valid, current_player
    if current_match >= value:
        qstn = tmsg.askyesno("Warning", "Want to play More?")
        if qstn:
            current_player = "X"
            button_construction()
            screen["text"] = "Ready...X's turn"
            value = 0
            current_match = 0
            entry_match["text"] = ""
            count_x = 0
            count_o = 0
            entry_O["text"] = count_o
            entry_X["text"] = count_x
            play_game()
        else:
            exit_code()
    if check_for_winner():
        valid = True
        return True
    elif check_for_tie():
        valid = True
        return

    return False


def reset_turn():

    global push_button, current_player
    if push_button == 0:
        return

    if push_button["text"] != " ":
        push_button.config(
            text=" ",
            bg="blanched almond",
            fg = "black"
        )
        flipped_player()


def exit_code():
    MsgBox = tmsg.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()

def help_code():
    tmsg.showinfo("Help", "Tic Tac Toe is a popular game for children\n\n 1. Enter the number of time you want to play.\n 2. Then click the submit button.\n\n Now you are ready to play")

def submit_code():
    global number_of_match_entry, entry_match, current_match, value
    if number_of_match_entry.get().isdigit():
        value = int(number_of_match_entry.get())
        #print(value)
        entry_match.config(text = f"{current_match} / {value}")
        return
    tmsg.showinfo("Warning", "Please enter valid number.")
    entry_match.config(text = "")
    return




def b1_enter(event):
    global current_player, b1

    if b1["text"] == " " and current_player == "X":
        b1.config(
            bg = "#F2746B"
        )
    elif b1["text"] == " " and current_player == "O":
        b1.config(
            bg = "#118C8B"
        )

def b1_leave(event):
    global b1
    if b1["text"] == " ":
        b1.config(
            bg="blanched almond",
        )


def b2_enter(event):
    global current_player, b2

    if b2["text"] == " " and current_player == "X":
        b2.config(
            bg = "#F2746B"
        )
    elif b2["text"] == " " and current_player == "O":
        b2.config(
            bg = "#118C8B"
        )

def b2_leave(event):
    global b2
    if b2["text"] == " ":
        b2.config(
            bg="blanched almond",
        )


def b3_enter(event):
    global current_player, b3

    if b3["text"] == " " and current_player == "X":
        b3.config(
            bg = "#F2746B"
        )
    elif b3["text"] == " " and current_player == "O":
        b3.config(
            bg = "#118C8B"
        )

def b3_leave(event):
    global b3
    if b3["text"] == " ":
        b3.config(
            bg="blanched almond",
        )

def b4_enter(event):
    global current_player, b4

    if b4["text"] == " " and current_player == "X":
        b4.config(
            bg = "#F2746B"
        )
    elif b4["text"] == " " and current_player == "O":
        b4.config(
            bg = "#118C8B"
        )

def b4_leave(event):
    global b4
    if b4["text"] == " ":
        b4.config(
            bg="blanched almond",
        )

def b5_enter(event):
    global current_player, b5

    if b5["text"] == " " and current_player == "X":
        b5.config(
            bg = "#F2746B"
        )
    elif b5["text"] == " " and current_player == "O":
        b5.config(
            bg = "#118C8B"
        )

def b5_leave(event):
    global b5
    if b5["text"] == " ":
        b5.config(
            bg="blanched almond",
        )

def b6_enter(event):
    global current_player, b6

    if b6["text"] == " " and current_player == "X":
        b6.config(
            bg = "#F2746B"
        )
    elif b6["text"] == " " and current_player == "O":
        b6.config(
            bg = "#118C8B"
        )

def b6_leave(event):
    global b6
    if b6["text"] == " ":
        b6.config(
            bg="blanched almond",
        )

def b7_enter(event):
    global current_player, b7

    if b7["text"] == " " and current_player == "X":
        b7.config(
            bg = "#F2746B"
        )
    elif b7["text"] == " " and current_player == "O":
        b7.config(
            bg = "#118C8B"
        )

def b7_leave(event):
    global b7
    if b7["text"] == " ":
        b7.config(
            bg="blanched almond",
        )

def b8_enter(event):
    global current_player, b8

    if b8["text"] == " " and current_player == "X":
        b8.config(
            bg = "#F2746B"
        )
    elif b8["text"] == " " and current_player == "O":
        b8.config(
            bg = "#118C8B"
        )

def b8_leave(event):
    global b8
    if b8["text"] == " ":
        b8.config(
            bg="blanched almond",
        )

def b9_enter(event):
    global current_player, b9

    if b9["text"] == " " and current_player == "X":
        b9.config(
            bg = "#F2746B"
        )
    elif b9["text"] == " " and current_player == "O":
        b9.config(
            bg = "#118C8B"
        )

def b9_leave(event):
    global b9
    if b9["text"] == " ":
        b9.config(
            bg="blanched almond",
        )

def play_game():

    screen()
    score_board()
    frame_board()
    board_side()



play_game()


def button_construction():
    b1.config(
        text=" ",
        bg="blanched almond"
    )
    b2.config(
        text=" ",
        bg="blanched almond"
    )
    b3.config(
        text=" ",
        bg="blanched almond"
    )
    b4.config(
        text=" ",
        bg="blanched almond"
    )
    b5.config(
        text=" ",
        bg="blanched almond"
    )
    b6.config(
        text=" ",
        bg="blanched almond"
    )
    b7.config(
        text=" ",
        bg="blanched almond"
    )
    b8.config(
        text=" ",
        bg="blanched almond"
    )
    b9.config(
        text=" ",
        bg="blanched almond"
    )

root.mainloop()





