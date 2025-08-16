from tkinter import *
from customtkinter import *
from tkcalendar import Calendar
import pickle
from PIL import Image,ImageTk
from tkinter.messagebox import showerror
from Tree_Processing import TreeNode


class Input_Data():

    def __init__(self, window, p, l, team, root, ind):
        self.window = window
        # self.window.state('zoomed')
        self.temp_dt = []
        self.tr_var = root
        self.tim = team
        self.main_fr = Frame(self.window, bg="#0E4186")
        self.main_fr.place(x=0, y=0, width=1366, height=768)
        global img1
        img1 = ImageTk.PhotoImage(Image.open('Image/Background/bg_1.png').resize((1366,768)))
        self.lbl_bg = Label(self.main_fr, image=img1, bg="#0E4186")
        self.lbl_bg.place(x=-2, y=-2)
        self.fr_idk1 = CTkFrame(self.main_fr, width=350, height=420, fg_color='#060644', bg_color="#0E4186")
        self.fr_idk1.place(x=150, y=130)
        self.lbl_ketadd = Label(self.fr_idk1, text='Tambah Pemain', font=('Bookman Old Style',20), bg='#060644', fg='#DBDBDB')
        self.lbl_ketadd.place(x=10, y=0, width=320, height=40)
        self.fr1 = Frame(self.fr_idk1, bg='#DBDBDB')
        self.fr1.place(x=0, y=40, width=350, height=340)
        self.lbl1 = Label(self.fr1, text='Nama', anchor='w', bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12))
        self.lbl1.grid(pady=6,row=0, column=0, sticky='w', padx=10)
        self.inp1 = CTkEntry(self.fr1, width=180, height=30, corner_radius=90, border_color='#DBDBDB')
        self.inp1.grid(pady=6,row=0, column=1)
        self.inp1.bind('<FocusIn>', lambda e: self.cbd(e, self.inp1))
        self.lblno = Label(self.fr1, text='Nomor Punggung', anchor='w', bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12))
        self.lblno.grid(pady=6,row=1, column=0, sticky='w', padx=10)
        self.inpno = CTkEntry(self.fr1, width=70, border_color='#DBDBDB', corner_radius=90, height=30)
        self.inpno.grid(pady=6,row=1, column=1, sticky='w')
        self.inpno.bind('<FocusIn>', lambda e: self.cbd(e, self.inp1))
        self.lbl2 = Label(self.fr1, text='Tanggal_Lahir', anchor='w', bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12))
        self.lbl2.grid(pady=6,row=2, column=0, sticky='w', padx=10)
        self.inp2 = CTkEntry(self.fr1, width=180, height=30, corner_radius=90, border_color='#DBDBDB')
        self.inp2.grid(pady=6,row=2, column=1)
        self.inp2.insert(0, 'DD/MM/YYYY')
        self.inp2.bind('<FocusIn>', lambda e:self.dt(e, self.inp2))


        self.lbl3 = Label(self.fr1, text='Tinggi Badan', anchor='w', bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12))
        self.lbl3.grid(pady=6,row=3, column=0, sticky='w', padx=10)
        self.inp3 = CTkEntry(self.fr1, width=180, height=30, corner_radius=90, border_color='#DBDBDB')
        self.inp3.grid(pady=6,row=3, column=1)
        self.inp3.bind('<FocusIn>', lambda e: self.cbd(e, self.inp3))
        self.lbl4 = Label(self.fr1, text='Berat Badan', anchor='w', bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12))
        self.lbl4.grid(pady=6,row=4, column=0, sticky='w', padx=10)
        self.inp4 = CTkEntry(self.fr1, width=180, height=30, corner_radius=90, border_color='#DBDBDB')
        self.inp4.grid(pady=6,row=4, column=1)
        self.inp4.bind('<FocusIn>', lambda e: self.cbd(e, self.inp4))
        self.lbl5 = Label(self.fr1, text='Tipe Badan', anchor='w', bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12))
        self.lbl5.grid(pady=6,row=5, column=0, sticky='w', padx=10)
        self.inp5 = CTkComboBox(self.fr1, values=['Normal','Lean','Stocky'], width=180, height=30, corner_radius=90, border_color='#DBDBDB',)
        self.inp5.grid(pady=6,row=5, column=1)
        self.inp5.bind('<FocusIn>', lambda e: self.cbd(e, self.inp5))
        self.lbl7 = Label(self.fr1, text='Kaki Dominan', anchor='w', bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12))
        self.lbl7.grid(pady=6,row=6, column=0, sticky='w', padx=10)
        self.inp7 = CTkComboBox(self.fr1, values=['Kanan','Kiri'], width=180, height=30, corner_radius=90, border_color='#DBDBDB')
        self.inp7.grid(pady=6,row=6, column=1)
        self.lbl6 = Label(self.fr1, text='Posisi', anchor='w', bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12))
        self.lbl6.grid(pady=6,row=7, column=0, sticky='w', padx=10)
        self.inp6 = CTkComboBox(self.fr1, values=['Unknown','CAM', 'CB', 'CDM', 'CF', 'CM', 'GK', 'LB', 'LM', 'LW', 'LWB', 'RB', 'RM', 'RW', 'RWB', 'ST'],
                                width=180, height=30, corner_radius=90, border_color='#DBDBDB')
        self.inp6.grid(pady=6,row=7, column=1)

        self.btt_add = CTkButton(self.fr_idk1, text='Tambahkan', command= self.add_player, width=346, height=40, fg_color='#060644', hover_color='#000630', font=('Bookman Old Style', 20))
        self.btt_add.place(x=2, y=380)

        self.fr_idk2 = CTkFrame(self.main_fr, width=500, height=480, fg_color='#060644', bg_color="#0E4186")
        self.fr_idk2.place(x=735, y=170)
        self.lbl_ketlist = Label(self.fr_idk2, text='Daftar Pemain Yang Ditambahkan', font=('Bookman Old Style',20), bg='#060644', fg='#DBDBDB')
        self.lbl_ketlist.place(x=10, y=0, width=480, height=50)
        self.fr_trv = CTkScrollableFrame(self.fr_idk2, width=485, height=375, corner_radius=0, fg_color='#DBDBDB', scrollbar_button_color='#060644', scrollbar_button_hover_color='#000680')
        self.fr_trv.place(x=0, y=50)
        
        self.btt_sv = CTkButton(self.fr_idk2, text='Selesai', width=496, height=50, command=self.done, fg_color='#060644', hover_color='#000630', font=('Bookman Old Style', 20))
        self.btt_sv.place(x=2, y=427)
        if ind:
            global img_return0
            img_return0 = ImageTk.PhotoImage(Image.open('Image/return.png').resize((110, 50)))
            self.button_back = Button(self.main_fr, image=img_return0, cursor="hand2", command=lambda : self.main_fr.destroy(), bg='#093D83', relief='flat', borderwidth=0, activebackground='#093D83')
            self.button_back.place(x=35, y=635)
        
        
    def cbd(self, e, widget):
        widget.configure(border_color = '#DBDBDB')

    def dt(self, e, ip):
        ip.configure(state='disabled', border_color = '#DBDBDB')
        self.cal()


    def cal(self):
        def ambil():
            self.inp2.configure(state='normal')
            self.inp2.delete(0, END)
            self.inp2.insert(0, str(cal.get_date()))
            self.fr_cal.destroy()

        self.fr_cal = Frame(self.main_fr)
        self.fr_cal.place(x=500, y=130)
        cal = Calendar(self.fr_cal, selectmode = 'day', year = 2004, month = 1, day = 6, locale='en_US', date_pattern='dd/mm/yyyy')
        cal.pack()
        Button(self.fr_cal, text = "Get Date", command = ambil).pack(pady = 20)

    def add_player(self):
        val = 0
        nama = self.inp1.get()
        if nama == '' or nama.isdigit():
            self.inp1.configure(border_color = 'red')
        else: val += 1
        nomer = self.inpno.get()
        if nomer == '' or nomer.isdigit() == False:
            self.inpno.configure(border_color = 'red')
        else: val+=1
        ttl = self.inp2.get()
        if len(ttl) == 10:
            if ttl[0:2].isdigit() and ttl[3:5].isdigit() and ttl[6:10].isdigit() and ttl[2] == '/' and ttl[5] == '/':
                val += 1
                pass
            else:
                self.inp2.configure(border_color = 'red')
        else:
                self.inp2.configure(border_color = 'red')

        try:
            tgi = int(self.inp3.get())
            val += 1
        except:
            self.inp3.configure(border_color = 'red')
        
        try:
            brt = int(self.inp4.get())
            val += 1
        except:
            self.inp4.configure(border_color = 'red')

        tpb = self.inp5.get()
        bdn = ['Normal','Lean','Stocky']
        if tpb in bdn:
            val += 1
        else: self.inp5.configure(border_color = 'red')

        kkd = self.inp7.get()
        kaki = ['Kanan','Kiri']
        if kkd in kaki:
            val += 1
        else: self.inp7.configure(border_color = 'red')

        pss = self.inp6.get()
        pos = ['Unknown','CAM', 'CB', 'CDM', 'CF', 'CM', 'GK', 'LB', 'LM', 'LW', 'LWB', 'RB', 'RM', 'RW', 'RWB', 'ST']
        if pss in pos:
            val += 1
        else: self.inp6.configure(border_color = 'red')

        if val < 8:
            return
        self.temp_dt.append((nama,ttl,tgi,brt,tpb,kkd,pss, nomer))
        try:
            self.fr_trv.destroy()
        except: pass
        self.fr_trv = CTkScrollableFrame(self.fr_idk2, width=485, height=375, corner_radius=0, fg_color='#DBDBDB', scrollbar_button_color='#060644', scrollbar_button_hover_color='#000680')
        self.fr_trv.place(x=0, y=50)
        
        while () in self.temp_dt:
            self.temp_dt.remove(())
        i = 1
        for tdt in self.temp_dt:
            self.createLabel(i=i, frame=self.fr_trv, data=tdt)
            i += 1
        self.inp1.delete(0, END)
        self.inpno.delete(0, END)
        self.inp2.delete(0, END)
        self.inp2.insert(0, 'DD/MM/YYYY')
        self.inp3.delete(0, END)
        self.inp4.delete(0, END)
        self.inp5.set('Normal')
        self.inp7.set('Kanan')
        self.inp6.set('Unknown')
        

    def createLabel(self,i, frame, data):
            def see_data(data):
                try:
                    self.w2.destroy()
                except: pass
                def balik():
                    self.w2.destroy()
                    self.btt_balik.destroy()
                self.w2 = Frame(self.fr1, bg='#DBDBDB')
                self.w2.place(x=0, y=0, width=350, height=340)
                Label(self.fr_idk1, text='Detail',fg='#DBDBDB', bg='#060644', font=('Bookman Old Style', 20)).place(x=0, y=0, width=350, height=40)
                Label(self.w2, text=f'Nama\t: {data[0]}', anchor='w',bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12)).grid(pady=8,row=0, column=0, sticky='w', padx=10) 
                Label(self.w2, text=f'Nomor\t: {data[7]}', anchor='w',bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12)).grid(pady=8,row=1, column=0, sticky='w', padx=10)
                Label(self.w2, text=f'Lahir\t: {data[1]}', anchor='w',bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12)).grid(pady=8,row=2, column=0, sticky='w', padx=10)
                Label(self.w2, text=f'Tinggi\t: {data[2]}', anchor='w',bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12)).grid(pady=8,row=3, column=0, sticky='w', padx=10)
                Label(self.w2, text=f'Berat\t: {data[3]}', anchor='w',bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12)).grid(pady=8,row=4, column=0, sticky='w', padx=10)
                Label(self.w2, text=f'Body\t: {data[4]}', anchor='w',bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12)).grid(pady=8,row=5, column=0, sticky='w', padx=10)
                Label(self.w2, text=f'Kaki\t: {data[5]}', anchor='w',bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12)).grid(pady=8,row=6, column=0, sticky='w', padx=10)
                Label(self.w2, text=f'Pos\t: {data[6]}', anchor='w',bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12)).grid(pady=8,row=7, column=0, sticky='w', padx=10)
                self.btt_balik = CTkButton(self.fr_idk1, text='back', command=balik, width=346, height=40, fg_color='#060644', hover_color='#000630', font=('Bookman Old Style', 20))
                self.btt_balik.place(x=2, y=380)

            def edt_data(i):
                try:
                    self.w2.destroy()
                    self.btt_sv1.destroy()
                except: pass
                def edt():
                    dtemp = (inp1.get(),inp2.get(),int(inp3.get()),int(inp4.get()),inp5.get(),inp7.get(),inp6.get(),inpno.get())
                    dt = self.temp_dt[i-1]
                    if dt == dtemp:
                        pass
                    else:
                        self.temp_dt[i-1] = dtemp
                        lbl.configure(text= dtemp[0])
                        btt_see.configure(command=lambda:see_data(dtemp))
                        self.w2.destroy()
                        self.btt_sv1.destroy()

                def balik():
                    self.w2.destroy()
                self.w2 = Frame(self.fr1, bg='#DBDBDB')
                self.w2.place(x=0, y=0, width=350, height=340)
                lbl1 = Label(self.w2, text='Nama', anchor='w', bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12))
                lbl1.grid(pady=6, row=0, column=0,  sticky='w', padx=10)
                inp1 = CTkEntry(self.w2, width=180, height=30, corner_radius=90, border_color='#DBDBDB')
                inp1.grid(pady=6, row=0, column=1)
                inp1.insert(0, f'{data[0]}')
                lblno = Label(self.w2, text='Nomor', anchor='w', bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12))
                lblno.grid(pady=6, row=1, column=0,  sticky='w', padx=10)
                inpno = CTkEntry(self.w2, width=70)
                inpno.grid(pady=6, row=1, column=1, sticky='w')
                inpno.insert(0, f'{data[7]}')
                lbl2 = Label(self.w2, text='Tanggal_Lahir', anchor='w', bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12))
                lbl2.grid(pady=6, row=1+1, column=0,  sticky='w', padx=10)
                inp2 = CTkEntry(self.w2, width=180, height=30, corner_radius=90, border_color='#DBDBDB')
                inp2.grid(pady=6, row=1+1, column=1)
                inp2.insert(0, f'{data[1]}')
                inp2.bind('<FocusIn>', lambda e:self.dt(e, self.inp2))
                lbl3 = Label(self.w2, text='Tinggi Badan', anchor='w', bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12))
                lbl3.grid(pady=6, row=2+1, column=0,  sticky='w', padx=10)
                inp3 = CTkEntry(self.w2, width=180, height=30, corner_radius=90, border_color='#DBDBDB')
                inp3.grid(pady=6, row=2+1, column=1)
                inp3.insert(0, f'{data[2]}')
                lbl4 = Label(self.w2, text='Berat Badan', anchor='w', bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12))
                lbl4.grid(pady=6, row=3+1, column=0,  sticky='w', padx=10)
                inp4 = CTkEntry(self.w2, width=180, height=30, corner_radius=90, border_color='#DBDBDB')
                inp4.grid(pady=6, row=3+1, column=1)
                inp4.insert(0, f'{data[3]}')
                lbl5 = Label(self.w2, text='Tipe Badan', anchor='w', bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12))
                lbl5.grid(pady=6, row=4+1, column=0,  sticky='w', padx=10)
                inp5 = CTkComboBox(self.w2, values=['Normal','Lean','Stocky'], width=180, height=30, corner_radius=90, border_color='#DBDBDB')
                inp5.grid(pady=6, row=4+1, column=1)
                inp5.set(value=f'{data[4]}')
                lbl7 = Label(self.w2, text='Kaki Dominan', anchor='w', bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12))
                lbl7.grid(pady=6, row=5+1, column=0,  sticky='w', padx=10)
                inp7 = CTkComboBox(self.w2, values=['Kanan','Kiri'], width=180, height=30, corner_radius=90, border_color='#DBDBDB')
                inp7.grid(pady=6, row=5+1, column=1)
                inp7.set(value=f'{data[5]}')
                lbl6 = Label(self.w2, text='Posisi', anchor='w', bg='#DBDBDB', fg='#060644', font=('Bookman Old Style', 12))
                lbl6.grid(pady=6, row=6+1, column=0,  sticky='w', padx=10)
                inp6 = CTkComboBox(self.w2, values=['Unknown','CAM', 'CB', 'CDM', 'CF', 'CM', 'GK', 'LB', 'LM', 'LW', 'LWB', 'RB', 'RM', 'RW', 'RWB', 'ST'],
                                        width=180, height=30, corner_radius=90, border_color='#DBDBDB')
                inp6.grid(pady=6, row=6+1, column=1)
                inp6.set(value=f'{data[6]}')
                self.btt_sv1 = CTkButton(self.fr_idk1, text='Edit', command=edt, width=346, height=40, fg_color='#060644', hover_color='#000630', font=('Bookman Old Style', 20))
                self.btt_sv1.place(x=2, y=380)

            def dlt_data():
                lbl.destroy()
                btt_see.destroy()
                btt_edt.destroy()
                btt_dlt.destroy()
                self.temp_dt[i-1] = ()
            fr_lst = CTkFrame(frame, fg_color='#DBDBDB', width=480, height=60, border_color='Black', border_width=2)
            fr_lst.grid(row=i, column=0, pady=10, padx=10)
            lbl = CTkLabel(fr_lst, text = data[0], width=280, anchor='w', text_color='#060644', font=('Bookman Old Style', 16, 'bold'))
            lbl.grid(row=0, column = 0, sticky='w', pady = 10, padx=10)
            btt_see = CTkButton(fr_lst, text='Lihat', command=lambda:see_data(data), width= 30, fg_color='#060644', hover_color='#000630', font=('Bookman Old Style', 11))
            btt_see.grid(row=0, column=1, padx=6)
            btt_edt = CTkButton(fr_lst, text='Edit', command=lambda:edt_data(i), width= 30, fg_color='#060644', hover_color='#000630', font=('Bookman Old Style', 11))
            btt_edt.grid(row=0, column=2, padx=6)
            btt_dlt = CTkButton(fr_lst, text='Hapus', command=dlt_data, width= 30, fg_color='#060644', hover_color='#000630', font=('Bookman Old Style', 11))
            btt_dlt.grid(row=0, column=3, padx=6)

    def done(self):
        while () in self.temp_dt:
            self.temp_dt.remove(())
        if len(self.temp_dt) < 1:
            showerror("Invalid Input","Jumlah Pemain dalam Tim Minimal 11 Orang")
            return
        else:
            for dtp in self.temp_dt:
                name = TreeNode((dtp[0],dtp[7]))
                name.add_child(TreeNode(dtp[1]))
                name.add_child(TreeNode(dtp[2]))
                name.add_child(TreeNode(dtp[3]))
                name.add_child(TreeNode(dtp[4]))
                name.add_child(TreeNode(dtp[5]))
                name.add_child(TreeNode(dtp[6]))
                self.tim.child[0].add_child(name)
            fl = open('Data/treeDatabase.pickle', 'wb')
            pickle.dump(self.tr_var,fl)
            self.main_fr.destroy()



# w = Tk()
# l = w.winfo_screenheight()
# p = w.winfo_screenwidth()
# fl = open('Data/treeDatabase.pickle', 'rb')
# tree_data = pickle.load(fl)
# fl.close()
# Input_Data(w, p=p, l=l, team=tree_data.child[0].child[0], root=tree_data)
# w.mainloop()

