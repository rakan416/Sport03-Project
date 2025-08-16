from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import pickle
from datetime import datetime
from tkinter.messagebox import *
from Tree_Processing import TreeNode



class AddDataMatch():

    def __init__(self, window, tim_data, root, data_match):
        self.window = window
        self.tim = tim_data
        self.tr_var = root
        self.match = data_match
        # self.window.state('zoomed')
        self.FRAME = Frame(self.window, bg='#093D83', width=1366, height=768)
        self.FRAME.place(x=0, y=0)
        foto = Image.open("Image/Background/bg_1.png").resize((1366, 768))
        self.photoo = ImageTk.PhotoImage(foto)
        self.label_background = Label(self.FRAME, image=self.photoo)
        self.label_background.place(x=-2, y=-2)
        self.fr1 = CTkFrame(self.FRAME, fg_color='#060644', width=1100, height=570)
        self.fr1.place(x=133, y=50)
        self.lbl_ketlstptd = Label(self.fr1, text='Pilih Pertandingan', font=('Times', 30, 'bold'), fg='white', bg='#060644')
        self.lbl_ketlstptd.place(x=300, y=0, width=500, height=70)
        self.scfr1 = CTkScrollableFrame(self.fr1, fg_color='#DBDBDB', width=1083, height=500, corner_radius=0)
        self.scfr1.place(x=0, y=70)
        rw = 0
        if self.match != []:
            for dt in self.match:
                self.summon_btt_match(fr=self.scfr1,data=dt, rw=rw)
                rw += 1
        global img_return0
        img_return0 = ImageTk.PhotoImage(Image.open('Image/return.png').resize((110, 50)))
        self.button_back = Button(self.FRAME, image=img_return0, cursor="hand2", command=lambda : self.FRAME.destroy(), bg='#093D83', relief='flat', borderwidth=0, activebackground='#093D83')
        self.button_back.place(x=35, y=645)


    def summon_btt_match(self, fr, data, rw):

        def pencet(e):
            self.pilih_pemain_inti(data=data)

        def masuk(e):
            fr_btt.configure(border_width=5)

        def keluar(e):
            fr_btt.configure(border_width=2)

        fr_btt = CTkFrame(master=fr, fg_color='white', border_color='black', border_width=3, width=1045, height=80)
        fr_btt.grid(column=0, row=rw, pady=10, padx=20)
        lbl_tgl = Label(fr_btt, text=data[0], fg='black', bg='white', font=('Times', 18, 'bold'))
        lbl_tgl.place(x=20, y=10, width=130)
        lbl_jam = Label(fr_btt, text=data[1], fg='black', bg='white', font=('Times', 13, 'bold'))
        lbl_jam.place(x=20, y=40, width=130)
        lbl_vs = Label(fr_btt, text='VS', fg='black', bg='white', font=('Times', 20, 'bold'))
        lbl_vs.place(x=(1045/2)-35, y=5, width=70, height=70)
        lbl_mine = Label(fr_btt, text=self.tim.data.upper(), fg='black', bg='white', font=('Times', 32, 'bold'),anchor='e')
        lbl_mine.place(x=(1045/2)-300, y=5, width=250, height=70)
        lbl_musuh = Label(fr_btt, text=data[2].upper(), fg='black', bg='white', font=('Times', 32, 'bold'), anchor='w')
        lbl_musuh.place(x=(1045/2)+50, y=5, width=250, height=70)

        fr_btt.bind('<Button-1>', pencet)
        lbl_tgl.bind('<Button-1>', pencet)
        lbl_jam.bind('<Button-1>', pencet)
        lbl_vs.bind('<Button-1>', pencet)
        lbl_mine.bind('<Button-1>', pencet)
        lbl_musuh.bind('<Button-1>', pencet)
        fr_btt.bind('<Enter>', masuk)
        fr_btt.bind('<Leave>', keluar)
        lbl_tgl.bind('<Enter>', masuk)
        lbl_tgl.bind('<Leave>', keluar)
        lbl_jam.bind('<Enter>', masuk)
        lbl_jam.bind('<Leave>', keluar)
        lbl_vs.bind('<Enter>', masuk)
        lbl_vs.bind('<Leave>', keluar)
        lbl_mine.bind('<Enter>', masuk)
        lbl_mine.bind('<Leave>', keluar)
        lbl_musuh.bind('<Enter>', masuk)
        lbl_musuh.bind('<Leave>', keluar)
        
    def pilih_pemain_inti(self, data):

        def lanjut():
            if len(self.plycore_choosed) >= 1:
                self.pilih_pemain_cadangan(data)
            else: showerror('Invalid Input', 'Pilihan harus berjumlah 11 Pemain')

        self.plycore_choosed = []
        self.fr_main2 = Frame(self.FRAME, bg='#093D83', width=1366, height=768)
        self.fr_main2.place(x=0, y=0)
        self.bg2 = Label(self.fr_main2, image=self.photoo)
        self.bg2.place(x=-2, y=-2)
        self.fr2 = CTkFrame(self.fr_main2, fg_color='#060644', width=960, height=570)
        self.fr2.place(x=203, y=50)
        self.lbl_11 = Label(self.fr2, text='Pilih 11 Pemain Inti', font=('Times', 30, 'bold'), bg='#060644', fg='white')
        self.lbl_11.place(x=100, y=0, width=760, height=70)
        self.scfr2 = CTkScrollableFrame(self.fr2, fg_color='#DBDBDB', width=943, height=500, corner_radius=0)
        self.scfr2.place(x=0, y=70)
        rw = 0
        for player in self.tim.child[0].child:
            self.summon_plyr(self.scfr2, player, rw, 0, status=self.plycore_choosed)
            rw += 1
        self.btt_next1 = CTkButton(self.fr_main2, text='NEXT', width=190, height=60,font=('Times', 32, 'bold'), command=lanjut)
        self.btt_next1.place(x=1075, y=640)
        self.btt_prev1 = CTkButton(self.fr_main2, text='PREV', width=190, height=60,font=('Times', 32, 'bold'), command=lambda: self.prev(self.fr_main2))
        self.btt_prev1.place(x=105, y=640)

    def pilih_pemain_cadangan(self, data):
        
        def lanjut():
            if len(self.plycdgn_choosed) <= 15:
                self.entry_sta1(data)
            else: showerror('Invalid Input', 'Pilihan maksimal berjumlah 11 Pemain')

        self.plycdgn_choosed = []
        self.fr_main3 = Frame(self.FRAME, bg='#093D83', width=1366, height=768)
        self.fr_main3.place(x=0, y=0)
        self.bg3 = Label(self.fr_main3, image=self.photoo)
        self.bg3.place(x=-2, y=-2)
        self.fr3 = CTkFrame(self.fr_main3,fg_color='#060644', width=960, height=570)
        self.fr3.place(x=203, y=50)
        self.lbl_15 = Label(self.fr3, text='Pilih Pemain Cadangan', font=('Times', 30, 'bold'), bg='#060644', fg='white')
        self.lbl_15.place(x=100, y=0, width=760, height=70)
        self.scfr3 = CTkScrollableFrame(self.fr3, fg_color='#DBDBDB', width=943, height=500, corner_radius=0)
        self.scfr3.place(x=0, y=70)
        rw = 0
        for player in self.tim.child[0].child:
            if player.data[0] in self.plycore_choosed:
                continue
            self.summon_plyr(self.scfr3, player, rw, 0, status=self.plycdgn_choosed)
            rw += 1
        self.btt_next1 = CTkButton(self.fr_main3, text='NEXT', width=190, height=60,font=('Times', 32, 'bold'), command=lanjut)
        self.btt_next1.place(x=1075, y=640)
        self.btt_prev1 = CTkButton(self.fr_main3, text='PREV', width=190, height=60,font=('Times', 32, 'bold'), command=lambda: self.prev(self.fr_main3))
        self.btt_prev1.place(x=105, y=640)

    def entry_sta1(self, data):
        self.fr_main4 = Frame(self.FRAME, bg='#093D83', width=1366, height=768)
        self.fr_main4.place(x=0, y=0)
        self.bg4 = Label(self.fr_main4, image=self.photoo)
        self.bg4.place(x=-2, y=-2)
        self.fr_inp_goal = CTkFrame(self.fr_main4, fg_color='white', width=600, height=75)
        self.fr_inp_goal.place(x=70, y=350)
        self.fr_inp_card = CTkFrame(self.fr_main4, fg_color='white', width=600, height=75)
        self.fr_inp_card.place(x=710, y=350)
        self.lbl_tim1 = Label(self.fr_inp_goal, text=self.tim.data.upper(), bg='white', fg='black', font=('Times', 20, 'bold'))
        self.lbl_tim1.place(x=20, y=15, width=165)
        self.lbl_tim2 = Label(self.fr_inp_goal, text=data[-1], bg='white', fg='black', font=('Times', 20, 'bold'))
        self.lbl_tim2.place(x=415, y=15, width=165)
        self.inp_gol1 = CTkEntry(self.fr_inp_goal, width=45, height=50, corner_radius=90,font=('times',20,'bold'), fg_color='white')
        self.inp_gol1.place(x=200, y=15)
        self.inp_gol2 = CTkEntry(self.fr_inp_goal, width=45, height=50, corner_radius=90, font=('times',20,'bold'), fg_color='white')
        self.inp_gol2.place(x=355, y=15)
        
        self.lbl_ycard = Label(self.fr_inp_card, text='YELLOW CARD', bg='white', fg='black', font=('Times', 15, 'bold'))
        self.lbl_ycard.place(x=20, y=15, width=165, height=40)
        self.lbl_rcard = Label(self.fr_inp_card, text='RED CARD', bg='white', fg='black', font=('Times', 15, 'bold'))
        self.lbl_rcard.place(x=415, y=15, width=165, height=40)
        self.inp_card1 = Entry(self.fr_inp_card,font=('times',20,'bold'), bg='yellow', justify='center')
        self.inp_card1.place(x=200, y=10, width=45, height=50)
        self.inp_card2 = Entry(self.fr_inp_card, font=('times',20,'bold'), bg='red', justify=CENTER)
        self.inp_card2.place(x=355, y=10, width=45, height=50)

        def ok():
            if self.inp_gol1.get() == '':
                self.mygoal = 0
            else:
                try:
                    self.mygoal = int(self.inp_gol1.get())
                except:
                    showerror('Invalid Input', 'Masukkan hanya angka')
                    return
                
            if self.inp_gol2.get() == '':
                self.enmgoal = 0
            else:
                try:
                    self.enmgoal = int(self.inp_gol2.get())
                except:
                    showerror('Invalid Input', 'Masukkan hanya angka')
                    return

            if self.inp_card1.get() == '':
                self.kuning = 0
            else:
                try:
                    self.kuning = int(self.inp_card1.get())
                except:
                    showerror('Invalid Input', 'Masukkan hanya angka')
                    return

            if self.inp_card2.get() == '':
                self.merah = 0
            else:
                try:
                    self.merah = int(self.inp_card2.get())
                except:
                    showerror('Invalid Input', 'Masukkan hanya angka')
                    return
            self.btt_ok1.destroy()
            if self.mygoal > 0:
                self.geser_ver(self.fr_inp_goal, 'atas', 350, 30)
                self.window.after(1000, lambda: self.pencetak_gol(self.mygoal))
            if self.kuning+self.merah > 0:
                self.geser_ver(self.fr_inp_card, 'atas', 350, 30)
                self.window.after(1000, lambda: self.pencetak_kartu(self.kuning, self.merah))
            if self.mygoal + self.kuning + self.merah == 0:
                self.entry_sta2(data)
            self.inp_card1.configure(state='disabled')
            self.inp_card2.configure(state='disabled')
            self.inp_gol1.configure(state='disabled')
            self.inp_gol2.configure(state='disabled')


        def lanjut():
            temp = 0
            if self.mygoal == 0:
                temp+=1
            elif self.dt_goal != []:
                g = 0
                for gl in self.dt_goal:
                    g += int(gl[1])
                if g == self.mygoal:
                    temp += 1
                else:
                    showerror('Input Tidak Sesuai', 'Mohon Dicek Kembali!') 
                    return
            elif self.mygoal > 0 and self.dt_goal == []:
                showerror('Input Tidak Sesuai', 'Mohon Dicek Kembali!')
                return


            kng = 0
            mrh = 0
            if self.kuning == 0 and self.merah == 0:
                temp+=1
            elif self.dt_card != []:
                for cr in self.dt_card:
                    kng += int(cr[1])
                    mrh += int(cr[2])
                if kng == self.kuning and mrh == self.merah:
                    temp += 1
                else:
                    showerror('Input Tidak Sesuai', 'Mohon Dicek Kembali!')
                    return
            else:
                showerror('Input Tidak Sesuai', 'Mohon Dicek Kembali!')
                return
            if temp >= 2:
                self.entry_sta2(data)
            else:
                showerror('Input Tidak Sesuai', 'Mohon Dicek Kembali!')
                return

            

        self.btt_ok1 = CTkButton(self.fr_main4, text='OK', width=80, height=30, command=ok)
        self.btt_ok1.place(x=(1366/2)-40, y= 600)
        self.btt_next3 = CTkButton(self.fr_main4, text='NEXT', width=190, height=60,font=('Times', 32, 'bold'), command=lanjut)
        self.btt_next3.place(x=1075, y=640)
        self.btt_prev3 = CTkButton(self.fr_main4, text='PREV', width=190, height=60,font=('Times', 32, 'bold'), command=lambda: self.prev(self.fr_main4))
        self.btt_prev3.place(x=105, y=640)

    def entry_sta2(self, data):
        self.fr_main5 = Frame(self.FRAME, bg='#093D83', width=1366, height=768)
        self.fr_main5.place(x=0, y=0)
        self.bg5 = Label(self.fr_main5, image=self.photoo)
        self.bg5.place(x=-2, y=-2)
        self.fr_idk1 = CTkFrame(self.fr_main5, fg_color='#060644', width=1100, height=570)
        self.fr_idk1.place(x=133, y=40)
        self.lbl_ketsta2 = Label(self.fr_idk1, bg='#060644', fg="white", text="Data Pertandingan", font=('Times', 25, 'bold'))
        self.lbl_ketsta2.place(x=50, y=0, width=1000, height=70)
        self.fr_inp_sta2 = CTkFrame(self.fr_idk1, fg_color='#DBDBDB', width=1100, height=495)
        self.fr_inp_sta2.place(x=0, y=70)
        self.fr_sld1 = CTkFrame(self.fr_inp_sta2, fg_color='white', border_color='black', border_width=3, width=530, height=130)
        self.fr_sld1.place(x=10, y=50)
        self.fr_sld2 = CTkFrame(self.fr_inp_sta2, fg_color='white', border_color='black', border_width=3, width=530, height=130)
        self.fr_sld2.place(x=560, y=50)
        self.fr_shot = CTkFrame(self.fr_inp_sta2, fg_color='white', border_color='black', border_width=3, width=530, height=220)
        self.fr_shot.place(x=10, y=240)
        self.fr_warn = CTkFrame(self.fr_inp_sta2, fg_color='white', border_color='black', border_width=3, width=530, height=130)
        self.fr_warn.place(x=560, y=285)

        self.lbl_sld1 = Label(self.fr_sld1, text='PERSENTASE PENGUASAAN BOLA', bg='white', fg='#060644', font=('Times', 20, 'bold'), anchor='w')
        self.lbl_sld1.place(x=5, y=5)
        self.sld_1 = CTkSlider(self.fr_sld1, from_=0, to=100, width=470, command= lambda val: self.sliding(val, self.num1), border_width=0, button_color='purple', progress_color='#060644')
        self.sld_1.place(x=30, y=60)
        self.sld_1.set(0)
        self.num1 = Label(self.fr_sld1, text='0 %', bg='white', fg='#060644', anchor='center', font=('Bookman Old Style', 20, 'bold'))
        self.num1.place(x=230, y=95, width=70, height=30)

        self.lbl_sld2 = Label(self.fr_sld2, text='PERSENTASE KETEPATAN UMPAN', bg='white', fg='#060644', font=('Times', 20, 'bold'), anchor='w')
        self.lbl_sld2.place(x=5, y=5)
        self.sld_2 = CTkSlider(self.fr_sld2, from_=0, to=100, width=470, command= lambda val: self.sliding(val, self.num2), border_width=0, button_color='purple', progress_color='#060644')
        self.sld_2.place(x=30, y=60)
        self.sld_2.set(0)
        self.num2 = Label(self.fr_sld2, text='0 %', bg='white', fg='#060644', anchor='center', font=('Bookman Old Style', 20, 'bold'))
        self.num2.place(x=230, y=95, width=70, height=30)

        self.lbl_shot1 = Label(self.fr_shot, text='Total Tembakan Akurat', bg='white', fg='#060644', font=('Times', 20, 'bold'))
        self.lbl_shot1.place(x=5, y=5, width=520)
        self.num3 = Label(self.fr_shot, text=0, bg='white', fg='#060644', font=('Bookman Old Style', 25, 'bold'))
        self.num3.place(x=240, y=45, width=50, height=50)
        self.bttplus_shot1 = CTkButton(self.fr_shot, text='+', width=50, height=50, command= lambda: self.tambah(self.num3, 50), font=('Bookman Old Style', 30, 'bold'), fg_color="white", text_color='#060644', border_color='#060644', border_width=3, hover_color="purple")
        self.bttplus_shot1.place(x=290, y=45)
        self.bttmin_shot1 = CTkButton(self.fr_shot, text='-', width=50, height=50, command= lambda: self.kurang(self.num3), font=('Bookman Old Style', 30, 'bold'), fg_color="white", text_color='#060644', border_color='#060644', border_width=3, hover_color="purple")
        self.bttmin_shot1.place(x=190, y=45)

        self.lbl_shot2 = Label(self.fr_shot, text='Total Tembakan Meleset', bg='white', fg='#060644', font=('Times', 20, 'bold'))
        self.lbl_shot2.place(x=5, y=115, width=520)
        self.num4 = Label(self.fr_shot, text='0', bg='white', fg='#060644', font=('Bookman Old Style', 25, 'bold'))
        self.num4.place(x=240, y=155, width=50, height=50)
        self.bttplus_shot2 = CTkButton(self.fr_shot, text='+', width=50, height=50, command= lambda: self.tambah(self.num4, 50), font=('Bookman Old Style', 30, 'bold'), fg_color="white", text_color='#060644', border_color='#060644', border_width=3, hover_color="purple")
        self.bttplus_shot2.place(x=290, y=155)
        self.bttmin_shot2 = CTkButton(self.fr_shot, text='-', width=50, height=50, command= lambda: self.kurang(self.num4), font=('Bookman Old Style', 30, 'bold'), fg_color="white", text_color='#060644', border_color='#060644', border_width=3, hover_color="purple")
        self.bttmin_shot2.place(x=190, y=155)

        self.lbl_warn = Label(self.fr_warn, text='Total Pelanggaran', bg='white', fg='#060644', font=('Times', 20, 'bold'))
        self.lbl_warn.place(x=5, y=5, width=520)
        self.num5 = Label(self.fr_warn, text='0', bg='white', fg='#060644', font=('Bookman Old Style', 25, 'bold'))
        self.num5.place(x=240, y=45, width=50, height=50)
        self.bttplus_warn = CTkButton(self.fr_warn, text='+', width=50, height=50, command= lambda: self.tambah(self.num5, 50), font=('Bookman Old Style', 30, 'bold'), fg_color="white", text_color='#060644', border_color='#060644', border_width=3, hover_color="purple")
        self.bttplus_warn.place(x=290, y=45)
        self.bttmin_warn = CTkButton(self.fr_warn, text='-', width=50, height=50, command= lambda: self.kurang(self.num5), font=('Bookman Old Style', 30, 'bold'), fg_color="white", text_color='#060644', border_color='#060644', border_width=3, hover_color="purple")
        self.bttmin_warn.place(x=190, y=45)

        self.btt_next4 = CTkButton(self.fr_main5, text='SAVE', width=190, height=60,font=('Times', 32, 'bold'), command=lambda: self.simpan(data))
        self.btt_next4.place(x=1075, y=640)
        self.btt_prev4 = CTkButton(self.fr_main5, text='PREV', width=190, height=60,font=('Times', 32, 'bold'), command=lambda: self.prev(self.fr_main5))
        self.btt_prev4.place(x=105, y=640)

    def sliding(self, val, num_lbl):
        num_lbl.configure(text=f'{int(val)} %')

    def pencetak_gol(self, gol):
        self.dt_goal = []
        self.fr_plygol = CTkFrame(self.fr_main4, width=600, height=470, fg_color='white')
        self.fr_plygol.place(x=70, y=140)
        self.lbl_ctkgol = Label(self.fr_plygol, text='PEMAIN PENCETAK GOL', font=("TImes", 32, 'bold'), bg='white')
        self.lbl_ctkgol.place(x=0, y=10, width=600, height=50)
        self.input_goal_players()

    def pencetak_kartu(self, kuning, merah):
        self.dt_card = []
        self.fr_plycard = CTkFrame(self.fr_main4, width=600, height=470, fg_color='white')
        self.fr_plycard.place(x=710, y=140)
        self.lbl_ctkcard = Label(self.fr_plycard, text='PEMAIN YANG MENDAPAT KARTU', font=("TImes", 24, 'bold'), bg='white')
        self.lbl_ctkcard.place(x=0, y=10, width=600, height=50)
        self.input_card_players()

    def update_goal(self, lbl_num, lbl_name):
        ply_name = lbl_name['text']
        goal = int(lbl_num['text'])
        if goal == 0:
            for j in range(len(self.dt_goal)):
                if ply_name in self.dt_goal[j]:
                    self.dt_goal.remove(self.dt_goal[j])
                    break
        elif goal > 0:
            itemp = 0
            for i in range(len(self.dt_goal)):
                if ply_name in self.dt_goal[i]:
                    self.dt_goal[i][1] = goal
                    itemp += 1
                    break
            if itemp == 0:
                self.dt_goal.append([ply_name, goal])

        self.input_goal_players()
        self.geser_hor(self.fr_scinp, 'kanan', -600, 0)

    def update_card(self, lbl_num1, lbl_num2, lbl_name):
        ply_name = lbl_name['text']
        ycard = int(lbl_num1['text'])
        rcard = int(lbl_num2['text'])
        if ycard > 2 or rcard > 1:
            showerror('Invalid Input', 'Max Yelllow card = 2\nMax Red card = 1')
            return
        if (ycard + rcard) > 0:
            itemp = 0
            for i in range(len(self.dt_card)):
                if ply_name in self.dt_card[i]:
                    self.dt_card[i] = [ply_name, ycard, rcard]
                    itemp += 1
                    break
            if itemp == 0:
                self.dt_card.append([ply_name, ycard, rcard])
        elif (ycard+rcard) == 0:
            for j in range(len(self.dt_card)):
                if ply_name in self.dt_card[j]:
                    self.dt_card.pop(j)
        self.input_card_players()
        self.geser_hor(self.fr_scinp1, 'kanan', -600, 0)

    def tambah(self, lbl_num, maks):
        num = int(lbl_num['text'])
        if num >= maks:
            return
        num+=1
        lbl_num.configure(text=num)

    def kurang(self, lbl_num):
        num = int(lbl_num['text'])
        if num <= 0:
            return
        num-=1
        lbl_num.configure(text=num)


    def input_goal_players(self):
        try:
            self.fr_scinp.destroy()
        except: pass
        scr_temp = 0
        if self.dt_goal != []:
            for gl in self.dt_goal:
                scr_temp += int(gl[1])
        sisa = self.mygoal - scr_temp
        self.fr_scinp = Frame(self.fr_plygol, bg='white')
        self.fr_scinp.place(x=0, y=65, width=1200, height=370)
        self.scfr_gol = CTkScrollableFrame(self.fr_scinp, fg_color='#060644', width=530, height=370)
        self.scfr_gol.place(x=25, y=0)
        self.fr_inp_plygol = Frame(self.fr_scinp, bg='#060644')
        self.fr_inp_plygol.place(x=625, y=0, width=550, height=370)
        self.lbl_nameply_gol = Label(self.fr_inp_plygol, text="Player's Name", font=('Times',20,'bold'), bg='#060644', fg='white')
        self.lbl_nameply_gol.place(x=20, y=20)
        self.lbl_angka_gol = Label(self.fr_inp_plygol, text='0', bg='#060644', fg='#66fcf1', font=('Bookman Old Style', 25, 'bold'))
        self.lbl_angka_gol.place(x=250, y=160, width=50, height=50)
        self.bttplus_gol = CTkButton(self.fr_inp_plygol, text='+', width=50, height=50, command= lambda: self.tambah(self.lbl_angka_gol, sisa), fg_color='#060644', border_width=2, border_color='#66fcf1', hover_color='blue', font=('Bookman Old Style', 30, 'bold'))
        self.bttplus_gol.place(x=300, y=160)
        self.bttmin_gol = CTkButton(self.fr_inp_plygol, text='-', width=50, height=50, command= lambda: self.kurang(self.lbl_angka_gol), fg_color='#060644', border_width=2, border_color='#66fcf1', hover_color='blue', font=('Bookman Old Style', 30, 'bold'))
        self.bttmin_gol.place(x=200, y=160)
        self.btt_ok2 = CTkButton(self.fr_inp_plygol, text='OK', width=150, height=35, command= lambda: self.update_goal(self.lbl_angka_gol, self.lbl_nameply_gol), fg_color='#060644', border_width=2, border_color='#66fcf1', hover_color='blue', font=('Bookman Old Style', 20, 'bold'))
        self.btt_ok2.place(x=200, y=230)
        rw = 0
        for ply in self.tim.child[0].child:
            i = 1
            if ply.data[0] in self.plycore_choosed or ply.data[0] in self.plycdgn_choosed:
                for gl in self.dt_goal:
                    if ply.data[0] in gl:
                        i = 0
                        self.summon_plyr_gol(self.scfr_gol, ply, rw, 0, gl[1])
                        break
                if i:
                    self.summon_plyr_gol(self.scfr_gol, ply, rw, 0, 0)
                rw += 1


    def input_card_players(self):
        try:
            self.fr_scinp1.destroy()
        except: pass
        y_temp = 0
        r_temp = 0
        if len(self.dt_card) >= 0:
            for cr in self.dt_card:
                y_temp += int(cr[1])
                r_temp += int(cr[2])
        sisa_y = self.kuning - y_temp
        sisa_r = self.merah - r_temp
        self.fr_scinp1 = Frame(self.fr_plycard, bg='white')
        self.fr_scinp1.place(x=0, y=65, width=1200, height=370)
        self.scfr_card = CTkScrollableFrame(self.fr_scinp1, fg_color='#060644', width=530, height=370)
        self.scfr_card.place(x=25, y=0)
        self.fr_inp_plycard = Frame(self.fr_scinp1, bg='#060644')
        self.fr_inp_plycard.place(x=625, y=0, width=550, height=370)
        self.lbl_nameply_card = Label(self.fr_inp_plycard, text="Player's Name", font=('Times',20,'bold'), bg='#060644', fg='white')
        self.lbl_nameply_card.place(x=20, y=20)

        self.lbl_ycard1 = Label(self.fr_inp_plycard, bg='yellow')
        self.lbl_ycard1.place(x=130, y=70, width=50, height=80)
        self.lbl_angka_ycard = Label(self.fr_inp_plycard, text=0, bg='#060644',fg='yellow', font=('Bookman Old Style', 25, 'bold'))
        self.lbl_angka_ycard.place(x=250, y=85, width=50, height=50)
        if sisa_y > 1:
            sisa_y = 1
        self.bttplus_ycard = CTkButton(self.fr_inp_plycard, text='+', width=50, height=50, command= lambda: self.tambah(self.lbl_angka_ycard, sisa_y), fg_color='#060644', border_width=2, border_color='#66fcf1', hover_color='blue', font=('Bookman Old Style', 30, 'bold'))
        self.bttplus_ycard.place(x=300, y=85)
        self.bttmin_ycard = CTkButton(self.fr_inp_plycard, text='-', width=50, height=50, command= lambda: self.kurang(self.lbl_angka_ycard), fg_color='#060644', border_width=2, border_color='#66fcf1', hover_color='blue', font=('Bookman Old Style', 30, 'bold'))
        self.bttmin_ycard.place(x=200, y=85)

        self.lbl_ycard1 = Label(self.fr_inp_plycard, bg='red')
        self.lbl_ycard1.place(x=130, y=180, width=50, height=80)
        self.lbl_angka_rcard = Label(self.fr_inp_plycard, text='0', bg='#060644',fg='red', font=('Bookman Old Style', 25, 'bold'))
        self.lbl_angka_rcard.place(x=250, y=195, width=50, height=50)
        if sisa_r > 1:
            sisa_r = 1
        self.bttplus_rcard = CTkButton(self.fr_inp_plycard, text='+', width=50, height=50, command= lambda: self.tambah(self.lbl_angka_rcard, sisa_r), fg_color='#060644', border_width=2, border_color='#66fcf1', hover_color='blue', font=('Bookman Old Style', 30, 'bold'))
        self.bttplus_rcard.place(x=300, y=195)
        self.bttmin_rcard = CTkButton(self.fr_inp_plycard, text='-', width=50, height=50, command= lambda: self.kurang(self.lbl_angka_rcard), fg_color='#060644', border_width=2, border_color='#66fcf1', hover_color='blue', font=('Bookman Old Style', 30, 'bold'))
        self.bttmin_rcard.place(x=200, y=195)

        self.btt_ok2 = CTkButton(self.fr_inp_plycard, text='OK', width=150, height=35, command= lambda: self.update_card(self.lbl_angka_ycard, self.lbl_angka_rcard, self.lbl_nameply_card),fg_color='#060644', border_width=2, border_color='#66fcf1', hover_color='blue', font=('Bookman Old Style', 20, 'bold'))
        self.btt_ok2.place(x=200, y=280)
        rw = 0
        for ply in self.tim.child[0].child:
            i = 1
            if ply.data[0] in self.plycore_choosed or ply.data[0] in self.plycdgn_choosed:
                for cr in self.dt_card:
                    if ply.data[0] in cr:
                        i = 0
                        self.summon_plyr_card(self.scfr_card, ply, rw, 0, cr[1], cr[2])
                        break
                if i:
                    self.summon_plyr_card(self.scfr_card, ply, rw, 0, 0, 0)
                rw += 1


    def geser_ver(self, fr, arah, y_pos_bef, y_pos_aft):
        if arah == 'atas':
            if y_pos_bef <= y_pos_aft:
                return
            y_pos_bef -= 20
            fr.place_configure(y=y_pos_bef)
            self.window.after(10, lambda: self.geser_ver(fr, arah, y_pos_bef, y_pos_aft))
        elif arah == 'bawah':
            if y_pos_bef >= y_pos_aft:
                return
            y_pos_bef += 20
            fr.place_configure(y=y_pos_bef)
            self.window.after(10, lambda: self.geser_ver(fr, arah, y_pos_bef, y_pos_aft))


    def geser_hor(self, fr, arah, x_pos_bef, x_pos_aft):
        if arah == 'kiri':
            if x_pos_bef <= x_pos_aft:
                return
            x_pos_bef -= 20
            fr.place_configure(x=x_pos_bef)
            self.window.after(10, lambda: self.geser_hor(fr, arah, x_pos_bef, x_pos_aft))
        elif arah == 'kanan':
            if x_pos_bef >= x_pos_aft:
                return
            x_pos_bef += 20
            fr.place_configure(x=x_pos_bef)
            self.window.after(10, lambda: self.geser_hor(fr, arah, x_pos_bef, x_pos_aft))


    def prev(self, fr):
        fr.destroy()


    def summon_plyr(self,fr, player, row, col, status):

        def hover_frame(e, wdg1, wd3, wd4, clr):
            wd3.configure(fg=clr)
            wd4.configure(fg=clr)

        def default_frame(e, wdg1, wd3, wd4, clr):
            wd3.configure(fg=clr)
            wd4.configure(fg=clr)

        def tampil(e, wd1, wd3, wd4):
            if player.data[0] in status:
                status.remove(player.data[0])
                wd1.configure(border_color='red')
                wd3.configure(fg='#060644')
                wd4.configure(fg='#060644')
                hovering(clr1='red', clr2='#060644')
            else:
                status.append(player.data[0])
                wd1.configure(border_color='green')
                wd3.configure(fg='green')
                wd4.configure(fg='green')
                hovering('black', 'green')



        def hovering(clr1, clr2):
            fr_btt.bind('<Enter>', lambda e:hover_frame(e, fr_btt, lbl_nama, lbl_pos, clr1))
            fr_btt.bind('<Leave>', lambda e:default_frame(e, fr_btt, lbl_nama, lbl_pos, clr2))
            lbl_nama.bind('<Enter>', lambda e:hover_frame(e, fr_btt, lbl_nama, lbl_pos, clr1))
            lbl_nama.bind('<Leave>', lambda e:default_frame(e, fr_btt, lbl_nama, lbl_pos, clr2))
            lbl_pos.bind('<Enter>', lambda e:hover_frame(e, fr_btt, lbl_nama, lbl_pos, clr1))
            lbl_pos.bind('<Leave>', lambda e:default_frame(e, fr_btt, lbl_nama, lbl_pos, clr2))


        fr_btt = CTkFrame(fr, width=925, height=60, border_width=3, border_color='red', fg_color='#DBDBDB', corner_radius=20)
        fr_btt.grid(row=row, column=col, pady=10, padx=10)

        lbl_nama = Label(fr_btt, text=player.data[0].upper(), font=('Times', 20, 'bold'), bg='#DBDBDB', fg='#060644')
        lbl_nama.place(x=20, y=5, height=50)
        lbl_pos = Label(fr_btt, text=player.child[5].data, font=('Times', 20, 'bold'), bg='#DBDBDB', fg='#060644', anchor='e')
        lbl_pos.place(x=750, y=5, height=50, width=130)


        hovering(clr1='red', clr2='#060644')
        fr_btt.bind('<Button-1>',lambda e: tampil(e, fr_btt, lbl_nama, lbl_pos))
        lbl_nama.bind('<Button-1>',lambda e: tampil(e, fr_btt, lbl_nama, lbl_pos))
        lbl_pos.bind('<Button-1>',lambda e: tampil(e, fr_btt, lbl_nama, lbl_pos))


    def summon_plyr_gol(self, fr, player, row, col, jum_gol):

        def tampil_gol(e):
            self.geser_hor(self.fr_scinp, 'kiri', 0, -600)
            self.lbl_nameply_gol.configure(text=player.data[0])
            self.lbl_angka_gol.configure(text=jum_gol)

        fr_btt = CTkFrame(fr, width=530, height=50, border_width=1, border_color='white', fg_color='#060644', corner_radius=90)
        fr_btt.grid(row=row, column=col, pady=3)

        lbl_nama = Label(fr_btt, text=player.data[0].upper(), font=('Times', 10, 'bold'), bg='#060644', fg='white')
        lbl_nama.place(x=10, y=5, height=40)

        lbl_gol = Label(fr_btt, text=jum_gol, font=('Times', 15, 'bold'), bg='#060644', fg='white', anchor='e')
        lbl_gol.place(x=430, y=5, height=40, width=50)

        fr_btt.bind('<Button-1>',tampil_gol)
        lbl_nama.bind('<Button-1>',tampil_gol)
        lbl_gol.bind('<Button-1>',tampil_gol)

    def summon_plyr_card(self, fr, player, row, col, y_card, r_card):

        def tampil_card(e):
            self.geser_hor(self.fr_scinp1, 'kiri', 0, -600)
            self.lbl_nameply_card.configure(text=player.data[0])
            self.lbl_angka_ycard.configure(text=y_card)
            self.lbl_angka_rcard.configure(text=r_card)

        fr_btt = CTkFrame(fr, width=530, height=50, border_width=1, border_color='white', fg_color='#060644', corner_radius=90)
        fr_btt.grid(row=row, column=col, pady=3)

        lbl_nama = Label(fr_btt, text=player.data[0].upper(), font=('Times', 10, 'bold'), bg='#060644', fg='white')
        lbl_nama.place(x=10, y=5, height=40)

        lbl_ycard = Label(fr_btt, text=y_card, font=('Times', 15, 'bold'), bg='yellow', fg='#060644')
        lbl_ycard.place(x=440, y=5, height=40, width=20)
        lbl_rcard = Label(fr_btt, text=r_card, font=('Times', 15, 'bold'), bg='red', fg='#060644')
        lbl_rcard.place(x=480, y=5, height=40, width=20)

        fr_btt.bind('<Button-1>',tampil_card)
        lbl_nama.bind('<Button-1>',tampil_card)
        lbl_ycard.bind('<Button-1>',tampil_card)
        lbl_rcard.bind('<Button-1>',tampil_card)

    def simpan(self, data):
        pertandingan = TreeNode(data)
        inti = TreeNode(self.plycore_choosed)
        cadangan = TreeNode(self.plycdgn_choosed)
        data_match = TreeNode('Data Match')
        goal = TreeNode((self.mygoal, self.enmgoal))
        card = TreeNode((self.kuning, self.merah))
        if self.mygoal > 0:
            goal.add_child(TreeNode(self.dt_goal))
        if (self.kuning + self.merah) > 0:
            card.add_child(TreeNode(self.dt_card))
        dt_sta = (int(self.sld_1.get()),
                 int(self.sld_2.get()),
                 (int(self.num3['text']), int(self.num4['text'])),
                 int(self.num5['text']))
        data_match.add_child(goal)
        data_match.add_child(card)
        data_match.add_child(TreeNode(dt_sta))
        pertandingan.add_child(inti)
        pertandingan.add_child(cadangan)
        pertandingan.add_child(data_match)
        itemp = 0

        for i in range(len(self.tim.child[2].child[0].child)):
            dt_pert = self.tim.child[2].child[0].child[i]
            if data == dt_pert.data:
                dt_pert = pertandingan
                itemp += 1
        if itemp == 0:
            self.tim.child[2].child[0].add_child(pertandingan)

        for ply in self.tim.child[0].child:
            if ply.data[0] in self.plycore_choosed or ply.data[0] in self.plycdgn_choosed:
                prtd = TreeNode((data[0],data[2]))
                temp = 0
                if self.mygoal != 0:
                    for plygol in self.dt_goal:
                        if ply.data[0] in plygol:
                            prtd.add_child(TreeNode(plygol[1]))
                            temp += 1
                            break
                if temp == 0:
                    prtd.add_child(TreeNode(0))
                try:
                    ply.child[8].add_child(prtd)
                except IndexError:
                    ply.add_child(TreeNode('Kemampuan'))
                    ply.add_child(TreeNode('History Training'))
                    ply.add_child(TreeNode('Match History'))
                    ply.child[8].add_child(prtd)

        fl = open('Data/treeDatabase.pickle', 'wb')
        pickle.dump(self.tr_var, fl)
        fl.close()
        self.dt_card = []
        self.dt_goal = []
        self.prev(self.FRAME)




# w = Tk()
# fl = open('Data/treeDatabase.pickle', 'rb')
# tree_data = pickle.load(fl)
# fl.close()
# jadwal = [['12/05/2024','13:00','SDA_01'],['15/05/2024','10:00','SDA_05'],['27/05/2024','12:00','SDA_07'],['02/06/2024','11:00','SDA_08']]
# AddDataMatch(w, tree_data.child[0].child[0], tree_data, jadwal)
# w.mainloop()