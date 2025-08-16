from tkinter import *
from customtkinter import *
import pickle
from PIL import Image, ImageTk
import numpy as np
from sklearn.svm import SVC
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Code.AddTrain import AddDataTrain
from Code.Train_Sta import TrainStatistic
from Code.AddMatch import AddDataMatch
from Code.Match_Sta import MatchStatistic
from Code.Input_Skill import InputSkill


class AnaliticMenu():
    pic_list = []
    def __init__(self, window, tim_data, root):
        self.window = window
        self.window.state('zoomed')
        self.tr_var = root

        self.tim = tim_data

        self.FRAME = Frame(self.window, bg='#093D83', width=1366, height=768)
        self.FRAME.place(x=0, y=0)
        foto = Image.open("Image/Background/bg_1.png").resize((1366, 768))
        self.photoo = ImageTk.PhotoImage(foto)
        self.label_background = Label(self.FRAME, image=self.photoo)
        self.label_background.place(x=-2, y=-2)

        global img_return0
        img_return0 = ImageTk.PhotoImage(Image.open('Image/return.png').resize((110, 50)))
        self.button_back = Button(self.FRAME, image=img_return0, cursor="hand2", command=lambda : self.FRAME.destroy(), bg='#093D83', relief='flat', borderwidth=0, activebackground='#093D83')
        self.button_back.place(x=35, y=645)
        self.fr1 = Frame(self.FRAME, bg='#060644')
        self.fr1.place(x=30, y=10, width=550, height=640)
        self.lbl_head1 = CTkLabel(self.fr1, text='PLAYERS STATISTIC', font=('Times', 30, 'bold'), fg_color='#060644', text_color='white', width=530, height=60, anchor='w')
        self.lbl_head1.place(x=10, y=10)
        self.btt_addskill = CTkButton(self.fr1, text='(+) Tambah Kemampuan Pemain', width=530, height=50, command=self.Add_skill, fg_color='#060644', font=('Times', 20, 'bold'), hover_color='#000630')
        self.btt_addskill.place(x=10, y=590)
        # self.btt_refresh = CTkButton(self.fr1, text='Refresh', width=60, height=20, command=self.refresh)
        # self.btt_refresh.place(x=5, y=5)
        try:
            self.jadwal_train = self.tim.child[1].child[0].data
        except:
            self.jadwal_train = []
        try:
            self.jadwal_match = self.tim.child[2].child[0].data
        except:
            self.jadwal_match = []
        self.subj = ['ATT','TEC','STA','DEF','POW','SPD']
        self.mean = [0,0,0,0,0,0]
        self.analitic_skill = {
                                'ATT': [0, 1, 2, 4, 24],
                                'TEC': [3, 4, 5, 6, 7, 8, 9],
                                'STA': [12, 13, 14, 17],
                                'DEF': [20, 21, 22, 26, 27, 28],
                                'POW': [15, 16, 18, 19, 23, 25],
                                'SPD': [10, 11]
                                }
        
        i = self.checking()
        if i == 0:
            self.Add_skill()
        self.fr_listplyr = CTkScrollableFrame(self.fr1, bg_color='black', width=533, height=505, fg_color='#DBDBDB')
        self.fr_listplyr.place(x=0, y=80)
        for ply in self.ply_list:
            self.summon_plyr(player=ply[0], row=ply[1], col=0, gambar=AnaliticMenu.pic_list[ply[1]], skll=ply[2])

        self.fr2 = CTkFrame(self.FRAME, width=480, height=240, fg_color='white')
        self.fr2.place(x=760, y=130)
        self.lbl_train = CTkLabel(self.fr2, text='Statistik Latihan', font=('Times', 30, 'bold'), width=400)
        self.lbl_train.place(x=40, y=0)

        ft_add = Image.open('Image/adddata.png').resize((105,105))
        global img_add
        img_add = ImageTk.PhotoImage(ft_add)

        ft_sta = Image.open('Image/statistic_icon.png').resize((115,105))
        global img_sta
        img_sta = ImageTk.PhotoImage(ft_sta)
        self.btt_addtrain = CTkButton(self.fr2, image=img_add, text='', width=155, height=155, command=self.Train_data, corner_radius=20, fg_color='#060644', hover_color='black')
        self.btt_addtrain.place(x=35, y=65)
        self.btt_trainstt = CTkButton(self.fr2, image=img_sta, text='', width=155, height=155, command=self.Train_statistic, corner_radius=20, fg_color='#060644', hover_color='black')
        self.btt_trainstt.place(x=290, y=65)

        self.fr3 = CTkFrame(self.FRAME, width=480, height=240, fg_color='white')
        self.fr3.place(x=760, y=400)
        self.lbl_match = CTkLabel(self.fr3, text='Statistik Pertandingan', font=('Times', 30, 'bold'), width=400)
        self.lbl_match.place(x=40, y=0)
        self.btt_addmatch = CTkButton(self.fr3, image=img_add, text='', width=155, height=155, corner_radius=20, fg_color='#060644', hover_color='black', command=self.Match_data)
        self.btt_addmatch.place(x=35, y=65)
        self.btt_matchstt = CTkButton(self.fr3, image=img_sta, text='', width=155, height=155, corner_radius=20, fg_color='#060644', hover_color='black', command=self.Match_statistic)
        self.btt_matchstt.place(x=290, y=65)

        fl_ml = open('Data/ML_pos_svc.pickle', 'rb')
        self.ml_pos = pickle.load(fl_ml)

    def refresh(self):
        try:
            self.fr_listplyr.destroy()
        except: pass
        self.checking()
        self.fr_listplyr = CTkScrollableFrame(self.fr1, bg_color='black', width=533, height=505, fg_color='#DBDBDB')
        self.fr_listplyr.place(x=0, y=80)
        for ply in self.ply_list:
            self.summon_plyr(player=ply[0], row=ply[1], col=0, gambar=AnaliticMenu.pic_list[ply[1]], skll=ply[2])

    def checking(self):
        AnaliticMenu.pic_list.clear()
        i = 0
        self.ply_list = []
        for player in self.tim.child[0].child:
            try:
                data_skill = player.child[6].child[0].data
            except: continue
            skill_ply = []
            for cat, item in self.analitic_skill.items():
                val = 0
                for itm in item:
                    val += data_skill[itm]
                val /= len(item)
                self.mean[self.subj.index(cat)] += val
                skill_ply.append(val/100)
            img = Image.open('Image/icon_player.png').resize((50,50))
            global gmbr
            gmbr = ImageTk.PhotoImage(img)
            AnaliticMenu.pic_list.append(gmbr)
            l_ply = (player, i, skill_ply)
            self.ply_list.append(l_ply)
            i += 1

        if i != 0:
            for m in range(len(self.mean)):
                self.mean[m] = self.mean[m]/(i*100)

        return i

    def Add_skill(self):
        InputSkill(self.window, self.tim, self.tr_var, self)

    def summon_plyr(self, player, row, col, gambar, skll):

        def hover_frame(e, wdg1, wdg2, wd3, wd4):
            wdg1.configure(border_width = 6)
            # wdg2.configure(fg='#ff9800')
            # wd3.configure(fg='#ff9800')
            # wd4.configure(fg='#ff9800')
            # wdg1.configure(fg_color='grey')
            # wdg2.configure(bg='grey')
            # wd3.configure(bg='grey')
            # wd4.configure(bg='grey')

        def default_frame(e, wdg1, wdg2, wd3, wd4):
            wdg1.configure(border_width = 2)

        def tampil(e):
            self.statistic(player, skll)

        fr_btt = CTkFrame(self.fr_listplyr, width=530, height=70, border_width=2, border_color='black', fg_color='#DBDBDB')
        fr_btt.grid(row=row, column=col, pady=10)
 
        lbl_gmbr = Label(fr_btt, image=gambar, bg='#DBDBDB', fg='#060644')
        lbl_gmbr.place(x=10, y=10)
        lbl_nama = Label(fr_btt, text=player.data[0].upper(), font=('Times', 15, 'bold'), bg='#DBDBDB', fg='#060644')
        lbl_nama.place(x=60, y=10, height=50)
        lbl_pos = Label(fr_btt, text=player.child[5].data, font=('Times', 15, 'bold'), bg='#DBDBDB', fg='#060644')
        lbl_pos.place(x=450, y=10, width=75, height=50)

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

    def statistic(self, player, skll):
        self.fr_plyr = CTkFrame(self.FRAME, fg_color='white', width=1300, height=690, corner_radius=30)
        self.fr_plyr.place(x=30, y=10)
        self.btt_back = CTkButton(self.fr_plyr, text='<=', width=30, height=30, corner_radius=30, command=self.back)
        self.btt_back.place(x=10, y=10)
        self.summon_radar(self.subj, skll)
        self.profile_player(player)
        self.pos_recom(player.child[6].child[0].data, player.child[4].data)
        self.rincian_skill(skll)
        self.summon_linechart(player)
        
    def summon_radar(self, subj, skill):
        self.fr_radar = CTkFrame(self.fr_plyr, fg_color='white', width=350, height=350, border_width=5, border_color='red')
        self.fr_radar.place(x=930, y=320)
        self.fr_cvrdr = CTkFrame(self.fr_radar, fg_color='black', width=300, height=300)
        self.fr_cvrdr.place(x=25, y=40)

        angles = np.linspace(0, 2*np.pi, len(subj),endpoint=(False))
        angles = np.concatenate((angles,[angles[0]]))

        subj.append(subj[0])
        skill.append(skill[0])
        self.mean.append(self.mean[0])

        fig = Figure(figsize=(3,3))
        ax = fig.add_subplot(polar=True)
        ax.plot(angles, [1,1,1,1,1,1,1], color='w')

        ax.plot(angles, self.mean, 'o--', color='r', label='Average')
        ax.fill(angles, self.mean, alpha=0.25, color='r')

        ax.plot(angles, skill, 'o--', color='g', label='Player')
        ax.fill(angles, skill, alpha=0.25, color='g')

        ax.set_facecolor('white')
        

        ax.set_thetagrids(angles * 180/np.pi, subj)

        canvas1 = FigureCanvasTkAgg(fig, self.fr_cvrdr)
        canvas1.draw()
        canvas1.get_tk_widget().place(x=0, y=0)
        subj.pop()
        skill.pop()
        self.mean.pop()
        
        self.fr_legends = CTkFrame(self.fr_radar, fg_color='white', width=80, height=50)
        self.fr_legends.place(x=220, y=5)
        self.lbl_clr1 = CTkLabel(self.fr_legends, fg_color='red', width=10, height=5, text='')
        self.lbl_clr1.grid(row=0, column=0, pady=5)
        self.lbl_clr2 = CTkLabel(self.fr_legends, fg_color='green', width=10, height=5, text='')
        self.lbl_clr2.grid(row=1, column=0, pady=5)
        self.lbl_name1 = CTkLabel(self.fr_legends, text='Avarage', anchor='w')
        self.lbl_name1.grid(row=0, column=1, padx=5)
        self.lbl_name2 = CTkLabel(self.fr_legends, text='Player', anchor='w')
        self.lbl_name2.grid(row=1, column=1,padx=5, sticky='w')

    def profile_player(self, player):
        self.fr_idnplyr = CTkFrame(self.fr_plyr, fg_color='white', width=350, height=620, border_width=5, border_color='red')
        self.fr_idnplyr.place(x=15, y=50)
        try:
            self.fr_identity.destroy()
            self.lbl_name.destroy()
        except: pass
        self.lbl_name = CTkLabel(self.fr_idnplyr, text=player.data[0].upper(), width=310, height=30, text_color='black', font=('russo one', 18, 'bold'))
        self.lbl_name.place(x=20, y=300)
        self.fr_identity = CTkFrame(self.fr_idnplyr, fg_color='white', width=328, height=232, border_color='red', border_width=3)
        self.fr_identity.place(x=12, y=350)
        self.lbl_birth = CTkLabel(self.fr_identity, text=f'BIRTHDAY\n{player.child[0].data}', width=110, height=50, anchor='w', text_color='black', font=('russo one', 13, 'bold'))
        self.lbl_birth.place(x=22, y=16)
        self.lbl_height = CTkLabel(self.fr_identity, text=f'HEIGHT\n{player.child[1].data}', width=110, height=50, anchor='w', text_color='black', font=('russo one', 13, 'bold'))
        self.lbl_height.place(x=22, y=85)
        self.lbl_weight = CTkLabel(self.fr_identity, text=f'WEIGHT\n{player.child[2].data}', width=110, height=50, anchor='w', text_color='black', font=('russo one', 13, 'bold'))
        self.lbl_weight.place(x=22, y=160)
        kaki = player.child[4].data
        if kaki == 'Kanan':
            path_img = 'Image/right_feet.png'
        elif kaki == 'Kiri':
            path_img = 'Image/left_feet.png'
        img_open = Image.open(path_img).resize((85,75))
        global gambar
        gambar = ImageTk.PhotoImage(img_open)
        self.lbl_prefot = CTkLabel(self.fr_identity, text=f'PREFFERD FOOT\n{kaki.upper()}', width=150, height=55, text_color='black', font=('russo one', 13, 'bold'))
        self.lbl_prefot.place(x=160, y=5)
        self.lbl_imgfot = Label(self.fr_identity, image=gambar, bg='white')
        self.lbl_imgfot.place(x=195, y=50)
        self.lbl_position = CTkLabel(self.fr_identity, text=f'POSITION\n{player.child[5].data}', width=160, height=50, text_color='black', font=('russo one', 13, 'bold'))
        self.lbl_position.place(x=160, y=150)
        self.lbl_identity = CTkLabel(self.fr_idnplyr, text= 'IDENTITY', width=80, height=15, text_color='red', font=('russo one', 13, 'italic'), fg_color='transparent')
        self.lbl_identity.place(x=30,y=340)

    def pos_recom(self, data_skill, foot):

        if foot == 'Kanan':
            foot = 1
        else: foot = 0


        lst = []
        for num in data_skill:
            lst.append(num)

        lst.insert(0, foot)
        value = []
        dt = np.array([lst])

        for row in dt:
            arai = [row[0]]
            for i in range(1,30):
                val = (row[i]-0)/100
                arai.append(val)
            value.append(arai)
        hasil = self.ml_pos.predict(value)

        self.fr_recom = CTkFrame(self.fr_plyr, fg_color='white', width=350, height=250, border_color='red', border_width=5)
        self.fr_recom.place(x=930, y=50)
        self.lbl_pos1 = CTkLabel(self.fr_recom, text='Recomendation\nPosition', font=('Times', 30, 'bold'), width=340)
        self.lbl_pos1.place(x=5, y=5)
        self.lbl_pos2 = CTkLabel(self.fr_recom, text=f'{hasil[0]}', font=('Times', 40, 'bold'), width=340)
        self.lbl_pos2.place(x=5, y=100)

    def rincian_skill(self, skll):
        self.fr_rinc = CTkScrollableFrame(self.fr_plyr, fg_color='white',width=500, height=330, border_color='red', border_width=5, scrollbar_fg_color='white', scrollbar_button_color='red', scrollbar_button_hover_color='pink')
        self.fr_rinc.place(x=385, y=320)
        i = 0
        for gol in self.subj:
            self.summon_slider(i, 0, gol, self.fr_rinc,  int(skll[i]*100))
            i+=1

    def summon_linechart(self, player):
        self.fr_lc = CTkFrame(self.fr_plyr, width=530, height=250, fg_color='black')
        self.fr_lc.place(x=385, y=50)

        histori = []
        for dt in player.child[7].child:
            histori.append([dt.data,dt.child[0].data])

        big_place = []
        for tg in histori:
            skill_ply = [0,100]
            for cat, item in self.analitic_skill.items():
                val = 0
                for itm in item:
                    val += tg[1][itm]
                skill_ply.append(val/len(item))
            big_place.append(skill_ply)

        arr = np.array(big_place)
        at = arr.transpose()

        x = []
        for dt in histori:
            x.append(dt[0])

        fig = Figure(figsize=(5,2.5))
        plt = fig.add_subplot()

        plt.plot(x, at[0], c='w')
        plt.plot(x, at[1], c='w')
        plt.plot(x, at[2], c='r', marker='o')
        plt.plot(x, at[3], c='g', marker='o')
        plt.plot(x, at[4], c='b', marker='o')
        plt.plot(x, at[5], c='y', marker='o')
        plt.plot(x, at[6], c='purple', marker='o')
        plt.plot(x, at[7], c='black', marker='o')

        canvas = FigureCanvasTkAgg(fig, master = self.fr_lc) 
        canvas.draw()
        canvas.get_tk_widget().place(x=5, y=5, width=520, height=240)


    def summon_slider(self, nm, cl, dt, fr, stv):

        temp_fr = CTkFrame(fr, width=450, height=75, border_color='blue', border_width=1, fg_color='white')
        temp_fr.grid(column=cl, row=nm, pady=5, padx=10)
        lbl = Label(temp_fr, text=dt , bg='white', font=('Times', 20, 'bold'), anchor='w', fg='black')
        lbl.place(x=10, y=0,height=20)
        sld = CTkSlider(temp_fr, bg_color='white', from_=0, to= 100,width=390, button_color='blue', button_hover_color='#45A29E', progress_color='blue', state='disabled', border_width=0)
        sld.place(x=10, y = 30)
        sld.set(stv)
        hsl = int(sld.get())
        num = Label(temp_fr,text=hsl, bg='white',anchor='w', fg='black', font=('Times', 15, 'bold'))
        num.place(x=405, y=27, width=40, height=20)

    def Train_data(self):
        AddDataTrain(window=self.FRAME, tim_data=self.tim, sch=self.jadwal_train, root=self.tr_var)

    def Train_statistic(self):
        TrainStatistic(window=self.FRAME, tim_data=self.tim, sch=self.jadwal_train)
    
    def Match_data(self):
        AddDataMatch(self.window, self.tim, self.tr_var, self.jadwal_match)

    def Match_statistic(self):
        MatchStatistic(self.window, self.tim, self.tr_var)

    def back(self):
        self.fr_plyr.destroy()

    def close(self):
        self.FRAME.destroy()


# w = Tk()
# fl = open('Data/treeDatabase.pickle', 'rb')
# tree_data = pickle.load(fl)
# fl.close()
# AnaliticMenu(w, tree_data.child[0].child[0], tree_data)
# w.mainloop()