from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from datetime import datetime
from tkinter.messagebox import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pickle



class MatchStatistic():

    def __init__(self, window, tim_data, root):
        self.window = window
        self.tim = tim_data
        self.tr_var = root
        self.match = []
        for dt_match in self.tim.child[2].child[0].child:
            self.match.append(dt_match)
        self.window.state('zoomed')
        self.FRAME = Frame(self.window, bg='#093D83', width=1366, height=768)
        self.FRAME.place(x=0, y=0)
        foto = Image.open("Image/Background/bg_1.png").resize((1366, 768))
        self.photoo = ImageTk.PhotoImage(foto)
        self.label_background = Label(self.FRAME, image=self.photoo)
        self.label_background.place(x=-2, y=-2)
        self.fr1 = CTkFrame(self.FRAME, fg_color='#060644', width=1100, height=570)
        self.fr1.place(x=133, y=50)
        self.lbl_ketlstptd = Label(self.fr1, text='Daftar Pertandingan Selesai', font=('Times', 30, 'bold'), fg='white', bg='#060644')
        self.lbl_ketlstptd.place(x=300, y=0, width=500, height=70)
        self.scfr1 = CTkScrollableFrame(self.fr1, fg_color='#DBDBDB', width=1083, height=500, corner_radius=0)
        self.scfr1.place(x=0, y=70)
        rw = 0
        for dt in self.match:
            self.summon_btt_match(fr=self.scfr1,data_list=dt.data, datatree=dt, rw=rw)
            rw += 1
        global img_return0
        img_return0 = ImageTk.PhotoImage(Image.open('Image/return.png').resize((110, 50)))
        self.button_back = Button(self.FRAME, image=img_return0, cursor="hand2", command=lambda : self.FRAME.destroy(), bg='#093D83', relief='flat', borderwidth=0, activebackground='#093D83')
        self.button_back.place(x=35, y=645)

    def prev(self, fr):
        fr.destroy()

    def summon_btt_match(self, fr, data_list, datatree, rw):

        def pencet(e):
            self.statistic(datatree)

        def masuk(e):
            fr_btt.configure(border_width=5)

        def keluar(e):
            fr_btt.configure(border_width=2)

        fr_btt = CTkFrame(master=fr, fg_color='white', border_color='black', border_width=3, width=1045, height=80)
        fr_btt.grid(column=0, row=rw, pady=10, padx=20)
        lbl_tgl = Label(fr_btt, text=data_list[0], fg='black', bg='white', font=('Times', 18, 'bold'))
        lbl_tgl.place(x=20, y=10, width=130)
        lbl_jam = Label(fr_btt, text=data_list[1], fg='black', bg='white', font=('Times', 13, 'bold'))
        lbl_jam.place(x=20, y=40, width=130)
        lbl_vs = Label(fr_btt, text='VS', fg='black', bg='white', font=('Times', 20, 'bold'))
        lbl_vs.place(x=(1045/2)-35, y=5, width=70, height=70)
        lbl_mine = Label(fr_btt, text=self.tim.data.upper(), fg='black', bg='white', font=('Times', 32, 'bold'),anchor='e')
        lbl_mine.place(x=(1045/2)-300, y=5, width=250, height=70)
        lbl_musuh = Label(fr_btt, text=data_list[2].upper(), fg='black', bg='white', font=('Times', 32, 'bold'), anchor='w')
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

    def statistic(self, data):
        self.fr_submain1 = Frame(self.FRAME, bg='#093D83')
        self.fr_submain1.place(x=0, y=0, width=1366, height=768)
        self.label_background1 = Label(self.fr_submain1, image=self.photoo)
        self.label_background1.place(x=-2, y=-2)
        self.fr_title = CTkFrame(self.fr_submain1, fg_color='#060644', width=1326, height=70)
        self.fr_title.place(x=20, y=20)
        self.lbl_vs = CTkLabel(self.fr_title, text='VS', font=('Times', 32, 'bold'), width=80, height=60, text_color='white')
        self.lbl_vs.place(x=623, y=5)
        self.lbl_mygoal = CTkLabel(self.fr_title, text=data.child[2].child[0].data[0], font=('Times', 35, 'bold'), width=60, height=60, corner_radius=30, fg_color='black', text_color='white')
        self.lbl_mygoal.place(x=553, y=5)
        self.lbl_myteam = CTkLabel(self.fr_title, text=self.tim.data, font=('Times', 35, 'bold'), width=200, height=60, anchor='e', text_color='white')
        self.lbl_myteam.place(x=323, y=5)
        self.lbl_enmgoal = CTkLabel(self.fr_title, text=data.child[2].child[0].data[1], font=('Times', 35, 'bold'), width=60, height=60, corner_radius=30, fg_color='black', text_color='white')
        self.lbl_enmgoal.place(x=713, y=5)
        self.lbl_enmteam = CTkLabel(self.fr_title, text=data.data[2], font=('Times', 35, 'bold'), width=200, height=60, anchor='w', text_color='white')
        self.lbl_enmteam.place(x=803, y=5)
        
        self.fr_statistic = CTkFrame(self.fr_submain1, fg_color='white', width=1326, height=555)
        self.fr_statistic.place(x=20, y=90)

        self.fr_pengbol = CTkFrame(self.fr_statistic, fg_color='#060644', width=400, height=300)
        self.fr_pengbol.place(x=10, y=10)
        labels_pengbol = ['My Team',f'{data.data[2]}']
        control = data.child[2].child[-1].data[0]
        sizes_pengbol = [control, 100-control]
        self.summon_pie(self.fr_pengbol, labels=labels_pengbol, sizes=sizes_pengbol, x_pos=5, y_pos=45, width=390, height=250)
        self.lbl_pengbol = CTkLabel(self.fr_pengbol, text='Penguasaan Bola', font=('Times', 35, 'bold'), width=390, height=40, fg_color='white')
        self.lbl_pengbol.place(x=5, y=5)

        self.fr_passbol = CTkFrame(self.fr_statistic, fg_color='#060644', width=400, height=300)
        self.fr_passbol.place(x=420, y=10)
        labels_passbol = ['Good','Bad']
        passing = data.child[2].child[-1].data[1]
        sizes_passbol = [passing, 100-passing]
        self.summon_pie(self.fr_passbol, labels=labels_passbol, sizes=sizes_passbol, x_pos=5, y_pos=45, width=390, height=250)
        self.lbl_passbol = CTkLabel(self.fr_passbol, text='Umpan Bola', font=('Times', 35, 'bold'), width=390, height=40, fg_color='white')
        self.lbl_passbol.place(x=5, y=5)

        self.fr_shotbol = CTkFrame(self.fr_statistic, fg_color='white', width=810, height=205, border_color='#060644', border_width=5)
        self.fr_shotbol.place(x=10, y=330)
        global gambar
        img = Image.open('Image/gawang.png').resize((350,160))
        gambar = ImageTk.PhotoImage(img)
        self.lbl_gawang = Label(self.fr_shotbol, image=gambar, bg='white')
        self.lbl_gawang.place(x=5, y=5)
        shot = data.child[2].child[-1].data[2]
        self.lbl_akurat = Label(self.fr_shotbol, text=shot[0], bg='white', font=('Times', 25, 'bold'))
        self.lbl_akurat.place(x=152, y=95)
        self.lbl_mleset = Label(self.fr_shotbol, text=shot[1], bg='white', font=('Times', 25, 'bold'))
        self.lbl_mleset.place(x=302, y=18)
        self.lbl_ketakurat = Label(self.fr_shotbol, text='Tembakan Akurat:', bg='white', font=('Times', 15, 'bold'), anchor='w')
        self.lbl_ketakurat.place(x=420, y=5)
        self.lbl_totakurat = Label(self.fr_shotbol, text=shot[0], bg='white', font=('Times', 15, 'bold'))
        self.lbl_totakurat.place(x=605, y=5)
        self.lbl_ketmleset = Label(self.fr_shotbol, text='Tembakan Meleset:', bg='white', font=('Times', 15, 'bold'), anchor='w')
        self.lbl_ketmleset.place(x=420, y=30)
        self.lbl_totmleset = Label(self.fr_shotbol, text=shot[1], bg='white', font=('Times', 15, 'bold'))
        self.lbl_totmleset.place(x=605, y=30)
        self.lbl_ketefshot =Label(self.fr_shotbol, text='Efisiensi Tembakan:', bg='white', font=('Times', 15, 'bold'), anchor='w')
        self.lbl_ketefshot.place(x=420, y=110)
        self.fr_pieshot = CTkFrame(self.fr_shotbol, fg_color='#060644', width=140, height=140)
        self.fr_pieshot.place(x=605, y=55)
        efisiensi = int((shot[0]/sum(shot))*100)
        self.summon_pieshot(self.fr_pieshot, sizes=[efisiensi, 100-efisiensi], x_pos=0, y_pos=0, width=140, height=140)
        self.lbl_perspie = Label(self.fr_pieshot, text=f'{efisiensi}%', font=('Times', 17, 'bold'), bg='white')
        self.lbl_perspie.place(x=57, y=57)



        self.fr_plylist = CTkFrame(self.fr_statistic, fg_color='#060644', width=486, height=525)
        self.fr_plylist.place(x=830, y=10)
        self.lbl_plylist = CTkLabel(self.fr_plylist, fg_color='white', width=476, height=40, text='Daftar Pemain', font=('Times', 35, 'bold'))
        self.lbl_plylist.place(x=5, y=5)
        self.fr_ketplylist = CTkFrame(self.fr_plylist, fg_color='white', width=476, height=475, corner_radius=0)
        self.fr_ketplylist.place(x=5, y=45)
        self.lbl_ketpos = CTkLabel(self.fr_ketplylist, text='POS', fg_color='white', font=('Times', 10), width=35, height=35)
        self.lbl_ketpos.place(x=5, y=5)
        self.lbl_ketname = CTkLabel(self.fr_ketplylist, text='NAME PLAYER', fg_color='white', font=('Times', 20, 'bold'), height=35)
        self.lbl_ketname.place(x=50, y=5)
        self.lbl_ycard = CTkLabel(self.fr_ketplylist, text='', fg_color='yellow', height=35, width=25)
        self.lbl_ycard.place(x=280, y=5)
        self.lbl_rcard = CTkLabel(self.fr_ketplylist, text='', fg_color='red', height=35, width=25)
        self.lbl_rcard.place(x=320, y=5)
        self.lbl_ketgoal = CTkLabel(self.fr_ketplylist, text='GOAL', fg_color='white', height=35, width=50, font=('Times', 20))
        self.lbl_ketgoal.place(x=370, y=5)
        self.sc_plylist = CTkScrollableFrame(self.fr_ketplylist, fg_color='white', width=456, height=425)
        self.sc_plylist.place(x=0, y=40)
        plylist = []
        for ply in self.tim.child[0].child:
            if ply.data[0] in data.child[0].data or ply.data[0] in data.child[1].data:
                lst = [ply]
                if data.child[2].child[0].data[0] > 0:
                    itemp_gol = 0
                    for plygol in data.child[2].child[0].child[0].data:
                        if ply.data[0] in plygol:
                            lst.append(plygol[1])
                            itemp_gol += 1
                            break
                    if itemp_gol == 0:
                        lst.append(0)
                else: lst.append(0)

                if sum(data.child[2].child[1].data) > 0:
                    itemp_card = 0
                    for plycard in data.child[2].child[1].child[0].data:
                        if ply.data[0] in plycard:
                            lst.append(plycard[1])
                            lst.append(plycard[2])
                            itemp_card += 1
                    if itemp_card == 0:
                        lst.append(0)
                        lst.append(0)
                else:
                    lst.append(0)
                    lst.append(0)

                plylist.append(lst)
        rw = 0
        for matchply in plylist:
            self.summon_plyr(self.sc_plylist, matchply[0], rw, 0, matchply[2], matchply[3], matchply[1])
            rw += 1
        self.btt_back = Button(self.fr_submain1, image=img_return0, cursor="hand2", command=lambda : self.fr_submain1.destroy(), bg='#093D83', relief='flat', borderwidth=0, activebackground='#093D83')
        self.btt_back.place(x=35, y=645)


    def summon_pie(self, fr, sizes, labels, x_pos, y_pos, width, height):
        explode = (0.1, 0)
        fig = Figure(figsize=(10,10))

        ax = fig.add_subplot()
        ax.pie(sizes, explode=explode, labels=labels, autopct='%i%%', startangle=90, colors=['#121288', 'grey'])

        canvas = FigureCanvasTkAgg(fig, master = fr)
        canvas.draw()
        canvas.get_tk_widget().place(x = x_pos, y = y_pos, width=width, height=height)


    def summon_pieshot(self, fr, sizes, x_pos, y_pos, width, height):
        fig = Figure(figsize=(10,10))

        ax = fig.add_subplot()
        ax.pie(sizes, startangle=90, colors=['#060644', 'white'], wedgeprops=dict(width=0.5))

        canvas = FigureCanvasTkAgg(fig, master = fr)
        canvas.draw()
        canvas.get_tk_widget().place(x = x_pos, y = y_pos, width=width, height=height)


    def summon_plyr(self, fr, player, row, col, jum_ycard, jum_rcard, jum_gol):

        fr_btt = CTkFrame(fr, width=450, height=40, fg_color='white')
        fr_btt.grid(row=row, column=col, pady=3)

        lbl_pos = Label(fr_btt, text=player.child[5].data, font=('Times', 10, 'bold'), bg='white', fg='black')
        lbl_pos.place(x=0, y=0, height=40, width=35)
        lbl_nama = Label(fr_btt, text=player.data[0].upper(), font=('Times', 20, 'bold'), bg='white', fg='black')
        lbl_nama.place(x=40, y=0, height=40)
        lbl_ycard = Label(fr_btt, text=jum_ycard, font=('Times', 14, 'bold'), bg='white', fg='black')
        lbl_ycard.place(x=280, y=0, height=40)
        lbl_rcard = Label(fr_btt, text=jum_rcard, font=('Times', 14, 'bold'), bg='white', fg='black')
        lbl_rcard.place(x=320, y=0, height=40)
        lbl_gol = Label(fr_btt, text=jum_gol, font=('Times', 14, 'bold'), bg='white', fg='black')
        lbl_gol.place(x=380, y=0, height=40, width=30)



# w = Tk()
# fl = open('Data/treeDatabase.pickle', 'rb')
# tree_data = pickle.load(fl)
# fl.close()
# MatchStatistic(w, tree_data.child[0].child[0], tree_data)
# w.mainloop()