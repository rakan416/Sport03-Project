from tkinter import *
from customtkinter import *
import time
import pickle
from PIL import Image, ImageTk
from Tree_Processing import TreeNode


class InputSkill():

    def __init__(self, window, data_tree, root, kelas):
        self.tr_var = root
        self.tree_data = data_tree
        self.kelas = kelas

        self.window = window
        # self.window.geometry('1366x768')
        self.window.state('zoomed')
        self.FRAME = Frame(self.window, bg='black', width=1366, height=768)
        self.FRAME.place(x=0, y=0)
        self.fr1 = CTkFrame(self.FRAME, fg_color='#1F2833', width=840, height=110, corner_radius=30)
        self.fr1.place(x=263, y=35)
        self.btt_pilih = CTkButton(self.fr1, text='CHOOSE PLAYER', width=330, height=70, corner_radius=30, font=('russo one',20), command=self.pilih,
                                   border_color='#66FCF1', fg_color='transparent', border_width=5, hover_color='#45A29E')
        self.btt_pilih.place(x = 20, y=20)
        self.analitic_skill = {
                                'ATT': [0, 1, 2, 24],
                                'TEC': [3, 4, 5, 6, 7, 8, 9],
                                'STA': [12, 13, 14, 17],
                                'DEF': [20, 21, 22, 26, 27, 28],
                                'POW': [15, 16, 18, 19, 23, 25],
                                'SPD': [10, 11]
                                }

        self.data_det = ['Crossing','Finishing','Heading Accuracy','Short Passing','Volleys','Dribbling','Curve','Freekick Accuracy','Long Passing','Ball Control','Acceleration','Sprint Speed','Agility','Reactions','Balance','Shot Power','Jumping','Stamina','Strength','Long Shots','Aggression','Interceptions','Positioning','Vision','Penalties','Composure','Marking','Standing Tackle','Sliding Tackle']
        



        self.fr_plyr = CTkFrame(self.FRAME, width=30, height=690, corner_radius=30, fg_color='#1F2833')
        self.fr_plyr.place(x=35, y=35)
        self.i = 0

        self.fr_att = Frame(self.fr1, bg='#1F2833', width=270, height=80)
        self.lbl_att = Label(self.fr_att, text='ATTACK' , bg='#1F2833', font=('russo one', 13, 'bold'), fg='#D9D9D9', anchor='w')
        self.sld_att = CTkSlider(self.fr_att, bg_color='#1F2833', from_=0, to= 100,width=250, button_color='#66fcf1', button_hover_color='#45A29E', progress_color='#66fcf1',
                                 command=lambda val: self.Sliding(val=int(val), lbl=self.num_att, indx=0, gol=self.analitic_skill['ATT']))
        self.sld_att.set(0)
        self.num_att = Label(self.fr_att,text=0, bg='#1F2833', font=('russo one', 13, 'bold'), fg='#D9D9D9')

        self.fr_tec = Frame(self.fr1, bg='#1F2833', width=270, height=80)
        self.lbl_tec = Label(self.fr_tec, text='TECHNIQUE' , bg='#1F2833', font=('russo one', 13, 'bold'), fg='#D9D9D9', anchor='w')
        self.sld_tec = CTkSlider(self.fr_tec, bg_color='#1F2833', from_=0, to= 100,width=250, button_color='#66fcf1', button_hover_color='#45A29E', progress_color='#66fcf1',
                                 command=lambda val: self.Sliding(val=int(val), lbl=self.num_tec, indx=1, gol=self.analitic_skill['TEC']))
        self.sld_tec.set(0)
        self.num_tec = Label(self.fr_tec,text=0, bg='#1F2833', font=('russo one', 13, 'bold'), fg='#D9D9D9')

        self.fr_sta = Frame(self.fr1, bg='#1F2833', width=270, height=80)
        self.lbl_sta = Label(self.fr_sta, text='STAMINA' , bg='#1F2833', font=('russo one', 13, 'bold'), fg='#D9D9D9', anchor='w')
        self.sld_sta = CTkSlider(self.fr_sta, bg_color='#1F2833', from_=0, to= 100,width=250, button_color='#66fcf1', button_hover_color='#45A29E', progress_color='#66fcf1',
                                 command=lambda val: self.Sliding(val=int(val), lbl=self.num_sta, indx=2, gol=self.analitic_skill['STA']))
        self.sld_sta.set(0)
        self.num_sta = Label(self.fr_sta,text=0, bg='#1F2833', font=('russo one', 13, 'bold'), fg='#D9D9D9')

        self.fr_def = Frame(self.fr1, bg='#1F2833', width=270, height=80)
        self.lbl_def = Label(self.fr_def, text='DEFENSE' , bg='#1F2833', font=('russo one', 13, 'bold'), fg='#D9D9D9', anchor='w')
        self.sld_def = CTkSlider(self.fr_def, bg_color='#1F2833', from_=0, to= 100,width=250, button_color='#66fcf1', button_hover_color='#45A29E', progress_color='#66fcf1',
                                 command=lambda val: self.Sliding(val=int(val), lbl=self.num_def, indx=3, gol=self.analitic_skill['DEF']))
        self.sld_def.set(0)
        self.num_def = Label(self.fr_def,text=0, bg='#1F2833', font=('russo one', 13, 'bold'), fg='#D9D9D9')

        self.fr_pow = Frame(self.fr1, bg='#1F2833', width=270, height=80)
        self.lbl_pow = Label(self.fr_pow, text='POWER' , bg='#1F2833', font=('russo one', 13, 'bold'), fg='#D9D9D9', anchor='w')
        self.sld_pow = CTkSlider(self.fr_pow, bg_color='#1F2833', from_=0, to= 100,width=250, button_color='#66fcf1', button_hover_color='#45A29E', progress_color='#66fcf1',
                                 command=lambda val: self.Sliding(val=int(val), lbl=self.num_pow, indx=4, gol=self.analitic_skill['POW']))
        self.sld_pow.set(0)
        self.num_pow = Label(self.fr_pow,text=0, bg='#1F2833', font=('russo one', 13, 'bold'), fg='#D9D9D9')

        self.fr_spd = Frame(self.fr1, bg='#1F2833', width=270, height=80)
        self.lbl_spd = Label(self.fr_spd, text='SPEED' , bg='#1F2833', font=('russo one', 13, 'bold'), fg='#D9D9D9', anchor='w')
        self.sld_spd = CTkSlider(self.fr_spd, bg_color='#1F2833', from_=0, to= 100,width=250, button_color='#66fcf1', button_hover_color='#45A29E', progress_color='#66fcf1',
                                 command=lambda val: self.Sliding(val=int(val), lbl=self.num_spd, indx=5, gol=self.analitic_skill['SPD']))
        self.sld_spd.set(0)
        self.num_spd = Label(self.fr_spd,text=0, bg='#1F2833', font=('russo one', 13, 'bold'), fg='#D9D9D9')

        self.btt_more = CTkButton(self.fr1, text='MORE DETAIL \/', width=820, height=30, command=self.detail)

        self.btt_save = CTkButton(self.fr1, text='SAVE', fg_color='transparent', text_color='#D9D9D9', font=('russo one', 13, 'bold'), width=250, height=50, corner_radius=30, border_color='#66fcf1', border_width=2, hover_color='#45a29e', command=self.simpan)

        self.btt_done = CTkButton(self.fr1, text='DONE', fg_color='transparent', text_color='#D9D9D9', font=('russo one', 13, 'bold'), width=100, height=50, corner_radius=30, border_color='green', border_width=2, hover_color='#075E54', command=self.done)
        
    def muncul_input(self):
            self.fr_att.place(x=10, y=136)
            self.lbl_att.place(x=0, y=0,height=20,width=168)
            self.sld_att.place(x=0, y = 30)
            self.num_att.place(x=120, y=55, width=30, height=20)
            self.fr_tec.place(x=290, y=136)        
            self.lbl_tec.place(x=0, y=0,height=20,width=168)
            self.sld_tec.place(x=0, y = 30)
            self.num_tec.place(x=120, y=55, width=30, height=20)
            self.fr_sta.place(x=570, y=136)        
            self.lbl_sta.place(x=0, y=0,height=20,width=168)
            self.sld_sta.place(x=0, y = 30)
            self.num_sta.place(x=120, y=55, width=30, height=20)
            self.fr_def.place(x=10, y=236)        
            self.lbl_def.place(x=0, y=0,height=20,width=168)
            self.sld_def.place(x=0, y = 30)
            self.num_def.place(x=120, y=55, width=30, height=20)
            self.fr_pow.place(x=290, y=236)        
            self.lbl_pow.place(x=0, y=0,height=20,width=168)
            self.sld_pow.place(x=0, y = 30)
            self.num_pow.place(x=120, y=55, width=30, height=20)
            self.fr_spd.place(x=570, y=236)        
            self.lbl_spd.place(x=0, y=0,height=20,width=168)
            self.sld_spd.place(x=0, y = 30)
            self.num_spd.place(x=120, y=55, width=30, height=20)
            self.btt_more.place(x=15, y=330)
            self.btt_save.place(x=20, y=600)
            self.btt_done.place(x=700, y=600)


    def geser(self, pos_bef, pos_x, width_bef, width_after, height_bef, height_after):
        if self.i > 0:
            self.profile_player(self.name)
            return
        
        if pos_bef >= pos_x:
            pass
            if height_bef >= height_after:
                pass
            else: height_bef += 20
            self.fr1.configure(height = height_bef)
        else: pos_bef += 20

        if width_bef >= width_after:
            pass
        else: width_bef += 20

        if pos_bef >= pos_x and width_bef >= width_after and height_bef >= height_after:
            self.i += 1
            self.profile_player(self.name)
            return
        self.fr1.place_configure(x=pos_bef)
        self.fr_plyr.configure(width = width_bef)
        self.window.after(10, lambda: self.geser(pos_bef, pos_x, width_bef, width_after, height_bef, height_after))

    def profile_player(self, player):
        try:
            self.fr_identity.destroy()
            self.lbl_name.destroy()
        except: pass
        self.lbl_name = CTkLabel(self.fr_plyr, text=player.data[0].upper(), width=310, height=30, text_color='#D9D9D9', font=('russo one', 18, 'bold'))
        self.lbl_name.place(x=50, y=300)
        self.fr_identity = CTkFrame(self.fr_plyr, fg_color='#1F2833', width=328, height=232, border_color='#66fcf1', border_width=3)
        self.fr_identity.place(x=42, y=350)
        self.lbl_birth = CTkLabel(self.fr_identity, text=f'BIRTHDAY\n{player.child[0].data}', width=110, height=50, anchor='w', text_color='#D9D9D9', font=('russo one', 13, 'bold'))
        self.lbl_birth.place(x=22, y=16)
        self.lbl_height = CTkLabel(self.fr_identity, text=f'HEIGHT\n{player.child[1].data}', width=110, height=50, anchor='w', text_color='#D9D9D9', font=('russo one', 13, 'bold'))
        self.lbl_height.place(x=22, y=85)
        self.lbl_weight = CTkLabel(self.fr_identity, text=f'WEIGHT\n{player.child[2].data}', width=110, height=50, anchor='w', text_color='#D9D9D9', font=('russo one', 13, 'bold'))
        self.lbl_weight.place(x=22, y=160)
        kaki = player.child[4].data
        if kaki == 'Kanan':
            path_img = 'Image/right_feet.png'
        elif kaki == 'Kiri':
            path_img = 'Image/left_feet.png'
        img_open = Image.open(path_img).resize((85,75))
        global gambar
        gambar = ImageTk.PhotoImage(img_open)
        self.lbl_prefot = CTkLabel(self.fr_identity, text=f'PREFFERD FOOT\n{kaki.upper()}', width=150, height=55, text_color='#D9D9D9', font=('russo one', 13, 'bold'))
        self.lbl_prefot.place(x=160, y=5)
        self.lbl_imgfot = Label(self.fr_identity, image=gambar, bg='#1F2833')
        self.lbl_imgfot.place(x=195, y=50)
        self.lbl_position = CTkLabel(self.fr_identity, text=f'POSITION\n{player.child[5].data}', width=160, height=50, text_color='#D9D9D9', font=('russo one', 13, 'bold'))
        self.lbl_position.place(x=160, y=150)
        self.lbl_identity = CTkLabel(self.fr_plyr, text= 'IDENTITY', width=80, height=15, text_color='#66fcf1', font=('russo one', 13, 'italic'), fg_color='transparent')
        self.lbl_identity.place(x=60,y=340)

    def tutup(self, fr):
        self.btt_pilih.configure(state='normal')
        fr.destroy()

    def pilih(self):
        self.btt_pilih.configure(state='disabled')
        try:
            self.fr_pilih.destroy()
        except: pass
        self.fr2 = CTkFrame(self.FRAME, fg_color='black', width=530, height=360, corner_radius=10, border_color='#ff8c00', border_width=3)
        self.fr2.place(x=(1366/2)-250, y=768/4)
        self.btt_cancel = CTkButton(self.fr2, text='Cancel', command=lambda: self.tutup(self.fr2), width=50, height=30, border_color='#a21424', border_width=2, fg_color='transparent', text_color='red', font=('Russo one', 10, 'bold'), hover_color='#3e1816')
        self.btt_cancel.place(x=530-55,y=5)
        self.fr_pilih = CTkScrollableFrame(self.fr2, fg_color='black', width=500, height=300)
        self.fr_pilih.place(x=3, y=40)
        dt = self.tree_data.child[0].child
        i = 0
        for player in dt:
            try:
                player.child[6].child[0].data
                brdr = '#66fcf1'
            except:
                brdr = '#1f2833'
            self.summon_button(self.fr_pilih, player, player.child[5].data, i, brdr)
            i+=1

    
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

    def summon_button(self, frame, nama, pos, row, border):
        def plyr():
            self.name = nama
            self.geser(int(self.fr1.place_info()['x']), 483, 30, 430, self.fr1['height'], 690)
            if self.i <= 1:
                self.window.after(1500, lambda: self.muncul_input())
            self.fr2.destroy()
            self.btt_pilih.configure(state='normal')
            try:
                self.temp = self.name.child[6].child[0].data
            except:
                self.temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
            self.btt_save.configure(state='normal')
            self.btt_done.configure(state='disabled')
            self.cancel()

            

        btt_ply = CTkButton(frame,text='',  command=plyr, corner_radius=0, width=480, height= 30, hover=None, fg_color='black', border_width=2, border_color=border)
        btt_ply.grid(row=row, column=0, sticky='w', pady=5)
        lbl1 = Label(btt_ply, text=nama.data[0].upper(), bg='black', fg='#d9d9d9', font=('Russo one', 10, 'bold'))
        lbl1.place(x=2, y=2, height= 26)
        lbl1.bind("<Button-1>", lambda e: plyr())
        lbl2 = Label(btt_ply, text=pos, bg='black', fg='#d9d9d9', anchor='e')
        lbl2.place(x=415, y=2,width=60, height= 26)
        lbl2.bind("<Button-1>", lambda e: plyr())
        
    def Sliding(self, val, lbl, indx, gol):
        lbl.configure(text = val)
        temp = 0
        for i in gol:
            self.temp[i] = val
            temp += val
        self.skill_ply[indx] = temp



    def count_mean(self, before, after, indk, indx, ln):
        try:
            self.skill_ply[indx] += (after-before)
        except:
            self.skill_ply = []
            self.skill_ply[indx] += (after-before)
        indk[0].set(self.skill_ply[indx]/ln)
        indk[1].configure(text=int(self.skill_ply[indx]/ln))

    def detail(self):
        self.frsld = Frame(self.fr1, width=830, height=230, bg='#1F2833')
        self.frsld.place(x=10, y=370)
        self.fr_sld_inp = CTkScrollableFrame(self.frsld, width=810, height=230, fg_color='#1F2833')
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

    def summon_slider(self, rw,cl, dt, fr, stv, indk, indx, ln):
        def sliding(value, sc):
            sc.configure(text=value)
            temp_num = self.temp[self.data_det.index(dt)]
            self.temp[self.data_det.index(dt)] = value
            self.count_mean(temp_num, value, indk, indx, ln)

        temp_fr = CTkFrame(fr, width=250, height=45, border_color='#66fcf1', border_width=1, fg_color='#1F2833')
        temp_fr.grid(column=cl, row=rw, pady=5, padx=10)
        lbl = Label(temp_fr, text=dt , bg='#1F2833', font=('Russo one', 10, 'bold'), anchor='w', fg='#D9D9D9')
        lbl.place(x=10, y=-5,height=20)
        sld = CTkSlider(temp_fr, bg_color='#1F2833', from_=0, to= 100,width=200, command= lambda val:sliding(int(val), num), button_color='#66fcf1', button_hover_color='#45A29E', progress_color='#66fcf1')
        sld.place(x=10, y = 20)
        sld.set(stv)
        hsl = int(sld.get())
        num = Label(temp_fr,text=hsl, bg='#1F2833',anchor='w', fg='#D9D9D9')
        num.place(x=210, y=20, width=30, height=20)



    def simpan(self):
        if sum(self.temp) == 0:
            return
        self.fr_identity.destroy()
        self.lbl_name.destroy()
        self.lbl_identity.destroy()
        self.fr_plyr.configure(width=30)
        try:
            self.name.child[6].child[0].data = self.temp
        except:
            try:
                self.name.child[6].add_child(TreeNode(self.temp))
            except:
                self.skill = TreeNode('Kemampuan')
                self.skill.add_child(TreeNode(self.temp))
                self.name.add_child(self.skill)

        temp_list = []
        for num in self.temp:
            temp_list.append(num)

        try:
            histrain = self.name.child[7].child[0]
            if histrain.data == 0:
                histrain.child[0].data = temp_list
            else:
                first = TreeNode(0)
                first.add_child(TreeNode(temp_list))
                self.name.child[7].child.insert(0, first)
        except:
            first = TreeNode(0)
            first.add_child(TreeNode(temp_list))
            try:
                self.name.child[7].add_child(first)
            except:
                head = TreeNode('History Training')
                head.add_child(first)
                self.name.add_child(head)

        try:
            self.name.child[8].data
        except:
            self.name.add_child(TreeNode('Match History'))

        fl = open('Data/treeDatabase.pickle', 'wb')
        pickle.dump(self.tr_var, fl)
        fl.close()
        self.btt_save.configure(state='disabled')
        self.btt_done.configure(state='normal')
        self.i = 0
        self.name = None
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
        self.btt_save.configure(state='disabled')
        self.btt_done.configure(state='normal')
        self.cancel()


    def done(self):
        self.kelas.refresh()
        self.FRAME.destroy()



# w = Tk()
# fl = open('Data/treePlayer.pickle', 'rb')
# root = pickle.load(fl)
# tree_data = root.child[0]
# fl.close()
# InputSkill(w, tree_data, root)

# w.mainloop()