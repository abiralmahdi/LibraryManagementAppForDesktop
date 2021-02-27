from tkinter import *
from tkinter import ttk
import pandas as pd
import csv, sys, os, shutil
import tkinter.messagebox

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




def submit_value():

    if idval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')


    elif idval.get() == '':
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
                    [idval.get(), nameval.get(), fnameval.get(), mnameval.get(), contactval.get(), emailval.get(),
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

            database.insert("", END, values=(id, namevalcsv, fnamevalcsv, mnamealcsv, contactvalcsv,
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

submit = Button(frame2_member, text='Submit', command=submit_value)
submit.place(x=175, y=360)

del_data = Button(frame2_member, text='Delete', command=delete)
del_data.place(x=115, y=400)


update = Button(frame2_member, text='Update')
update.place(x=175, y=400)



idval, nameval, fnameval, mnameval, contactval, emailval, professionval, desigval, payval = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
searchval = StringVar()
password_registryval = StringVar()

id_entry = Entry(frame2_member, textvariable=idval)
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
text3 = Label(frame3_member, text='Search ID : ', bg='deepskyblue4', fg='white', padx=40, pady=20, font=('Calibri', 12, 'bold'))
text3.grid(row=0, column=0, sticky='w')

search = ttk.Combobox(frame3_member, values=
[
    'Name',
    'ID',
    'Contact',
    
], 
textvariable=searchval)
search.grid(row=0, column=1)

search_button = Button(frame3_member, text='Search')
search_button.grid(row=0, column=3, padx=10)

load_button = Button(frame3_member, text='Load record', command=load)
load_button.grid(row=0, column=4)


frame4_member = Frame(frame3_member, bg='deepskyblue4', borderwidth='10', relief=RIDGE)



scrollbar = Scrollbar(frame4_member)
scrollbar.pack(side=RIGHT, fill=Y)

scrollbarh = Scrollbar(frame4_member, orient='horizontal')
scrollbarh.pack(side=BOTTOM, fill=X)

tuples = ['test']

database = ttk.Treeview(frame4_member)

database['columns'] = ['ID No', 'Name', 'Fathers Name', 'Mothers Name', 'Contact', 'Email', 'profession', 'Designation', 'Pay', 'No of Borrows']
database['show'] = 'headings'
database.heading('ID No', text='ID No')
database.heading('Name', text='Name')
database.heading('Fathers Name', text='Fathers Name')
database.heading('Mothers Name', text='Mothers Name')
database.heading('Contact', text='Contact')
database.heading('Email', text='Email')
database.heading('profession', text='profession')
database.heading('Designation', text='Designation')
database.heading('Pay', text='Pay')
database.heading('No of Borrows', text='No of Borrows')

database.column('ID No', width=100)
database.column('Name',  width=100)
database.column('Fathers Name', width=100)
database.column('Mothers Name', width=100)
database.column('Contact', width=100)
database.column('Email', width=100)
database.column('profession', width=100)
database.column('Designation', width=100)
database.column('Pay', width=100)
database.column('No of Borrows', width=100)

database.pack(fill=BOTH, expand=1)



scrollbar.config(command=database.yview)
scrollbarh.config(command=database.xview)



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

            database.insert("", END, values=(id, namevalcsv, fnamevalcsv, mnamealcsv, contactvalcsv,
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

framex_member.pack(fill=BOTH, expand=1)

root.mainloop()
