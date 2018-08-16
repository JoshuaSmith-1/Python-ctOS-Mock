# START OF CODE
import os
from tkinter import *
from datetime import datetime
import time
import sys
# The current time
readable = datetime.now().strftime('%d-%m-%Y %j, %I:%M:%S')

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

# This outputs the current working drive and the current time and day of the week at the top of the screen
os_get_cwd = Label(ctOS, text=os.getcwd(), bg='black', fg='white', font=('Consolas', 10)).grid(row=0, column=0, columnspan=2)
# sys_version = Label(ctOS, text=sys.version, bg='black', fg='white', font=('Consolas', 10)).grid(row=1, column=0)
os_get_login = Label(ctOS, text=os_login, bg='black', fg='white', font=('Consolas', 10)).grid(row=1, column=0, columnspan=2)
time_t = Label(ctOS, text=readable, bg='black', fg='white', font=('Consolas', 10)).grid(row=2, column=0, columnspan=2)


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
    ctOS_Login = Toplevel(ctOS)
    ctOS_Login.geometry("280x300")
    ctOS_Login.resizable(False, False)
    ctOS_Login.configure(bg='black')
    ctOS_U_Entry = Entry(ctOS_Login)
    ctOS_U_Entry.grid(row=1, column=1)
    Username = Label(ctOS_Login, text="Username: ", bg='black', fg='white', font=('Consolas', 10))
    Username.grid(row=1, column=0)
    ctOS_P_Entry = Entry(ctOS_Login, show="*")
    ctOS_P_Entry.grid(row=2, column=1)
    Password = Label(ctOS_Login, text="Password: ", bg='black', fg='white', font=('Consolas', 10))
    Password.grid(row=2, column=0)

    def hint_subroutine():
        with open('H:\ctOS\Syst\CREDENTIALS.txt', 'r') as hint:
            hint_content = hint.readline()
            while hint_content != "":
                field = hint_content.split(",")
                UsernameHintField = field[0]
                hint_content = hint.readline()
                the_hint = "HINT:\nUsername: " + str(UsernameHintField)
                ctOS_Hint_L = Label(ctOS_Login, text=the_hint, bg='black', fg='white', font=('Consolas', 10))
                ctOS_Hint_L.grid(row=5, column=1)
        hint.close()

    def login_subroutine():
        user_text = ctOS_U_Entry.get()
        pass_text = ctOS_P_Entry.get()
        u_text = str(user_text)
        p_text = str(pass_text)
        with open('H:\ctOS\Syst\CREDENTIALS.txt', 'r') as f:
            f_content = f.readline()
            while f_content != "":
                field = f_content.split(",")
                UsernameField = field[0]
                PasswordField = field[1]
                if UsernameField == u_text:
                    pass
                if PasswordField == p_text:
                    ctOS_Login.destroy()
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
                        except SyntaxError:  # This checks to see if you made a mistake and alerts you without pausing the program or outputing a huge error message
                            print("Sorry this file is not found")
                        except OSError:
                            file_size_error = "You have ran out of space. " + "st-size=" + str(os.stat('os_Walk_Log.txt').st_size)
                            Error_Message = Label(ctOS_os_Walk, text=file_size_error, font=('Consolas', 10), bg='white')
                            Error_Message.grid(row=3, column=1)
                    Button(ctOS_os_Walk, command=submit, bg='black', text="H:\Submit\..", fg='white', font=('Consolas', 10)).grid(row=2, column=1)
                    # This close the os_stat window
                    Button(ctOS_os_Walk, command=ctOS_os_Walk.destroy, bg='black', text="H:\Exit-2803\..", fg='white', font=('Consolas', 10)).grid(row=7, column=1)

                l_error = 'Sorry you have done this incorrectly!'
                if u_text != UsernameField and p_text == "":
                    Error_Message = Label(ctOS_Login, text=l_error, bg='black', fg='red', font=('Consolas', 10))
                    Error_Message.grid(row=5, column=1)
                if p_text != PasswordField and u_text == "":
                    Error_Message = Label(ctOS_Login, text=l_error, bg='black', fg='blue', font=('Consolas', 10))
                    Error_Message.grid(row=6, column=1)
                f_content = f.readline()
        f.close()
    Button(ctOS_Login, command=ctOS_Login.destroy, bg='black', text="H:\Exit-2803\..", fg='white', font=('Consolas', 10)).grid(row=3, column=1)
    Login = Button(ctOS_Login, command=login_subroutine, text="H:\Login\..")
    Login.grid(row=3, column=0)
    Hint = Button(ctOS_Login, command=hint_subroutine, text="H:\Hint\...")
    Hint.grid(row=4, column=0)



def sys_copyright():
    ctOS_sys_Copyright = Toplevel(ctOS)
    ctOS_sys_Copyright.geometry("280x540")
    # ctOS_sys_Copyright.resizable(False, False)
    ctOS_sys_Copyright.configure(bg='black')
    Label(ctOS_sys_Copyright, text=sys.copyright, bg='black', fg='white', font=('Consolas', 5)).grid(row=0, column=0)


# This outputs the Blume logo on the main screen
ctOS_logo = PhotoImage(file='H:\ctOS\images\WatchDogs-logo.png')
ctOS_logo_L = Label(ctOS, image=ctOS_logo, width='275', bg='black', highlightbackground='black', highlightcolor='black', highlightthickness=1, compound=CENTER).grid(row=7, column=0, columnspan=2)

list_dir_photo = PhotoImage(file="H:\ctOS\images\ctOS-logo-white.png")
os_stat_photo = PhotoImage(file="H:\ctOS\images\ctOS-logo-white.png")
os_walk_photo = PhotoImage(file="H:\ctOS\images\ctOS-logo-white.png")
sys_copyR_photo = PhotoImage(file="H:\ctOS\images\ctOS-logo-white.png")

# Main Screen Buttons
try:
    list_dir = Button(ctOS, command=os_list_dir, bg='black', highlightbackground='black', highlightcolor='black', highlightthickness=1, image=list_dir_photo).grid(row=3, column=0, pady=0, padx=0)
    ctOS_logo_L = Label(ctOS, text="os_List", bg='black', fg='white', font=('Consolas', 10)).grid(row=4, column=0)
    os_stat = Button(ctOS, command=os_stat, bg='black', highlightbackground='black', highlightcolor='black', highlightthickness=1, image=os_stat_photo).grid(row=3, column=1, pady=0, padx=0)
    ctOS_logo_L = Label(ctOS, text="os_Stat", bg='black', fg='white', font=('Consolas', 10)).grid(row=4, column=1)
    os_walk = Button(ctOS, command=os_walk, bg='black', highlightbackground='black', highlightcolor='black', highlightthickness=1, image=os_walk_photo).grid(row=5, column=0, pady=0, padx=0)
    ctOS_logo_L = Label(ctOS, text="os_Walk", bg='black', fg='white', font=('Consolas', 10)).grid(row=6, column=0)
    sys_copyright = Button(ctOS, command=sys_copyright, bg='black', highlightbackground='black', highlightcolor='black', highlightthickness=1, image=sys_copyR_photo).grid(row=5, column=1, pady=0, padx=0)
    ctOS_logo_L = Label(ctOS, text="sys_Copyright", bg='black', fg='white', font=('Consolas', 10)).grid(row=6, column=1)
except AttributeError as e:
    print(e)
# This button closes the program down once finished
exit_2803 = Button(ctOS, command=ctOS.destroy, bg='black', text="H:\Exit-2803\...", fg='white', font=('Consolas', 10), highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=8, column=0, pady=10, padx=10)

ctOSLog_File.close()
# This runs the program and opens the program window
ctOS.mainloop()
# END OF CODE
