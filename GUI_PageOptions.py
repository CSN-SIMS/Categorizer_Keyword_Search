from tkinter import Tk, Button, Frame, PhotoImage, Message, Canvas, Label, Listbox, Scrollbar, \
    RIGHT, X, Y, END, BOTTOM, HORIZONTAL, VERTICAL, filedialog, StringVar, OptionMenu, Checkbutton, IntVar
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
        self.var = "Sentiment Classification and Categorization of txt files"
        self.infoMessage = Message(self.higher_frame, text=self.var, justify='center', width=350, font=("Courier bold", 16))
        self.infoMessage.place(relx=0.4, rely=0.05, relwidth=0.5, relheight=0.3)

        # Menubar with Option, Result and Direct input
        self.menubar()

        # Lower frame with scrollbars for displaying of categories and file names
        self.lower_frame = Frame(self.root, bg='#FFD164', bd=5)
        self.lower_frame.place(relx=0.5, rely=0.35, relwidth=0.85, relheight=0.55, anchor='n')
        self.lower_frame.grid_rowconfigure(0, weight=1)
        self.lower_frame.grid_columnconfigure(0, weight=1)
        self.optionCanvas = Canvas(self.lower_frame, bg='white', bd=3)
        self.optionCanvas.place(relwidth=1, relheight=1)
        # select language (English or Swedish)
        self.selectLanguage(self.optionCanvas)
        # open folder with input files
        self.openFolder = Label(self.optionCanvas, text="Open a folder with input files", justify='left',
                                bg='white',
                                font=("Courier bold", 12))
        self.openFolder.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.2)
        self.button = Button(self.optionCanvas, text="Browse", font=("Courier", 12), bg='#EE7C7D',
                             activebackground='#f2d9e6',
                             command=lambda: self.fileDialog())
        self.button.place(relx=0.5, rely=0.4, relwidth=0.3, relheight=0.15)
        # save result in excel file
        self.CheckVar = IntVar()
        self.excelFileCheckbutton = Checkbutton(self.optionCanvas, text="Save as excel", variable=self.CheckVar, \
                         onvalue=1, offvalue=0, bg='white', font=("Courier bold", 12), height=5, width=20)
        self.excelFileCheckbutton.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.15)

    # Middle frame with buttons bar
    def menubar(self):
        self.middle_frame = Frame(self.root, bg='#FFD164', bd=5)
        self.middle_frame.place(relx=0.5, rely=0.25, relwidth=0.85, relheight=0.1, anchor='n')
        self.button = Button(self.middle_frame, text="Options", font=("Courier", 12), bg='#EE7C7D',
                             activebackground='#f2d9e6',
                             command=lambda: self.fileDialog())
        self.button.place(relx=0.1, relwidth=0.2, relheight=1)
        self.button = Button(self.middle_frame, text="Result", font=("Courier", 12), bg='#EE7C7D',
                             activebackground='#f2d9e6',
                             command=lambda: self.fileDialog())
        self.button.place(relx=0.4, relwidth=0.2, relheight=1)
        self.button = Button(self.middle_frame, text="Direct input", font=("Courier", 12), bg='#EE7C7D',
                             activebackground='#f2d9e6',
                             command=lambda: self.fileDialog())
        self.button.place(relx=0.7, relwidth=0.2, relheight=1)

    # select language (English or Swedish)
    def selectLanguage(self, parentWidget):
        # Create a Tkinter variable
        self.tkvar = StringVar()
        # Dictionary with options
        self.choices = {'English', 'Swedish'}
        self.tkvar.set('English')  # set the default option
        # Popup menu with languages
        self.popupMenu = OptionMenu(parentWidget, self.tkvar, *self.choices)
        self.popupLabel = Label(parentWidget, text="Choose a language", bg='white', justify='left',
                                font=("Courier bold", 12))
        self.popupLabel.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.2)
        self.popupMenu.configure(bd=3, bg='#EE7C7D')
        self.popupMenu.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.15)
        # on change dropdown value
        def change_dropdown(*args):
            print(self.tkvar.get())
        # link function to change dropdown
        self.tkvar.trace('w', change_dropdown)

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


