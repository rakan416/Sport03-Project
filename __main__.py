from tkinter import *
from customtkinter import *
from tkinter.messagebox import askokcancel,showerror, showinfo
from PIL import Image, ImageTk
import pickle
from Tree_Processing import TreeNode
from Code.Input_data import Input_Data
from Code.Menu import Menu


class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Log In")
        self.master.state('zoomed')
        fl = open('Data/treeDatabase.pickle','rb')
        self.tr_var = pickle.load(fl)
        self.tr_var.print_tree()

        def on_closing():
                if askokcancel("Quit?", "Do you want to quit?"):
                    master.destroy()
        master.protocol("WM_DELETE_WINDOW", on_closing)

        self.FRAME = Frame(self.master, bg='black')
        self.FRAME.pack(expand=True)

        self.foto=Image.open("Image/sign in.png").resize((1366,768))
        self.photoo=ImageTk.PhotoImage(self.foto)
        label_background = Label(self.FRAME, image=self.photoo)
        label_background.pack(fill=BOTH, expand=YES)
        label_background.photo = self.photoo

        self.name = Entry(self.FRAME, width=30, fg='black', border=0, bg='#B3B1B1', font=('Microsoft Yahei UI Light', 13))
        self.name.place(x=894, y=295)

        self.code = Entry(self.FRAME, width=30, fg='black', border=0, bg='#B3B1B1', font=('Microsoft Yahei UI Light', 13))
        self.code.place(x=894, y=378)

        self.SignIn = Button(self.FRAME, width=10, text="Send", border=0, bg='#EF6B48', activebackground='#EF6B48', cursor='hand2', fg='White', font=('Microsoft Yahei UI Light', 13),
                         command= self.signin)
        self.SignIn.place(x=975, y=450)

        self.SignUplabel = Label(self.FRAME, width=20, text="Don't Have An Account?", border=0, bg='white', fg="black",font=('Helvetica 12 bold'))
        self.SignUplabel.place(x=105,y=258)

        self.SignUp = Button(self.FRAME, width=6, text='Register', border=0, bg='white', cursor='hand2', fg="#57a1f8",font=('Helvetica 12 bold'),command=self.signup_command)
        self.SignUp.place(x=305,y=255)

    def signin(self):
        username = self.name.get()
        password = self.code.get()

        for i in range(len(self.tr_var.child)):
            un = self.tr_var.child[i].data[0]
            pw = self.tr_var.child[i].data[1]
            if username == un and password == pw:
                self.homepage(self.tr_var.child[i],self.tr_var)
                return
        else:
            showerror('Invalid', 'Invalid username and password')

    def homepage(self, acc, root):
        self.FRAME.destroy()
        if acc.child == []:
            Input_Team(self.master, acc, root)
        else:
            Menu(self.master, acc.child[0], root)


    def signup_command(self):
        self.window = Frame(self.master)
        self.window.place(x=-2,y=-2)
        
        self.foto=Image.open("Image/sign up.png").resize((1366,768))
        self.photoo=ImageTk.PhotoImage(self.foto)
        label_background = Label(self.window, image=self.photoo)
        label_background.pack()
        label_background.photo = self.photoo

        def sign_up():
            username_signup = self.name2.get()
            password_signup = self.code2.get()
            confirm_password = self.confirm_code.get()
            if password_signup == confirm_password:
                if self.tr_var.child == []:
                    temp_1 = TreeNode([username_signup,password_signup])
                    self.tr_var.add_child(temp_1)
                else:
                    for i in range(len(self.tr_var.child)):
                        un = self.tr_var.child[i].data[0]
                        pw = self.tr_var.child[i].data[1]
                        if username_signup == un:
                            showerror('Invalid', 'Username sudah digunakan')
                            return
                    temp_1 = TreeNode([username_signup,password_signup])
                    self.tr_var.add_child(temp_1)
                fl = open('Data/treeDatabase.pickle','wb')
                pickle.dump(self.tr_var,fl)
                showinfo('Sign Up', 'Successfully sign up!')
                sign()

            else:
                showerror('Invalid', 'Both Password Should Match')

        def sign():
            self.window.destroy()
            self.homepage(self.tr_var.child[-1],self.tr_var)

        def back():
            self.window.destroy()

        self.name2 = Entry(self.window, width=30, fg='black', border=0, bg='#B3B1B1', font=('Microsoft Yahei UI Light', 13))
        self.name2.place(x=894, y=283)

        self.code2 = Entry(self.window, width=30, fg='black', border=0, bg='#B3B1B1', font=('Microsoft Yahei UI Light', 13))
        self.code2.place(x=894, y=371)

        self.confirm_code = Entry(self.window, width=30, fg='black', border=0, bg='#B3B1B1', font=('Microsoft Yahei UI Light', 13))
        self.confirm_code.place(x=894, y=458)


        Button(self.window, width=13, pady=10, text='Send', bg='#EF6B48', fg='white',
               activebackground='#EF6B48', font=('Microsoft Yahei UI Light', 13), border=0, command=sign_up, cursor='hand2').place(x=962, y=530, height=30)

        self.SignIn = Button(self.window, width=4, text="Login", border=0, bg='white', cursor='hand2', fg='#57a1f8',font=('Helvetica 14 bold'),
                         command=back)
        self.SignIn.place(x=320, y=300)

class Input_Team:
    def __init__(self,window, acc, root):
        self.window = window
        window.title("Team Name")
        window.state('zoomed')
        self.tr_var = root
        self.user = acc
        if self.user.child != []:
            Input_Data(self.window, 1366, 768, self.user.child[0], self.tr_var)
            return
        self.FRAME = Frame(self.window, bg='#0E4186')
        self.FRAME.place(x=0, y=0, width=1366, height=768)
        global img1
        img1 = ImageTk.PhotoImage(Image.open('Image/Background/bg_1.png').resize((1366,768)))
        self.bg = Label(self.FRAME, image=img1, bg='#0E4186')
        self.bg.place(x=-2, y=-1)
        self.bg = Label(self.FRAME,text='Masukkan Nama Tim Anda', bg='#0E4186', fg='white', font=('Bookman Old Style',23))
        self.bg.place(x=433, y=302, width=500)
        self.inp1 = CTkEntry(self.FRAME, width=420, height=50, fg_color='#DBDBDB', bg_color='#0E4186', border_width=0, corner_radius=90, font=('Roboto',20,'bold'))
        self.inp1.place(x=473, y=360)
        self.btt_confirm = CTkButton(self.FRAME, text='CONFIRM', width=170, height=45, command=self.confirm, font=('Bookman Old Style',20), bg_color='#0E4186', fg_color='#060644', border_width=0, corner_radius=90)
        self.btt_confirm.place(x=598, y=430)

    def confirm(self):
        name = self.inp1.get()
        team = TreeNode(name)
        team.add_child(TreeNode('Players'))
        team.add_child(TreeNode('Latihan'))
        team.add_child(TreeNode('Pertandingan'))
        self.user.add_child(team)
        self.FRAME.destroy()
        fl = open('Data/treeDatabase.pickle', 'wb')
        pickle.dump(self.tr_var, fl)
        fl.close()
        Menu(self.window, team, self.tr_var)



top = Tk()
gui = LoginPage(top)
top.mainloop()
