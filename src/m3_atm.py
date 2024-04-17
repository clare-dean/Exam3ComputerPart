import tkinter as tk

###############################################################################
# DONE: 1. (2 pts)
#
#   The todos in this module are in one comment because you will be modifying
#   the same bit of code each time. Here you will create a basic ATM
#   application that allows a user to withdraw funds and deposit funds
#
#   For this _todo_, you will create a window with the title "ATM" and call its
#   mainloop() method so it runs.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (3 pts)
#
#   For this _todo_, you will create an area where the user's current balance
#   is displayed. There should be a label that says "Current Balance ($):" and
#   below it another label that has the dollar amount of their current balance
#   displayed. For the purposes of this problem, we will assume that all users
#   start out with 1000 dollars in their account. So, this label should start
#   out with "1000" as its text.
#
#   All of the elements on this window should be centered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 3 (3 pts)
#
#   For this _todo_, create two more labels: one that says "Amount ($):" and
#   another that starts out empty beneath it. This is where the user's amount
#   that they will either withdraw or deposit will display.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 4. (7 pts)
#
#   For this _todo_, you will create all the buttons that the user needs:
#
#       - One for each digit 0-9
#       - A withdrawal button
#       - A deposit button
#
#   They should be in the standard configuration for a numberpad (see the
#   images in the README file on GitHub). Each button is 75px by 75px.
#
#   HINT: I used a frame to surround the buttons and grid for this.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 5. (10 pts)
#
#   For this _todo_, using the command keyword on each button to have each
#   number button type that digit in the amount label above (just like you
#   would if you were typing in an amount). Pressing each button should add
#   that number to end of the text in the label.
#
#   HINT: I found that the easiest way to accomplish this was to use a
#   different handler for each button.
#
#   You also need a handler for the withdrawal and deposit buttons.
#
#   The withdrawal button should subtract the amount typed into the amount box
#   from the user's current balance. It should clear the amount label and
#   update the current balance label.
#
#   The deposit button should add the amount typed into the amount box to the
#   user's current balance. It should also clear the amount label and update
#   the current balance label.
#
#   Remember that, for these handlers, you will need to convert the strings in
#   the label's to floats before you do your calculations.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 5. (3 pts)
#
#   For this _todo_, bind the window to any keypress so that if the user types
#   a number, it also types that number into the amount label. Remember, you
#   can use isdigit() to check if the key pressed is a digit.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
root = tk.Tk()
root.title("ATM")

current_balance = 1000

balance_label = tk.Label(root, text="Current Balance ($):", font=("Helvetica", 12))
balance_label.pack(pady=10)

amount_label = tk.Label(root, text=str(current_balance), font=("Helvetica", 14, "bold"))
amount_label.pack()

amount_text = tk.Label(root, text="Amount ($):", font=("Helvetica", 12))
amount_text.pack(pady=10)

amount_display = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
amount_display.pack()

button_frame = tk.Frame(root)
button_frame.pack()

def add_number(num):
    current_amount = amount_display.cget("text")
    amount_display.config(text=current_amount + str(num))

for i in range(1, 10):
    button = tk.Button(button_frame, text=str(i), width=5, height=2, command=lambda i=i: add_number(i))
    button.grid(row=(i-1)//3, column=(i-1)%3)

button_0 = tk.Button(button_frame, text="0", width=5, height=2, command=lambda: add_number(0))
button_0.grid(row=3, column=1)

def withdraw_amount():
    global current_balance
    amount = float(amount_display.cget("text"))
    current_balance -= amount
    amount_display.config(text="")
    amount_label.config(text=str(current_balance))

withdraw_button = tk.Button(button_frame, text="Withdrawal", width=10, height=2, command=withdraw_amount)
withdraw_button.grid(row=4, column=0, columnspan=2)

def deposit_amount():
    global current_balance
    amount = float(amount_display.cget("text"))
    current_balance += amount
    amount_display.config(text="")
    amount_label.config(text=str(current_balance))

deposit_button = tk.Button(button_frame, text="Deposit", width=5, height=2, command=deposit_amount)
deposit_button.grid(row=4, column=2)


for widget in root.winfo_children():
    widget.pack_configure(anchor='center')


def keypress(event):
    key = event.char
    if key.isdigit():
        add_number(int(key))

root.bind('<Key>', keypress)

root.mainloop()