from tkinter import *
from customtkinter import *
from tkcalendar import Calendar
from PIL import Image, ImageTk
import pickle
from Code.Input_data import Input_Data
from Tree_Processing import TreeNode


class PlayersManagement():
    def __init__(self, window, tim_data, root):
        self.window = window
        self.tim = tim_data
        self.tr_var = root
        self.window.state('zoomed')
        self.FRAME = Frame(self.window, bg='#093D83', width=1366, height=768)
        self.FRAME.place(x=0, y=0)
        foto = Image.open("Image/Background/bg_4.png").resize((1366,768))
        self.photoo = ImageTk.PhotoImage(foto)
        self.label_background = Label(self.FRAME, image=self.photoo)
        self.label_background.place(x=-2, y=-2)
        self.fr_listply = CTkFrame(self.FRAME, fg_color='#060644', width=1200, height=600)
        self.fr_listply.place(x=83, y=30)
        self.lbl_listply = Label(self.fr_listply, text='DAFTAR PEMAIN DALAM TIM', font=('Times', 32, 'bold'), bg='#060644', fg='#DBDBDB')
        self.lbl_listply.place(x=100, y=0, width=1000, height=70)
        self.sc_listply = CTkScrollableFrame(self.fr_listply, fg_color='#DBDBDB', width=1183, height=455, corner_radius=0)
        self.sc_listply.place(x=0, y=70)
        rw = 0
        for ply in self.tim.child[0].child:
            self.summon_button(self.sc_listply, ply, rw, 'white')
            rw += 1
        # self.btt_back = CTkButton(self.fr_listply, text='Cancel', command=lambda: self.prev(self.FRAME))
        # self.btt_back.place(x=10, y=10)
        self.btt_add = CTkButton(self.fr_listply, text='+ Tambah Pemain', width=500, height=70, fg_color='#060644', hover_color='#000630', font=('Times', 32, 'bold'), command=self.input_player)
        self.btt_add.place(x=350, y=530)
        global img_return0
        img_return0 = ImageTk.PhotoImage(Image.open('Image/return.png').resize((110, 50)))
        self.button_back = Button(self.FRAME, image=img_return0, cursor="hand2", command=lambda : self.FRAME.destroy(), bg='#093D83', relief='flat', borderwidth=0, activebackground='#093D83')
        self.button_back.place(x=35, y=635)

    def input_player(self):
        Input_Data(self.window, 1366, 768, self.tim, self.tr_var, 1)


    def prev(self, fr):
        fr.destroy()

    def summon_button(self, frame, plyr, row, border):
        def detail():
            self.Identitas(plyr)
        
        def masuk(e):
            fr_ply.configure(border_width=5)

        def keluar(e):
            fr_ply.configure(border_width=2)

        fr_ply = CTkFrame(frame, width=1150, height= 65, fg_color='#DBDBDB', border_width=2, border_color=border)
        fr_ply.grid(row=row, column=0, sticky='w', pady=15, padx=20)
        fr_ply.bind("<Button-1>", lambda e: detail())
        fr_ply.bind("<Enter>", masuk)
        fr_ply.bind("<Leave>", keluar)
        lbl1 = Label(fr_ply, text=plyr.data[0].upper(), bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 25))
        lbl1.place(x=5, y=7, height= 50)
        lbl1.bind("<Button-1>", lambda e: detail())
        lbl2 = Label(fr_ply, text=plyr.child[5].data, bg='#DBDBDB', fg='#060644', anchor='e', font=('Bookman Old Style', 25))
        lbl2.place(x=1040, y=7,width=100, height= 50)
        lbl2.bind("<Button-1>", lambda e: detail())

    def Identitas(self, ply):
        self.fr_submain1 = Frame(self.FRAME, bg='#093D83')
        self.fr_submain1.place(x=0, y=0, width=1366, height=768)
        self.lbl_bg = Label(self.fr_submain1, image=self.photoo)
        self.lbl_bg.place(x=-2, y=-2)

        self.fr_identity = CTkFrame(self.fr_submain1, fg_color='#DBDBDB', width=1246, height=600)
        self.fr_identity.place(x=60, y=30)

        self.fr_plyid = CTkFrame(self.fr_identity, fg_color='white', width=880, height=270, border_width=3, border_color='#060644')
        self.fr_plyid.place(x=336, y=20)
        self.lbl_name = Label(self.fr_plyid, text=ply.data[0].upper(), font=('Times', 25, 'bold'), bg='white', fg='#060644')
        self.lbl_name.place(x=10, y=10)
        self.lbl_ketteam = Label(self.fr_plyid, text='TIM:', font=('Times', 20, 'bold'), bg='white', fg='#060644')
        self.lbl_ketteam.place(x=10, y=70)
        self.lbl_team = Label(self.fr_plyid, text=self.tim.data.upper(), font=('Times', 20, 'bold'), bg='white', fg='#060644')
        self.lbl_team.place(x=150, y=70)
        self.lbl_ketheight = Label(self.fr_plyid, text='Tinggi:', font=('Times', 20, 'bold'), bg='white', fg='#060644')
        self.lbl_ketheight.place(x=10, y=130)
        self.lbl_height = Label(self.fr_plyid, text=f'{ply.child[1].data} cm', font=('Times', 20, 'bold'), bg='white', fg='#060644')
        self.lbl_height.place(x=150, y=130)
        self.lbl_ketweight = Label(self.fr_plyid, text='Berat:', font=('Times', 20, 'bold'), bg='white', fg='#060644')
        self.lbl_ketweight.place(x=10, y=190)
        self.lbl_weight = Label(self.fr_plyid, text=f'{ply.child[2].data} kg', font=('Times', 20, 'bold'), bg='white', fg='#060644')
        self.lbl_weight.place(x=150, y=190)

        self.lbl_ketbirth = Label(self.fr_plyid, text='Kelahiran:', font=('Times', 20, 'bold'), bg='white', fg='#060644')
        self.lbl_ketbirth.place(x=400, y=70)
        self.lbl_birth = Label(self.fr_plyid, text=ply.child[0].data, font=('Times', 20, 'bold'), bg='white', fg='#060644')
        self.lbl_birth.place(x=600, y=70)
        self.lbl_ketfoot = Label(self.fr_plyid, text='Kaki Dominan:', font=('Times', 20, 'bold'), bg='white', fg='#060644')
        self.lbl_ketfoot.place(x=400, y=130)
        self.lbl_foot = Label(self.fr_plyid, text=ply.child[4].data, font=('Times', 20, 'bold'), bg='white', fg='#060644')
        self.lbl_foot.place(x=600, y=130)
        self.lbl_ketpos = Label(self.fr_plyid, text='Posisi:', font=('Times', 20, 'bold'), bg='white', fg='#060644')
        self.lbl_ketpos.place(x=400, y=190)
        self.lbl_pos = Label(self.fr_plyid, text=ply.child[5].data, font=('Times', 20, 'bold'), bg='white', fg='#060644')
        self.lbl_pos.place(x=600, y=190)


        self.fr_plypic = CTkFrame(self.fr_identity, border_width=3, border_color='#060644', fg_color='white', width=250, height=270)
        self.fr_plypic.place(x=43, y=20)
        gmbr = Image.open('Image/icon_playernum.png').resize((235,235))
        global img
        img = ImageTk.PhotoImage(gmbr)
        gmbr.close()
        self.lbl_img = Label(self.fr_plypic, image=img, bg='white')
        self.lbl_img.place(x=5, y=25)
        self.lbl_no = Label(self.fr_plypic, text=ply.data[1], font=('Roboto', 50, 'bold'), bg='white', anchor='n')
        self.lbl_no.place(x=50, y=185, width=150, height=80)


        self.fr_plytrain = CTkFrame(self.fr_identity, border_width=3, border_color='#060644', fg_color='white', width=430, height=270)
        self.fr_plytrain.place(x=336, y=305)
        self.lbl_kettrain = Label(self.fr_plytrain, text='Riwayat Latihan', font=('Times', 25, 'bold'), bg='#060644', fg="white")
        self.lbl_kettrain.place(x=3, y=3, width=424, height=47)
        self.sc_train = CTkScrollableFrame(self.fr_plytrain, fg_color='white', width=400, height=210, corner_radius=0)
        self.sc_train.place(x=5, y=50)
        try:
            rw_tr = 0
            for dt_train in ply.child[7].child:
                if dt_train.data == 0: continue
                self.summon_lbl_train(dt_train.data, rw_tr)
                rw_tr += 1
        except: Label(self.sc_train, text='Data Kosong', font=('Times', 20, 'bold'), fg='#060644', bg='white').grid()


        self.fr_plymatch = CTkFrame(self.fr_identity, border_width=3, border_color='#060644', fg_color='white', width=430, height=270)
        self.fr_plymatch.place(x=786, y=305)
        self.lbl_ketmatch = Label(self.fr_plymatch, text='Riwayat Pertandingan', font=('Times', 25, 'bold'), bg='#060644', fg='white')
        self.lbl_ketmatch.place(x=3, y=3, width=424, height=47)
        self.sc_match = CTkScrollableFrame(self.fr_plymatch, fg_color='white', width=400, height=210, corner_radius=0)
        self.sc_match.place(x=5, y=50)
        try:
            rw_mt = 0
            for dt_match in ply.child[8].child:
                self.summon_lbl_match(dt_match, rw_mt)
                rw_mt += 1
        except: Label(self.sc_match, text='Data Kosong', font=('Times', 20, 'bold'), fg='#060644', bg='white').grid()
        
        self.fr_plytotal = CTkFrame(self.fr_identity, border_width=3, border_color='#060644', fg_color='white', width=276, height=200)
        self.fr_plytotal.place(x=30, y=305)
        self.lbl_ketttltrain = Label(self.fr_plytotal, text='Total Latihan:', font=('Times', 20, 'bold'), bg='white', fg='#060644')
        self.lbl_ketttltrain.place(x=5, y=10)
        try:
            ttl_train = len(ply.child[7].child)-1
        except: ttl_train = 0
        if ttl_train < 0:
            ttl_train = 0
        self.lbl_ttltrain = Label(self.fr_plytotal, text=ttl_train, font=('Times', 20, 'bold'), bg='white', fg='#060644')
        self.lbl_ttltrain.place(x=200, y=10)
        self.lbl_ketttlmatch = Label(self.fr_plytotal, text='Total\nPertandingan:', font=('Times', 20, 'bold'), bg='white', fg='#060644', justify='left', anchor='nw')
        self.lbl_ketttlmatch.place(x=5, y=55)
        try:
            ttl_match = len(ply.child[8].child)
        except: ttl_match = 0
        if ttl_match < 0:
            ttl_match = 0
        self.lbl_ttlmatch = Label(self.fr_plytotal, text=ttl_match, font=('Times', 20, 'bold'), bg='white', fg='#060644')
        self.lbl_ttlmatch.place(x=200, y=70)
        self.lbl_ketttlgoal = Label(self.fr_plytotal, text='Total Gol:', font=('Times', 20, 'bold'), bg='white', fg='#060644')
        self.lbl_ketttlgoal.place(x=5, y=130)
        ttl_goal = 0
        try:
            for mtc in ply.child[8].child:
                ttl_goal += int(mtc.child[0].data)
        except: pass
        self.lbl_ttlgoal = Label(self.fr_plytotal, text=ttl_goal, font=('Times', 20, 'bold'), bg='white', fg='#060644')
        self.lbl_ttlgoal.place(x=200, y=130)

        self.button_back1 = Button(self.fr_submain1, image=img_return0, cursor="hand2", command=lambda : self.fr_submain1.destroy(), bg='#093D83', relief='flat', borderwidth=0, activebackground='#093D83')
        self.button_back1.place(x=35, y=635)



    def summon_lbl_train(self, tgl, rw):
        lbl_num = CTkLabel(self.sc_train, text=rw+1, font=('Times', 17, 'bold'), text_color='#060644', anchor='e')
        lbl_num.grid(row=rw, column=0, pady=5, padx=20)
        lbl_train = CTkLabel(self.sc_train, text=tgl, font=('Times', 17, 'bold'), text_color='#060644', anchor='e')
        lbl_train.grid(row=rw, column=1, pady=5)

    def summon_lbl_match(self, match, rw):
        lbl_num = CTkLabel(self.sc_match, text=rw+1, font=('Times', 17, 'bold'), text_color='#060644', anchor='w')
        lbl_num.grid(row=rw, column=0, pady=5, padx=20, sticky='w')
        lbl_tglmatch = CTkLabel(self.sc_match, text=match.data[0], font=('Times', 17, 'bold'), text_color='#060644', anchor='e')
        lbl_tglmatch.grid(row=rw, column=1, pady=5, sticky='w')
        lbl_enmmatch = CTkLabel(self.sc_match, text=f'VS: {match.data[1]}', font=('Times', 15, 'bold'), text_color='#060644', anchor='e')
        lbl_enmmatch.grid(row=rw, column=2, pady=5, padx=30)
        lbl_glmatch = CTkLabel(self.sc_match, text=f'Goal: {match.child[0].data}', font=('Times', 13, 'bold'), text_color='#060644', anchor='e')
        lbl_glmatch.grid(row=rw, column=3, pady=5, sticky='e')


# w = Tk()
# fl = open('Data/treeDatabase.pickle', 'rb')
# tree_data = pickle.load(fl)
# fl.close()
# PlayersManagement(w, tree_data.child[0].child[0], tree_data)
# w.mainloop()