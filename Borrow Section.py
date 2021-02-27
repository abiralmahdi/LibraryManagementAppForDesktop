from tkinter import *
from tkinter import ttk
import pandas as pd
import csv
import shutil
import sys
import os
import time
import tkinter.messagebox
import datetime
import schedule


def raise_fame(frame):
    frame.tkraise()

def load():
    try:
        selected_item = database.focus()  ## get selected item
        print(selected_item)
        # print(selected_item[])
        idval.set(database.item(selected_item)['values'][0])
        nameval.set(database.item(selected_item)['values'][1])
        fnameval.set(database.item(selected_item)['values'][2])
        mnameval.set(database.item(selected_item)['values'][3])
        contactval.set(database.item(selected_item)['values'][4])
        emailval.set(database.item(selected_item)['values'][5])
        professionval.set(database.item(selected_item)['values'][6])
        desigval.set(database.item(selected_item)['values'][7])
        payval.set(database.item(selected_item)['values'][8])


    except IndexError:
        tkinter.messagebox.showinfo('Error', 'Please select one record')





def delete():
        msg = tkinter.messagebox.askquestion('Sure?', 'Are you sure you want to remove the Member and all his/her details?')
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

        database_pd = pd.read_csv('MemberRecords.csv')
        remove = database.item(selected_item)['values'][0]
        specify = database_pd.loc[database_pd['ID No'] == remove]
        id = specify.iloc[0, 0]
        name_remove = specify.iloc[0, 1]
        shutil.rmtree('Member Profile\\' + str(id) + str(name_remove))
        database_pd = database_pd.loc[database_pd['ID No'] != remove]
        database_pd.to_csv('MemberRecords.csv', index=0)

        database.delete(selected_item)
        with open('MemberRecords.csv', 'a+') as records:
            writer = csv.writer(records)

    except IndexError:
        tkinter.messagebox.showinfo('Error', 'Please choose a record')


def autofill():
    member_pd = pd.read_csv('MemberRecords.csv')
    member_specify = member_pd.loc[member_pd['ID No'] == idval.get()]
    nameval.set(member_specify.iloc[0, 1])
    fnameval.set(member_specify.iloc[0, 2])
    mnameval.set(member_specify.iloc[0, 3])
    contactval.set(member_specify.iloc[0, 4])
    emailval.set(member_specify.iloc[0, 5])
    professionval.set(member_specify.iloc[0, 6])
    desigval.set(member_specify.iloc[0, 7])
    payval.set(member_specify.iloc[0, 8])




def borrow_book():
    global member_specify
    
    book_pd = pd.read_csv('BookRecords.csv')
    borrow_pd = pd.read_csv('BorrowRecords.csv')
    member_pd = pd.read_csv('MemberRecords.csv')
    
    
    selected_item = database.focus()
    book_index = database.index(selected_item)
    
    print(database.item(selected_item)['values'][6])
    
    deducted = database.item(selected_item)['values'][6] - 1
    database.insert("", book_index, values=(database.item(selected_item)['values'][0], 
                                            database.item(selected_item)['values'][1] ,
                                            database.item(selected_item)['values'][2], 
                                            database.item(selected_item)['values'][3],
                                            database.item(selected_item)['values'][4],
                                            database.item(selected_item)['values'][5],
                                            deducted, 
                                            database.item(selected_item)['values'][7], 
                                            database.item(selected_item)['values'][8]))
    
    
    member_specify = member_pd.loc[member_pd['ID No'] == idval.get()]
    
    book_pd.iloc[book_index, 6] = book_pd.iloc[book_index, 6] - 1
    
    
    borrow_book_id = book_pd.iloc[book_index, 0]
    borrow_book_title = book_pd.iloc[book_index, 1]
    borrow_book_writer = book_pd.iloc[book_index, 2]
    member_id = member_specify.iloc[0, 0]
    member_name = member_specify.iloc[0, 1]
    borrow_publisher = book_pd.iloc[book_index, 3]
    borrow_genre  = book_pd.iloc[book_index, 4]
    
    database.delete(selected_item)

    
    try:
        
        with open('BorrowRecords.csv', 'a+') as borrow_records:
            writer = csv.writer(borrow_records)
            writer.writerow([borrow_book_id, 
                            borrow_book_title,
                            borrow_book_writer, 
                            member_id, 
                            member_name,
                            borrow_publisher, 
                            borrow_genre,
                            datetime.datetime.today().strftime('%d-%m-%Y'),
                            datetime.datetime.today() + datetime.timedelta(days=7)])

    #borrow_pd.read_csv('BorrowRecords.csv', index=0)
        book_pd.to_csv('BookRecords.csv', index=0)

  

        borrow_database.insert("", END, values=(borrow_book_id,
                                                borrow_book_title,
                                                borrow_book_writer, 
                                                member_id,
                                                member_name, 
                                                borrow_publisher, 
                                                borrow_genre, 
                                                datetime.datetime.today().strftime('%d-%m-%Y'),
                                                datetime.datetime.today() + datetime.timedelta(days=7)))
        
        
    except PermissionError:
        pass



def returned():
    
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    
    book_pd = pd.read_csv('BookRecords.csv')
    borrow_pd = pd.read_csv('BorrowRecords.csv')
    
    selected_item = borrow_database.focus()
    book_id = borrow_database.item(selected_item)['values'][0]
    index_no = borrow_database.index(selected_item)
    borrow_pd = borrow_pd.drop(index_no)     
    
    borrow_pd.to_csv('BorrowRecords.csv', index=0)
    borrow_database.delete(selected_item)

    
    idx = book_pd.index[book_pd['ID No'] == book_id]
    if str(idx)[13] == ']':
        idx_no = str(idx)[12]
        idx_no = int(idx_no)
        print(idx_no)
    elif str(idx)[13] in numbers:
        idx_no = str(idx)[12] + str(idx)[13]
        idx_no = int(idx_no)
        print(idx_no)
    elif str(idx)[13] in numbers and str(idx)[14] in numbers:
        id_no = (str(idx)[12] + str(idx)[13] + str(idx)[14])
        idx_no = int(idx_no)
        print(id_no)
    elif str(idx)[13] in numbers and str(idx)[14] in numbers and str(idx)[15] in numbers:
        idx_no = (str(idx)[12] + str(idx)[13] + str(idx)[14] + str(idx)[15])
        idx_no = int(idx_no)
        print(id_no)
    elif str(idx)[13] in numbers and str(idx)[14] in numbers and str(idx)[15] in numbers and str(idx)[16] in numbers:
        idx_no = (str(idx)[12] + str(idx)[13] + str(idx)[14] + str(idx)[15] + str(idx)[16])
        idx_no = int(idx_no)
        
    book_pd.iloc[idx_no, 6] = book_pd.iloc[idx_no, 6] + 1
    book_pd.to_csv('BookRecords.csv', index=0)
    
    #returned = database.item(idx_no)['values'][6] + 1
    #database.insert("", idx_no, values=(database.item(idx)['values'][0], 
     #                                       database.item(idx)['values'][1] ,
      #                                      database.item(idx)['values'][2], 
       #                                     database.item(idx)['values'][3],
        #                                    database.item(idx)['values'][4],
         #                                   database.item(idx)['values'][5],
          #                                  returned, 
           #                                 database.item(idx)['values'][7], 
            #                                database.item(idx)['values'][8]))
    


root = Tk()

root.geometry('1000x550')
root.title('Retail Management System')
# root.minsize(460, 540)
# root.maxsize(460, 540)

frame1 = Frame(root, borderwidth='10', relief=RIDGE, bg='deepskyblue4')
title = Label(frame1, text='Library Management System', fg='white', bg='deepskyblue4', pady='20',
              font=('Copperplate Gothic Bold', 20, 'bold'))

title.pack()
frame1.pack(fill=X)

framex_borrow = Frame(root)

menubar_borrow = Menu(root)
sections_borrow = Menu(menubar_borrow)
sections_borrow.add_command(label='Member Section', command=lambda:raise_frame(framex_member))
sections_borrow.add_command(label='Books Section', command=lambda:raise_frame(framex_books))
menubar_borrow.add_cascade(label="Sections", menu=sections_borrow)
root.config(menu=menubar_borrow)


frame2_borrow = Frame(framex_borrow, borderwidth='10', relief=RIDGE, bg='deepskyblue4')
form_text = Label(frame2_borrow, text='Fill up the following form for recruiting Member ', fg='white', bg='deepskyblue4',
                  pady='20', padx='5', font=('Calibri', 15, 'bold'))
form_text.grid()

id = Label(frame2_borrow, text='ID No : ', fg='white', bg='deepskyblue4', font=(10))
id.grid(row=1, column=0, stick=W, padx=20)

name = Label(frame2_borrow, text='Name : ', fg='white', bg='deepskyblue4', font=(10))
name.grid(row=2, column=0, stick=W, padx=20)

fname = Label(frame2_borrow, text='Fathers Name : ', fg='white', bg='deepskyblue4', font=(10))
fname.grid(row=3, column=0, stick=W, padx=20)

mname = Label(frame2_borrow, text='Mothers Name : ', fg='white', bg='deepskyblue4', font=(10))
mname.grid(row=4, column=0, stick=W, padx=20)

contact = Label(frame2_borrow, text='Contact : ', fg='white', bg='deepskyblue4', font=(10))
contact.grid(row=5, column=0, stick=W, padx=20)

email = Label(frame2_borrow, text='Email Address : ', fg='white', bg='deepskyblue4', font=(10))
email.grid(row=6, column=0, stick=W, padx=20)

profession = Label(frame2_borrow, text='profession : ', fg='white', bg='deepskyblue4', font=(10))
profession.grid(row=7, column=0, stick=W, padx=20)

desig = Label(frame2_borrow, text='Designation : ', fg='white', bg='deepskyblue4', font=(10))
desig.grid(row=8, column=0, stick=W, padx=20)

pay = Label(frame2_borrow, text='Pay : ', fg='white', bg='deepskyblue4', font=(10))
pay.grid(row=9, column=0, stick=W, padx=20)

no_of_borrows_registry = Label(frame2_borrow, text='No of Borrows : ', fg='white', bg='deepskyblue4', font=(10))
no_of_borrows_registry.grid(row=10, column=0, stick=W, padx=20)


del_data = Button(frame2_borrow, text='Delete', command=delete)
del_data.place(x=115, y=400)


update = Button(frame2_borrow, text='Update')
update.place(x=175, y=400)

autofill_button = Button(frame2_borrow, text='Autofill Data', command=autofill)
autofill_button.place(x=240, y=400)



idval, nameval, fnameval, mnameval, contactval, emailval, professionval, desigval, payval = IntVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
searchval = StringVar()
no_of_borrows_registryval = StringVar()

id_entry = Entry(frame2_borrow, textvariable=idval)
id_entry.place(x=150, y=69)

name_entry = Entry(frame2_borrow, textvariable=nameval)
name_entry.place(x=150, y=93)

fname_entry = Entry(frame2_borrow, textvariable=fnameval)
fname_entry.place(x=150, y=117)

mname_entry = Entry(frame2_borrow, textvariable=mnameval)
mname_entry.place(x=150, y=142)

contact_entry = Entry(frame2_borrow, textvariable=contactval)
contact_entry.place(x=150, y=167)

email_entry = Entry(frame2_borrow, textvariable=emailval)
email_entry.place(x=150, y=191)

profession_entry = Entry(frame2_borrow, textvariable=professionval)
profession_entry.place(x=150, y=215)

desig_entry = Entry(frame2_borrow, textvariable=desigval)
desig_entry.place(x=150, y=239)

payentry = Entry(frame2_borrow, textvariable=payval)
payentry.place(x=150, y=263)

no_of_borrows_registry_entry = Entry(frame2_borrow, textvariable=no_of_borrows_registryval)
no_of_borrows_registry_entry.place(x=150, y=288)




frame3_borrow = Frame(framex_borrow, bg='deepskyblue4', borderwidth='10', relief=RIDGE)
text3 = Label(frame3_borrow, text='Search ID : ', bg='deepskyblue4', fg='white', padx=40, pady=20, font=('Calibri', 12, 'bold'))
text3.grid(row=0, column=0, sticky='w')

search = ttk.Combobox(frame3_borrow, values=
[
    'Name',
    'ID',
    'Contact',
    
], 
textvariable=searchval)
search.grid(row=0, column=1)

search_button = Button(frame3_borrow, text='Search')
search_button.grid(row=0, column=3, padx=10)

borrow_button = Button(frame3_borrow, text='Borrow', command=borrow_book)
borrow_button.grid(row=0, column=4)


frame4_borrow = Frame(frame3_borrow, bg='deepskyblue4', borderwidth='10', relief=RIDGE)



scrollbar = Scrollbar(frame4_borrow)
scrollbar.pack(side=RIGHT, fill=Y)

scrollbarh = Scrollbar(frame4_borrow, orient='horizontal')
scrollbarh.pack(side=BOTTOM, fill=X)

tuples = ['test']

database = ttk.Treeview(frame4_borrow)

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


frame5_borrow = Frame(framex_borrow, borderwidth='10', relief=RIDGE, bg='deepskyblue4')
frame6_borrow = Frame(frame5_borrow, borderwidth='10', relief=RIDGE, bg='deepskyblue4')

scrollbar = Scrollbar(frame6_borrow)
scrollbar.pack(side=RIGHT, fill=Y)

scrollbarh = Scrollbar(frame6_borrow, orient='horizontal')
scrollbarh.pack(side=BOTTOM, fill=X)

tuples = ['test']

borrow_database = ttk.Treeview(frame6_borrow)

borrow_database['columns'] = ['Book ID No', 'Title', 'Writers Name', 'Borrower ID No', 'Borrowers Name', 'Publisher', 'Genre', 'Date of Borrow', 'Date of Return']
borrow_database['show'] = 'headings'
borrow_database.heading('Book ID No', text='Book ID No')
borrow_database.heading('Title', text='Title')
borrow_database.heading('Writers Name', text='Writers Name')
borrow_database.heading('Borrower ID No', text='Borrower ID No')
borrow_database.heading('Borrowers Name', text='Borrowers Name')
borrow_database.heading('Publisher', text='Publisher')
borrow_database.heading('Genre', text='Genre')
borrow_database.heading('Date of Borrow', text='Date of Borrow')
borrow_database.heading('Date of Return', text='Date of Return')


borrow_database.column('Book ID No', width=100)
borrow_database.column('Title',  width=100)
borrow_database.column('Writers Name', width=100)
borrow_database.column('Borrower ID No', width=100)
borrow_database.column('Borrowers Name', width=100)
borrow_database.column('Publisher', width=100)
borrow_database.column('Genre', width=100)
borrow_database.column('Date of Borrow', width=100)
borrow_database.column('Date of Return', width=100)



borrow_database.pack(fill=BOTH, expand=1)



scrollbar.config(command=borrow_database.yview)
scrollbarh.config(command=borrow_database.xview)



try:
    with open('BorrowRecords.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            bookid = row['Book ID No']
            titlevalcsv = row['Title']
            wnamevalcsv = row['Writers Name']
            borrowidval = row['Borrower ID No']
            borrownameval = row['Borrowers Name']
            pubvalcsv = row['Publisher']
            genrevalcsv= row['Genre']
            dateborrowvalcsv = row['Date of Borrow']
            datereturnvalcsv = row['Date of Return']


            borrow_database.insert("", END, values=(bookid, titlevalcsv, wnamevalcsv, borrowidval, borrownameval, pubvalcsv, genrevalcsv,
             dateborrowvalcsv, datereturnvalcsv))

except FileNotFoundError:
    with open('BorrowRecords.csv', 'a+') as records:
        writer = csv.writer(records)
        writer.writerow(
            ['Book ID No', 'Title', 'Writers Name', 'Borrower ID No', 'Borrowers Name', 'Publisher', 'Genre', 'Date of Borrow', 'Date of Return'])
    records.close()


search_borrow_label = Label(frame5_borrow,text='Search ID : ', bg='deepskyblue4', fg='white', padx=20, pady=20, font=('Calibri', 12, 'bold'))
search_borrow_label.grid(row=0, column=0, sticky='w')

search_borrowed_books = ttk.Combobox(frame5_borrow, values=
[
    'Name',
    'ID',
    'Contact',
    
], 
textvariable=searchval)
search_borrowed_books.grid(row=0, column=1)

search_button_borrow = Button(frame5_borrow, text='Search')
search_button_borrow.grid(row=0, column=2, padx=10)

returned_button_borrow = Button(frame5_borrow, text='Returned', command=returned)
returned_button_borrow.grid(row=0, column=3)




frame2_borrow.pack(side=LEFT, fill=BOTH)
frame4_borrow.place(x=50, y=60, width=700, height=170)
frame3_borrow.pack(fill=BOTH, expand=1)
frame6_borrow.place(x=50, y=60, width=700, height=170)
frame5_borrow.pack(fill=BOTH, expand=1)

framex_borrow.pack(fill=BOTH, expand=1)

root.mainloop()
