# START OF CODE
import os
from tkinter import *
from datetime import datetime
import time
import sys
# The current time
readable = time.ctime(1534153278)

# ctOS is the main window
# This code below configures the program window with Tkinter
ctOS = Tk()
os.chdir('H:\ctOS')
ctOSLog_File = open("ctOS-log-2803.txt", "a")
ctOS.geometry("280x540")
ctOS.title('.\ctOS\..')
ctOS.resizable(False, False)
ctOS.configure(bg='black')
# ctOSLog_File.write(os.getcwd())
# ctOSLog_File.write("\nProgram Accessed: " + readable)
os_login = "User: " + os.getlogin()
ctOS.withdraw()

# print(os.listdir('C:\Program Files'))
# print(os.listdir('C:\Windows'))

# This outputs the current working drive and the current time and day of the week at the top of the screen
os_get_cwd = Label(ctOS, text=os.getcwd(), bg='black', fg='white', font=('Consolas', 10)).grid(row=0, column=0)
# sys_version = Label(ctOS, text=sys.version, bg='black', fg='white', font=('Consolas', 10)).grid(row=1, column=0)
os_get_login = Label(ctOS, text=os_login, bg='black', fg='white', font=('Consolas', 10)).grid(row=2, column=0)
time_t = Label(ctOS, text=readable, bg='black', fg='white', font=('Consolas', 10)).grid(row=3, column=0)


# list_dir button sub-routine
# This os_list_dir() sub-routine requires the specific directories to be updated if any changes occurs
def os_list_dir():
    ctOS_os_List_Dir = Toplevel(ctOS)
    ctOS_os_List_Dir.geometry("685x540")
    ctOS_os_List_Dir.resizable(False, False)
    ctOS_os_List_Dir.configure(bg='black')
    # The code below is what outputs a list of what is in the specified directories
    try:
         Label(ctOS_os_List_Dir, text=os.listdir('H:\ctOS'), bg='white', font=('Consolas', 10)).grid(row=2, column=0)
         Label(ctOS_os_List_Dir, text=os.listdir('H:\ctOS\images'), bg='white', font=('Consolas', 10)).grid(row=3, column=0)
    except AttributeError:
        print("This is not working")
    Button(ctOS_os_List_Dir, command=ctOS_os_List_Dir.destroy, bg='black', text="H:\Exit-2803\..", fg='white', font=('Consolas', 10)).grid(row=6, column=0)
    # logo_1 = PhotoImage(file='H:\ctOS\images\ctOS-systemLoading.png')
    # Label(ctOS_os_List_Dir, image=logo_1, width='280', highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=7, column=0, columnspan=2)


# os_stat button sub-routine
# This os_stat() sub-routine requires two things, a text file and the text file to be located in the main directory
def os_stat():
    ctOS_os_Stat = Toplevel(ctOS)
    ctOS_os_Stat.geometry("280x540")
    ctOS_os_Stat.resizable(False, False)
    ctOS_os_Stat.configure(bg='black')
    ctOS_Entry = Entry(ctOS_os_Stat)  # This is where you enter the text file name (eg. ctOS-log-2803.txt)
    ctOS_Entry.grid(row=1, column=1)

    def submit():
        try:
            ctos_entry_text = ctOS_Entry.get()  # This gets the text file name from 'ctOS_Entry' (Line 49) and stores it in 'ctos_entry_text'
            m_time = os.stat(ctos_entry_text).st_mtime  # This gets the last modified time from entry
            c_time = os.stat(ctos_entry_text).st_ctime  # This gets the time it was created from entry
            a_time = os.stat(ctos_entry_text).st_atime  # This gets the time when it was last accessed
            size = os.stat(ctos_entry_text).st_size     # This gets the file size from the entry
            time_covert_1 = datetime.fromtimestamp(m_time)  # This converts it to a readable timestamp
            time_covert_2 = datetime.fromtimestamp(c_time)  # "
            time_covert_3 = datetime.fromtimestamp(a_time)  # "
            text_output_1 = "st_mtime=" + str(time_covert_1)  # This formats what it is gonna look like
            text_output_2 = "st_ctime=" + str(time_covert_2)  # "
            text_output_3 = "st_atime=" + str(time_covert_3)  # "
            text_output_4 = "st_size=" + str(size)            # "
            Label(ctOS_os_Stat, text=text_output_1, bg='white', font=('Consolas', 10)).grid(row=3, column=1, pady=10, padx=10)  # This outputs the data to the screen
            Label(ctOS_os_Stat, text=text_output_2, bg='white', font=('Consolas', 10)).grid(row=4, column=1, pady=10, padx=10)  # "
            Label(ctOS_os_Stat, text=text_output_3, bg='white', font=('Consolas', 10)).grid(row=5, column=1, pady=10, padx=10)  # "
            Label(ctOS_os_Stat, text=text_output_4, bg='white', font=('Consolas', 10)).grid(row=6, column=1, pady=10, padx=10)  # "
        except FileNotFoundError:  # This checks to see if you made a mistake and alerts you without pausing the program or outputing a huge error message on the python console
            print("Sorry this file is not found")
            ctOS_Entry.delete(0, END)
            
    # This button run the submit() sub-routine       
    Button(ctOS_os_Stat, command=submit, bg='black', text="H:\Submit\..", fg='white', font=('Consolas', 10)).grid(row=2, column=1)    
    # This close the os_stat window
    Button(ctOS_os_Stat, command=ctOS_os_Stat.destroy, bg='black', text="H:\Exit-2803\..", fg='white', font=('Consolas', 10)).grid(row=7, column=1)
    ctOS_Sys_Load = PhotoImage(file='H:\ctOS\images\ctOS-logo.png')
    Label(ctOS_os_Stat, image=ctOS_Sys_Load, width='280', highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=7, column=0, columnspan=2)


def os_walk():
    ctOS_os_Walk = Toplevel(ctOS)
    ctOS_os_Walk.geometry("280x540")
    ctOS_os_Walk.resizable(False, False)
    ctOS_os_Walk.configure(bg='black')
    ctOS_os_W_Entry = Entry(ctOS_os_Walk)  # This is where you enter the text file name (eg. ctOS-log-2803.txt)
    ctOS_os_W_Entry.grid(row=1, column=1)

    def submit():
        try:
            ctos_w_entry_text = ctOS_os_W_Entry.get()
            os_walk_log = open("os_Walk_Log.txt", "w")
            os_walk_log.write("File Path Issued: " + ctos_w_entry_text + "\n")
            os_walk_log.write("User that Issued Command: " + os.getlogin())
            os_walk_log.write("\n=========================")
            for dirpath, dirnames, filenames in os.walk(ctos_w_entry_text):
                os_walk_log.write("\nCurrent Path: " + str(dirpath))
                os_walk_log.write("\nDirectories: " + str(dirnames))
                os_walk_log.write("\nFiles: " + str(filenames))
                os_walk_log.write("\n=========================")
        except SyntaxError:  # This checks to see if you made a mistake and alerts you without pausing the program or outputing a huge error message on the python console
            print("Sorry this file is not found")
        except OSError:
            print("You have ran out of room")
    Button(ctOS_os_Walk, command=submit, bg='black', text="H:\Submit\..", fg='white', font=('Consolas', 10)).grid(row=2, column=1)
    # This close the os_stat window
    Button(ctOS_os_Walk, command=ctOS_os_Walk.destroy, bg='black', text="H:\Exit-2803\..", fg='white', font=('Consolas', 10)).grid(row=7, column=1)


def sys_copyright():
    ctOS_sys_Copyright = Toplevel(ctOS)
    ctOS_sys_Copyright.geometry("280x540")
    # ctOS_sys_Copyright.resizable(False, False)
    ctOS_sys_Copyright.configure(bg='black')
    Label(ctOS_sys_Copyright, text=sys.copyright, bg='black', fg='white', font=('Consolas', 5)).grid(row=0, column=0)


# This outputs the Blume logo on the main screen
ctOS_logo = PhotoImage(file='H:\ctOS\images\ctOS-logo.png')
ctOS_logo_L = Label(ctOS, image=ctOS_logo, width='275', highlightbackground='black', highlightcolor='black', highlightthickness=1, compound=CENTER).grid(row=7, column=0, columnspan=2)

# Main Screen Buttons
list_dir = Button(ctOS, command=os_list_dir, bg='white', text="List-Dir", fg='black', font=('Consolas', 10), highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=3, column=0, pady=0, padx=0)
os_stat = Button(ctOS, command=os_stat, bg='white', text="os-Stat", fg='black', font=('Consolas', 10), highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=3, column=1, pady=0, padx=0)
os_walk = Button(ctOS, command=os_walk, bg='white', text="os-Walk", fg='black', font=('Consolas', 10), highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=4, column=0, pady=0, padx=0)
sys_copyright = Button(ctOS, command=sys_copyright, bg='white', text="sys-copyright", fg='black', font=('Consolas', 10), highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=4, column=1, pady=0, padx=0)
# This button closes the program down once finished
exit_2803 = Button(ctOS, command=ctOS.destroy, bg='black', text="H:\Exit-2803\...", fg='white', font=('Consolas', 10), highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=8, column=0, pady=10, padx=10)

ctOSLog_File.close()
# This runs the program and opens the program window
ctOS.mainloop()
# END OF CODE
