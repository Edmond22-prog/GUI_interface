from tkinter import *

def registerCustomer():

    def clearAllEntry():
        companyEntry.configure(bg="white")
        companyEntry.delete(0, len(companyEntry.get()))
        streetEntry.configure(bg="white")
        streetEntry.delete(0, len(streetEntry.get()))
        locationEntry.configure(bg="white")
        locationEntry.delete(0, len(locationEntry.get()))
        postalEntry.configure(bg="white")
        postalEntry.delete(0, len(postalEntry.get()))
        phoneEntry.configure(bg="white")
        phoneEntry.delete(0, len(phoneEntry.get()))
        emailEntry.configure(bg="white")
        emailEntry.delete(0, len(emailEntry.get()))
        nameEntry.configure(bg="white")
        nameEntry.delete(0, len(nameEntry.get()))
        surnameEntry.configure(bg="white")
        surnameEntry.delete(0, len(surnameEntry.get()))


    # def save():
    #     company = companyEntry.get()
    #     street = streetEntry.get()
    #     location = locationEntry.get()
    #     postal_code = postalEntry.get()
    #     phone = phoneEntry.get()
    #     email = emailEntry.get()
    #     name = nameEntry.get()
    #     surname =  surnameEntry.get()
    #     if (phone != "" and name != "" and surname != ""):
    #         try:
    #             phone = int(phone)
    #         except:
    #             phoneEntry.configure(bg="darkred", foreground="white")
    #             window.after(1000,  clearAllEntry)
    #         else:
    #             print("Saved !")
    #             companyEntry.config(bg="green")
    #             streetEntry.config(bg="green")
    #             locationEntry.config(bg="green")
    #             postalEntry.config(bg="green")
    #             phoneEntry.config(bg="green")
    #             emailEntry.config(bg="green")
    #             nameEntry.config(bg="green")
    #             surnameEntry.config(bg="green")
    #     else:
    #         if phone == "":
    #             phoneEntry.configure(bg="darkred")
    #         if name == "":
    #             nameEntry.configure(bg="darkred", invalidcommand="Test")
    #         if surname == "":
    #             surnameEntry.configure(bg="darkred")
    #         window.after(1000,  clearAllEntry)
        
        

    window = Tk()
    window.title("Customer Registration")
    frame = Frame(window, background="lightpink", height=800, width=700, highlightbackground="black", highlightthickness=3)
    frame.pack(ipadx=5, ipady=20)
    
    title = Label(frame, text="Customer Registration", background="red", foreground="white", highlightbackground="black", highlightthickness=3,
                         width=40, height=3, font="sans-serif 18 bold")
    title.grid(row=0, column=0, padx=20, pady=20)

    formFrame = Frame(frame,  width=600, height=600, background="red", highlightbackground="black", highlightthickness=3)
    formFrame.grid(row=1, column=0, padx=10, pady=10)
 
    companyLabel = Label(formFrame, text="Company", background="red", foreground="white", font="sans-serif 15 bold underline")
    companyLabel.grid(row=0, padx=20, pady=10, sticky=W)
    companyEntry = Entry(formFrame, width=50)
    companyEntry.grid(row=0, column=1, padx=20)
    streetLabel = Label(formFrame, text="Street", background="red", foreground="white", font="sans-serif 15 bold underline")
    streetLabel.grid(row=1, padx=20, pady=10, sticky=W)
    streetEntry = Entry(formFrame, width=50)
    streetEntry.grid(row=1, column=1, padx=20)
    locationLabel = Label(formFrame, text="Location", background="red", foreground="white", font="sans-serif 15 bold underline")
    locationLabel.grid(row=2, padx=20, pady=10, sticky=W)
    locationEntry = Entry(formFrame, width=50)
    locationEntry.grid(row=2, column=1, padx=20)
    postalLabel = Label(formFrame, text="Postal Code", background="red", foreground="white", font="sans-serif 15 bold underline")
    postalLabel.grid(row=3, padx=20, pady=10, sticky=W)
    postalEntry = Entry(formFrame, width=50)
    postalEntry.grid(row=3, column=1, padx=20)
    phoneLabel = Label(formFrame, text="Phone*", background="red", foreground="white", font="sans-serif 15 bold underline")
    phoneLabel.grid(row=4, padx=20, pady=10, sticky=W)
    phoneEntry = Entry(formFrame, width=50)
    phoneEntry.grid(row=4, column=1, padx=20)
    emailLabel = Label(formFrame, text="Email", background="red", foreground="white", font="sans-serif 15 bold underline")
    emailLabel.grid(row=5, padx=20, pady=10, sticky=W)
    emailEntry = Entry(formFrame, width=50)
    emailEntry.grid(row=5, column=1, padx=20)
    nameLabel = Label(formFrame, text="Name*", background="red", foreground="white", font="sans-serif 15 bold underline")
    nameLabel.grid(row=6, padx=20, pady=10, sticky=W)
    nameEntry = Entry(formFrame, width=50)
    nameEntry.grid(row=6, column=1, padx=20)
    surnameLabel = Label(formFrame, text="Surname*", background="red", foreground="white", font="sans-serif 15 bold underline")
    surnameLabel.grid(row=7, padx=20, pady=10, sticky=W)
    surnameEntry = Entry(formFrame, width=50)
    surnameEntry.grid(row=7, column=1, padx=20)

    saveButton = Button(formFrame, text="Save", command=save, width=10, background="green", foreground="white", font="Sans-Serif 15 bold")
    saveButton.grid(row=8, column=0, padx=30, pady=20)
    cancelButton = Button(formFrame, text="Cancel", command=window.destroy, width=10, background="darkred", foreground="white", font="Sans-Serif 15 bold")
    cancelButton.grid(row=8, column=1, padx=10, pady=20)

    window.mainloop()
