import os
from tkinter import *
from datetime import datetime

ctOS = Tk()
os.chdir('H:\ctOS')
ctOSLog_File = open("ctOS-log-2803.txt", "a")
ctOS.geometry("280x540")
ctOS.title('.\ctOS\..')
ctOS.resizable(False, False)
ctOS.configure(bg='black')

os_get_cwd = Label(ctOS, text=os.getcwd(), bg='black', fg='white', font=('Consolas', 10)).grid(row=0, column=0)


def os_list_dir():
    window_1 = Toplevel(ctOS)
    window_1.geometry("685x540")
    # window_1.resizable(False, False)
    window_1.configure(bg='black')
    try:
        Label(window_1, text=os.listdir('H:\ctOS'), bg='green', font=('Consolas', 10)).grid(row=2, column=0) # , pady=10, padx=10)
        Label(window_1, text=os.listdir('H:\ctOS\images'), bg='green', font=('Consolas', 10)).grid(row=3, column=0) # , pady=10, padx=10)
        Label(window_1, text=os.listdir('H:\ctOS\images\portable-network-graphic\ctOS'), bg='green', font=('Consolas', 10)).grid(row=4, column=0) # , pady=10, padx=10)
        Label(window_1, text=os.listdir('H:\ctOS\images\portable-network-graphic\WatchDogs'), bg='green', font=('Consolas', 10)).grid(row=5, column=0) # , pady=10, padx=10)
    except Exception:
        print("This label is not working..")
    Button(window_1, command=window_1.destroy, bg='black', text="H:\Exit-2803\..", fg='white', font=('Consolas', 10)).grid(row=6, column=0)


def os_stat():
    window_2 = Toplevel(ctOS)
    window_2.geometry("280x540")
    window_2.resizable(False, False)
    window_2.configure(bg='black')
    mod_time = os.stat('ctOS-log-2803.txt').st_mtime
    time_covert = datetime.fromtimestamp(mod_time)
    Label(window_2, text=time_covert, bg='green', font=('Consolas', 10)).grid(row=1, column=1, pady=10, padx=10)
    Button(window_2, command=window_2.destroy, bg='black', text="H:\Exit-2803\..", fg='white', font=('Consolas', 10)).grid(row=2, column=1)
    # file.write("\nHello")


ctOS_logo = PhotoImage(file="H:\ctOS\images\portable-network-graphic\ctOS-logo.png")
ctOS_logo_L = Label(ctOS, image=ctOS_logo, width='280', highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=7, column=0, columnspan=2)
# Buttons
list_dir = Button(ctOS, command=os_list_dir, bg='black', text="H:\List-Dir\..", fg='white', font=('Consolas', 10), highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=2, column=0, pady=10, padx=10)
os_stat = Button(ctOS, command=os_stat, bg='black', text="H:\os-Stat\...", fg='white', font=('Consolas', 10), highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=3, column=0, pady=10, padx=10)

ctOSLog_File.close()
ctOS.mainloop()
