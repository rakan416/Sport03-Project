from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import pickle
from datetime import datetime
from tkinter.messagebox import *
from Tree_Processing import TreeNode



class AddDataTrain():

    def __init__(self, window, tim_data, sch, root):
        self.window = window
        self.tim = tim_data
        self.jadwal = sch
        self.tr_var = root
        # self.window.state('zoomed')
        self.FRAME = Frame(self.window, bg='#093D83', width=1366, height=768)
        self.FRAME.place(x=0, y=0)
        foto = Image.open("Image/Background/bg_1.png").resize((1366, 768))
        self.photoo = ImageTk.PhotoImage(foto)
        self.label_background = Label(self.FRAME, image=self.photoo)
        self.label_background.place(x=-2, y=-2)

        self.data_det = ['Crossing','Finishing','Heading Accuracy','Short Passing','Volleys','Dribbling','Curve','Freekick Accuracy','Long Passing','Ball Control','Acceleration','Sprint Speed','Agility','Reactions','Balance','Shot Power','Jumping','Stamina','Strength','Long Shots','Aggression','Interceptions','Positioning','Vision','Penalties','Composure','Marking','Standing Tackle','Sliding Tackle']
        self.temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.skill_ply = [0,0,0,0,0,0]
        self.analitic_skill = {
                                'ATT': [0, 1, 2, 24],
                                'TEC': [3, 4, 5, 6, 7, 8, 9],
                                'STA': [12, 13, 14, 17],
                                'DEF': [20, 21, 22, 26, 27, 28],
                                'POW': [15, 16, 18, 19, 23, 25],
                                'SPD': [10, 11]
                                }

        self.fr1 = CTkFrame(self.FRAME, fg_color='#060644', width=760, height=400)
        self.fr1.place(x=303, y=170)
        self.lbl_sch = Label(self.fr1, text='Pilih Jadwal', bg='#060644', font=('Times', 30, 'bold'), fg='white')
        self.lbl_sch.place(x=30, y=0, width=700, height=50)
        self.fr_sch = CTkScrollableFrame(self.fr1, fg_color='#DBDBDB', width=743, height=350, corner_radius=0)
        self.fr_sch.place(x=0, y=50)
        self.sekarang = datetime.now()
        self.tgl_now = self.sekarang.strftime('%d/%m/%Y')
        rw = 0
        cl = 0
        for i in range(len(self.jadwal)):
            color = '#060644'
            try:
                ind = self.jadwal[i][2]
            except: ind = 0
            if ind == 1:
                color = 'green'
            if cl >= 6:
                cl = 0
                rw += 1
            self.button_sch(self.jadwal[i], rw, cl,color)
            cl += 1

        global img_return0
        img_return0 = ImageTk.PhotoImage(Image.open('Image/return.png').resize((110, 50)))
        self.button_back = Button(self.FRAME, image=img_return0, cursor="hand2", command=lambda : self.FRAME.destroy(), bg='#093D83', relief='flat', borderwidth=0, activebackground='#093D83')
        self.button_back.place(x=35, y=645)


    def back(self):
        self.FRAME.destroy()

    def button_sch(self, jdwl, rw, cl, bdc):
        fr_btt = CTkFrame(self.fr_sch, fg_color='#DBDBDB', width=100, height=100, border_width=3, border_color=bdc, corner_radius=15)
        fr_btt.grid(row=rw, column=cl, padx=11, pady=10)
        lbl_btt = Label(fr_btt, text=jdwl[0], fg='black', bg='#DBDBDB', font=('Bookman Old Style',10))
        lbl_btt.place(x=10, y=13, width=80)
        text = jdwl[1]
        if text == 'Spesifikasi Posisi':
            text = 'Spesifikasi\nPosisi'
        lbl_jns = Label(fr_btt, text=text, fg='black', bg='#DBDBDB', font=('Bookman Old Style',10))
        lbl_jns.place(x=10, y=38, width=80)

        def hover_in_fr(e):
            fr_btt.configure(border_width = 10)

        def hover_out_fr(e):
            fr_btt.configure(border_width = 3)

        def edit_train(e):
            # self.fr1.destroy()
            self.choose_ply(jdwl[0])

        if bdc != 'grey':
            fr_btt.bind('<Enter>', hover_in_fr)
            fr_btt.bind('<Leave>', hover_out_fr)
            lbl_btt.bind('<Enter>', hover_in_fr)
            lbl_btt.bind('<Leave>', hover_out_fr)
            lbl_jns.bind('<Enter>', hover_in_fr)
            lbl_jns.bind('<Leave>', hover_out_fr)
            fr_btt.bind('<Button-1>', edit_train)
            lbl_btt.bind('<Button-1>', edit_train)
            lbl_jns.bind('<Button-1>', edit_train)

    def choose_ply(self, tgl):
        self.fr2 = Frame(self.FRAME, bg='#093D83')
        self.fr2.place(x=0, y=0, width=1366, height=768)
        self.label_background1 = Label(self.fr2, image=self.photoo)
        self.label_background1.place(x=-2, y=-2)
        self.fr_lst = CTkFrame(self.fr2, fg_color='#060644', width=400, height=470, corner_radius=20)
        self.fr_lst.place(x=45, y=15)
        self.fr_inp = CTkFrame(self.fr2, fg_color='#060644', width=850, height=620, corner_radius=20)
        self.fr_inp.place(x=480, y=15)
        self.lbl_cply = CTkLabel(self.fr_lst, text='PILIH PEMAIN', font=('Times', 20, 'bold'), text_color='white', width=390, height=45)
        self.lbl_cply.place(x=5, y=5)
        self.fr_listplyr = Frame(self.fr_lst, bg='#DBDBDB')
        self.fr_listplyr.place(x=0, y=50, width=800, height=420)
        self.fr_listplyr1 = CTkScrollableFrame(self.fr_listplyr, fg_color='#DBDBDB', width=370, height=400)
        self.fr_listplyr1.place(x=0, y=0)
        self.btt_change = CTkButton(self.fr_listplyr, text='GANTI PEMAIN', width=100, height=30, border_color='green', border_width=2, corner_radius=30, fg_color='#DBDBDB', text_color='#060644', command=lambda : self.geser(self.fr_listplyr, 'kanan', -395, 0))
        self.btt_change.place(x=400, y=10)
        i = 0
        for p_data in self.tim.child[0].child:
            try:
                p_data.child[6].child[0].data
                clr = 'blue'
            except IndexError:
                clr = 'grey'
            self.summon_plyr(p_data, i, 0, clr)
            i += 1

        self.lbl_name = Label(self.fr_inp, text="PLAYER'S NAME", font=('Times', 20, 'bold'), bg='#060644', fg='white')
        self.lbl_name.place(x=30, y=0, height=60)
        self.lbl_date = Label(self.fr_inp, text=tgl, font=('Times', 18, 'bold'), bg='#060644', anchor='e', fg='white')
        self.lbl_date.place(x=680, y=0, width=130, height=60)

        self.fr_att = Frame(self.fr_inp, bg='#060644', width=270, height=80)
        self.fr_att.place(x=10, y=66)
        self.lbl_att = Label(self.fr_att, text='PENYERANGAN' , bg='#060644', font=('russo one', 13, 'bold'), fg='#D9D9D9', anchor='w')
        self.lbl_att.place(x=0, y=0,height=20,width=168)
        self.sld_att = CTkSlider(self.fr_att, bg_color='#060644', from_=0, to= 100,width=250, button_color='#66fcf1', button_hover_color='#45A29E', progress_color='#66fcf1',
                                 command=lambda val: self.Sliding(val=int(val), lbl=self.num_att, indx=0, gol=self.analitic_skill['ATT']))
        self.sld_att.place(x=0, y = 30)
        self.sld_att.set(0)
        self.num_att = Label(self.fr_att,text=0, bg='#060644', font=('russo one', 13, 'bold'), fg='#D9D9D9')
        self.num_att.place(x=120, y=55, width=30, height=20)

        self.fr_tec = Frame(self.fr_inp, bg='#060644', width=270, height=80)
        self.fr_tec.place(x=290, y=66)
        self.lbl_tec = Label(self.fr_tec, text='TEKNIK' , bg='#060644', font=('russo one', 13, 'bold'), fg='#D9D9D9', anchor='w')
        self.lbl_tec.place(x=0, y=0,height=20,width=168)
        self.sld_tec = CTkSlider(self.fr_tec, bg_color='#060644', from_=0, to= 100,width=250, button_color='#66fcf1', button_hover_color='#45A29E', progress_color='#66fcf1',
                                 command=lambda val: self.Sliding(val=int(val), lbl=self.num_tec, indx=1, gol=self.analitic_skill['TEC']))
        self.sld_tec.place(x=0, y = 30)
        self.sld_tec.set(0)
        self.num_tec = Label(self.fr_tec,text=0, bg='#060644', font=('russo one', 13, 'bold'), fg='#D9D9D9')
        self.num_tec.place(x=120, y=55, width=30, height=20)

        self.fr_sta = Frame(self.fr_inp, bg='#060644', width=270, height=80)
        self.fr_sta.place(x=570, y=66)
        self.lbl_sta = Label(self.fr_sta, text='STAMINA' , bg='#060644', font=('russo one', 13, 'bold'), fg='#D9D9D9', anchor='w')
        self.lbl_sta.place(x=0, y=0,height=20,width=168)
        self.sld_sta = CTkSlider(self.fr_sta, bg_color='#060644', from_=0, to= 100,width=250, button_color='#66fcf1', button_hover_color='#45A29E', progress_color='#66fcf1',
                                 command=lambda val: self.Sliding(val=int(val), lbl=self.num_sta, indx=2, gol=self.analitic_skill['STA']))
        self.sld_sta.place(x=0, y = 30)
        self.sld_sta.set(0)
        self.num_sta = Label(self.fr_sta,text=0, bg='#060644', font=('russo one', 13, 'bold'), fg='#D9D9D9')
        self.num_sta.place(x=120, y=55, width=30, height=20)

        self.fr_def = Frame(self.fr_inp, bg='#060644', width=270, height=80)
        self.fr_def.place(x=10, y=166)
        self.lbl_def = Label(self.fr_def, text='PERTAHANAN' , bg='#060644', font=('russo one', 13, 'bold'), fg='#D9D9D9', anchor='w')
        self.lbl_def.place(x=0, y=0,height=20,width=168)
        self.sld_def = CTkSlider(self.fr_def, bg_color='#060644', from_=0, to= 100,width=250, button_color='#66fcf1', button_hover_color='#45A29E', progress_color='#66fcf1',
                                 command=lambda val: self.Sliding(val=int(val), lbl=self.num_def, indx=3, gol=self.analitic_skill['DEF']))
        self.sld_def.place(x=0, y = 30)
        self.sld_def.set(0)
        self.num_def = Label(self.fr_def,text=0, bg='#060644', font=('russo one', 13, 'bold'), fg='#D9D9D9')
        self.num_def.place(x=120, y=55, width=30, height=20)

        self.fr_pow = Frame(self.fr_inp, bg='#060644', width=270, height=80)
        self.fr_pow.place(x=290, y=166)
        self.lbl_pow = Label(self.fr_pow, text='KEKUATAN' , bg='#060644', font=('russo one', 13, 'bold'), fg='#D9D9D9', anchor='w')
        self.lbl_pow.place(x=0, y=0,height=20,width=168)
        self.sld_pow = CTkSlider(self.fr_pow, bg_color='#060644', from_=0, to= 100,width=250, button_color='#66fcf1', button_hover_color='#45A29E', progress_color='#66fcf1',
                                 command=lambda val: self.Sliding(val=int(val), lbl=self.num_pow, indx=4, gol=self.analitic_skill['POW']))
        self.sld_pow.place(x=0, y = 30)
        self.sld_pow.set(0)
        self.num_pow = Label(self.fr_pow,text=0, bg='#060644', font=('russo one', 13, 'bold'), fg='#D9D9D9')
        self.num_pow.place(x=120, y=55, width=30, height=20)

        self.fr_spd = Frame(self.fr_inp, bg='#060644', width=270, height=80)
        self.fr_spd.place(x=570, y=166)
        self.lbl_spd = Label(self.fr_spd, text='KECEPATAN' , bg='#060644', font=('russo one', 13, 'bold'), fg='#D9D9D9', anchor='w')
        self.lbl_spd.place(x=0, y=0,height=20,width=168)
        self.sld_spd = CTkSlider(self.fr_spd, bg_color='#060644', from_=0, to= 100,width=250, button_color='#66fcf1', button_hover_color='#45A29E', progress_color='#66fcf1',
                                 command=lambda val: self.Sliding(val=int(val), lbl=self.num_spd, indx=5, gol=self.analitic_skill['SPD']))
        self.sld_spd.place(x=0, y = 30)
        self.sld_spd.set(0)
        self.num_spd = Label(self.fr_spd,text=0, bg='#060644', font=('russo one', 13, 'bold'), fg='#D9D9D9')
        self.num_spd.place(x=120, y=55, width=30, height=20)

        self.btt_more = CTkButton(self.fr_inp, text='MORE DETAIL \/', width=820, height=30, command=self.detail, fg_color='#060644', hover_color='blue', font=('Times',15, 'bold'), corner_radius=50,border_color='#66fcf1',border_width=2)
        self.btt_more.place(x=15, y=260)

        self.btt_upd = CTkButton(self.fr_inp, text='Update', width=100, height=50, command=lambda: self.update_player(tgl), fg_color='#060644', hover_color='blue', font=('Times',15, 'bold'), corner_radius=50,border_color='#66fcf1',border_width=2)
        self.btt_upd.place(x=20, y=550)
        self.btt_done = CTkButton(self.fr_inp, text='Done', width=100, height=50, fg_color='#060644', hover_color='blue', font=('Times',15, 'bold'), corner_radius=50,border_color='#66fcf1',border_width=2, command=lambda: self.FRAME.destroy())
        self.btt_done.place(x=730, y=550)
        self.button_back1 = Button(self.fr2, image=img_return0, cursor="hand2", command=lambda : self.fr2.destroy(), bg='#093D83', relief='flat', borderwidth=0, activebackground='#093D83')
        self.button_back1.place(x=35, y=645)


    def profile_player(self, player):
        try:
            self.fr_identity.destroy()
        except: pass
        self.fr_identity = CTkFrame(self.fr_listplyr, fg_color='#DBDBDB', width=390, height=267, border_color='blue', border_width=3)
        self.fr_identity.place(x=400, y=70)
        self.lbl_name1 = CTkLabel(self.fr_identity, text=player.data[0].upper(), width=380, height=30, text_color='#060644', font=('Bookman Old Style', 18))
        self.lbl_name1.place(x=5, y=5)
        self.lbl_birth = CTkLabel(self.fr_identity, text=f'BIRTHDAY\n{player.child[0].data}', width=110, height=50, anchor='w', text_color='#060644', font=('Bookman Old Style', 13))
        self.lbl_birth.place(x=22, y=56)
        self.lbl_height = CTkLabel(self.fr_identity, text=f'HEIGHT\n{player.child[1].data}', width=110, height=50, anchor='w', text_color='#060644', font=('Bookman Old Style', 13))
        self.lbl_height.place(x=22, y=126)
        self.lbl_weight = CTkLabel(self.fr_identity, text=f'WEIGHT\n{player.child[2].data}', width=110, height=50, anchor='w', text_color='#060644', font=('Bookman Old Style', 13))
        self.lbl_weight.place(x=22, y=186)
        kaki = player.child[4].data
        if kaki == 'Kanan':
            path_img = 'Image/right_feet.png'
        elif kaki == 'Kiri':
            path_img = 'Image/left_feet.png'
        img_open = Image.open(path_img).resize((85,75))
        global gambar
        gambar = ImageTk.PhotoImage(img_open)
        self.lbl_prefot = CTkLabel(self.fr_identity, text=f'PREFFERD FOOT\n{kaki.upper()}', width=150, height=55, text_color='#060644', font=('russo one', 13, 'bold'))
        self.lbl_prefot.place(x=230, y=45)
        self.lbl_imgfot = Label(self.fr_identity, image=gambar, bg='#DBDBDB')
        self.lbl_imgfot.place(x=263, y=100)
        self.lbl_position = CTkLabel(self.fr_identity, text=f'POSITION\n{player.child[5].data}', width=160, height=50, text_color='#060644', font=('russo one', 13, 'bold'))
        self.lbl_position.place(x=220, y=180)
        self.lbl_identity = CTkLabel(self.fr_listplyr, text= 'IDENTITY', width=80, height=15, text_color='blue', font=('russo one', 13, 'italic'), fg_color='transparent')
        self.lbl_identity.place(x=420,y=63)

    def geser(self, fr, arah, x_pos_bef, x_pos_aft):
        if x_pos_bef == x_pos_aft:
            return
        if arah == 'kiri':
            x_pos_bef -= 20
            if x_pos_bef <= x_pos_aft:
                x_pos_bef = x_pos_aft
            fr.place_configure(x=x_pos_bef)
            self.window.after(10, lambda: self.geser(fr, arah, x_pos_bef, x_pos_aft))
        elif arah == 'kanan':
            x_pos_bef += 20
            if x_pos_bef >= x_pos_aft:
                x_pos_bef = x_pos_aft
            fr.place_configure(x=x_pos_bef)
            self.window.after(10, lambda: self.geser(fr, arah, x_pos_bef, x_pos_aft))


    def Sliding(self, val, lbl, indx, gol):
        lbl.configure(text = val)
        temp = 0
        for i in gol:
            self.temp[i] = val
            temp += val
        self.skill_ply[indx] = temp


    def cancel(self):
        try:
            self.frsld.destroy()
            self.sld_att.configure(state='normal')
            self.sld_tec.configure(state='normal')
            self.sld_sta.configure(state='normal')
            self.sld_def.configure(state='normal')
            self.sld_pow.configure(state='normal')
            self.sld_spd.configure(state='normal')
            self.btt_more.configure(text='More \/', command=self.detail)
        except: pass

    def detail(self):
        self.frsld = Frame(self.fr_inp, width=830, height=230, bg='#060644')
        self.frsld.place(x=10, y=300)
        self.fr_sld_inp = CTkScrollableFrame(self.frsld, width=810, height=230, fg_color='#060644')
        self.fr_sld_inp.place(x=0, y=0)
        rw = 0
        cl = 0
        for dt_skll in self.data_det:
            if rw == 10:
                rw = 0
                cl += 1
            for key in self.analitic_skill.keys():
                if self.data_det.index(dt_skll) in self.analitic_skill[key]:
                    indk = key
                    if indk == 'ATT':
                        indk = (self.sld_att, self.num_att)
                        indx = 0
                        ln = 4
                    elif indk == 'TEC':
                        indk = (self.sld_tec, self.num_tec)
                        indx = 1
                        ln = 7
                    elif indk == 'STA':
                        indk = (self.sld_sta, self.num_sta)
                        indx = 2
                        ln = 4
                    elif indk == 'DEF':
                        indk = (self.sld_def, self.num_def)
                        indx = 3
                        ln = 6
                    elif indk == 'POW':
                        indk = (self.sld_pow, self.num_pow)
                        indx = 4
                        ln = 6
                    elif indk == 'SPD':
                        indk = (self.sld_spd, self.num_spd)
                        indx = 5
                        ln = 2
                    break
                else: 
                    continue
            self.summon_slider(rw=rw, cl=cl, dt=dt_skll, fr=self.fr_sld_inp, stv=self.temp[(self.data_det.index(dt_skll))], indk=indk, indx=indx, ln=ln)
            rw += 1
        self.btt_more.configure(text='Cancel /\\', command=self.cancel)
        self.sld_att.configure(state='disabled')
        self.sld_tec.configure(state='disabled')
        self.sld_sta.configure(state='disabled')
        self.sld_def.configure(state='disabled')
        self.sld_pow.configure(state='disabled')
        self.sld_spd.configure(state='disabled')

    def summon_plyr(self, player, row, col, brdc):

        def hover_frame(e, wdg1, wdg2, wd3, wd4):
            wdg2.configure(fg=brdc)
            wd3.configure(fg=brdc)
            wd4.configure(fg=brdc)


        def default_frame(e, wdg1, wdg2, wd3, wd4):
            wdg2.configure(fg='#060644')
            wd3.configure(fg='#060644')
            wd4.configure(fg='#060644')

        def tampil(e):
            self.lbl_name.configure(text=player.data[0].upper())
            self.player = player
            try:
                self.temp = player.child[6].child[0].data
            except:
                self.temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                
            self.skill_ply = []
            for cat, item in self.analitic_skill.items():
                val = 0
                for itm in item:
                    val += self.temp[itm]
                self.skill_ply.append(val)
            self.sld_att.set(self.skill_ply[0]/4)
            self.sld_tec.set(self.skill_ply[1]/7)
            self.sld_sta.set(self.skill_ply[2]/4)
            self.sld_def.set(self.skill_ply[3]/6)
            self.sld_pow.set(self.skill_ply[4]/6)
            self.sld_spd.set(self.skill_ply[5]/2)
            self.num_att.configure(text=int(self.skill_ply[0]/4))
            self.num_tec.configure(text=int(self.skill_ply[1]/7))
            self.num_sta.configure(text=int(self.skill_ply[2]/4))
            self.num_def.configure(text=int(self.skill_ply[3]/6))
            self.num_pow.configure(text=int(self.skill_ply[4]/6))
            self.num_spd.configure(text=int(self.skill_ply[5]/2))
            self.cancel()
            # self.fr_listplyr.place_configure(x=-390)
            self.profile_player(player)
            
            self.window.after(1000, lambda:self.geser(self.fr_listplyr, 'kiri', 0, -395))



        fr_btt = CTkFrame(self.fr_listplyr1, width=365, height=40, border_width=3, border_color=brdc, fg_color='#DBDBDB', corner_radius=10)
        fr_btt.grid(row=row, column=col, pady=4)

        lbl_gmbr = Label(fr_btt, bg='#DBDBDB', fg='#060644')
        lbl_nama = Label(fr_btt, text=player.data[0].upper(), font=('Times', 10, 'bold'), bg='#DBDBDB', fg='#060644')
        lbl_nama.place(x=5, y=5, height=30)
        lbl_pos = Label(fr_btt, text=player.child[5].data, font=('Times', 10, 'bold'), bg='#DBDBDB', fg='#060644')
        lbl_pos.place(x=290, y=5, height=30, width=60)

        fr_btt.bind('<Enter>', lambda e:hover_frame(e, fr_btt, lbl_gmbr, lbl_nama, lbl_pos))
        fr_btt.bind('<Leave>', lambda e:default_frame(e, fr_btt, lbl_gmbr, lbl_nama, lbl_pos))
        lbl_gmbr.bind('<Enter>', lambda e:hover_frame(e, fr_btt, lbl_gmbr, lbl_nama, lbl_pos))
        lbl_gmbr.bind('<Leave>', lambda e:default_frame(e, fr_btt, lbl_gmbr, lbl_nama, lbl_pos))
        lbl_nama.bind('<Enter>', lambda e:hover_frame(e, fr_btt, lbl_gmbr, lbl_nama, lbl_pos))
        lbl_nama.bind('<Leave>', lambda e:default_frame(e, fr_btt, lbl_gmbr, lbl_nama, lbl_pos))
        lbl_pos.bind('<Enter>', lambda e:hover_frame(e, fr_btt, lbl_gmbr, lbl_nama, lbl_pos))
        lbl_pos.bind('<Leave>', lambda e:default_frame(e, fr_btt, lbl_gmbr, lbl_nama, lbl_pos))
        fr_btt.bind('<Button-1>',tampil)
        lbl_gmbr.bind('<Button-1>',tampil)
        lbl_nama.bind('<Button-1>',tampil)
        lbl_pos.bind('<Button-1>',tampil)

    def count_mean(self, before, after, indk, indx, ln):
        try:
            self.skill_ply[indx] += (after-before)
        except:
            self.skill_ply = [0,0,0,0,0,0]
            self.skill_ply[indx] += (after-before)
        indk[0].set(self.skill_ply[indx]/ln)
        indk[1].configure(text=int(self.skill_ply[indx]/ln))


    def summon_slider(self, rw,cl, dt, fr, stv, indk, indx, ln):
        def sliding(value, sc):
            sc.configure(text=value)
            temp_num = self.temp[self.data_det.index(dt)]
            self.temp[self.data_det.index(dt)] = value
            self.count_mean(temp_num, value, indk, indx, ln)

        temp_fr = CTkFrame(fr, width=250, height=45, border_color='#66fcf1', border_width=1, fg_color='#060644')
        temp_fr.grid(column=cl, row=rw, pady=5, padx=10)
        lbl = Label(temp_fr, text=dt , bg='#060644', font=('Russo one', 10, 'bold'), anchor='w', fg='#D9D9D9')
        lbl.place(x=10, y=-5,height=20)
        sld = CTkSlider(temp_fr, bg_color='#060644', from_=0, to= 100,width=200, command= lambda val:sliding(int(val), num), button_color='#66fcf1', button_hover_color='#45A29E', progress_color='#66fcf1')
        sld.place(x=10, y = 20)
        sld.set(stv)
        hsl = int(sld.get())
        num = Label(temp_fr,text=hsl, bg='#060644',anchor='w', fg='#D9D9D9')
        num.place(x=210, y=20, width=30, height=20)
        # self.temp[self.data_det.index(dt)] = hsl

    def update_player(self, tgl):

        try:
            self.player.data
        except:
            showerror(message='NoPlayer had Choosen!')
            return
        
        if sum(self.temp) == 0:
            showerror(message='Empty Data!')
            return
        
        try:
            self.player.child[6].child[0].data = self.temp
        except:
            kmpp = TreeNode('Kemampuan')
            kmpp.add_child(TreeNode(self.temp))
            self.player.add_child(kmpp)
            train = TreeNode('Data_Training')
            self.player.add_child(train)

        temp_list = []
        for num in self.temp:
            temp_list.append(num)

        tn = 0
        for dttgl in self.player.child[7].child:
            if dttgl.data == tgl:
                dttgl.child[0].data = temp_list
                tn += 1
                break


        if tn == 0:
            tre_tgl = TreeNode(tgl)
            tre_tgl.add_child(TreeNode(temp_list))
            self.player.child[7].add_child(tre_tgl)

        for idx in range(len(self.jadwal)): 
            if self.jadwal[idx][0] == tgl:
                try: self.jadwal[idx][2] = 1
                except: self.jadwal[idx].append(1)
                break
            else:
                try: self.jadwal[idx][2]
                except: self.jadwal[idx].append(0)

        fl = open('Data/treeDatabase.pickle', 'wb')
        pickle.dump(self.tr_var, fl)
        fl.close()

        self.player = None
        self.temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.skill_ply = [0,0,0,0,0,0]
        self.sld_att.set(0)
        self.sld_tec.set(0)
        self.sld_sta.set(0)
        self.sld_def.set(0)
        self.sld_pow.set(0)
        self.sld_spd.set(0)
        self.num_att.configure(text=0)
        self.num_tec.configure(text=0)
        self.num_sta.configure(text=0)
        self.num_def.configure(text=0)
        self.num_pow.configure(text=0)
        self.num_spd.configure(text=0)
        self.lbl_name.configure(text="PLAYER'S NAME")
        self.geser(self.fr_listplyr, 'kanan', -395, 0)
        self.cancel()




# w = Tk()
# fl = open('Data/treeDatabase.pickle', 'rb')
# tree_data = pickle.load(fl)
# fl.close()
# # jadwal = [['11/05/2024'],['14/05/2024'],['17/05/2024'],['20/05/2024'],['23/05/2024']]
# tim = tree_data.child[0].child[0]
# jadwal = tim.child[1].child[0].data

# AddDataTrain(w, tim, jadwal, tree_data)
# w.mainloop()