from tkinter import *
from customtkinter import *
import pickle
from datetime import datetime
from PIL import Image,ImageTk
import textwrap


class TrainStatistic():

    def __init__(self, window, tim_data, sch):
        self.window = window
        self.tim = tim_data
        self.jadwal = sch
        # self.window.state('zoomed')
        self.FRAME = Frame(self.window, bg='#093D83', width=1366, height=768)
        self.FRAME.place(x=0, y=0)
        fl_lat = open('Data/detail_latihan.txt','r')
        lst  = fl_lat.read().split('\n\n')
        self.lstlat = [lt.split('\n') for lt in lst]

        foto = Image.open("Image/Background/bg_1.png").resize((1366, 768))
        self.photoo = ImageTk.PhotoImage(foto)
        self.label_background = Label(self.FRAME, image=self.photoo)
        self.label_background.place(x=-2, y=-2)
        self.data_det = ['Crossing','Finishing','Heading Accuracy','Short Passing','Volleys','Dribbling','Curve','Freekick Accuracy','Long Passing','Ball Control','Acceleration','Sprint Speed','Agility','Reactions','Balance','Shot Power','Jumping','Stamina','Strength','Long Shots','Aggression','Interceptions','Positioning','Vision','Penalties','Composure','Marking','Standing Tackle','Sliding Tackle']
        self.temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
        rw, cl = (0, 0)
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
            if color == 'green':
                self.button_sch(self.jadwal[i], 0, i,color)
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
            self.choose_ply(jdwl[0], jdwl)

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


    def choose_ply(self, tgl, dtlat):
        self.fr2 = Frame(self.FRAME, bg='#093D83')
        self.fr2.place(x=0, y=0, width=1366, height=768)
        self.label_background1 = Label(self.fr2, image=self.photoo)
        self.label_background1.place(x=-2, y=-2)
        self.button_back1 = Button(self.fr2, image=img_return0, cursor="hand2", command=lambda : self.fr2.destroy(), bg='#093D83', relief='flat', borderwidth=0, activebackground='#093D83')
        self.button_back1.place(x=35, y=645)
        self.fr_lst = CTkFrame(self.fr2, fg_color='#060644', width=400, height=470, corner_radius=20)
        self.fr_lst.place(x=45, y=15)
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
                for train_dt in p_data.child[7].child:
                    if train_dt.data == tgl:
                        clr = 'blue'
                        self.summon_plyr(p_data, i, 0, clr, train_dt)
                        i += 1
            except IndexError:
                clr = 'grey'
        
        self.fr_inp = CTkFrame(self.fr2, fg_color='#060644', width=850, height=620, corner_radius=20)
        self.fr_inp.place(x=480, y=15)
        self.lbl_desk = Label(self.fr_inp, text='DESKRIPSI LATIHAN :', font=('Times', 20, 'bold'), fg='white', bg='#060644')
        self.lbl_desk.place(x=10, y=10, height=60)
        self.fr_desk = Frame(self.fr_inp, bg='#DBDBDB')
        self.fr_desk.place(x=0, y=70, width=850, height=160)
        text_bef = ''
        for detail in self.lstlat:
            if detail[0] == dtlat[1]:
                text_bef = str(detail[1])
                break
        wrap = textwrap.wrap(text_bef, width=102)
        wrapsrc = textwrap.wrap(detail[2], width=102)
        text = '\n'.join(wrap)
        wrapsrc = '\n'.join(wrapsrc)
        self.lbl_ketdes = Label(self.fr_desk,text=(text+'\n\n'+wrapsrc),bg='#DBDBDB', fg='black', anchor='w', justify='left', font=('Times', 15))
        self.lbl_ketdes.place(x=10, y=10)


    def summon_plyr(self, player, row, col, brdc, dt_now):

        def hover_frame(e, wdg1, wdg2, wd3, wd4):
            wdg2.configure(fg=brdc)
            wd3.configure(fg=brdc)
            wd4.configure(fg=brdc)


        def default_frame(e, wdg1, wdg2, wd3, wd4):
            wdg2.configure(fg='#060644')
            wd3.configure(fg='#060644')
            wd4.configure(fg='#060644')

        def tampil(e):
            self.profile_player(player)
            self.window.after(500, lambda:self.geser(self.fr_listplyr, 'kiri', 0, -395))

            first = player.child[7].child[0].child[0].data
            new = dt_now.child[0].data 
            self.skill_ply = [[],[]]
            for cat, item in self.analitic_skill.items():
                val = 0
                val_now = 0
                for itm in item:
                    val += first[itm]
                    val_now += new[itm]
                self.skill_ply[0].append(val/len(item))
                self.skill_ply[1].append(val_now/len(item))
            self.peningkatan(self.skill_ply[0], self.skill_ply[1])


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

    def peningkatan(self, skl_bef, skl_aft):
        try:
            self.lbl_pen.destroy()
            self.fr_upper.destroy()
        except: pass
        self.lbl_pen = Label(self.fr_inp, text='PENINGKATAN PEMAIN', font=('Times', 20, 'bold'), fg='white', bg='#060644')
        self.lbl_pen.place(x=10, y=230, height=70)
        self.fr_upper = CTkFrame(self.fr_inp, fg_color='white', width=800, height=400)
        self.fr_upper.place(x=30, y=300)
        self.subj = ['ATT','TEC','STA','DEF','POW','SPD']
        rw = 0
        cl = 0
        i = 0
        for sub in self.subj:
            if rw >= 3:
                rw = 0
                cl = 1
            self.summon_slider(rw, cl, sub, self.fr_upper, skl_bef[i], skl_aft[i])
            rw += 1
            i += 1
            
        

    def summon_slider(self, nm, cl, dt, fr, stv1, stv2):

        temp_fr = CTkFrame(fr, width=370, height=80, border_color='blue', border_width=1, fg_color='white')
        temp_fr.grid(column=cl, row=nm, pady=5, padx=10)
        lbl = Label(temp_fr, text=dt , bg='white', font=('Times', 20, 'bold'), anchor='w', fg='black')
        lbl.place(x=10, y=1,height=20)
        sld = CTkSlider(temp_fr, bg_color='white', from_=0, to= 100,width=310, button_color='blue', button_hover_color='#45A29E', progress_color='blue', state='disabled', border_width=0)
        sld.place(x=10, y = 30)
        sld.set(stv1)
        hsl = int(sld.get())
        num = Label(temp_fr,text=hsl, bg='white',anchor='w', fg='black', font=('Times', 15, 'bold'))
        num.place(x=330, y=27, width=30, height=20)

        sld1 = CTkSlider(temp_fr, bg_color='white', from_=0, to= 100,width=310, button_color='green', button_hover_color='#45A29E', progress_color='green', state='disabled', border_width=0)
        sld1.place(x=10, y = 50)
        sld1.set(stv2)
        hsl1 = int(sld1.get())
        num1 = Label(temp_fr,text=hsl1, bg='white',anchor='w', fg='black', font=('Times', 15, 'bold'))
        num1.place(x=330, y=47, width=30, height=20)
        
        cng = int(stv2-stv1)
        if cng < 0:
            text=f'- {-cng}'
            clr = 'red'
        elif cng > 0:
            text=f'+ {cng}'
            clr = 'green'
        else:
            text=f'~~'
            clr = 'grey'

        lbl_cng = Label(temp_fr, bg='white', text=text, fg=clr, font=('Times', 12, 'bold'), anchor='w')
        lbl_cng.place(x=80, y=1, width=35)


    def profile_player(self, player):
        try:
            self.fr_identity.destroy()
        except: pass
        self.fr_identity = CTkFrame(self.fr_listplyr, fg_color='#DBDBDB', width=390, height=267, border_color='blue', border_width=3)
        self.fr_identity.place(x=405, y=70)
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
        if arah == 'kiri':
            if x_pos_bef <= x_pos_aft:
                return
            x_pos_bef -= 20
            fr.place_configure(x=x_pos_bef)
            self.window.after(10, lambda: self.geser(fr, arah, x_pos_bef, x_pos_aft))
        elif arah == 'kanan':
            if x_pos_bef >= x_pos_aft:
                return
            x_pos_bef += 20
            fr.place_configure(x=x_pos_bef)
            self.window.after(10, lambda: self.geser(fr, arah, x_pos_bef, x_pos_aft))


# w = Tk()
# fl = open('Data/treeDatabase.pickle', 'rb')
# tree_data = pickle.load(fl)
# fl.close()
# tim = tree_data.child[0].child[0]
# jadwal = tim.child[1].child[0].data
# TrainStatistic(w, tim, jadwal)
# w.mainloop()