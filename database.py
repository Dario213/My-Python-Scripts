from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title('Database')
root.iconphoto(True, PhotoImage(file = 'images/python.png'))
root.geometry("400x600")

# Databases

# Create database or connect to one

conn = sqlite3.connect('adress_book.db')

# Create cursor

cursor = conn.cursor()
# Create table
'''
cursor.execute("""CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer)
    """)
'''

# Create Update F to Update a Record
def Update():
    conn = sqlite3.connect('adress_book.db')
    cursor = conn.cursor()

    record_id = delete_box.get()

    cursor.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode


        WHERE oid = :oid""",
        {
            'first': f_name_editor.get(),
            'last': l_name_editor.get(),
            'address': address_editor.get(),
            'city': city_editor.get(),
            'state': state_editor.get(),
            'zipcode': zipcode_editor.get(),

            'oid': record_id
        })






    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    editor.destroy()

    



# Create Edit F to Update a Record
def Edit():
    global editor
    editor = Tk()
    editor.title('Update a Record')
    editor.geometry("400x600")

    conn = sqlite3.connect('adress_book.db')
    cursor = conn.cursor()

    record_ID = delete_box.get()

    #Query the database
    cursor.execute("SELECT * FROM addresses WHERE oid = " + record_ID)
    records = cursor.fetchall()

   
    #Create global vars
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    


    # create text boxes
    f_name_editor = Entry(editor, width = 30)
    f_name_editor.grid(row = 0, column = 1, padx = 20, pady = (10, 0))
    l_name_editor = Entry(editor, width = 30)
    l_name_editor.grid(row = 1, column = 1)
    address_editor = Entry(editor, width = 30)
    address_editor.grid(row = 2, column = 1)
    city_editor = Entry(editor, width = 30)
    city_editor.grid(row = 3, column = 1)
    state_editor = Entry(editor, width = 30)
    state_editor.grid(row = 4, column = 1)
    zipcode_editor = Entry(editor, width = 30)
    zipcode_editor.grid(row = 5, column = 1, pady = 5)



    # create text box labels
    f_name_label_editor = Label(editor, text = "First Name: ")
    f_name_label_editor.grid(row = 0, column = 0, pady = (10, 0))
    l_name_label_editor = Label(editor, text = "Last Name: ")
    l_name_label_editor.grid(row = 1, column = 0)
    address_label_editor = Label(editor, text = "Address: ")
    address_label_editor.grid(row = 2, column = 0)
    city_label_editor = Label(editor, text = "City: ")
    city_label_editor.grid(row = 3, column = 0)
    state_label_editor = Label(editor, text = "State: ")
    state_label_editor.grid(row = 4, column = 0)
    zipcode_label_editor = Label(editor, text = "Zipcode: ")
    zipcode_label_editor.grid(row = 5, column = 0)

     #Loop through rsults
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])


    # Create an Save Changes Button
    save_btn = Button(editor, text = "Save a Record ", command = Update)
    save_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 145)




# Create delete record function
def Delete():
    conn = sqlite3.connect('adress_book.db')

    # Create cursor

    cursor = conn.cursor()

    # Delete a record
    cursor.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    delete_box.delete(0, END)


    # Commit changes
    conn.commit()

    # Close connection
    conn.close()




# Create Submit F to Databases
def Submit():
    conn = sqlite3.connect('adress_book.db')
    cursor = conn.cursor()

    # Insert into table
    cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            })





    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


    # Clear the textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)




# Create Query f
def Query():
    conn = sqlite3.connect('adress_book.db')
    cursor = conn.cursor()

    #Query the database
    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()
    
    print_records = ''

    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[6]) + '\n'


    query_lbl = Label(root, text = print_records)
    query_lbl.grid(row = 12, column = 0, columnspan = 2)
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()



# create text boxes
f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20, pady = (10, 0))
l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1)
address = Entry(root, width = 30)
address.grid(row = 2, column = 1)
city = Entry(root, width = 30)
city.grid(row = 3, column = 1)
state = Entry(root, width = 30)
state.grid(row = 4, column = 1)
zipcode = Entry(root, width = 30)
zipcode.grid(row = 5, column = 1, pady = 5)

delete_box = Entry(root, width = 30)
delete_box.grid(row = 9, column = 1)

# create text box labels
f_name_label = Label(root, text = "First Name: ")
f_name_label.grid(row = 0, column = 0, pady = (10, 0))
l_name_label = Label(root, text = "Last Name: ")
l_name_label.grid(row = 1, column = 0)
address_label = Label(root, text = "Address: ")
address_label.grid(row = 2, column = 0)
city_label = Label(root, text = "City: ")
city_label.grid(row = 3, column = 0)
state_label = Label(root, text = "State: ")
state_label.grid(row = 4, column = 0)
zipcode_label = Label(root, text = "Zipcode: ")
zipcode_label.grid(row = 5, column = 0)

delete_box_lbl = Label(root, text = "Select ID:")
delete_box_lbl.grid(row = 9, column = 0, pady = 5)

# Create submit button
submit_button = Button(root, text = "Add Info To Database", command = Submit)
submit_button.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# Create a Query button
query_btn = Button(root, text = "Show database", command = Query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 130)

# Create Delete Btn
delete_btn = Button(root, text = "Delete a Record ", command = Delete)
delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 129)

# Create an Update Button
edit_btn = Button(root, text = "Edit a Record ", command = Edit)
edit_btn.grid(row = 11, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 135)



# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()
