from tkinter import Tk, Button, Frame, PhotoImage, Message, Canvas, Label, Listbox, Scrollbar, \
    RIGHT, X, Y, END, BOTTOM, HORIZONTAL, VERTICAL, Entry, Menubutton, Menu, Checkbutton, OptionMenu, RAISED, filedialog, StringVar, IntVar
from keywordSearch import *

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

def backgroundSet(self):
    # Background
    self.HEIGHT = 600
    self.WIDTH = 800
    self.canvas = Canvas(self, height=self.HEIGHT, width=self.WIDTH)
    self.background_label = Label(self, bg='#3C1E5F')
    self.background_label.place(relwidth=1, relheight=1)
    self.canvas.pack()

# select language (English or Swedish)
def selectLanguage(self, parentWidget, backgroundColor):
    # Create a Tkinter variable
    self.tkvar = StringVar()
    # Dictionary with options
    self.choices = {'English', 'Swedish'}
    self.tkvar.set('English')  # set the default option
    # Popup menu with languages
    self.popupMenu = OptionMenu(parentWidget, self.tkvar, *self.choices)
    self.popupLabel = Label(parentWidget, text="Choose a language", font=("Courier bold", 12), bg=backgroundColor)
    self.popupLabel.place(relx=0.1, rely=0, relwidth=0.3, relheight=0.2)
    self.popupMenu.configure(bd=3, bg='#EE7C7D')
    self.popupMenu.place(relx=0.5, rely=0, relwidth=0.3, relheight=0.15)
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

        # 1. Shows the amount of analyzed Emails
        amountOfFiles = self.categorizer.amountOfFiles(self.folderSelected)
        self.results.insert(END, "Amount of analysed Emails: " + str(amountOfFiles))
        self.results.insert(END, "\n")

        # Shows a List of categories with their emails
        self.dict_obj = self.categorizer.categorizeFilesFromDirectoryInMapAndSubDirectory()
        self.results.insert(END, "Category".ljust(20, ' ') + "File name")
        self.results.insert(END, "\n")
        for key, val in self.dict_obj.items():
            self.results.insert(END, str(key).ljust(20, ' ') + str(val))
    except UnicodeDecodeError:
        self.results.insert(END, "Selected folder does not contain txt files.")

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       backgroundSet(self)
       # Lower frame with scrollbars for displaying of categories and file names
       lower_frame = Frame(self, bg='#FFD164', bd=5)
       lower_frame.place(relx=0.5, rely=0.15, relwidth=0.9, relheight=0.7, anchor='n')
       lower_frame.grid_rowconfigure(0, weight=1)
       lower_frame.grid_columnconfigure(0, weight=1)
       optionCanvas = Canvas(lower_frame, bg='white', bd=3)
       optionCanvas.place(relwidth=1, relheight=1)
       # select language (English or Swedish)
       selectLanguage(self, optionCanvas, 'white')
       # save result in excel file
       CheckVar = IntVar()
       excelFileCheckbutton = Checkbutton(optionCanvas, text="Save as excel", variable=CheckVar, onvalue=1,
                                          offvalue=0, bg='white', font=("Courier bold", 12), height=5, width=20)
       excelFileCheckbutton.place(relx=0.1, rely=0.3, relwidth=0.3, relheight=0.15)
       # open folder with input files
       openFolder = Label(optionCanvas, text="Open a folder with input files", justify='left',
                               bg='white',
                               font=("Courier bold", 12))
       openFolder.place(relx=0.05, rely=0.6, relwidth=0.4, relheight=0.2)
       button = Button(optionCanvas, text="Browse", font=("Courier", 12), bg='#EE7C7D',
                            activebackground='#f2d9e6',
                            command=lambda: fileDialog(self))
       button.place(relx=0.5, rely=0.6, relwidth=0.3, relheight=0.15)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       backgroundSet(self)
       # Lower frame with scrollbars for displaying of categories and file names
       lower_frame = Frame(self, bg='#FFD164', bd=5)
       lower_frame.place(relx=0.5, rely=0.15, relwidth=0.9, relheight=0.7, anchor='n')
       lower_frame.grid_rowconfigure(0, weight=1)
       lower_frame.grid_columnconfigure(0, weight=1)
       results = Listbox(lower_frame, font=("Courier", 12), bg='white', fg='#EE7C7D', justify='left', bd=3)
       results.grid(column=1, row=1, padx=10, ipady=10)
       results.place(relwidth=1, relheight=1)
       scrollbar_vertical = Scrollbar(lower_frame, orient=VERTICAL)
       scrollbar_vertical.pack(side=RIGHT, fill=Y)
       scrollbar_vertical.configure(command=results.yview)
       scrollbar_horizontal = Scrollbar(lower_frame, orient=HORIZONTAL)
       scrollbar_horizontal.pack(side=BOTTOM, fill=X)
       scrollbar_horizontal.configure(command=results.xview)
       results.configure(yscrollcommand=scrollbar_vertical.set)
       results.configure(xscrollcommand=scrollbar_horizontal.set)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       backgroundSet(self)
       lower_frame = Frame(self, bg='#FFD164', bd=5)
       lower_frame.place(relx=0.5, rely=0.15, relwidth=0.9, relheight=0.7, anchor='n')
       lower_frame.grid_rowconfigure(0, weight=1)
       lower_frame.grid_columnconfigure(0, weight=1)
       # Entry text box
       selectLanguage(self, lower_frame, '#FFD164')
       entryLabel = Label(lower_frame, text="Enter text", bg='#FFD164', font=("Courier bold", 12))
       entryLabel.place(relx=0.37, rely=0.2, relwidth=0.25, relheight=0.1)
       entryContent = Entry(lower_frame, font=("Courier", 12,), justify='center')
       entryContent.place(relx=0, rely=0.3, relwidth=1, relheight=0.6)
       button = Button(lower_frame, text="Analyze", font=("Courier", 12), bg='#b3b3b3',
                       activebackground='#f2d9e6', command=lambda: self.fileDialog())
       button.place(relx=0.4, rely=0.91, relwidth=0.2, relheight=0.1)

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        menu_frame = Frame(self, bg='#FFD164', bd=5)
        menu_frame.place(relx=0, rely=0, relwidth=1, relheight=0.2)
        logo = Canvas(menu_frame, bd=1)
        logo.place(relx=0, rely=0, relwidth=0.21, relheight=0.5)
        img = PhotoImage(file="logo.png")
        img = img.subsample(2)
        logo.create_image(0, 0, anchor='nw', image=img)
        var = "Sentiment analysis/Categorization"
        infoMessage = Message(menu_frame, text=var, justify='center', width=350,
                                   font=("Courier bold", 14))
        infoMessage.place(relx=0.5, rely=0.05, relwidth=0.4, relheight=0.5)
        button_frame = Frame(self, bg='#FFD164', bd=5)
        button_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.3)
        button1 = Button(button_frame, text="Options", font=("Courier", 12), bg='#EE7C7D',
                         activebackground='#f2d9e6',
                         command=p1.lift)
        button1.place(relx=0.1, relwidth=0.2, relheight=1)
        button2 = Button(button_frame, text="Result", font=("Courier", 12), bg='#EE7C7D',
                         activebackground='#f2d9e6',
                         command=p2.lift)
        button2.place(relx=0.4, relwidth=0.2, relheight=1)
        button3 = Button(button_frame, text="Direct input", font=("Courier", 12), bg='#EE7C7D',
                         activebackground='#f2d9e6',
                         command=p3.lift)
        button3.place(relx=0.7, relwidth=0.2, relheight=1)

        container = Frame(self)
        container.place(relx=0, rely=0.3, relwidth=1, relheight=0.7)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        button1.pack(side="left")
        button2.pack(side="left")
        button3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.title("Sentiment Classification/Categorization Dialog Widget")
    root.minsize(750, 550)
    root.mainloop()