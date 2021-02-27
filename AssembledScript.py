from tkinter import *
from tkinter import ttk
import pandas as pd
import csv, sys, os, shutil, datetime
import tkinter.messagebox

global id


'''THIS ARE THE FRAME SWAPPING FUNCTIONS'''


def raise_frame_books():
    framex_member.pack_forget()
    framex_borrow.pack_forget()
    framex_books.pack(fill=BOTH, expand=1)
    
def raise_frame_members():
    framex_books.pack_forget()
    framex_borrow.pack_forget()
    framex_member.pack(fill=BOTH, expand=1)

    
def raise_frame_borrow():
    framex_books.pack_forget()
    framex_member.pack_forget()
    framex_borrow.pack(fill=BOTH, expand=1)


def update_book():
    book_pd = pd.read_csv('BookRecords.csv')
    selected_item = database_book.focus()
    book_index = database_book.index(selected_item)
    
    database_book.insert("", book_index, values=(idval_books.get(), titleval.get(), wnameval.get(), pubval.get(), genreval.get(),
                                             dateval.get(), copiesval.get(), costval.get(), pubwebval.get()))
    
    database_book_for_borrow.insert("", book_index, values=(idval_books.get(), titleval.get(), wnameval.get(), pubval.get(), genreval.get(),
                                             dateval.get(), copiesval.get(), costval.get(), pubwebval.get()))

    
    
    book_pd.iloc[book_index, 0] = idval_books.get()
    book_pd.iloc[book_index, 1] = titleval.get()
    book_pd.iloc[book_index, 2] = wnameval.get()
    book_pd.iloc[book_index, 3] = pubval.get()
    book_pd.iloc[book_index, 4] = genreval.get()
    book_pd.iloc[book_index, 5] = dateval.get()
    book_pd.iloc[book_index, 6] = copiesval.get()
    book_pd.iloc[book_index, 7] = costval.get()
    book_pd.iloc[book_index, 8] = pubwebval.get()
    
    book_pd.to_csv('BookRecords.csv', index=0)

    database_book.delete(selected_item)
    database_book_for_borrow.delete(selected_item)
    
    tkinter.messagebox.showinfo('Success', 'Update Successful')

    
    

def load_book():
    
    '''THIS FUNCTION LOADS BOOK RECORDS'''
    
    try:
        selected_item = database_book.focus()  ## get selected item
        print(selected_item)
        # print(selected_item[])
        idval_books.set(database_book.item(selected_item)['values'][0])
        titleval.set(database_book.item(selected_item)['values'][1])
        wnameval.set(database_book.item(selected_item)['values'][2])
        pubval.set(database_book.item(selected_item)['values'][3])
        genreval.set(database_book.item(selected_item)['values'][4])
        dateval.set(database_book.item(selected_item)['values'][5])
        copiesval.set(database_book.item(selected_item)['values'][6])
        costval.set(database_book.item(selected_item)['values'][7])
        pubwebval.set(database_book.item(selected_item)['values'][8])


    except IndexError:
        tkinter.messagebox.showinfo('Error', 'Please select one record')


def submit_value_book():

    '''THIS FUNCTION ADDS THE NEW BOOK'''


    if idval_books.get() == '':
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
                    [idval_books.get(), titleval.get(), wnameval.get(), pubval.get(), genreval.get(), dateval.get(),
                     copiesval.get(), costval.get(), pubwebval.get()])
                records.close()

            with open('BookRecords.csv') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    idval_bookscsv = row['ID No']
                    titlevalcsv = row['Title']
                    wnamevalcsv = row['Writers Name']
                    pubvalcsv = row['Publisher']
                    genrevalcsv = row['Genre']
                    datevalcsv = row['Date of issue']
                    copiesvalcsv = row['No of Copies']
                    costvalcsv = row['Cost']
                    pubwebvalcsv = row['Publishers Website']

            database_book.insert("", END, values=(idval_bookscsv, titlevalcsv, wnamevalcsv, pubvalcsv, genrevalcsv,
                                             datevalcsv, copiesvalcsv, costvalcsv, pubwebvalcsv))

            database_book_for_borrow.insert("", END, values=(id, titlevalcsv, wnamevalcsv, pubvalcsv, genrevalcsv,
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


def delete_book():
    
    '''THIS FUNCTION DELETES ANY BOOK FROM THE RECORDS'''
    
    msg = tkinter.messagebox.askquestion('Sure?', 'Are you sure you want to remove the Book and all his/her details?')
    if msg == 'yes':
        remove_book()
    else:
        pass



def remove_book():
    
    '''THIS FUNCTION DELETES ANY BOOK FROM THE RECORDS'''

    
    try:
            #selected_item = database_book.selection()[0] ## get selected item
            # print(database_book.item(selected_item))
            # print(remove)
        selected_item = database_book.focus() ## get selected item

        database_pd = pd.read_csv('BookRecords.csv')
        remove = database_book.item(selected_item)['values'][0]
        specify = database_pd.loc[database_pd['ID No'] == remove]
        id = specify.iloc[0, 0]
        name_remove = specify.iloc[0, 1]
        database_pd = database_pd.loc[database_pd['ID No'] != remove]
        database_pd.to_csv('BookRecords.csv', index=0)

        database_book.delete(selected_item)
        
        
        with open('BookRecords.csv', 'a+') as records:
            writer = csv.writer(records)

    except IndexError:
        tkinter.messagebox.showinfo('Error', 'Please choose a record')



def load_member():
    
    '''THIS FUNCTION LOADS ANY MEMBER RECORDS IN THE ENTRY FIELDS'''
    
    try:
        selected_item = database_member.focus()  ## get selected item
        print(selected_item)
        # print(selected_item[])
        idval_member.set(database_member.item(selected_item)['values'][0])
        nameval.set(database_member.item(selected_item)['values'][1])
        fnameval.set(database_member.item(selected_item)['values'][2])
        mnameval.set(database_member.item(selected_item)['values'][3])
        contactval.set(database_member.item(selected_item)['values'][4])
        emailval.set(database_member.item(selected_item)['values'][5])
        professionval.set(database_member.item(selected_item)['values'][6])
        desigval.set(database_member.item(selected_item)['values'][7])
        payval.set(database_member.item(selected_item)['values'][8])


    except IndexError:
        tkinter.messagebox.showinfo('Error', 'Please select one record')



def autofill():
    
    '''THIS FUNCTION AUTOFILLS THE MEMBER RECORDS UPON ENTRANCE OF THE ID NO'''
    
    member_pd = pd.read_csv('MemberRecords.csv')
    member_specify = member_pd.loc[member_pd['Name'] == nameval.get()]
    nameval.set(member_specify.iloc[0, 1])
    fnameval.set(member_specify.iloc[0, 2])
    mnameval.set(member_specify.iloc[0, 3])
    contactval.set(member_specify.iloc[0, 4])
    emailval.set(member_specify.iloc[0, 5])
    professionval.set(member_specify.iloc[0, 6])
    desigval.set(member_specify.iloc[0, 7])
    payval.set(member_specify.iloc[0, 8])




def borrow_book():
    
    '''THIS FUNCTION BORROWS ANY BOOK WITH THE MEMBERS NAME'''
    
    global member_specify
    
    book_pd = pd.read_csv('BookRecords.csv')
    borrow_pd = pd.read_csv('BorrowRecords.csv')
    member_pd = pd.read_csv('MemberRecords.csv')
    
    
    selected_item = database_book_for_borrow.focus()
    book_index = database_book_for_borrow.index(selected_item)
    
    print(database_book_for_borrow.item(selected_item)['values'][6])
    
    deducted = database_book_for_borrow.item(selected_item)['values'][6] - 1
    database_book_for_borrow.insert("", book_index, values=(database_book_for_borrow.item(selected_item)['values'][0], 
                                            database_book_for_borrow.item(selected_item)['values'][1] ,
                                            database_book_for_borrow.item(selected_item)['values'][2], 
                                            database_book_for_borrow.item(selected_item)['values'][3],
                                            database_book_for_borrow.item(selected_item)['values'][4],
                                            database_book_for_borrow.item(selected_item)['values'][5],
                                            deducted, 
                                            database_book_for_borrow.item(selected_item)['values'][7], 
                                            database_book_for_borrow.item(selected_item)['values'][8]))
    

    member_specify = member_pd.loc[member_pd['Name'] == nameval.get()]
    #member_specify = member_pd.loc[member_pd['ID No'] == idval_member.get()]

    book_pd.iloc[book_index, 6] = book_pd.iloc[book_index, 6] - 1
    
    
    borrow_book_id = book_pd.iloc[book_index, 0]
    borrow_book_title = book_pd.iloc[book_index, 1]
    borrow_book_writer = book_pd.iloc[book_index, 2]
    member_id = member_specify.iloc[0, 0]
    member_name = member_specify.iloc[0, 1]
    borrow_publisher = book_pd.iloc[book_index, 3]
    borrow_genre  = book_pd.iloc[book_index, 4]
    
    database_book_for_borrow.delete(selected_item)

    
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


        database_borrow.insert("", END, values=(borrow_book_id,
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
    
    '''THIS FUNCTION RETURNS ANY BORROWED BOOK'''
    
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    
    book_pd = pd.read_csv('BookRecords.csv')
    borrow_pd = pd.read_csv('BorrowRecords.csv')
    
    selected_item = database_borrow.focus()
    book_id = database_borrow.item(selected_item)['values'][0]
    index_no = database_borrow.index(selected_item)
    borrow_pd = borrow_pd.drop(index_no)     
    
    borrow_pd.to_csv('BorrowRecords.csv', index=0)
    database_borrow.delete(selected_item)

    
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
    
    
    '''THIS PART IS CURRENTLY UNDER DEDVELOPMENT'''
    
    #returned = database_book_for_borrow.item(idx_no)['values'][6] + 1
    #database_book_for_borrow.insert("", idx_no, values=(database_book_for_borrow.item(idx)['values'][0], 
     #                                       database_book_for_borrow.item(idx)['values'][1] ,
      #                                      database_book_for_borrow.item(idx)['values'][2], 
       #                                     database_book_for_borrow.item(idx)['values'][3],
        #                                    database_book_for_borrow.item(idx)['values'][4],
         #                                   database_book_for_borrow.item(idx)['values'][5],
          #                                  returned, 
           #                                 database_book_for_borrow.item(idx)['values'][7], 
            #                                database_book_for_borrow.item(idx)['values'][8]))
    


def search_member():
    #global searchval_member
    #print(searchval_member.get())
    
    member_pd = pd.read_csv('MemberRecords.csv')
    
    for i in database_member.get_children():
        database_member.delete(i)
    
    if searchbyval.get() == 'Name':
        #searchval_member = StringVar()
        #searched_data = member_pd.loc[member_pd['Name'] == searchval_member.get()]
        #database_member.insert("", END, values=(searched_data.iloc[0,0], searched_data.iloc[0,1], searched_data.iloc[0,2], 
        #                                       searched_data.iloc[0,5], searched_data.iloc[0,4], searched_data.iloc[0,5],
        #                                       searched_data.iloc[0,6], searched_data.iloc[0,7], searched_data.iloc[0,8]))
        tkinter.messagebox.showerror('Development Error', 'Searching by Name is currently under development.\n Sorry for the inconvenience')
    elif searchbyval.get() == 'ID':
        #searchval_member = IntVar()
        searched_data = member_pd.loc[member_pd['ID No'] == searchval_member.get()]
        database_member.insert("", END, values=(searched_data.iloc[0,0], searched_data.iloc[0,1], searched_data.iloc[0,2], 
                                               searched_data.iloc[0,3], searched_data.iloc[0,4], searched_data.iloc[0,5],
                                               searched_data.iloc[0,6], searched_data.iloc[0,7], searched_data.iloc[0,8]))
    else:
        tkinter.messagebox.showerror('Error', 'Invalid category.')


def search_members():
    #database_member.selection_set(database_member.tag_has(searchval_member.get()))
    pass



def reset_view_member():
    for i in database_member.get_children():
        database_member.delete(i)

    with open('MemberRecords.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            id = row['ID No']
            namevalcsv = row['Name']
            fnamevalcsv = row['Fathers Name']
            mnamealcsv = row['Mothers Name']
            contactvalcsv= row['Contact']
            emailvalcsv = row['Email']
            professionvalcsv = row['profession']
            desigvalcsv = row['Designation']
            payvalcsv = row['Pay']

            database_member.insert("", END, values=(id, namevalcsv, fnamevalcsv, mnamealcsv, contactvalcsv,
             emailvalcsv, professionvalcsv, desigvalcsv, payvalcsv))



def update_member():
    member_pd = pd.read_csv('MemberRecords.csv')
    selected_item = database_member.focus()
    member_index = database_member.index(selected_item)
    
    database_member.insert("", member_index, values=(idval_member.get(), nameval.get(), fnameval.get(), mnameval.get(), contactval.get(),
                                                      emailval.get(),
                     professionval.get(), desigval.get(), payval.get()))
    
    
    
    member_pd.iloc[member_index, 0] = idval_member.get()
    member_pd.iloc[member_index, 1] = nameval.get()
    member_pd.iloc[member_index, 2] = fnameval.get()
    member_pd.iloc[member_index, 3] = mnameval.get()
    member_pd.iloc[member_index, 4] = contactval.get()
    member_pd.iloc[member_index, 5] = emailval.get()
    member_pd.iloc[member_index, 6] = professionval.get()
    member_pd.iloc[member_index, 7] = desigval.get()
    member_pd.iloc[member_index, 8] = payval.get()
    
    member_pd.to_csv('MemberRecords.csv', index=0)

    database_member.delete(selected_item)

    tkinter.messagebox.showinfo('Success', 'Update Successful')




def submit_value_member():
    
    '''THIS FUNCTION ADDS NEW MEMBERS'''
    

    if idval_member.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')
    elif nameval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')
    elif fnameval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')

    elif mnameval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')
    elif contactval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')
    elif emailval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')

    elif professionval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')

    elif desigval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')

    elif payval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')



    else:
        try:
            with open('MemberRecords.csv', 'a+') as records:
                writer = csv.writer(records)
                writer.writerow(
                    [idval_member.get(), nameval.get(), fnameval.get(), mnameval.get(), contactval.get(), emailval.get(),
                     professionval.get(), desigval.get(), payval.get()])
                records.close()

            with open('MemberRecords.csv') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    id = row['ID No']
                    namevalcsv = row['Name']
                    fnamevalcsv = row['Fathers Name']
                    mnamealcsv = row['Mothers Name']
                    contactvalcsv = row['Contact']
                    emailvalcsv = row['Email']
                    professionvalcsv = row['profession']
                    desigvalcsv = row['Designation']
                    payvalcsv = row['Pay']

            database_member.insert("", END, values=(id, namevalcsv, fnamevalcsv, mnamealcsv, contactvalcsv,
                                             emailvalcsv, professionvalcsv, desigvalcsv, payvalcsv), tags='Name')


            id_entry.delete(0, END)
            name_entry.delete(0, END)
            fname_entry.delete(0, END)
            mname_entry.delete(0, END)
            contact_entry.delete(0, END)
            email_entry.delete(0, END)
            profession_entry.delete(0, END)
            desig_entry.delete(0, END)
            payentry.delete(0, END)
            password_registry_entry.delete(0, END)

        except PermissionError:
            tkinter.messagebox.showinfo('Permission Error', 'Please close the database (csv) file ')


def delete_member():
        msg = tkinter.messagebox.askquestion('Sure?', 'Are you sure you want to remove the Member and all his/her details?')
        if msg == 'yes':
            remove_member()

        else:
            pass



def remove_member():
    
    '''THIS FUNCTION REMOVES ANY MEMBER'''
    
    try:
            #selected_item = database_member.selection()[0] ## get selected item
            # print(database_member.item(selected_item))
            # print(remove)
        selected_item = database_member.focus() ## get selected item

        database_pd = pd.read_csv('MemberRecords.csv')
        remove = database_member.item(selected_item)['values'][0]
        specify = database_pd.loc[database_pd['ID No'] == remove]
        id = specify.iloc[0, 0]
        name_remove = specify.iloc[0, 1]
        database_pd = database_pd.loc[database_pd['ID No'] != remove]
        database_pd.to_csv('MemberRecords.csv', index=0)

        database_member.delete(selected_item)
        with open('MemberRecords.csv', 'a+') as records:
            writer = csv.writer(records)

    except IndexError:
        tkinter.messagebox.showinfo('Error', 'Please choose a record')





'''THIS IS THE GUI PART OF THE SOFTWARE'''



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




"""THIS IS THE BORROW SECTION OF THE SOFTWARE"""



framex_borrow = Frame(root)


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


del_data = Button(frame2_borrow, text='Delete')
del_data.place(x=115, y=400)


update = Button(frame2_borrow, text='Update')
update.place(x=175, y=400)

autofill_button = Button(frame2_borrow, text='Autofill Data', command=autofill)
autofill_button.place(x=240, y=400)



idval_member_borrow, nameval, fnameval, mnameval, contactval, emailval, professionval, desigval, payval = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
searchval = StringVar()
no_of_borrows_registryval = StringVar()

id_entry = Entry(frame2_borrow, textvariable=idval_member_borrow)
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
text3 = Label(frame3_borrow, text='Search By : ', bg='deepskyblue4', fg='white', padx=40, pady=20, font=('Calibri', 12, 'bold'))
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

database_book_for_borrow = ttk.Treeview(frame4_borrow)

database_book_for_borrow['columns'] = ['ID No', 'Title', 'Writers Name', 'Publisher', 'Genre', 'Date of issue', 'No of Copies', 'Cost', 'Publishers Website']
database_book_for_borrow['show'] = 'headings'
database_book_for_borrow.heading('ID No', text='ID No')
database_book_for_borrow.heading('Title', text='Title')
database_book_for_borrow.heading('Writers Name', text='Writers Name')
database_book_for_borrow.heading('Publisher', text='Publisher')
database_book_for_borrow.heading('Genre', text='Genre')
database_book_for_borrow.heading('Date of issue', text='Date of issue')
database_book_for_borrow.heading('No of Copies', text='No of Copies')
database_book_for_borrow.heading('Cost', text='Cost')
database_book_for_borrow.heading('Publishers Website', text='Publishers Website')

database_book_for_borrow.column('ID No', width=100)
database_book_for_borrow.column('Title',  width=100)
database_book_for_borrow.column('Writers Name', width=100)
database_book_for_borrow.column('Publisher', width=100)
database_book_for_borrow.column('Genre', width=100)
database_book_for_borrow.column('Date of issue', width=100)
database_book_for_borrow.column('No of Copies', width=100)
database_book_for_borrow.column('Cost', width=100)
database_book_for_borrow.column('Publishers Website', width=100)

database_book_for_borrow.pack(fill=BOTH, expand=1)



scrollbar.config(command=database_book_for_borrow.yview)
scrollbarh.config(command=database_book_for_borrow.xview)



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

            database_book_for_borrow.insert("", END, values=(id, titlevalcsv, wnamevalcsv, pubvalcsv, genrevalcsv,
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

database_borrow = ttk.Treeview(frame6_borrow)

database_borrow['columns'] = ['Book ID No', 'Title', 'Writers Name', 'Borrower ID No', 'Borrowers Name', 'Publisher', 'Genre', 'Date of Borrow', 'Date of Return']
database_borrow['show'] = 'headings'
database_borrow.heading('Book ID No', text='Book ID No')
database_borrow.heading('Title', text='Title')
database_borrow.heading('Writers Name', text='Writers Name')
database_borrow.heading('Borrower ID No', text='Borrower ID No')
database_borrow.heading('Borrowers Name', text='Borrowers Name')
database_borrow.heading('Publisher', text='Publisher')
database_borrow.heading('Genre', text='Genre')
database_borrow.heading('Date of Borrow', text='Date of Borrow')
database_borrow.heading('Date of Return', text='Date of Return')


database_borrow.column('Book ID No', width=100)
database_borrow.column('Title',  width=100)
database_borrow.column('Writers Name', width=100)
database_borrow.column('Borrower ID No', width=100)
database_borrow.column('Borrowers Name', width=100)
database_borrow.column('Publisher', width=100)
database_borrow.column('Genre', width=100)
database_borrow.column('Date of Borrow', width=100)
database_borrow.column('Date of Return', width=100)



database_borrow.pack(fill=BOTH, expand=1)



scrollbar.config(command=database_borrow.yview)
scrollbarh.config(command=database_borrow.xview)



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


            database_borrow.insert("", END, values=(bookid, titlevalcsv, wnamevalcsv, borrowidval, borrownameval, pubvalcsv, genrevalcsv,
             dateborrowvalcsv, datereturnvalcsv))

except FileNotFoundError:
    with open('BorrowRecords.csv', 'a+') as records:
        writer = csv.writer(records)
        writer.writerow(
            ['Book ID No', 'Title', 'Writers Name', 'Borrower ID No', 'Borrowers Name', 'Publisher', 'Genre', 'Date of Borrow', 'Date of Return'])
    records.close()


search_borrow_label = Label(frame5_borrow,text='Search By : ', bg='deepskyblue4', fg='white', padx=20, pady=20, font=('Calibri', 12, 'bold'))
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





"""THIS IS THE BOOK SECTION OF THE SOFTWARE"""




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

submit = Button(frame2_books, text='Submit', command=submit_value_book)
submit.place(x=175, y=360)

del_data = Button(frame2_books, text='Delete', command=delete_book)
del_data.place(x=115, y=400)


update = Button(frame2_books, text='Update', command=update_book)
update.place(x=175, y=400)



idval_books, titleval, wnameval, pubval, genreval, dateval, copiesval, costval, pubwebval = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
searchval = StringVar()


id_entry = Entry(frame2_books, textvariable=idval_books)
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
text3 = Label(frame3_books, text='Search By : ', bg='deepskyblue4', fg='white', padx=40, pady=20, font=('Calibri', 12, 'bold'))
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

load_button = Button(frame3_books, text='Load record', command=load_book)
load_button.grid(row=0, column=4)


frame4_books = Frame(frame3_books, bg='deepskyblue4', borderwidth='10', relief=RIDGE)



scrollbar = Scrollbar(frame4_books)
scrollbar.pack(side=RIGHT, fill=Y)

scrollbarh = Scrollbar(frame4_books, orient='horizontal')
scrollbarh.pack(side=BOTTOM, fill=X)

tuples = ['test']

database_book = ttk.Treeview(frame4_books)

database_book['columns'] = ['ID No', 'Title', 'Writers Name', 'Publisher', 'Genre', 'Date of issue', 'No of Copies', 'Cost', 'Publishers Website']
database_book['show'] = 'headings'
database_book.heading('ID No', text='ID No')
database_book.heading('Title', text='Title')
database_book.heading('Writers Name', text='Writers Name')
database_book.heading('Publisher', text='Publisher')
database_book.heading('Genre', text='Genre')
database_book.heading('Date of issue', text='Date of issue')
database_book.heading('No of Copies', text='No of Copies')
database_book.heading('Cost', text='Cost')
database_book.heading('Publishers Website', text='Publishers Website')

database_book.column('ID No', width=100)
database_book.column('Title',  width=100)
database_book.column('Writers Name', width=100)
database_book.column('Publisher', width=100)
database_book.column('Genre', width=100)
database_book.column('Date of issue', width=100)
database_book.column('No of Copies', width=100)
database_book.column('Cost', width=100)
database_book.column('Publishers Website', width=100)

database_book.pack(fill=BOTH, expand=1)



scrollbar.config(command=database_book.yview)
scrollbarh.config(command=database_book.xview)



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

            database_book.insert("", END, values=(id, titlevalcsv, wnamevalcsv, pubvalcsv, genrevalcsv,
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

#framex_books.pack(fill=BOTH, expand=1)







"""THIS IS THE MEMBER SECTION OF THE SOFTWARE"""






framex_member = Frame(root, borderwidth='1',bg='deepskyblue4')
frame2_member = Frame(framex_member, borderwidth='10', relief=RIDGE, bg='deepskyblue4')
form_text = Label(frame2_member, text='Fill up the following form for recruiting Member ', fg='white', bg='deepskyblue4',
                  pady='20', padx='5', font=('Calibri', 15, 'bold'))
form_text.grid()

id = Label(frame2_member, text='ID No : ', fg='white', bg='deepskyblue4', font=(10))
id.grid(row=1, column=0, stick=W, padx=20)

name = Label(frame2_member, text='Name : ', fg='white', bg='deepskyblue4', font=(10))
name.grid(row=2, column=0, stick=W, padx=20)

fname = Label(frame2_member, text='Fathers Name : ', fg='white', bg='deepskyblue4', font=(10))
fname.grid(row=3, column=0, stick=W, padx=20)

mname = Label(frame2_member, text='Mothers Name : ', fg='white', bg='deepskyblue4', font=(10))
mname.grid(row=4, column=0, stick=W, padx=20)

contact = Label(frame2_member, text='Contact : ', fg='white', bg='deepskyblue4', font=(10))
contact.grid(row=5, column=0, stick=W, padx=20)

email = Label(frame2_member, text='Email Address : ', fg='white', bg='deepskyblue4', font=(10))
email.grid(row=6, column=0, stick=W, padx=20)

profession = Label(frame2_member, text='profession : ', fg='white', bg='deepskyblue4', font=(10))
profession.grid(row=7, column=0, stick=W, padx=20)

desig = Label(frame2_member, text='Designation : ', fg='white', bg='deepskyblue4', font=(10))
desig.grid(row=8, column=0, stick=W, padx=20)

pay = Label(frame2_member, text='Pay : ', fg='white', bg='deepskyblue4', font=(10))
pay.grid(row=9, column=0, stick=W, padx=20)

password_registry = Label(frame2_member, text='Password : ', fg='white', bg='deepskyblue4', font=(10))
password_registry.grid(row=10, column=0, stick=W, padx=20)

submit = Button(frame2_member, text='Submit', command=submit_value_member)
submit.place(x=175, y=360)

del_data = Button(frame2_member, text='Delete', command=delete_member)
del_data.place(x=115, y=400)


update = Button(frame2_member, text='Update', command=update_member)
update.place(x=175, y=400)



idval_member, nameval, fnameval, mnameval, contactval, emailval, professionval, desigval, payval = IntVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
searchbyval = StringVar()
password_registryval = StringVar()

#if searchbyval.get() == 'Name':
searchval_member = IntVar()

id_entry = Entry(frame2_member, textvariable=idval_member)
id_entry.place(x=150, y=69)

name_entry = Entry(frame2_member, textvariable=nameval)
name_entry.place(x=150, y=93)

fname_entry = Entry(frame2_member, textvariable=fnameval)
fname_entry.place(x=150, y=117)

mname_entry = Entry(frame2_member, textvariable=mnameval)
mname_entry.place(x=150, y=142)

contact_entry = Entry(frame2_member, textvariable=contactval)
contact_entry.place(x=150, y=167)

email_entry = Entry(frame2_member, textvariable=emailval)
email_entry.place(x=150, y=191)

profession_entry = Entry(frame2_member, textvariable=professionval)
profession_entry.place(x=150, y=215)

desig_entry = Entry(frame2_member, textvariable=desigval)
desig_entry.place(x=150, y=239)

payentry = Entry(frame2_member, textvariable=payval)
payentry.place(x=150, y=263)

password_registry_entry = Entry(frame2_member, textvariable=password_registryval)
password_registry_entry.place(x=150, y=288)




frame3_member = Frame(framex_member, bg='deepskyblue4', borderwidth='10', relief=RIDGE)
text3 = Label(frame3_member, text='Search By : ', bg='deepskyblue4', fg='white', padx=40, pady=20, font=('Calibri', 12, 'bold'))
text3.grid(row=0, column=0, sticky='w')

search_by = ttk.Combobox(frame3_member, values=
[
    'Name',
    'ID',
    'Contact',
    
], 
textvariable=searchbyval, width=15)
search_by.grid(row=0, column=1)

search = Label(frame3_member, text='Search : ', bg='deepskyblue4', fg='white', padx=40, font=('Calibri', 12, 'bold'))
search.grid(row=1, column=0, padx=0) 

search_entry = Entry(frame3_member, textvariable=searchval_member, width=25)
search_entry.grid(row=1, column=1)


search_button = Button(frame3_member, text='Search', command=search_member)
search_button.grid(row=0, column=2, padx=10)

load_button = Button(frame3_member, text='Load record', command=load_member)
load_button.grid(row=0, column=3)

reset_button_member = Button(frame3_member, text='View full database', command=reset_view_member)
reset_button_member.grid(row=0, column=4, padx=10)



frame4_member = Frame(frame3_member, bg='deepskyblue4', borderwidth='10', relief=RIDGE)



scrollbar = Scrollbar(frame4_member)
scrollbar.pack(side=RIGHT, fill=Y)

scrollbarh = Scrollbar(frame4_member, orient='horizontal')
scrollbarh.pack(side=BOTTOM, fill=X)

tuples = ['test']

database_member = ttk.Treeview(frame4_member)

database_member['columns'] = ['ID No', 'Name', 'Fathers Name', 'Mothers Name', 'Contact', 'Email', 'profession', 'Designation', 'Pay', 'No of Borrows']
database_member['show'] = 'headings'
database_member.heading('ID No', text='ID No')
database_member.heading('Name', text='Name')
database_member.heading('Fathers Name', text='Fathers Name')
database_member.heading('Mothers Name', text='Mothers Name')
database_member.heading('Contact', text='Contact')
database_member.heading('Email', text='Email')
database_member.heading('profession', text='profession')
database_member.heading('Designation', text='Designation')
database_member.heading('Pay', text='Pay')
database_member.heading('No of Borrows', text='No of Borrows')

database_member.column('ID No', width=100)
database_member.column('Name',  width=100)
database_member.column('Fathers Name', width=100)
database_member.column('Mothers Name', width=100)
database_member.column('Contact', width=100)
database_member.column('Email', width=100)
database_member.column('profession', width=100)
database_member.column('Designation', width=100)
database_member.column('Pay', width=100)
database_member.column('No of Borrows', width=100)

database_member.pack(fill=BOTH, expand=1)



scrollbar.config(command=database_member.yview)
scrollbarh.config(command=database_member.xview)



try:
    with open('MemberRecords.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            id = row['ID No']
            namevalcsv = row['Name']
            fnamevalcsv = row['Fathers Name']
            mnamealcsv = row['Mothers Name']
            contactvalcsv= row['Contact']
            emailvalcsv = row['Email']
            professionvalcsv = row['profession']
            desigvalcsv = row['Designation']
            payvalcsv = row['Pay']

            database_member.insert("", END, values=(id, namevalcsv, fnamevalcsv, mnamealcsv, contactvalcsv,
             emailvalcsv, professionvalcsv, desigvalcsv, payvalcsv))

except FileNotFoundError:
    with open('MemberRecords.csv', 'a+') as records:
        writer = csv.writer(records)
        writer.writerow(
            ['ID No', 'Name', 'Fathers Name', 'Mothers Name', 'Contact', 'Email', 'profession', 'Designation', 'Pay', 'No of Borrows'
             ])
    records.close()



frame2_member.pack(side=LEFT, fill=BOTH)
frame4_member.place(x=50, y=100, width=700, height=300)
frame3_member.pack(fill=BOTH, expand=1)



'''THIS IS THE MENUBAR OF THE WHOLE SOFTWARE'''


menubar = Menu(root)

sections = Menu(menubar)
sections.add_command(label='Member Section', command=raise_frame_members) #IT SWAPS THE MEMBER SECTION
sections.add_command(label='Books Section', command=raise_frame_books) #IT SWAPS THE BOOK SECTION
sections.add_command(label='Borrow Section', command=raise_frame_borrow) #IT SWAPS THE BORROW SECTION
menubar.add_cascade(label="Sections", menu=sections) 

help_menu = Menu(menubar)
help_menu.add_command(label='Help')
help_menu.add_command(label='Developer Information')
menubar.add_cascade(label='Support', menu=help_menu)


root.config(menu=menubar)




root.mainloop()


