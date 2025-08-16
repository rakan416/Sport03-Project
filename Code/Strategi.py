from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from datetime import datetime
from tkinter.messagebox import *
import textwrap




class Formasi():

    def __init__(self, window):
        self.window = window
        self.window.state('zoomed')
        self.FRAME = Frame(self.window, bg='#093D83', width=1366, height=768)
        self.FRAME.place(x=0, y=0)
        foto = Image.open("Image/Background/bg_5.png").resize((1366,768))
        self.photoo = ImageTk.PhotoImage(foto)
        self.label_background = Label(self.FRAME, image=self.photoo)
        self.label_background.place(x=-2, y=-2)
        self.fr_lblket = CTkFrame(self.FRAME, fg_color='#060644', width=1326, height=70)
        self.fr_lblket.place(x=20, y=30)
        self.lbl_ketfor = CTkLabel(self.fr_lblket, text='REKOMENDASI FORMASI', font=('Times', 40), width=500, fg_color='#060644', text_color='#DBDBDB')
        self.lbl_ketfor.place(x=413, y=10)
        global img_close
        img_close = ImageTk.PhotoImage(Image.open('Image/close_icon.png').resize((50,50)))
        self.btt_closed = Button(self.fr_lblket, image=img_close,  command=lambda: self.prev(self.FRAME), bg='#060644', border=False, relief='flat', activebackground='#060644')
        self.btt_closed.place(x=5, y=10)
        self.fr_strategi = CTkFrame(self.FRAME, fg_color='#DBDBDB', width=1326, height=570)
        self.fr_strategi.place(x=20, y=100)
        fl = open('Data/data_formasi.txt', 'r')
        str_form = fl.read().split('\n\n')
        self.dt_formasi = []
        for form in str_form:
            frms = form.split('\n')
            imgopn = Image.open(frms[2]).resize((500,300))
            global gambar
            gambar = ImageTk.PhotoImage(imgopn)
            frms[2] = gambar
            self.dt_formasi.append(frms)

        x = 20
        y = 10
        for formasi in self.dt_formasi:
            self.summon_btt_formasi(self.fr_strategi, formasi[0], formasi[1], formasi[2], x, y)
            y += 80
            if y > 490:
                y = 10
                x = 686


        
    def summon_btt_formasi(self, fr, dt, ket, gambar, x_pos, y_pos):

        def keterangan():
            self.Detail_formasi(dt, ket, gambar)

        btt_form = CTkButton(fr, text=dt, width=620, height=70, command=keterangan, fg_color='#DBDBDB', border_color='black', hover_color='#AAB0E9', border_width=5, text_color='Black', font=('Times', 30, 'bold'))
        btt_form.place(x=x_pos, y=y_pos)


    def Detail_formasi(self, dt, ket, gmbr):
        self.fr_submain1 = Frame(self.FRAME, bg='black')
        self.fr_submain1.place(x=0, y=0, width=1366, height=768)
        self.label_background1 = Label(self.fr_submain1, image=self.photoo)
        self.label_background1.place(x=-2, y=-2)
        self.fr_keterangan = CTkFrame(self.fr_submain1, fg_color='#DBDBDB', width=1326, height=630)
        self.fr_keterangan.place(x=20, y=30)
        self.fr_tulisan = CTkFrame(self.fr_keterangan, fg_color='#DBDBDB', width=760, height=585)
        self.fr_tulisan.place(x=546, y=20)
        self.lbl_gambar = Label(self.fr_keterangan, image=gmbr)
        self.lbl_gambar.place(x=30, y=165)
        self.lbl_title = Label(self.fr_tulisan, text=dt, font=('Times', 32, 'bold'), anchor='w', bg='#DBDBDB')
        self.lbl_title.place(x=10, y=10)
        text = textwrap.fill(ket, width=70)
        self.lbl_detail = Label(self.fr_tulisan, text=text, font=('Times', 18), anchor='w', justify='left', bg='#DBDBDB')
        self.lbl_detail.place(x=10, y=80)
        link_source = 'https://www.idntimes.com/sport/soccer/yogama-wisnu-oktyandito/formasi-sepak-bola-lengkap-dengan-penjelasan-dan-contohnya'
        self.lbl_source = Label(self.fr_tulisan, text=link_source, bg='#DBDBDB')
        self.lbl_source.place(x=10, y=550)
        global img_back
        img_back = ImageTk.PhotoImage(Image.open('Image/back_logo.png').resize((50,50)))
        self.btt_back = Button(self.fr_keterangan, text='', image=img_back, command=lambda: self.prev(self.fr_submain1), bg='#DBDBDB', border=False, relief='flat', activebackground='#DBDBDB')
        self.btt_back.place(x=5, y=5, width=55, height=55)

    def prev(self, fr):
        fr.destroy()
        

# w = Tk()
# Formasi(w)
# w.mainloop()