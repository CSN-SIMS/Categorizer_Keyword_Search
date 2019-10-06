import tkinter as tk
from tkinter import filedialog
import keywordSearch

# Initial size of the app
HEIGHT = 600
WIDTH = 800
# Gets the selected folder by the user and uses keywordSearch in txt files, then presents categories and file names
def fileDialog():
    try:
        folderSelected = filedialog.askdirectory()
        dict_obj = keywordSearch.fileCategorizedInMap(folderSelected)
        results.insert(tk.END, "Category".ljust(20, ' ') + "File name")
        results.insert(tk.END, "\n")
        for key, val in dict_obj.items():
            results.insert(tk.END, str(key).ljust(20, ' ') + str(val))
    except UnicodeDecodeError:
        results.insert(tk.END, "Selected folder does not contain txt files.")
# Create GUI App
root = tk.Tk()
root.title("Categorization Dialog Widget")
root.minsize(750, 550)
# Background
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
background_label = tk.Label(root, bg='#ccfff2')
background_label.place(relwidth=1, relheight=1)
canvas.pack()
# Upper frame with logo and info message
higher_frame = tk.Frame(root, bg='#80c1ff', bd=5)
higher_frame.place(relx=0.5, rely=0.1, relwidth=0.85, relheight=0.35, anchor='n')
logo = tk.Canvas(higher_frame, bd=1)
logo.place(relx=0, rely=0, relwidth=1, relheight=0.5)
img = tk.PhotoImage(file="logo.png")
img = img.subsample(6)
logo.create_image(0, 0, anchor='nw', image=img)
var = "Categorization of txt files from a given folder and presenting them in a table"
infoMessage = tk.Message(higher_frame, text=var, width=350, font=("Courier bold", 14))
infoMessage.place(relx=0.4, rely=0.05, relwidth=0.5, relheight=0.3)
# Middle frame with info message and button
middle_frame = tk.Frame(root, bg='#80c1ff', bd=5)
middle_frame.place(relx=0.5, rely=0.25, relwidth=0.85, relheight=0.1, anchor='n')
openFolder = tk.Label(middle_frame, text = "Open a folder with \ninput files", justify='center', bg='white', font=("Courier", 12))
openFolder.place(relx=0, rely=0, relwidth=0.65, relheight=1)
button = tk.Button(middle_frame, text="Browse", font=("Courier", 12), bg='#b3b3b3', activebackground='#f2d9e6', command=lambda: fileDialog())
button.place(relx=0.7, relwidth=0.3, relheight=1)
# Lower frame with scrollbars for displaying of categories and file names
lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.35, relwidth=0.85, relheight=0.55, anchor='n')
lower_frame.grid_rowconfigure(0, weight=1)
lower_frame.grid_columnconfigure(0, weight=1)
results = tk.Listbox(lower_frame, font=("Courier", 12), bg='white', justify='left', bd=3)
results.grid(column=1, row = 1, padx = 10,ipady = 10)
results.place(relwidth=1, relheight=1)
scrollbar_vertical = tk.Scrollbar(lower_frame, orient=tk.VERTICAL)
scrollbar_vertical.pack( side = tk.RIGHT, fill = tk.Y )
scrollbar_vertical.configure(command=results.yview)
scrollbar_horizontal = tk.Scrollbar(lower_frame, orient=tk.HORIZONTAL)
scrollbar_horizontal.pack( side = tk.BOTTOM, fill = tk.X )
scrollbar_horizontal.configure(command=results.xview)
results.configure(yscrollcommand=scrollbar_vertical.set)
results.configure(xscrollcommand=scrollbar_horizontal.set)
# for i in range(1, 20):
#     results.insert(tk.END, "List" + str(i))

root.mainloop()