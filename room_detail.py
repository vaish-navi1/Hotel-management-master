from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import messagebox

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('1000x750')


# calling functions
def click_vacancy():
    call(["python", "vacancy.py"])





def click_allcust():
    call(['python', 'all_details.py'])


# variables
Room_no = IntVar()


# database
def click_proceed():
    text.delete('1.0', END)
    room_no = Room_no.get()

    if room_no == 0:
        rn_entry.delete(0, 'end')
        messagebox.showwarning("Warning", "Incomplete Data Entry")
    else:
        mydb = mysql.connector.connect(host='localhost', user='root', password='123456', database='hotel')
        cur = mydb.cursor()
        cur.execute('Select Exists(select * from hotel_management where Room_No=%s)', (room_no,))
        res = cur.fetchall()
        avail = 0
        for i in res:
            a = list(i)
            avail = a[0]
        if avail == 1:
            cur.execute('SELECT First_Name,Room_Type,No_People from hotel_management where Room_No =%s', (room_no,))
            result = cur.fetchall()
            tup = []
            for i in result:
                tup = list(i)
                rt = ''
                if tup[1] == 1:
                    rt = "AC"
                else:
                    rt = "Non-AC"
                final_detail = "\nFirst Name :\t " + tup[0] + "\n\n" + "Room Type :\t " + rt + "\n"
                text.insert(INSERT, final_detail)
            no_p = "\n\nNumber of People :\t " + str(tup[2])
            text.insert(INSERT, no_p)
        else:
            text.insert(INSERT, "The Entered Room Number is UN-OCCUPIED \t Please Enter a Valid Room Number !")



# heading
heading_label = Label(root, text="---------  ROOM DETAILS  ---------", font=('Orbitron', 15), bg="black", fg="white")
heading_label.pack(fill=X)

topFrame = Frame(root)
topFrame.pack()

blankspace = Label(topFrame, text="\n\n\n\n\n")
blankspace.grid(row=0)

# Room Number
rn_label = Label(topFrame, text="Room Number : ", font=('Orbitron', 30))
rn_entry = Entry(topFrame, textvar=Room_no, bd=5, bg="#ccefff", fg='blue', width=15, font=('Arial', 15))

rn_label.grid(row=1, column=0, padx=15, pady=10, sticky=E)
rn_entry.grid(row=1, column=1, ipady=5, ipadx=60, sticky=W)

# Search Button
submit_button = Button(root, text="SEARCH", width=12, bg="#269900", fg='Black', font=('ARIAL BLACK', 20), relief=RAISED,
                       command=click_proceed)
submit_button.place(relx=0.5, rely=0.40, anchor=S)

# text bar
text = Text(root, bd=5, bg="white", fg='blue', width=200, font=('Arial', 15))
text.place(rely=0.45)

root.mainloop()
