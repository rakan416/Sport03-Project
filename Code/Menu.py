from tkinter import *
from PIL import ImageTk, Image
import pickle
from Code.Menu_Analisa import AnaliticMenu
from Code.Strategi import Formasi
from Code.Menu_Players import PlayersManagement
from Code.Menu_Schedule import JadwalPertandinganLatihan
from Code.Input_data import Input_Data


class Menu:
        def __init__(self, window, tim, root):
                self.window = window
                self.tim = tim
                self.tr_var = root

                self.FRAME = Frame(self.window, bg='black', width=1366, height=768)
                self.FRAME.place(x=0, y=0)
                bg_image = ImageTk.PhotoImage(Image.open('Image/Background/bg_2.png').resize((1366, 768)))
                self.bg_label = Label(self.FRAME, image=bg_image)
                self.bg_label.image = bg_image
                self.bg_label.place(x=-2, y=-2, relwidth=1, relheight=1)
                self.lbl_manjp = Label(self.FRAME, bg='#093D83', text=f'Welcome,\n{self.tim.data}', font=('Times', 25, 'bold'), fg="white", anchor='w', justify='left')
                self.lbl_manjp.place(x=75, y=75)


                global img1
                img1 = ImageTk.PhotoImage(Image.open('Image/manplayer.png').resize((135,120)))
                self.Button_menu1 = Button(self.FRAME,cursor='hand2', activebackground='#093D83', command=self.manajemen_player, image=img1, bg='#093D83', relief='flat', borderwidth=0)
                self.Button_menu1.place(x=465,y=520)
                self.lbl_manjp = Label(self.FRAME, bg='#093D83', text='Manajemen Pemain', font=('Bookman Old Style', 12), fg="white")
                self.lbl_manjp.place(x=453, y=645, width=160, height=30)

                global img2
                img2 = ImageTk.PhotoImage(Image.open('Image/jadwal.png').resize((120,120)))
                self.Button_menu2 = Button(self.FRAME,cursor='hand2', activebackground='#093D83', command=self.jadwal, image=img2, bg='#093D83', relief='flat', borderwidth=0)
                self.Button_menu2.place( x=110,y=520)
                self.lbl_jadw = Label(self.FRAME, bg='#093D83', text='Jadwal', font=('Bookman Old Style', 12), fg="white")
                self.lbl_jadw.place(x=110, y=645, width=120, height=30)
          
                global img3
                img3 = ImageTk.PhotoImage(Image.open('Image/analisa.png').resize((120,120)))
                self.Button_menu4 = Button(self.FRAME,cursor='hand2', activebackground='#093D83', command=self.analisis_player, image=img3, bg='#093D83', relief='flat', borderwidth=0)
                self.Button_menu4.place(x=470,y=280)
                self.lbl_anls = Label(self.FRAME, bg='#093D83', text='Analisa Pemain', font=('Bookman Old Style', 12), fg="white")
                self.lbl_anls.place(x=470, y=405, width=120, height=30)

                global img4
                img4 = ImageTk.PhotoImage(Image.open('Image/strategi.png').resize((180,120)))
                self.Button_menu3 = Button(self.FRAME,cursor='hand2', activebackground='#093D83', command=self.strategi, image=img4, bg='#093D83', relief='flat', borderwidth=0)
                self.Button_menu3.place(x=85,y=280)
                self.lbl_strg = Label(self.FRAME, bg='#093D83', text='Strategi', font=('Bookman Old Style', 12), fg="white")
                self.lbl_strg.place(x=85, y=405, width=180, height=30)

                if len(self.tim.child[0].child) == 0:
                        Input_Data(self.FRAME, 1366, 768, self.tim, self.tr_var, 0)

        
        def manajemen_player(self):
                PlayersManagement(self.window, self.tim, self.tr_var)

        def jadwal(self):
                JadwalPertandinganLatihan(self.window, self.tim, self.tr_var)

        def analisis_player(self):
                AnaliticMenu(self.window, self.tim, self.tr_var)
        
        def strategi(self):
                Formasi(self.window)


# w = Tk()
# fl = open('Data/treeDatabase.pickle', 'rb')
# tree_data = pickle.load(fl)
# fl.close()
# Menu(w, tree_data.child[0].child[0], tree_data)
# w.mainloop()