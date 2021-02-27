from tkinter import *
from tkinter import ttk
import pandas as pd
import csv, sys, os, shutil
import tkinter.messagebox

global id

def load():
    try:
        selected_item = database.focus()  ## get selected item
        print(selected_item)
        # print(selected_item[])
        idval.set(database.item(selected_item)['values'][0])
        titleval.set(database.item(selected_item)['values'][1])
        wnameval.set(database.item(selected_item)['values'][2])
        pubval.set(database.item(selected_item)['values'][3])
        genreval.set(database.item(selected_item)['values'][4])
        dateval.set(database.item(selected_item)['values'][5])
        copiesval.set(database.item(selected_item)['values'][6])
        costval.set(database.item(selected_item)['values'][7])
        pubwebval.set(database.item(selected_item)['values'][8])


    except IndexError:
        tkinter.messagebox.showinfo('Error', 'Please select one record')




def submit_value():

    if idval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')


    elif idval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')

    elif titleval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')
    elif wnameval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')

    elif pubval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')
    elif genreval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')
    elif dateval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')

    elif copiesval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')

    elif costval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')

    elif pubwebval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')



    else:
        try:
            with open('BookRecords.csv', 'a+') as records:
                writer = csv.writer(records)
                writer.writerow(
                    [idval.get(), titleval.get(), wnameval.get(), pubval.get(), genreval.get(), dateval.get(),
                     copiesval.get(), costval.get(), pubwebval.get()])
                records.close()

            with open('BookRecords.csv') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    id = row['ID No']
                    titlevalcsv = row['Title']
                    wnamevalcsv = row['Writers Name']
                    pubvalcsv = row['Publisher']
                    genrevalcsv = row['Genre']
                    datevalcsv = row['Date of issue']
                    copiesvalcsv = row['No of Copies']
                    costvalcsv = row['Cost']
                    pubwebvalcsv = row['Publishers Website']

            database.insert("", END, values=(id, titlevalcsv, wnamevalcsv, pubvalcsv, genrevalcsv,
                                             datevalcsv, copiesvalcsv, costvalcsv, pubwebvalcsv))



            id_entry.delete(0, END)
            title_entry.delete(0, END)
            wname_entry.delete(0, END)
            pub_entry.delete(0, END)
            genre_entry.delete(0, END)
            date_entry.delete(0, END)
            copies_entry.delete(0, END)
            cost_entry.delete(0, END)
            pubweb_entry.delete(0, END)

        except PermissionError:
            tkinter.messagebox.showinfo('Permission Error', 'Please close the database (csv) file ')


def delete():
        msg = tkinter.messagebox.askquestion('Sure?', 'Are you sure you want to remove the Book and all his/her details?')
        if msg == 'yes':
            remove()

        else:
            pass



def remove():
    try:
            #selected_item = database.selection()[0] ## get selected item
            # print(database.item(selected_item))
            # print(remove)
        selected_item = database.focus() ## get selected item

        database_pd = pd.read_csv('BookRecords.csv')
        remove = database.item(selected_item)['values'][0]
        specify = database_pd.loc[database_pd['ID No'] == remove]
        id = specify.iloc[0, 0]
        name_remove = specify.iloc[0, 1]
        shutil.rmtree('Book Profile\\' + str(id) + str(name_remove))
        database_pd = database_pd.loc[database_pd['ID No'] != remove]
        database_pd.to_csv('BookRecords.csv', index=0)

        database.delete(selected_item)
        with open('BookRecords.csv', 'a+') as records:
            writer = csv.writer(records)

    except IndexError:
        tkinter.messagebox.showinfo('Error', 'Please choose a record')






root = Tk()

root.geometry('1000x550')
root.title('Library Management System')
# root.minsize(460, 540)
# root.maxsize(460, 540)

frame1 = Frame(root, borderwidth='10', relief=RIDGE, bg='deepskyblue4')
title = Label(frame1, text='Library Management System', fg='white', bg='deepskyblue4', pady='20',
              font=('Copperplate Gothic Bold', 20, 'bold'))

title.pack()
frame1.pack(fill=X)

framex_books = Frame(root)

frame2_books = Frame(framex_books, borderwidth='10', relief=RIDGE, bg='deepskyblue4')
form_text = Label(frame2_books, text='Fill up the following form for adiing New Book ', fg='white', bg='deepskyblue4',
                  pady='20', padx='5', font=('Calibri', 15, 'bold'))
form_text.grid()

id = Label(frame2_books, text='ID No : ', fg='white', bg='deepskyblue4', font=(10))
id.grid(row=1, column=0, stick=W, padx=20)

book_title = Label(frame2_books, text='Book Title : ', fg='white', bg='deepskyblue4', font=(10))
book_title.grid(row=2, column=0, stick=W, padx=20)

writers_name = Label(frame2_books, text='Writers Name : ', fg='white', bg='deepskyblue4', font=(10))
writers_name.grid(row=3, column=0, stick=W, padx=20)

publisher = Label(frame2_books, text='Publisher : ', fg='white', bg='deepskyblue4', font=(10))
publisher.grid(row=4, column=0, stick=W, padx=20)

genre = Label(frame2_books, text='Genre : ', fg='white', bg='deepskyblue4', font=(10))
genre.grid(row=5, column=0, stick=W, padx=20)


date = Label(frame2_books, text='Date of issue : ', fg='white', bg='deepskyblue4', font=(10))
date.grid(row=7, column=0, stick=W, padx=20)

copies = Label(frame2_books, text='Number of Copies : ', fg='white', bg='deepskyblue4', font=(10))
copies.grid(row=8, column=0, stick=W, padx=20)

cost = Label(frame2_books, text='Cost per copy : ', fg='white', bg='deepskyblue4', font=(10))
cost.grid(row=9, column=0, stick=W, padx=20)

pub_website = Label(frame2_books, text='Publishers website : ', fg='white', bg='deepskyblue4', font=(10))
pub_website.grid(row=10, column=0, stick=W, padx=20)

submit = Button(frame2_books, text='Submit', command=submit_value)
submit.place(x=175, y=360)

del_data = Button(frame2_books, text='Delete', command=delete)
del_data.place(x=115, y=400)


update = Button(frame2_books, text='Update')
update.place(x=175, y=400)



idval, titleval, wnameval, pubval, genreval, dateval, copiesval, costval, pubwebval = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
searchval = StringVar()


id_entry = Entry(frame2_books, textvariable=idval)
id_entry.place(x=150, y=69)

title_entry = Entry(frame2_books, textvariable=titleval)
title_entry.place(x=150, y=93)

wname_entry = Entry(frame2_books, textvariable=wnameval)
wname_entry.place(x=150, y=117)

pub_entry = Entry(frame2_books, textvariable=pubval)
pub_entry.place(x=150, y=142)

genre_entry = ttk.Combobox(frame2_books, values=
[
    'Action',
    'Thriller',
    'Romance',
    'Children',
    'GK',
    'Educational'
    
    
], 
textvariable=genreval)
genre_entry.place(x=150, y=167)

date_entry = Entry(frame2_books, textvariable=dateval)
date_entry.place(x=150, y=191)

copies_entry = Entry(frame2_books, textvariable=copiesval)
copies_entry.place(x=150, y=215)

cost_entry = Entry(frame2_books, textvariable=costval)
cost_entry.place(x=150, y=239)

pubweb_entry = Entry(frame2_books, textvariable=pubwebval)
pubweb_entry.place(x=150, y=263)





frame3_books = Frame(framex_books, bg='deepskyblue4', borderwidth='10', relief=RIDGE)
text3 = Label(frame3_books, text='Search ID : ', bg='deepskyblue4', fg='white', padx=40, pady=20, font=('Calibri', 12, 'bold'))
text3.grid(row=0, column=0, sticky='w')

search = ttk.Combobox(frame3_books, values=
[
    'Title',
    'ID',
    'Genre',
    
], 
textvariable=searchval)
search.grid(row=0, column=1)

search_button = Button(frame3_books, text='Search')
search_button.grid(row=0, column=3, padx=10)

load_button = Button(frame3_books, text='Load record', command=load)
load_button.grid(row=0, column=4)


frame4_books = Frame(frame3_books, bg='deepskyblue4', borderwidth='10', relief=RIDGE)



scrollbar = Scrollbar(frame4_books)
scrollbar.pack(side=RIGHT, fill=Y)

scrollbarh = Scrollbar(frame4_books, orient='horizontal')
scrollbarh.pack(side=BOTTOM, fill=X)

tuples = ['test']

database = ttk.Treeview(frame4_books)

database['columns'] = ['ID No', 'Title', 'Writers Name', 'Publisher', 'Genre', 'Date of issue', 'No of Copies', 'Cost', 'Publishers Website']
database['show'] = 'headings'
database.heading('ID No', text='ID No')
database.heading('Title', text='Title')
database.heading('Writers Name', text='Writers Name')
database.heading('Publisher', text='Publisher')
database.heading('Genre', text='Genre')
database.heading('Date of issue', text='Date of issue')
database.heading('No of Copies', text='No of Copies')
database.heading('Cost', text='Cost')
database.heading('Publishers Website', text='Publishers Website')

database.column('ID No', width=100)
database.column('Title',  width=100)
database.column('Writers Name', width=100)
database.column('Publisher', width=100)
database.column('Genre', width=100)
database.column('Date of issue', width=100)
database.column('No of Copies', width=100)
database.column('Cost', width=100)
database.column('Publishers Website', width=100)

database.pack(fill=BOTH, expand=1)



scrollbar.config(command=database.yview)
scrollbarh.config(command=database.xview)



try:
    with open('BookRecords.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            id = row['ID No']
            titlevalcsv = row['Title']
            wnamevalcsv = row['Writers Name']
            pubvalcsv = row['Publisher']
            genrevalcsv= row['Genre']
            datevalcsv = row['Date of issue']
            copiesvalcsv = row['No of Copies']
            costvalcsv = row['Cost']
            pubwebvalcsv = row['Publishers Website']

            database.insert("", END, values=(id, titlevalcsv, wnamevalcsv, pubvalcsv, genrevalcsv,
             datevalcsv, copiesvalcsv, costvalcsv, pubwebvalcsv))

except FileNotFoundError:
    with open('BookRecords.csv', 'a+') as records:
        writer = csv.writer(records)
        writer.writerow(
            ['ID No', 'Title', 'Writers Name', 'Publisher', 'Genre', 'Date of issue', 'No of Copies', 'Cost', 'Publishers Website'
             ])
    records.close()



frame2_books.pack(side=LEFT, fill=BOTH)
frame4_books.place(x=50, y=100, width=700, height=300)
frame3_books.pack(fill=BOTH, expand=1)

framex_books.pack(fill=BOTH, expand=1)

root.mainloop()

