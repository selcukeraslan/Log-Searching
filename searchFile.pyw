#Python Program to search string in text using Tkinter
#Programmed by Selcuk Eraslan
#Github.com/selcukeraslan


from string import hexdigits
from tkinter import *
from datetime import datetime
from tkinter import filedialog



#to create a window
root = Tk()
root.title("Ulak Haberleşme Log Çekme Programı")
root.iconbitmap('ulak.ico')
root.geometry('1400x1000')

#root window is the parent window
fram = Frame(root)


btnFile = Button(fram, text='Select File')
btnFile.pack(side=LEFT)

btn = Button(fram, text='Delete', command=lambda: text.delete(1.0,END))
btn.pack(side=LEFT)

#Before Line Search
varBefore = IntVar()
checkBoxBefore = Checkbutton(fram, text='Before Lines',variable=varBefore, onvalue=1, offvalue=0)
checkBoxBefore.pack(side=LEFT)
beforeEntry = Entry(fram, width=3).pack(side=LEFT,pady=3)

#After Line Search
varAfter = IntVar()
checkBoxAfter = Checkbutton(fram,text='After Lines',variable=varAfter, onvalue=1, offvalue=0)
checkBoxAfter.pack(side=LEFT)
afterEntry = Entry(fram,width=3).pack(side=LEFT)

var1 = IntVar()
checkBox1 = Checkbutton(fram, text='Word Only',variable=var1, onvalue=1, offvalue=0)
checkBox1.pack(side=LEFT)

#adding of single line text box
edit = Entry(fram)

#positioning of text box
edit.pack(side=LEFT, fill=BOTH, expand=1)

#setting focus
edit.focus_set()

var2 = IntVar()
checkBox2 = Checkbutton(fram, text='Starting Date',variable=var2, onvalue=1, offvalue=0).pack(side=LEFT)

tarih1 = Entry(fram, bd=3, font = ("Helvetica", 13, "bold"), cursor = "watch")
tarih1.pack(side=LEFT, fill= BOTH, expand=1)
tarih1.focus_set()


var3 = IntVar()
checkBox3 = Checkbutton(fram, text='End Date',variable=var3, onvalue=1, offvalue=0).pack(side=LEFT)

tarih2 = Entry(fram, bd=3, font = ("Helvetica", 13, "bold"), cursor = "watch")
tarih2.pack(side=LEFT, fill= BOTH, expand=1)
tarih2.focus_set()

print("Selcuk")
print("Hello")

#adding of search button
butt = Button(fram, text='Find')
butt.pack(side=RIGHT)

fram.pack(side=TOP)

# Add a Scrollbar(horizontal)
h=Scrollbar(root, orient='horizontal')
h.pack(side=BOTTOM, fill='x')

v=Scrollbar(root, orient='vertical')
v.pack(side=RIGHT, fill='y')

#text box in root window
text = Text(root, height=1000, width=1000, wrap=NONE, xscrollcommand=h.set)
text.bind("<Key>", lambda e: "break")

#text input area at index 1 in text window
text.pack()

h.config(command=text.xview)
v.config(command=text.yview)

def open_txt():
    global file
    file = filedialog.askopenfilename(initialdir='/',title='Select File')
    fp = open(file, 'r', encoding='latin1')
    fp.close()


def parse_date(date_str):
    # format mm/dd/yy HH:MM:SS[.NNNNNN]
    date_fmt = '%m/%d/%y %H:%M:%S'
    if '.' in date_str:
        date_fmt += '.%f'
    return datetime.strptime(date_str, date_fmt)


#function to search string in text
def search(msg, startingDate, endingDate):
    # clear current result
    text.delete('1.0', 'end')
    with open(file, 'r', encoding='latin1') as fp:
        for l_no, line in enumerate(fp, 1):
            if msg and msg not in line:
                # does not contain search message, skip it
                continue
            if startingDate or endingDate:
                # get the timestamp
                timestamp = parse_date(line[1:25])
                # within startingDate and endingDate ?
                if startingDate and timestamp < startingDate:
                    # before given starting date, skip it
                    continue
                if endingDate and timestamp > endingDate:
                    # after given ending date, skip it
                    continue
            # insert the log
            text.insert('end', ' \n ')
            text.insert('end', f'Line Number: {l_no} Log: {line}')
            text.insert('end', ' \n ')



def getInfo():
    msg = edit.get() if var1.get() == 1 else None
    startingDate = parse_date(tarih1.get()) if var2.get() == 1 else None
    endingDate = parse_date(tarih2.get()) if var3.get() == 1 else None

    search(msg, startingDate, endingDate)


butt.config(command=getInfo)
btnFile.config(command=open_txt)


#mainloop function calls the endless loop of the window,
#so the window will wait for any
#user interaction till we close it
root.mainloop()
