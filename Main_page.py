from subprocess import call
from tkinter import *

root = Tk(className=" HOTEL MANAGEMENT ")
root.geometry('1920x1080')


# calling functions
def click_checkin():
    call(["python", "check_in.py"])


def click_checkout():
    call(["python", "check_out.py"])


def click_roomdetail():
    call(["python", "room_detail.py"])


def click_custdetail():
    call(["python", "customer_detail.py"])


def click_vacancy():
    call(["python", "vacancy.py"])



def click_allcust():
    call(['python', 'all_details.py'])

    
def click_secondperson():
    call(['python', 'second_person.py'])





# Title label
title_label = Label(root, text="---------  HOTEL MANAGEMENT  ---------", height=2, font=('cooper black', 15,'bold'), bg="#ff80bf")
title_label.pack(fill=X)

# Welcome label
welcome_label = Label(root, text="WELCOME", bg="purple", fg="white", font=('cooper black', 25))
welcome_label.pack(fill=X)

blankspace = Label(root, text="\n")
blankspace.pack()


# Buttons
cin_button = Button(root, text="Check In", bg='#000000', fg='white', font=('Orbitron', 20, 'bold'), width=20,
                    command=click_checkin)
cin_button.pack(pady=10)

sp_button = Button(root, text="Second Person", bg="#000000", fg="white", width=20, command=click_secondperson ,font=('Orbitron', 20, 'bold'))
sp_button.pack(pady=10)


cot_button = Button(root, text="Check Out", bg='#1a1a1a', fg='white', font=('Orbitron', 20, 'bold'), width=20,
                    command=click_checkout)
cot_button.pack(pady=10)


rd_button = Button(root, text="Room Details", bg='#404040', fg='white', font=('Orbitron', 20, 'bold'), width=20,
                   command=click_roomdetail)
rd_button.pack(pady=10)


cd_button = Button(root, text="Customer Details", bg='#666666', fg='white', font=('Orbitron', 20, 'bold'), width=20,
                   command=click_custdetail)
cd_button.pack(pady=10)



ac_button = Button(root, text="All Customer Details", bg="#666666", fg="white", width=20, command=click_allcust ,font=('Orbitron', 20, 'bold'))
ac_button.pack(pady=10)



exit_button = Button(root, text="Exit", bg="#ff0000", fg="white", width=20, command=root.quit,
                     font=('Orbitron', 20, 'bold'))
exit_button.pack(pady=10)


root.mainloop()
