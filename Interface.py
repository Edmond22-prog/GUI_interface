from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from Button_functions import registerCustomer
from Data_functions import *

# Fonction qui vide le frame
def clear_frame():
    for widgets in secondFrame.winfo_children():
        widgets.destroy()


def homePage():
    clear_frame()
    homeButton.configure(background="deepskyblue")
    customerButton.configure(background="red")
    deviceButton.configure(background="red")
    measureButton.configure(background="red")
    titleLabel.configure(text="Home Page")
    # HOME FRAME
    homeTitleFrame = Label(secondFrame, text="Last edit...", background="red", foreground="white", font=tkFont.Font(family="Sans Serif", size=20, weight="bold"))
    homeTitleFrame.grid(row=0, column=0, columnspan=3, padx=10, pady=20)

    ## CUSTOMER COLUMN
    customersColumn = Label(secondFrame, text="Customers", width=20, background="red", foreground="white", font=tkFont.Font(family="Sans Serif", size=15, weight="bold", underline=True))
    customersColumn.grid(row=1, column=0, padx=5, pady=10, sticky=W)
    
    display_last_customers(secondFrame)
    ## CUSTOMER COLUMN END

    ## DEVICE COLOUMN
    devicesColumn = Label(secondFrame, text="Devices", width=20, background="red", foreground="white", font=tkFont.Font(family="Sans Serif", size=15, weight="bold", underline=True))
    devicesColumn.grid(row=1, column=1, padx=5, pady=10)
    
    display_last_devices(secondFrame)
    ## DEVICE COLUMN END

    measuresColumn = Label(secondFrame, text="Measures", background="red", width=20, foreground="white", font=tkFont.Font(family="Sans Serif", size=15, weight="bold", underline=True))
    measuresColumn.grid(row=1, column=2, padx=5, pady=10)
    # END HOME FRAME


def customerPage():
    clear_frame()
    homeButton.configure(background="red")
    customerButton.configure(background="deepskyblue")
    deviceButton.configure(background="red")
    measureButton.configure(background="red")
    titleLabel.configure(text="Customers Page")

    # SECTION STYLE OF TREEVIEW CUSTOMERS
    ## Creation du style
    style = ttk.Style()
    ## Definition du theme a utiliser
    style.theme_use("default")
    ## Configuration du style
    style.configure("Treeview",
        background="red",
        foreground="white",
        fieldbackground="red"
    )
    ## Configuration du style au niveau des selections
    style.map("Treeview",
       background=[("selected", "lightpink")],
       foreground=[("selected", "black")]
    )
    # END SECTION STYLE TREEVIEW CUSTOMERS
    
    ## Creation du frame de la treeView
    treeFrame = Frame(secondFrame)
    treeFrame.grid(row=0, column=0, columnspan=9, padx=5, pady=5)

    # SECTION SCROLLBAR
    scroll = Scrollbar(treeFrame)
    scroll.pack(side=RIGHT, fill=Y)
    # END SECTION SCROLLBAR

    # SECTION TREEVIEW CUSTOMERS
    ## Creation du Treeview et configuration du scrollbar
    treeView = ttk.Treeview(treeFrame, yscrollcommand=scroll.set)
    treeView.pack()
    scroll.config(command=treeView.yview)
    ## Definition des colonnes
    treeView["columns"] = ("ID", "Company", "Street", "Location", "Postal Code", "Phone", "Email", "Name", "Surname")
    columns = ["ID", "Company", "Street", "Location", "Postal Code", "Phone", "Email", "Name", "Surname"]
    ## Formatage des colonnes
    treeView.column("#0", width=0,stretch=NO)
    treeView.column(columns[0], anchor=CENTER, minwidth=20, width=20)
    for i in range(1, len(columns)):
        treeView.column(columns[i], anchor=W, minwidth=100, width=100)
    ## Creation des rubriques
    treeView.heading("#0", text="")
    treeView.heading(columns[0], text=columns[0], anchor=CENTER)
    for i in range(1, len(columns)):
        treeView.heading(columns[i], text=columns[i], anchor=W)
    ## Ajout des donnees
    display_customers_data(treeView)

    # END SECTION TREEVIEW CUSTOMERS

    # BUTTON SECTION CUSTOMERS
    registerCustomerButton = Button(secondFrame, text="Register", command=registerCustomer, background="green", foreground="white", font="Sans-Serif 15 bold")
    registerCustomerButton.grid(row=1, column=1, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)

    registerDeviceButton = Button(secondFrame, text="Register Device", background="green", foreground="white", font="Sans-Serif 15 bold")
    registerDeviceButton.grid(row=1, column=4, columnspan=3, padx=10, pady=10, ipadx=5, ipady=5)

    deleteCustomerButton = Button(secondFrame, text="Delete", background="darkred", foreground="white", font="Sans-Serif 15 bold")
    deleteCustomerButton.grid(row=1, column=7, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)
    # END BUTTON SECTION CUSTOMERS


def devicePage():
    clear_frame()
    homeButton.configure(background="red")
    customerButton.configure(background="red")
    deviceButton.configure(background="deepskyblue")
    measureButton.configure(background="red")
    titleLabel.configure(text="Devices Pages")


def mesurePage():
    clear_frame()
    homeButton.configure(background="red")
    customerButton.configure(background="red")
    deviceButton.configure(background="red")
    measureButton.configure(background="deepskyblue")
    titleLabel.configure(text="Measures Page")


###     MAIN CODE       ###
window = Tk()
window.title("GUI Interface")
mainFrame = Frame(window, height=800, width=800, background="lightpink", highlightbackground="black", highlightthickness=3)
mainFrame.pack(ipadx=5, ipady=20)

# LABEL SECTION
menuLabel = Label(mainFrame, text="Menu", width=10, height=3, background="red", foreground="white", highlightbackground="black",
                    highlightthickness=3, font="Sans-Serif 15 bold")
menuLabel.grid(row=0, column=0, padx=40, pady=20)

titleLabel = Label(mainFrame, text="Home Page", width=65, height=3, background="red", foreground="white", highlightbackground="black", 
                    highlightthickness=3, font="Sans-Serif 15 bold")
titleLabel.grid(row=0, column=1, padx=5, pady=20)

# END LABEL SECTION

# BUTTON SECTION
homeButton = Button(mainFrame, text="Home", command=homePage, background="deepskyblue", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font="Sans-Serif 15 bold")
homeButton.grid(row=1, column=0)

customerButton = Button(mainFrame, text="+ Customer", command=customerPage, background="red", foreground="white", width=10, font="Sans-Serif 15 bold")
customerButton.grid(row=2, column=0, padx=5, pady=10)

deviceButton = Button(mainFrame, text="+ Device", command=devicePage, background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font="Sans-Serif 15 bold")
deviceButton.grid(row=3, column=0, padx=5, pady=10)

measureButton = Button(mainFrame, text="Measure", command=mesurePage, background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font="Sans-Serif 15 bold")
measureButton.grid(row=4, column=0, padx=5, pady=10)

settingButton = Button(mainFrame, text="Setting", background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font="Sans-Serif 15 bold")
settingButton.grid(row=7, column=0, padx=5, pady=10)

# END BUTTON SECTION

# HOME FRAME
secondFrame = Frame(mainFrame, width=780, height=450, background="red", highlightbackground="black", highlightthickness=3)
secondFrame.grid(row=1, column=1, rowspan=7, ipadx=5, ipady=5, padx=5)

homePage()
# END HOME FRAME

window.mainloop()
