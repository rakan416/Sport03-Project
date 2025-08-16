import tkinter as tk
from tkinter import *
from customtkinter import *
from tkinter.messagebox import askokcancel, showerror, showinfo
from PIL import Image, ImageTk
from tkinter import ttk
from tkcalendar import DateEntry
import pickle
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from Tree_Processing import TreeNode


class JadwalPertandinganLatihan():
    def __init__(self, master, tim, root):
        self.master = master
        # self.master.title('Jadwal Latihan dan Jadwal Pertandingan')
        # self.master.geometry('1366x768')
        # self.master.configure(bg='#F3EEEA')
        self.master.state('zoomed')
        self.tim = tim
        self.tr_var = root
        self.FRAME = Frame(self.master, bg='#093D83')
        self.FRAME.place(x=0, y=0, width=1366, height=768)
        self.foto = Image.open("Image/Background/bg_3.png").resize((1366, 768))
        self.photoo = ImageTk.PhotoImage(self.foto)
        self.label_background = Label(self.FRAME, image=self.photoo)
        self.label_background.place(x=-2, y=-2)

        # Setup latihan canvas
        self.fr_idk1 = CTkFrame(self.FRAME, fg_color='#060644', width=470, height=550)
        self.fr_idk1.place(x=75, y=100)
        self.lbl_ketjdlt = Label(self.fr_idk1, text='JADWAL LATIHAN', bg='#060644', fg='white', font=('Bookman Old Style', 20, 'bold'))
        self.lbl_ketjdlt.place(x=20, y=0, width=430, height=50)
        self.inner_framelt = CTkScrollableFrame(self.fr_idk1, fg_color="#DBDBDB", width=454, height=450, corner_radius=0)
        self.inner_framelt.place(x=0, y=50)
        self.tambah_lt = Button(self.fr_idk1, text='+ Tambah Jadwal', font=("Constantia", 16, "bold"), fg="white", bg="#060644", command=self.ke_menu_lt, cursor='hand2', relief='flat', borderwidth=0, activebackground='#000644')
        self.tambah_lt.place(x=20, y=500, width=430, height=50)

        # Setup pertandingan canvas
        self.fr_idk2 = CTkFrame(self.FRAME, fg_color='#060644', width=470, height=550)
        self.fr_idk2.place(x=820, y=100)
        self.lbl_ketjdptd = Label(self.fr_idk2, text='JADWAL PERTANDINGAN', bg='#060644', fg='white', font=('Bookman Old Style', 20, 'bold'))
        self.lbl_ketjdptd.place(x=20, y=0, width=430, height=50)
        self.inner_frameptd = CTkScrollableFrame(self.fr_idk2, fg_color="#DBDBDB", width=454, height=450, corner_radius=0)
        self.inner_frameptd.place(x=0, y=50)
        self.tambah_ptd = Button(self.fr_idk2, text='+ Tambah Jadwal', font=("Constantia", 16, "bold"), fg="white", bg="#060644", command=self.ke_menu_ptd, cursor='hand2', relief='flat', borderwidth=0, activebackground='#000644')
        self.tambah_ptd.place(x=20,y=500, width=430, height=50)
        global img_return0
        img_return0 = ImageTk.PhotoImage(Image.open('Image/return.png').resize((120, 50)))
        self.button_back = Button(self.FRAME, image=img_return0, cursor="hand2", command=lambda : self.FRAME.destroy(), bg='#426CD0', relief='flat', borderwidth=0, activebackground='#426CD0')
        self.button_back.place(x=10, y=0)
        self.load_data()

    def selection_sort(self, source):
        for i in range(len(source)):
            minind = i
            for j in (i+1, len(source)):
                dttm1 = datetime.strptime(source[minind][0], '%d/%m/%Y')
                dttm2 = datetime.strptime(source[j][0], '%d/%m/%Y')
                if dttm1 > dttm2:
                    minind = j
            source[i], source[minind] = source[minind], source[i]
            return source

    def ke_menu_lt(self):
        self.fr_submain1 = Frame(self.FRAME, bg='#093D83')
        self.fr_submain1.place(x=0, y=0, width=1366, height=768)
        MenuJadwalLatihan(self.fr_submain1, self, self.tim, self.tr_var)

    def ke_menu_ptd(self):
        self.fr_submain3 = Frame(self.FRAME, bg='#093D83')
        self.fr_submain3.place(x=0, y=0, width=1366, height=768)
        MenuJadwalPertandingan(self.fr_submain3, self, self.tim, self.tr_var)

    def load_data(self):
        try: self.lbl_infoltd.destroy()
        except: pass
        try: self.lbl_infoptd.destroy()
        except: pass


        try:
                filtered_data = self.tim.child[1].child[0].data
                for i, row in enumerate(filtered_data):
                    if row:
                        tanggal = row[0]
                        jenis_latihan = row[1]

                        data_lt = CTkFrame(self.inner_framelt, fg_color="#DBDBDB", width=420, height=70, border_color='black', border_width=2)
                        data_lt.grid(row=i, column=0, pady=10, padx=20)

                        info_label = Label(data_lt, text=f"{i+1}.\t{tanggal}\n\t{jenis_latihan}", font=("Consolas", 16), bg="#DBDBDB", fg="#060644", justify=LEFT)
                        info_label.place(x=10, y=5)

        except IndexError:
            self.lbl_infoltd = Label(self.inner_framelt, text='Data Jadwal Belum Ada')
            self.lbl_infoltd.grid(row=0, column=0)

        try:
                filtered_data = self.tim.child[2].child[0].data

                for i, row in enumerate(filtered_data):
                    if row:
                        tanggal2 = row[0]
                        jam2 = row[1]
                        enemy_team = row[2]

                        data_ptd = CTkFrame(self.inner_frameptd, fg_color="#DBDBDB", width=420, height=90, border_color='black', border_width=2)
                        data_ptd.grid(row=i, column=0, pady=10, padx=20)
                        info_label = Label(data_ptd, text=f"Tanggal: {tanggal2}\nJam: {jam2}\nTim Lawan: {enemy_team}",
                                           font=("Consolas", 16), bg="#DBDBDB", fg="#060644", justify=LEFT)
                        info_label.place(x=10, y=5)

        except IndexError:
            self.lbl_infoptd = Label(self.inner_frameptd, text='Data Jadwal Belum Ada')
            self.lbl_infoptd.grid(row=0, column=0)


class MenuJadwalLatihan():

    def __init__(self, master2, main_app, tim, root):
        self.master2 = master2
        self.main_app = main_app
        self.tim = tim
        self.tr_var = root
        foto = Image.open('Image/Background/bg_3.png').resize((1366,768))
        global photoo
        photoo = ImageTk.PhotoImage(foto)
        self.lbl_bgjdwl = Label(self.master2, image=photoo)
        self.lbl_bgjdwl.place(x=-2, y=-2)
        global img_return1
        img_return1 = ImageTk.PhotoImage(Image.open('Image/return.png').resize((120, 55)))
        self.button_back = Button(self.master2, image=img_return1, cursor="hand2", command=self.go_back, bg='#093D83', relief='flat', borderwidth=0, activebackground='#093D83')
        self.button_back.place(x=30, y=630)

        global img_inpj
        img_inpj = ImageTk.PhotoImage(Image.open('Image/inputjdwl.png').resize((170,160)))
        self.fr_bttinp = CTkFrame(self.master2, width=300, height=230, fg_color='white', corner_radius=60)
        self.fr_bttinp.place(x=230, y=250)
        self.lbl_img_inpj = Label(self.fr_bttinp, image=img_inpj, bg='white', cursor='hand2')
        self.lbl_img_inpj.place(x=65, y=20)
        self.lbl_ketinpj = Label(self.fr_bttinp, text='INPUT JADWAL', font=("Constantia", 16, "bold"), bg='white', cursor='hand2')
        self.lbl_ketinpj.place(x=50, y=190, width=200)
        self.fr_bttinp.bind('<Button-1>', self.input_jadwal)
        self.lbl_img_inpj.bind('<Button-1>', self.input_jadwal)
        self.lbl_ketinpj.bind('<Button-1>', self.input_jadwal)

        global img_templ
        img_templ = ImageTk.PhotoImage(Image.open('Image/recomjdwl.png').resize((170,160)))
        self.fr_btttemp = CTkFrame(self.master2, width=300, height=230, fg_color='white', corner_radius=60)
        self.fr_btttemp.place(x=810, y=250)
        self.lbl_img_tempj = Label(self.fr_btttemp, image=img_templ, bg='white', cursor='hand2')
        self.lbl_img_tempj.place(x=65, y=20)
        self.lbl_kettempj = Label(self.fr_btttemp, text='REKOMENDASI JADWAL', font=("Constantia", 16, "bold"), bg='white', cursor='hand2')
        self.lbl_kettempj.place(x=25, y=185, width=250)
        self.fr_btttemp.bind('<Button-1>', self.rekomendasi_jadwal)
        self.lbl_img_tempj.bind('<Button-1>', self.rekomendasi_jadwal)
        self.lbl_kettempj.bind('<Button-1>', self.rekomendasi_jadwal)

    def selection_sort(self, source):
        for i in range(len(source)):
            minind = i
            for j in range(i+1, len(source)):
                dttm1 = datetime.strptime(source[minind][0], '%d/%m/%Y')
                dttm2 = datetime.strptime(source[j][0], '%d/%m/%Y')
                if dttm1 > dttm2:
                    minind = j
            source[i], source[minind] = source[minind], source[i]
        return source

    def go_back(self):
        self.master2.destroy()
        self.main_app.load_data()

    def input_jadwal(self, e):
        self.fr_submain2 = Frame(self.master2, bg='#093D83')
        self.fr_submain2.place(x=0, y=0, width=1366, height=768)
        label_background = Label(self.fr_submain2, image=photoo)
        label_background.place(x=-2, y=-2)
        label_background.image = photoo
        self.button_back1 = Button(self.fr_submain2, image=img_return1, cursor="hand2", command=lambda: self.fr_submain2.destroy(), bg='#093D83', relief='flat', borderwidth=0, activebackground='#093D83')
        self.button_back1.place(x=30, y=630)

        self.fr_idk2 = CTkFrame(self.fr_submain2, fg_color='#060644', width=370, height=350)
        self.fr_idk2.place(x=175, y=180)
        self.label_ketinplt = Label(self.fr_idk2, text='INPUT JADWAL', font=("Times", 20, 'bold'), fg='#DBDBDB', bg='#060644')
        self.label_ketinplt.place(x=20, y=0, width=330, height=50)
        self.framee = Frame(self.fr_idk2, bg="#DBDBDB")
        self.framee.place(x=0, y=50, width=370, height=250)
        self.label_dob = Label(self.framee, text='DD/MM/YYYY', font=("Bookman Old Style", 13), fg='#060644', bg='#DBDBDB')
        self.label_dob.place(x=40, y=20)
        self.dob_entry = DateEntry(self.framee, relief='flat', font=("consolas", 12), width=27, date_pattern='dd/mm/yyyy', showweeknumbers=True,
                                    selectbackground='#2196F3', selectforeground='white',
                                    normalbackground='white', normalforeground='black',
                                    weekendbackground='lightblue', weekendforeground='black',
                                    headersbackground='#2196F3', headersforeground='white',
                                    sundaybackground='red', sundayforeground='white')
        self.dob_entry.place(x=40, y=50, height=35, width=260)
        self.label_jenislt = Label(self.framee, text='Jenis Latihan', font=("Bookman Old Style", 13), fg='#060644', bg='#DBDBDB')
        self.label_jenislt.place(x=40, y=140)
        self.latihan_options = ["Teknis","Taktik","Fisik","Spesifikasi Posisi"]
        self.combobox_latihan = ttk.Combobox(self.framee, values=self.latihan_options, state="readonly", font=("Bookman Old Style", 13), width=27)
        self.combobox_latihan.place(x=40, y=170,width=260, height=35)
        self.button_submit = Button(self.fr_idk2, text="Submit", command=self.submit_data, bg='#060644', fg='#DBDBDB', activebackground='#060644', relief='flat', borderwidth=0)
        self.button_submit.place(x=30, y=300, width=310, height=50)

        self.fr_idk3 = CTkFrame(self.fr_submain2, fg_color='#060644', width=470, height=500)
        self.fr_idk3.place(x=820, y=100)
        self.label_ketlist = Label(self.fr_idk3, text='JADWAL LATIHAN', font=("Times", 20, 'bold'), fg='#DBDBDB', bg='#060644')
        self.label_ketlist.place(x=20, y=0, width=430, height=50)
        self.inner_frame = CTkScrollableFrame(self.fr_idk3, fg_color="#DBDBDB", width=454, height=450, corner_radius=0)
        self.inner_frame.place(x=0, y=50)

        self.display_filtered_data()

    def submit_data(self):
        tanggal = self.dob_entry.get()
        jenis_latihan = self.combobox_latihan.get()
        try:
            self.tim.child[1].child[0].data.append([tanggal,jenis_latihan])
        except IndexError:
            self.tim.child[1].add_child(TreeNode([[tanggal,jenis_latihan]]))
        tgl_list = self.tim.child[1].child[0].data
        tgl_list = self.selection_sort(tgl_list)
        self.tim.child[1].child[0].data = tgl_list


        self.display_filtered_data()

    def display_filtered_data(self):
        for widget in self.inner_frame.winfo_children():
            widget.destroy()

        try:
            filtered_data = self.tim.child[1].child[0].data

            for i, row in enumerate(filtered_data):
                if row: 
                    tanggal = row[0]
                    jenis_latihan = row[1]

                    data_lt = CTkFrame(self.inner_frame, fg_color="#DBDBDB", width=410, height=70, border_color='black', border_width=2)
                    data_lt.grid(row=i, column=0, pady=10, padx=20)

                    info_label = Label(data_lt, text=f"{i+1}.\t{tanggal}\n\t{jenis_latihan}", font=("Consolas", 16), bg="#DBDBDB", fg="#060644", justify=LEFT)
                    info_label.place(x=10, y=5)

        except IndexError:
            self.tim.child[1].add_child(TreeNode([]))
            Label(self.inner_frame, text='Data Kosong').grid(row=0, column=0)

    def rekomendasi_jadwal(self, e):
        self.fr_submain4 = Frame(self.master2, bg='#093D83')
        self.fr_submain4.place(x=0, y=0, width=1366, height=768)
        self.lbl_bgjdwl = Label(self.fr_submain4, image=photoo)
        self.lbl_bgjdwl.place(x=-2, y=-2)
        self.button_back2 = Button(self.fr_submain4, image=img_return1, cursor="hand2", command=lambda: self.fr_submain4.destroy(), bg='#093D83', relief='flat', borderwidth=0, activebackground='#093D83')
        self.button_back2.place(x=30, y=630)
        self.fr_template = CTkFrame(self.fr_submain4, fg_color='#060644', width=800, height=550)
        self.fr_template.place(x=283, y=70)
        self.lbl_ketjadtem = Label(self.fr_template, text='PILIH POLA HARIAN', font=('Times', 25, 'bold'), bg='#060644', fg='#DBDBDB')
        self.lbl_ketjadtem.place(x=150, y=0, width=500, height=50)
        self.sc_jadtem = CTkScrollableFrame(self.fr_template, fg_color='#DBDBDB', width=784, height=490, border_width=0, corner_radius=0)
        self.sc_jadtem.place(x=0, y=50)
        fl = open('Data/data_jadwaltemplate.txt','r')
        dt_tplt = fl.read().split('\n\n')
        dt_tplt1 = [tplt.split('\n') for tplt in dt_tplt]
        rw = 0
        for template in dt_tplt1:
            self.summon_btt_jadtem(self.sc_jadtem, template[0], template[1].split(','), rw, 0)
            rw += 1
    
    def summon_btt_jadtem(self, fr, title, dt_days, row, col):

        def pilih_pola(e, dt_days, title):
            self.choose_pole(dt_days, title)

        fr_btt = CTkFrame(fr, width=740, height=70, border_width=2, border_color='black', fg_color='#DBDBDB')
        fr_btt.grid(row=row, column=col, pady=10, padx=20)

        lbl_title = Label(fr_btt, text=title, font=('Times', 15, 'bold'), bg='#DBDBDB', fg='#060644')
        lbl_title.place(x=20, y=10, height=50)
        fr_btt.bind('<Button-1>', lambda e: pilih_pola(e, dt_days, title))
        lbl_title.bind('<Button-1>', lambda e: pilih_pola(e, dt_days, title))
        x = 650
        for i in range(len(dt_days)-1, -1, -1):
            self.summon_lbl_day(fr_btt, day=dt_days[i], x_pos=x, y_pos=15, func=pilih_pola, dt_days=dt_days, ttl=title)
            x -= 90

    def summon_lbl_day(self, fr, day, x_pos, y_pos, func, dt_days, ttl):
        lbl_day = CTkLabel(fr, text=day, width=80, height=40, fg_color='#DBDBDB', text_color='#060644', font=('Bookman Old Style', 13))
        lbl_day.place(x=x_pos, y=y_pos)
        lbl_day.bind('<Button-1>', lambda e: func(e, dt_days, ttl))

    def choose_pole(self, dt_days, ttl):
        self.fr_submain5 = Frame(self.master2, bg='black')
        self.fr_submain5.place(x=0, y=0, width=1366, height=768)
        self.lbl_bgpole = Label(self.fr_submain5, image=photoo)
        self.lbl_bgpole.place(x=-2, y=-2)
        self.fr_pole = CTkFrame(self.fr_submain5,fg_color='#060644', width=800, height=550)
        self.fr_pole.place(x=283, y=70)
        self.lbl_ketpole = Label(self.fr_pole, text='PILIH POLA LATIHAN', font=('Times', 25, 'bold'), bg='#060644', fg='#DBDBDB')
        self.lbl_ketpole.place(x=150, y=0, width=500, height=50)
        self.sc_pole = CTkScrollableFrame(self.fr_pole,fg_color='#DBDBDB', width=784, height=490, border_width=0, corner_radius=0)
        self.sc_pole.place(x=0, y=50)
        fl = open('Data/data_polajadwal.txt', 'r')
        dt_pole = fl.read().split('\n')
        fl.close()
        dt_pole1 = [pole.split(',') for pole in dt_pole]
        rw = 0
        for jenlt in dt_pole1:
            self.summon_btt_pole(self.sc_pole, dt_days, jenlt, rw, 0)
            rw += 1


    def summon_btt_pole(self,fr, dt_days, dt_pole, row, col):

        def pilihtgl(e, dt_days, dt_pole):
            self.pilih_tglmulai(dt_days, dt_pole)

        fr_btt = CTkFrame(fr, width=740, height=70, border_width=2, border_color='black', fg_color='#DBDBDB')
        fr_btt.grid(row=row, column=col, pady=10, padx=20)
        lbl_pole1 = Label(fr_btt, text=dt_pole[0], font=('Times', 15), bg='#DBDBDB', fg='#060644')
        lbl_pole1.place(x=20, y=10, height=50, width=160)
        lbl_pole2 = Label(fr_btt, text=dt_pole[1], font=('Times', 15), bg='#DBDBDB', fg='#060644')
        lbl_pole2.place(x=200, y=10, height=50, width=160)
        lbl_pole3 = Label(fr_btt, text=dt_pole[2], font=('Times', 15), bg='#DBDBDB', fg='#060644')
        lbl_pole3.place(x=380, y=10, height=50, width=160)
        lbl_pole4 = Label(fr_btt, text=dt_pole[3], font=('Times', 15), bg='#DBDBDB', fg='#060644')
        lbl_pole4.place(x=560, y=10, height=50, width=160)
        fr_btt.bind('<Button-1>', lambda e: pilihtgl(e, dt_days=dt_days, dt_pole=dt_pole))
        lbl_pole1.bind('<Button-1>', lambda e: pilihtgl(e, dt_days=dt_days, dt_pole=dt_pole))
        lbl_pole2.bind('<Button-1>', lambda e: pilihtgl(e, dt_days=dt_days, dt_pole=dt_pole))
        lbl_pole3.bind('<Button-1>', lambda e: pilihtgl(e, dt_days=dt_days, dt_pole=dt_pole))
        lbl_pole4.bind('<Button-1>', lambda e: pilihtgl(e, dt_days=dt_days, dt_pole=dt_pole))

    def pilih_tglmulai(self, dt_days, dt_pole):
        try:
            self.fr_pilihtgl.destroy()
        except: pass
        self.fr_pilihtgl = CTkFrame(self.fr_pole, width=800, height=550, fg_color='#060644')
        self.fr_pilihtgl.place(x=0, y=0)
        self.lbl_pilihtgl = Label(self.fr_pilihtgl, text='Pilih Tanggal Mulai', font=('Times', 25, 'bold'), bg='#060644', fg='#DBDBDB')
        self.lbl_pilihtgl.place(x=150, y=0, width=500, height=50)
        self.fr_dtent = Frame(self.fr_pilihtgl, bg='#DBDBDB')
        self.fr_dtent.place(x=0, y=50, height=450, width=800)
        self.date_entry = DateEntry(self.fr_dtent, relief='flat', font=('Bookman Old Style', 16), date_pattern='dd/mm/yyyy', showweeknumbers=False,
                            selectbackground='#2196F3', selectforeground='white', mindate= datetime.now(),
                            normalbackground='white', normalforeground='black',
                            weekendbackground='white', weekendforeground='black',
                            headersbackground='#2196F3', headersforeground='white',
                            sundaybackground='red', sundayforeground='white', justify='center')
        self.date_entry.place(x=250, y=20, height=50, width=300)
        btt_ok = CTkButton(self.fr_dtent, text='PILIH', width=200, height=40, command= lambda: self.pemilihan_tgl(dt_days, dt_pole), fg_color='#060644', corner_radius=90, hover_color="#000630")
        btt_ok.place(x=300, y=80)

    def pemilihan_tgl(self, dt_days, dtpole):
        try:
            self.lbl_listjadtem.destroy()
            self.sc_listjadtem.destroy()
            self.btt_submit.destroy()
        except: pass
        tgl_start_str = self.date_entry.get()
        tgl_start = datetime.strptime(tgl_start_str, '%d/%m/%Y')
        tanggal_akhir = tgl_start + relativedelta(weeks=4)
        all_dates = [tgl_start + timedelta(days=i) for i in range((tanggal_akhir - tgl_start).days)]
        mingguan = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        dt = [mingguan.index(dy) for dy in dt_days]
        filtered_dates = [date.strftime('%d/%m/%Y') for date in all_dates if date.weekday() in dt]
        i = 0
        self.jadtemp = []
        for date in filtered_dates:
            if i > 3:
                i = 0
            self.jadtemp.append([date,dtpole[i]])
            i += 1
        self.lbl_listjadtem = Label(self.fr_dtent, text='Jadwal Yang Akan Ditambahkan', font=('Times', 18, 'bold'), bg='#DBDBDB', fg='#060644')
        self.lbl_listjadtem.place(x=150, y=150, width=500, height=30)
        self.sc_listjadtem = CTkScrollableFrame(self.fr_dtent, fg_color='#DBDBDB', width=780, height=260, corner_radius=0, border_width=0)
        self.sc_listjadtem.place(x=5, y=190)
        self.btt_submit = CTkButton(self.fr_pilihtgl, text='SUBMIT', width=740, height=50, command=self.simpan, fg_color='#060644', hover_color="#000630")
        self.btt_submit.place(x=30, y=500)
        i = 1
        rw = 0
        cl = 0
        for jadwal in self.jadtemp:
            if rw >= len(dt):
                cl += 1
                rw = 0
            fr_lbl = CTkFrame(self.sc_listjadtem, fg_color='#DBDBDB', border_width=2, border_color='black', width=170, height=60)
            fr_lbl.grid(row=rw, column=cl, pady=5, padx=10)
            CTkLabel(fr_lbl, text=f'{i}. {jadwal[0]}\n{jadwal[1]}', width=160, height=50, font=('Times',17), fg_color='#DBDBDB', text_color='#060644').place(x=5, y=5)
            rw += 1
            i += 1
        
    def simpan(self):
        try:
            all_sch = self.tim.child[1].child[0].data
            for schtplt in self.jadtemp:
                self.tim.child[1].child[0].data.append(schtplt)
                tgl_list = self.tim.child[1].child[0].data
                tgl_list = self.selection_sort(tgl_list)
                self.tim.child[1].child[0].data = tgl_list
        except IndexError:
            self.tim.child[1].add_child(TreeNode([]))
            all_sch = self.tim.child[1].child[0].data
            for schtplt in self.jadtemp:
                all_sch.append(schtplt)
        self.fr_submain4.destroy()
        self.fr_submain5.destroy()
        self.fr_pilihtgl.destroy()
        self.main_app.load_data()


class MenuJadwalPertandingan():
    def __init__(self, master3, main_app, tim, root):
        self.master3 = master3
        self.main_app = main_app
        self.tim = tim
        self.tr_var = root
        foto = Image.open('Image/Background/bg_3.png').resize((1366,768))
        global bg_03
        bg_03 = ImageTk.PhotoImage(foto)
        self.lbl_bgjdwl = Label(self.master3, image=bg_03)
        self.lbl_bgjdwl.place(x=-2, y=-2)
        global img_return2
        img_return2 = ImageTk.PhotoImage(Image.open('Image/return.png').resize((120, 55)))
        self.button_back = Button(self.master3, image=img_return2, cursor="hand2", command=self.go_back, bg='#093D83', relief='flat', borderwidth=0, activebackground='#093D83')
        self.button_back.place(x=30, y=630)

        self.fr_idk3 = CTkFrame(self.master3, fg_color='#060644', width=370, height=400)
        self.fr_idk3.place(x=175, y=180)
        self.label_ketinpptd = Label(self.fr_idk3, text='INPUT JADWAL', font=("Times", 20, 'bold'), fg='#DBDBDB', bg='#060644')
        self.label_ketinpptd.place(x=20, y=0, width=330, height=50)
        self.fr_inpptd = Frame(self.fr_idk3, bg='#DBDBDB')
        self.fr_inpptd.place(x=0, y=50, width=370, height=300)
        self.label_dob = Label(self.fr_inpptd, text='DD/MM/YYYY', font=('Bookman Old Style', 13), fg='#060644', anchor='w', justify='left', bg='#DBDBDB')
        self.label_dob.place(x=50, y=20, height=30)
        self.dob_entry = DateEntry(self.fr_inpptd, relief='flat', font=('Bookman Old Style', 13), date_pattern='dd/mm/yyyy', showweeknumbers=True,
                                    selectbackground='#2196F3', selectforeground='white',
                                    normalbackground='white', normalforeground='#060644',
                                    weekendbackground='lightblue', weekendforeground='#060644',
                                    headersbackground='#2196F3', headersforeground='white',
                                    sundaybackground='red', sundayforeground='white')
        self.dob_entry.place(x=50,y=50,height=40, width=270) 
        self.label_enemy = Label(self.fr_inpptd, text='Tim Lawan', font=('Bookman Old Style', 13), fg='#060644', bg='#DBDBDB')
        self.label_enemy.place(x=50, y=200, height=30)
        self.Enemy_team = Entry(self.fr_inpptd,width=32, fg='#060644', bd=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        self.Enemy_team.place(x=50,y=230,height=40, width=270)
        self.label_time = Label(self.fr_inpptd, text='Jam (HH:MM)', font=('Bookman Old Style', 13), fg='#060644', bg='#DBDBDB')
        self.label_time.place(x=50, y=110, height=30)
        self.hours = [f"{i:02d}" for i in range(24)]
        self.minutes = [f"{i:02d}" for i in range(60)]
        self.combobox_hours_pert = ttk.Combobox(self.fr_inpptd, values=self.hours, state="readonly", font=('Bookman Old Style', 13))
        self.combobox_hours_pert.place(x=50, y=140, height=40, width=70)
        self.combobox_hours_pert.set("HH")
        self.combobox_minutes_pert = ttk.Combobox(self.fr_inpptd, values=self.minutes, state="readonly", font=('Bookman Old Style', 13))
        self.combobox_minutes_pert.place(x=130, y=140, height=40, width=70)
        self.combobox_minutes_pert.set("MM")
        self.button_submitptd = CTkButton(self.fr_idk3, text="SUMBIT", command=self.submit_dataptd, fg_color='#060644', hover_color="#000630", width=330, height=50)
        self.button_submitptd.place(x=20,y=350)

        self.fr_idk4 = CTkFrame(self.master3, fg_color='#060644', width=470, height=500)
        self.fr_idk4.place(x=820, y=100)
        self.label_ketlist = Label(self.fr_idk4, text='JADWAL PERTANDINGAN', font=("Times", 20, 'bold'), fg='#DBDBDB', bg='#060644')
        self.label_ketlist.place(x=20, y=0, width=430, height=50)
        self.inner_frame = CTkScrollableFrame(self.fr_idk4, fg_color="#DBDBDB", width=453, height=445, corner_radius=0)
        self.inner_frame.place(x=0, y=50)

        self.display_filtered_data()


    def go_back(self):
        self.master3.destroy()
        self.main_app.load_data()
        self.main_app.master.deiconify()

    def submit_dataptd(self):
        tanggal = self.dob_entry.get()
        jam_hours = self.combobox_hours_pert.get()
        jam_minutes = self.combobox_minutes_pert.get()
        enemy_team = self.Enemy_team.get()
        self.combobox_hours_pert.set("HH")
        self.combobox_minutes_pert.set("MM")
        self.Enemy_team.delete(0, END)

        if not tanggal or jam_hours == "HH" or jam_minutes == "MM" or not enemy_team:
            showerror('Error', 'Data yang anda masukan belum lengkap')
            return

        jam2 = f"{jam_hours}:{jam_minutes}"
        try:
            self.tim.child[2].child[0].data.append([tanggal, jam2, enemy_team])
        except IndexError:
            self.tim.child[2].add_child(TreeNode([[[tanggal, jam2, enemy_team]]]))
        src =  self.tim.child[2].child[0].data
        src = self.selection_sort(src)
        self.tim.child[2].child[0].data = src

        self.display_filtered_data()

    def selection_sort(self, source):
        for i in range(len(source)):
            minind = i
            for j in range(i+1, len(source)):
                dttm1 = datetime.strptime(source[minind][0], '%d/%m/%Y')
                dttm2 = datetime.strptime(source[j][0], '%d/%m/%Y')
                if dttm1 > dttm2:
                    minind = j
                elif dttm1 == dttm2:
                    jam1 = source[minind][1]
                    jam2 = source[j][1]
                    if int(jam1[:2]) > int(jam2[:2]):
                        minind = j
                    elif int(jam1[:2]) == int(jam2[:2]):
                        if int(jam1[3:5]) >= int(jam2[3:5]):
                            minind = j
            source[i], source[minind] = source[minind], source[i]
        return source

    def display_filtered_data(self):
        for widget in self.inner_frame.winfo_children():
            widget.destroy()

        try:
            filtered_data =  self.tim.child[2].child[0].data

            for i, row in enumerate(filtered_data):
                if row:  # Check if row is not empty
                    tanggal2 = row[0]
                    jam2 = row[1]
                    enemy_team = row[2]

                    location_info = CTkFrame(self.inner_frame, fg_color="#DBDBDB", width=435, height=85, border_color='black', border_width=2)
                    location_info.grid(row=i, column=0, pady=10, padx=10)

                    info_label = Label(location_info, text=f"Tanggal: {tanggal2}\nJam: {jam2}\nTim Lawan: {enemy_team}",
                                        font=("Bookman Old Style", 16), bg="#DBDBDB", fg="#060644", justify=LEFT)
                    info_label.place(x=10, y=3)

        except IndexError:
            self.tim.child[2].add_child(TreeNode([]))
            Label(self.inner_frame, text='Data Kosong').grid(row=0, column=0)


# w = Tk()
# fl = open('Data/treeDatabase.pickle', 'rb')
# tree_data = pickle.load(fl)
# fl.close()
# JadwalPertandinganLatihan(w, tree_data.child[0].child[0], tree_data)
# w.mainloop()