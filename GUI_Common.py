from tkinter import Tk, Button, Frame, PhotoImage, Message, Canvas, Label, Listbox, Scrollbar, \
    RIGHT, X, Y, END, BOTTOM, HORIZONTAL, VERTICAL, Entry, Menubutton, Menu, FLAT, OptionMenu, RAISED, filedialog, StringVar
from keywordSearch import *
from GUI_PageResult import *
from GUI_PageOptions import *
from GUI_PageDirectInput import *

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

# select language (English or Swedish)
def selectLanguage(self, parentWidget):
    # Create a Tkinter variable
    self.tkvar = StringVar()
    # Dictionary with options
    self.choices = {'English', 'Swedish'}
    self.tkvar.set('English')  # set the default option
    # Popup menu with languages
    self.popupMenu = OptionMenu(parentWidget, self.tkvar, *self.choices)
    self.popupLabel = Label(parentWidget, text="Choose a language", font=("Courier bold", 12), bg='#FFD164')
    self.popupLabel.place(relx=0.1, rely=0, relwidth=0.3, relheight=0.2)
    self.popupMenu.configure(bd=3, bg='#EE7C7D')
    self.popupMenu.place(relx=0.5, rely=0, relwidth=0.3, relheight=0.15)
    # on change dropdown value
    def change_dropdown(*args):
        print(self.tkvar.get())
    # link function to change dropdown
    self.tkvar.trace('w', change_dropdown)

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       lower_frame = Frame(self, bg='#FFD164', bd=5)
       lower_frame.place(relx=0.5, rely=0.35, relwidth=0.85, relheight=0.55, anchor='n')
       lower_frame.grid_rowconfigure(0, weight=1)
       lower_frame.grid_columnconfigure(0, weight=1)
       # Entry text box
       selectLanguage(self,lower_frame)
       entryLabel = Label(lower_frame, text="Enter text", bg='#FFD164', font=("Courier bold", 12))
       entryLabel.place(relx=0.37, rely=0.2, relwidth=0.25, relheight=0.1)
       entryContent = Entry(lower_frame, font=("Courier", 12,), justify='center')
       entryContent.place(relx=0, rely=0.3, relwidth=1, relheight=0.6)
       button = Button(lower_frame, text="Analyze", font=("Courier", 12), bg='#b3b3b3',
                            activebackground='#f2d9e6', command=lambda: self.fileDialog())
       button.place(relx=0.4, rely=0.91, relwidth=0.2, relheight=0.1)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        menu_frame = Frame(self, bg='#FFD164', bd=5)
        menu_frame.pack(side="top", fill="x", expand=False)
        logo = Canvas(menu_frame, bd=1)
        logo.place(relx=0, rely=0, relwidth=1, relheight=0.5)
        img = PhotoImage(file="logo.png")
        img = img.subsample(6)
        logo.create_image(0, 0, anchor='nw', image=img)
        var = "Sentiment analysis of a direct input"
        infoMessage = Message(menu_frame, text=var, justify='center', width=350,
                                   font=("Courier bold", 14))
        infoMessage.place(relx=0.4, rely=0.05, relwidth=0.5, relheight=0.3)
        button1 = Button(menu_frame, text="Options", font=("Courier", 12), bg='#EE7C7D',
                         activebackground='#f2d9e6',
                         command=p1.lift)
        button1.place(relx=0.1, relwidth=0.2, relheight=1)
        button2 = Button(menu_frame, text="Result", font=("Courier", 12), bg='#EE7C7D',
                         activebackground='#f2d9e6',
                         command=p2.lift)
        button2.place(relx=0.4, relwidth=0.2, relheight=1)
        button3 = Button(menu_frame, text="Direct input", font=("Courier", 12), bg='#EE7C7D',
                         activebackground='#f2d9e6',
                         command=p3.lift)
        button3.place(relx=0.7, relwidth=0.2, relheight=1)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

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
    root.title("Categorization Dialog Widget")
    root.minsize(750, 550)
    root.wm_geometry("400x400")
    root.mainloop()