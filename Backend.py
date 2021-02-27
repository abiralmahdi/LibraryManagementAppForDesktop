from tkinter import *
from tkinter import ttk
import pandas as pd
import csv, sys, os, shutil, datetime
import tkinter.messagebox


'''THIS IS THE FRAME SWAPPING FUNCTION'''



    

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
                    id = row['ID No']
                    titlevalcsv = row['Title']
                    wnamevalcsv = row['Writers Name']
                    pubvalcsv = row['Publisher']
                    genrevalcsv = row['Genre']
                    datevalcsv = row['Date of issue']
                    copiesvalcsv = row['No of Copies']
                    costvalcsv = row['Cost']
                    pubwebvalcsv = row['Publishers Website']

            database_book.insert("", END, values=(id, titlevalcsv, wnamevalcsv, pubvalcsv, genrevalcsv,
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
                                             emailvalcsv, professionvalcsv, desigvalcsv, payvalcsv))


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




