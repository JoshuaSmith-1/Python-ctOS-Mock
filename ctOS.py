import os
from tkinter import *
from datetime import datetime
import time
readable = time.ctime(1534153278)

ctOS = Tk()
os.chdir('H:\ctOS')
ctOSLog_File = open("ctOS-log-2803.txt", "a")
ctOS.geometry("280x540")
ctOS.title('.\ctOS\..')
ctOS.resizable(False, False)
ctOS.configure(bg='black')

os_get_cwd = Label(ctOS, text=os.getcwd(), bg='black', fg='white', font=('Consolas', 10)).grid(row=0, column=0)
time_t = Label(ctOS, text=readable, bg='black', fg='white', font=('Consolas', 10)).grid(row=2, column=0)
# print(os.stat('ctOS-log-2803.txt'))


def os_list_dir():
    window_1 = Toplevel(ctOS)
    window_1.geometry("685x540")
    # window_1.resizable(False, False)
    window_1.configure(bg='black')
    try:
         Label(window_1, text=os.listdir('H:\ctOS'), bg='white', font=('Consolas', 10)).grid(row=2, column=0) # , pady=10, padx=10)
         Label(window_1, text=os.listdir('H:\ctOS\images'), bg='white', font=('Consolas', 10)).grid(row=3, column=0) # , pady=10, padx=10)
         # Label(window_1, text=os.listdir('H:\ctOS\images\portable-network-graphic'), bg='white', font=('Consolas', 10)).grid(row=4, column=0) # , pady=10, padx=10)
         # Label(window_1, text=os.listdir('H:\ctOS\images\portable-network-graphic\ctOS'), bg='white', font=('Consolas', 10)).grid(row=4, column=0) # , pady=10, padx=10)
         # Label(window_1, text=os.listdir('H:\ctOS\images\portable-network-graphic\WatchDogs'), bg='white', font=('Consolas', 10)).grid(row=5, column=0) # , pady=10, padx=10)
    except AttributeError:
        print("This is not working")
    Button(window_1, command=window_1.destroy, bg='black', text="H:\Exit-2803\..", fg='white', font=('Consolas', 10)).grid(row=6, column=0)
    # logo_1 = PhotoImage(file='H:\ctOS\images\portable-network-graphic\ctOS\ctOS-systemLoading.png')
    # Label(window_1, image=logo_1, width='280', highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=7, column=0, columnspan=2)


def os_stat():
    window_2 = Toplevel(ctOS)
    window_2.geometry("280x540")
    window_2.resizable(False, False)
    window_2.configure(bg='black')
    ctOS_Entry = Entry(window_2)
    ctOS_Entry.grid(row=1, column=1)
    # print(os.stat('ctOS-log-2803.txt'))

    def submit():
        try:
            ctos_entry_text = ctOS_Entry.get()
            m_time = os.stat(ctos_entry_text).st_mtime
            c_time = os.stat(ctos_entry_text).st_ctime
            a_time = os.stat(ctos_entry_text).st_atime
            size = os.stat(ctos_entry_text).st_size
            time_covert_1 = datetime.fromtimestamp(m_time)
            time_covert_2 = datetime.fromtimestamp(c_time)
            time_covert_3 = datetime.fromtimestamp(a_time)
            text_output_1 = "st_mtime=" + str(time_covert_1)
            text_output_2 = "st_ctime=" + str(time_covert_2)
            text_output_3 = "st_atime=" + str(time_covert_3)
            text_output_4 = "st_size=" + str(size)
            Label(window_2, text=text_output_1, bg='white', font=('Consolas', 10)).grid(row=3, column=1, pady=10, padx=10)
            Label(window_2, text=text_output_2, bg='white', font=('Consolas', 10)).grid(row=4, column=1, pady=10, padx=10)
            Label(window_2, text=text_output_3, bg='white', font=('Consolas', 10)).grid(row=5, column=1, pady=10, padx=10)
            Label(window_2, text=text_output_4, bg='white', font=('Consolas', 10)).grid(row=6, column=1, pady=10, padx=10)
        except FileNotFoundError:
            print("Sorry this file is not found")
            ctOS_Entry.delete(0, END)

    Button(window_2, command=submit, bg='black', text="H:\Submit\..", fg='white', font=('Consolas', 10)).grid(row=2, column=1)

    # Label(window_2, text=file_stat, bg='white', font=('Consolas', 10)).grid(row=2, column=1, pady=10, padx=10)
    Button(window_2, command=window_2.destroy, bg='black', text="H:\Exit-2803\..", fg='white', font=('Consolas', 10)).grid(row=7, column=1)
    # file.write("\nHello")
    # tlogo_1 = PhotoImage(file='H:\ctOS\images\portable-network-graphic\ctOS\ctOS-systemLoading.png')
    # Label(window_2, image=logo_1, width='280', highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=7, column=0, columnspan=2)


ctOS_logo = PhotoImage(file='H:\ctOS\images\ctOS-logo.png')
ctOS_logo_L = Label(ctOS, image=ctOS_logo, width='275', highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=7, column=0, columnspan=1)
# Buttons
list_dir = Button(ctOS, command=os_list_dir, bg='black', text="H:\List-Dir\..", fg='white', font=('Consolas', 10), highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=3, column=0, pady=10, padx=10)
os_stat = Button(ctOS, command=os_stat, bg='black', text="H:\os-Stat\...", fg='white', font=('Consolas', 10), highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=4, column=0, pady=10, padx=10)
exit_2803 = Button(ctOS, command=ctOS.destroy, bg='black', text="H:\Exit-2803\...", fg='white', font=('Consolas', 10), highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=8, column=0, pady=10, padx=10)

ctOSLog_File.close()
ctOS.mainloop()
