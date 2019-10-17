from tkinter import Tk, Button, Frame, PhotoImage, Message, Canvas, Label, Listbox, Scrollbar, \
    RIGHT, X, Y, END, BOTTOM, HORIZONTAL, VERTICAL, filedialog
from keywordSearch import *


# Create GUI Application for Categorization of emails
class PageOptions():
    def __init__(self):
        self.root = Tk()
        self.createWidgets()
        self.root.mainloop()

    def initialize_variables(self):
        # Initial size of the app
        self.HEIGHT = 600
        self.WIDTH = 800
        self.root.title("Categorization Dialog Widget")
        self.root.minsize(750, 550)

    def createWidgets(self):
        self.initialize_variables()

        # Background
        self.canvas = Canvas(self.root, height=self.HEIGHT, width=self.WIDTH)
        self.background_label = Label(self.root, bg='#3C1E5F')
        self.background_label.place(relwidth=1, relheight=1)
        self.canvas.pack()

        # Upper frame with logo and info message
        self.higher_frame = Frame(self.root, bg='#FFD164', bd=5)
        self.higher_frame.place(relx=0.5, rely=0.1, relwidth=0.85, relheight=0.35, anchor='n')
        self.logo = Canvas(self.higher_frame, bd=1)
        self.logo.place(relx=0, rely=0, relwidth=1, relheight=0.5)
        self.img = PhotoImage(file="logo.png")
        self.img = self.img.subsample(6)
        self.logo.create_image(0, 0, anchor='nw', image=self.img)
        self.var = "Categorization of txt files from a given folder to sub-folders and presenting them in a table"
        self.infoMessage = Message(self.higher_frame, text=self.var, justify='center', width=350, font=("Courier bold", 14))
        self.infoMessage.place(relx=0.4, rely=0.05, relwidth=0.5, relheight=0.3)

        # Middle frame with info message and button
        self.middle_frame = Frame(self.root, bg='#FFD164', bd=5)
        self.middle_frame.place(relx=0.5, rely=0.25, relwidth=0.85, relheight=0.1, anchor='n')
        self.openFolder = Label(self.middle_frame, text="Open a folder with \ninput files", justify='center', bg='white', fg='#EE7C7D',
                              font=("Courier", 12,))
        self.openFolder.place(relx=0, rely=0, relwidth=0.65, relheight=1)
        self.button = Button(self.middle_frame, text="Browse", font=("Courier", 12), bg='#b3b3b3', activebackground='#f2d9e6',
                           command=lambda: self.fileDialog())
        self.button.place(relx=0.7, relwidth=0.3, relheight=1)

        # Lower frame with scrollbars for displaying of categories and file names
        self.lower_frame = Frame(self.root, bg='#FFD164', bd=5)
        self.lower_frame.place(relx=0.5, rely=0.35, relwidth=0.85, relheight=0.55, anchor='n')
        self.lower_frame.grid_rowconfigure(0, weight=1)
        self.lower_frame.grid_columnconfigure(0, weight=1)
        self.results = Listbox(self.lower_frame, font=("Courier", 12), bg='white', fg='#EE7C7D', justify='left', bd=3)
        self.results.grid(column=1, row=1, padx=10, ipady=10)
        self.results.place(relwidth=1, relheight=1)
        self.scrollbar_vertical = Scrollbar(self.lower_frame, orient=VERTICAL)
        self.scrollbar_vertical.pack(side=RIGHT, fill=Y)
        self.scrollbar_vertical.configure(command=self.results.yview)
        self.scrollbar_horizontal = Scrollbar(self.lower_frame, orient=HORIZONTAL)
        self.scrollbar_horizontal.pack(side=BOTTOM, fill=X)
        self.scrollbar_horizontal.configure(command=self.results.xview)
        self.results.configure(yscrollcommand=self.scrollbar_vertical.set)
        self.results.configure(xscrollcommand=self.scrollbar_horizontal.set)

    # Gets the selected folder by the user and uses keywordSearch in txt files, then presents categories and file names
    def fileDialog(self):
        try:
            self.folderSelected = filedialog.askdirectory()
            self.categorizer = Categorizer(self.folderSelected)
            self.dict_obj = self.categorizer.categorizeFilesFromDirectoryInMapAndSubDirectory()
            self.results.insert(END, "Category".ljust(20, ' ') + "File name")
            self.results.insert(END, "\n")
            for key, val in self.dict_obj.items():
                self.results.insert(END, str(key).ljust(20, ' ') + str(val))
        except UnicodeDecodeError:
            self.results.insert(END, "Selected folder does not contain txt files.")


