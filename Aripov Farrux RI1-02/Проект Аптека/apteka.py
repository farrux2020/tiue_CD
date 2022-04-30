from pydoc import classname
import tkinter as tk
from tkinter.constants import S
from tkinter import *







class SampleAPP(tk.Tk):
    def __init__(self, *arg, **kwargs ):
        tk.Tk.__init__(self, *arg, **kwargs)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        
   


        self.frames = {}
        for F in(StartPage, Admin, AdminMed_tab, AdminMed_tex, Registration, MenuPage, tabletki, Med_instrument, information, Optom, bases, texnika):
            page_name = F.__name__
            frame = F(parent = container, controller = self)
            self.frames[page_name] = frame



            frame. grid(row = 0, column = 0, sticky="nsew")

            self.show_frame("StartPage")


    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.backGroundImage = PhotoImage(file = r'img/fon_g.png')
        self.backGroundImageLabel = Label(self, width=0, height=0,  image=self.backGroundImage)
        self.backGroundImageLabel.place(x = 0, y = 0)


        self.controller = controller
        self.controller.title("Аптека 24/7")
        self.controller.geometry('1250x650')
        self.controller.resizable(0, 0)
        self.controller.iconbitmap('img\logo.ico')


        # Названия title
        heading_lable = tk.Label(self, text="Аптека 24/7", font = ('Monotype Corsiva', 50, 'bold'), fg="red", bg='#badee7')
        heading_lable.pack(pady=50)
        heading_lable.place(x=100, y = 20)

        # Авторизация
        # логин
        login_lable = tk.Label(self, text="введите логин", font = ('Monotype Corsiva', 20, 'bold'), bg="#b8dce7", fg='black')
        login_lable.pack()
        login_lable.place(x=180, y=120)
       
        my_login = tk.StringVar()

        login_entry = tk.Entry(self, textvariable = my_login, font = ('Monotype Corsiva', 20, 'bold'), bg="#b8dce7", fg="black")
        login_entry.pack(pady=20)
        login_entry.place(x=140, y=180)
       
       

       # пароль
        password_lable = tk.Label(self, text="введите пароль", font = ('Monotype Corsiva', 20, 'bold'), bg="#b8dce7", fg="black")
        password_lable.pack()
        password_lable.place(x=180, y=240)


        my_password = tk.StringVar()

        password_entry = tk.Entry(self, show="*", textvariable = my_password, font = ('Monotype Corsiva', 20, 'bold'), bg="#b8dce7", fg="black")
        password_entry.pack()
        password_entry.place(x=140, y=300)

        def check_password():
            if my_password.get() == "1" and my_login.get() == "1":
                controller.show_frame('MenuPage')

            elif my_password.get() == "1" and my_login.get() == "admin":
                controller.show_frame('Admin')
                
                
                #right_label = tk.Label(self, text="Добро пожаловать")
                #right_label.pack()

            else:
                wrong_lable['text'] = "Неверный логин или пароль"

        password_button = tk.Button(self, text=" Вход ", activebackground="#b8dce7", command=check_password, bg="#b8dce7", width = 15)
        password_button.pack()
        password_button.place(x=210, y=370)

        wrong_lable = tk.Label(self, font = ('Monotype Corsiva', 20, 'bold'), bg="#b8dce7", fg="red")
        wrong_lable.pack(pady=30)
        wrong_lable.place(x=130, y=410)


        def reg():
            controller.show_frame('Registration')
        pa_button = tk.Button(self, text=" Регистрация ", command=reg, bg="#b8dce7", activebackground="#b8dce7",  width = 15)
        pa_button.pack()
        pa_button.place(x=210, y=460)

# Пункт регистраци

class Registration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#58BAE1")
        self.controller = controller


        self.backGroundImage = PhotoImage(file = r'img/fon_register.png')
        self.backGroundImageLabel = Label(self, width=0, height=0,  image=self.backGroundImage)
        self.backGroundImageLabel.place(x = 0, y = 0)



        heading_lable = tk.Label(self, text="Регистрация нового пользователя", font = ('Monotype Corsiva', 25, 'bold'), fg="red", bg="#f4f0f8")
        heading_lable.pack()
        heading_lable.place(x=100, y=20)

        name_1_lable = tk.Label(self, text="Фамилия", font = ('Monotype Corsiva', 15, 'bold'), fg="red", bg="#efeef5")
        name_1_lable.pack()
        name_1_lable.place(x=270, y=70)

        name_1_entry = tk.Entry(self,  font = ('Monotype Corsiva', 15, 'bold'), bg='#eceaf2', fg="black")
        name_1_entry.pack(pady=0)
        name_1_entry.place(x=210, y=110)

        name_2_lable = tk.Label(self, text="Имя", font = ('Monotype Corsiva', 15, 'bold'), fg="red", bg="#efedf4")
        name_2_lable.pack()
        name_2_lable.place(x=290, y=150)

        name_2_entry = tk.Entry(self,  font = ('Monotype Corsiva', 15, 'bold'), bg="#efedf4", fg="black")
        name_2_entry.pack(pady=0)
        name_2_entry.place(x=210, y=200)

        name_3_lable = tk.Label(self, text="Логин", font = ('Monotype Corsiva', 15, 'bold'), fg="red", bg="#eae8ed")
        name_3_lable.pack()
        name_3_lable.place(x=290, y=250)

        name_3_entry = tk.Entry(self,  font = ('Monotype Corsiva', 15, 'bold'), bg="#eae8ed", fg="black")
        name_3_entry.pack()
        name_3_entry.place(x=210, y=300)

        name_4_lable = tk.Label(self, text="Пароль", font = ('Monotype Corsiva', 15, 'bold'), fg="red", bg="#eae8ed")
        name_4_lable.pack()
        name_4_lable.place(x=290, y=350)
        

        name_4_entry = tk.Entry(self, show="*", font = ('Monotype Corsiva', 15, 'bold'), bg="#eae8ed", fg="black")
        name_4_entry.pack()
        name_4_entry.place(x=210, y=400)
        

        name_5_lable = tk.Label(self, text="Пароль ещё раз", font = ('Monotype Corsiva', 15, 'bold'), fg="red", bg="#eae8ed")
        name_5_lable.pack()
        name_5_lable.place(x=260, y=450)
        

        name_5_entry = tk.Entry(self, show="*", font = ('Monotype Corsiva', 15, 'bold'), bg="#eae8ed", fg="black")
        name_5_entry.pack()
        name_5_entry.place(x=210, y=500)
        

        save_button = tk.Button(self, text=" создать нового пользователя ", activebackground="#eae8ed", command=0, bg="#eae8ed",  width = 25, font = ('Monotype Corsiva', 14, 'bold'),  fg="black")
        save_button.pack()
        save_button.place(x = 170, y = 550)

        def exit():
            controller.show_frame('StartPage')

        tabletki_button = tk.Button(self, text=" назад ", activebackground="#eae8ed",  command=exit, bg="#eae8ed",  width = 10,  font = ('Monotype Corsiva', 13, 'bold'),  fg="black")
        tabletki_button.pack()
        tabletki_button.place(x = 255, y = 600)
#---------------------------------------------------

# Пункт Админ

class Admin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.backGroundImage = PhotoImage(file = r'img/admin.png')
        self.backGroundImageLabel = Label(self, width=0, height=0,  image=self.backGroundImage)
        self.backGroundImageLabel.place(x = 0, y = 0)

        heading_lable = tk.Label(self, text=" Админ... Добро пожаловать! ", font = ('Monotype Corsiva', 25, 'bold'), fg="blue", bg="white")
        heading_lable.pack(pady=10)


        def Ntabletki():
            controller.show_frame('AdminMed_tab')  # Медикаменты

        tabletki_button = tk.Button(self, text=" Медикаменты ", activebackground="#c8e3e2", activeforeground="white", command = Ntabletki, bg="#c8e3e2",  width = 15, font = ('Monotype Corsiva', 25, 'bold'), fg="#003EFF")
        tabletki_button.pack()
        tabletki_button.place(x = 210, y = 70)


        def Med_instrument():
            controller.show_frame('AdminMed_tex')  # Мед-инструметы

        instrument_button = tk.Button(self, text=" Мед-инструметы ", activebackground="#c8e3e2", activeforeground="white",  command=Med_instrument,  width = 15, bg="#c8e3e2", font = ('Monotype Corsiva', 25, 'bold'), fg="#003EFF")
        instrument_button.pack()
        instrument_button.place(x = 550, y = 70)




       

        tabletki_button = tk.Button(self, text=" Выйте из системы ", command=exit, bg="#c8e3e2", activebackground="#c8e3e2", activeforeground="red", width = 15, font = ('Monotype Corsiva', 25, 'bold'), fg="#003EFF")
        tabletki_button.pack()
        tabletki_button.place(x = 900, y = 70)






class AdminMed_tab(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#4AF8A6")
        self.controller = controller

        self.backGroundImage = PhotoImage(file = r'img/fon_tabletki.png')
        self.backGroundImageLabel = Label(self, width=0, height=0,  image=self.backGroundImage)
        self.backGroundImageLabel.place(x = 0, y = 0)


     
           
        def admin():
            controller.show_frame('Admin')

        tabletki_button = tk.Button(self, text=" назад ", activebackground="white", activeforeground="red", command=admin, bg="#8bd1c7",  width = 10, font = ('Monotype Corsiva', 15, 'bold'), fg="red")
        tabletki_button.pack()
        tabletki_button.place(x = 590, y = 590)

    

        heading_lable = tk.Label(self, text="Выберите категорию", font = ('Monotype Corsiva', 25, 'bold'), fg="red", bg="#8bd1c7")
        heading_lable.pack(pady=50)

        #def bases():
        #    controller.show_frame('bases')

        tabletki_button = tk.Button(self, text=" Антиоксиданты ", activebackground="white", activeforeground="red", command=bases, bg="#8bd1c7",  width = 15, font = ('Monotype Corsiva', 20, 'bold'), fg="red")
        tabletki_button.pack()
        tabletki_button.place(x = 500, y = 110)



        #def bases():
        #    controller.show_frame('bases')

        tabletki_button = tk.Button(self, text=" Антибиотики ", activebackground="white", activeforeground="red", command=bases, bg="#8bd1c7",  width = 15, font = ('Monotype Corsiva', 20, 'bold'), fg="red")
        tabletki_button.pack()
        tabletki_button.place(x = 530, y = 190)



        #def bases():
        #    controller.show_frame('bases')

        tabletki_button = tk.Button(self, text=" Глазные капли ", activebackground="white", activeforeground="red", command=bases, bg="#8bd1c7",  width = 15, font = ('Monotype Corsiva', 20, 'bold'), fg="red")
        tabletki_button.pack()
        tabletki_button.place(x = 500, y = 270)


        #def bases():
        #    controller.show_frame('bases')

        tabletki_button = tk.Button(self, text=" Антисептики ", activebackground="white", activeforeground="red", command=bases, bg="#8bd1c7",  width = 15, font = ('Monotype Corsiva', 20, 'bold'), fg="red")
        tabletki_button.pack()
        tabletki_button.place(x = 530, y = 350)



        #def bases():
        #    controller.show_frame('bases')

        tabletki_button = tk.Button(self, text=" Противовирусные ", activebackground="white", activeforeground="red", command=bases, bg="#8bd1c7",  width = 15, font = ('Monotype Corsiva', 20, 'bold'), fg="red")
        tabletki_button.pack()
        tabletki_button.place(x = 500, y = 430)



        #def bases():
        #    controller.show_frame('bases')

        tabletki_button = tk.Button(self, text=" Дерматологические ", activebackground="white", activeforeground="red", command=bases, bg="#8bd1c7",  width = 15, font = ('Monotype Corsiva', 20, 'bold'), fg="red")
        tabletki_button.pack()
        tabletki_button.place(x = 530, y = 510)






class AdminMed_tex(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.backGroundImage = PhotoImage(file = r'img/fon_tex.png')
        self.backGroundImageLabel = Label(self, width=0, height=0,  image=self.backGroundImage)
        self.backGroundImageLabel.place(x = 0, y = 0)

        

        heading_lable = tk.Label(self, text="Выберите нужные мед инструменты", font = ('Monotype Corsiva', 30, 'bold'), fg="blue", bg="#7ed6d8")
        heading_lable.pack()
        heading_lable.place(x = 350, y = 30)


        #def texnika():
        #    controller.show_frame('texnika')

        tabletki_button = tk.Button(self, text=" Слуховые аппараты ", activebackground="white", activeforeground="red", command=texnika, bg="#7ed6d8",  width = 17, font = ('Monotype Corsiva', 16, 'bold'), fg="blue")
        tabletki_button.pack()
        tabletki_button.place(x = 20, y = 580)



        #def texnika():
        #    controller.show_frame('texnika')

        tabletki_button = tk.Button(self, text=" Диагностическая техника ", activebackground="white", activeforeground="red", command=texnika, bg="#7ed6d8",  width = 20, font = ('Monotype Corsiva', 16, 'bold'), fg="blue")
        tabletki_button.pack()
        tabletki_button.place(x = 260, y = 580)



        #def texnika():
        #    controller.show_frame('texnika')

        tabletki_button = tk.Button(self, text="Кварцевые лампы", activebackground="white", activeforeground="red", command=texnika, bg="#7ed6d8",  width = 15, font = ('Monotype Corsiva', 16, 'bold'), fg="blue")
        tabletki_button.pack()
        tabletki_button.place(x = 530, y = 580)


        #def texnika():
        #    controller.show_frame('texnika')

        tabletki_button = tk.Button(self, text=" Прочая медтехника ", activebackground="white", activeforeground="red", command=texnika, bg="#7ed6d8",  width = 15, font = ('Monotype Corsiva', 16, 'bold'), fg="blue")
        tabletki_button.pack()
        tabletki_button.place(x = 750, y = 580)



        def Admin():
            controller.show_frame('Admin')
            
        tabletki_button = tk.Button(self, text=" назад ", activebackground="white", activeforeground="red", command=Admin, bg="#7ed6d8",  width = 15, font = ('Monotype Corsiva', 16, 'bold'), fg="blue")
        tabletki_button.pack()
        tabletki_button.place(x = 1000, y = 580)





# Пункт главного меню

class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#4AF8A6")
        self.controller = controller

        self.backGroundImage = PhotoImage(file = r'img/fon_menu.png')
        self.backGroundImageLabel = Label(self, width=0, height=0,  image=self.backGroundImage)
        self.backGroundImageLabel.place(x = 0, y = 0)


        

     
              
        heading_lable = tk.Label(self, text=" Добро пожаловать! ", font = ('Monotype Corsiva', 25, 'bold'), fg="blue", bg="#96b7b9")
        heading_lable.pack(pady=10)

        heading_lable = tk.Label(self, text=" Выберите пункт ", font = ('Monotype Corsiva', 25, 'bold'), fg="blue", bg="#a2bbbd")
        heading_lable.pack(pady=10)




        def Ntabletki():
            controller.show_frame('tabletki')  # Медикаменты

        tabletki_button = tk.Button(self, text=" Медикаменты ", activebackground="#c8e3e2", activeforeground="white", command = Ntabletki, bg="#c8e3e2",  width = 15, font = ('Monotype Corsiva', 25, 'bold'), fg="#003EFF")
        tabletki_button.pack()
        tabletki_button.place(x = 210, y = 130)


        def Med_instrument():
            controller.show_frame('Med_instrument')  # Мед-инструметы

        instrument_button = tk.Button(self, text=" Мед-инструметы ", activebackground="#c8e3e2", activeforeground="white",  command=Med_instrument,  width = 15, bg="#c8e3e2", font = ('Monotype Corsiva', 25, 'bold'), fg="#003EFF")
        instrument_button.pack()
        instrument_button.place(x = 250, y = 260)


        





        def information():
            controller.show_frame('information')    # Информация

        tabletki_button = tk.Button(self, text=" Информация ", command=information, bg="#c8e3e2", activebackground="#c8e3e2", activeforeground="white", width = 15, font = ('Monotype Corsiva', 25, 'bold'), fg="#003EFF")
        tabletki_button.pack()
        tabletki_button.place(x = 290, y = 390)



        def exit():
            controller.show_frame('StartPage')    # Выйте из системы

        tabletki_button = tk.Button(self, text=" Выйте из системы ", command=exit, bg="#c8e3e2", activebackground="#c8e3e2", activeforeground="red", width = 15, font = ('Monotype Corsiva', 25, 'bold'), fg="#003EFF")
        tabletki_button.pack()
        tabletki_button.place(x = 330, y = 520)



      

class tabletki(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="yellow")
        self.controller = controller


        self.backGroundImage = PhotoImage(file = r'img/fon_tabletki.png')
        self.backGroundImageLabel = Label(self, width=0, height=0,  image=self.backGroundImage)
        self.backGroundImageLabel.place(x = 0, y = 0)


     
           
        def back_menu():
            controller.show_frame('MenuPage')

        tabletki_button = tk.Button(self, text=" назад ", activebackground="white", activeforeground="red", command=back_menu, bg="#8bd1c7",  width = 10, font = ('Monotype Corsiva', 15, 'bold'), fg="red")
        tabletki_button.pack()
        tabletki_button.place(x = 590, y = 590)

    

        heading_lable = tk.Label(self, text="Выберите категорию", font = ('Monotype Corsiva', 25, 'bold'), fg="red", bg="#8bd1c7")
        heading_lable.pack(pady=50)

        def bases():
            controller.show_frame('bases')

        tabletki_button = tk.Button(self, text=" Антиоксиданты ", activebackground="white", activeforeground="red", command=bases, bg="#8bd1c7",  width = 15, font = ('Monotype Corsiva', 20, 'bold'), fg="red")
        tabletki_button.pack()
        tabletki_button.place(x = 500, y = 110)



        def bases():
            controller.show_frame('bases')

        tabletki_button = tk.Button(self, text=" Антибиотики ", activebackground="white", activeforeground="red", command=bases, bg="#8bd1c7",  width = 15, font = ('Monotype Corsiva', 20, 'bold'), fg="red")
        tabletki_button.pack()
        tabletki_button.place(x = 530, y = 190)



        def bases():
            controller.show_frame('bases')

        tabletki_button = tk.Button(self, text=" Глазные капли ", activebackground="white", activeforeground="red", command=bases, bg="#8bd1c7",  width = 15, font = ('Monotype Corsiva', 20, 'bold'), fg="red")
        tabletki_button.pack()
        tabletki_button.place(x = 500, y = 270)


        def bases():
            controller.show_frame('bases')

        tabletki_button = tk.Button(self, text=" Антисептики ", activebackground="white", activeforeground="red", command=bases, bg="#8bd1c7",  width = 15, font = ('Monotype Corsiva', 20, 'bold'), fg="red")
        tabletki_button.pack()
        tabletki_button.place(x = 530, y = 350)



        def bases():
            controller.show_frame('bases')

        tabletki_button = tk.Button(self, text=" Противовирусные ", activebackground="white", activeforeground="red", command=bases, bg="#8bd1c7",  width = 15, font = ('Monotype Corsiva', 20, 'bold'), fg="red")
        tabletki_button.pack()
        tabletki_button.place(x = 500, y = 430)

        



        def bases():
            controller.show_frame('bases')

        tabletki_button = tk.Button(self, text=" Дерматологические ", activebackground="white", activeforeground="red", command=bases, bg="#8bd1c7",  width = 15, font = ('Monotype Corsiva', 20, 'bold'), fg="red")
        tabletki_button.pack()
        tabletki_button.place(x = 530, y = 510)

#-------------------------------------------------

class bases(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.backGroundImage = PhotoImage(file = r'img/zag.png')
        self.backGroundImageLabel = Label(self, width=0, height=0,  image=self.backGroundImage)
        self.backGroundImageLabel.place(x = 0, y = 0)

        heading_lable = tk.Label(self, text=" идет загрузка, пожалуйста подождите... ", font = ('Monotype Corsiva', 25, 'bold'), fg="white", bg="#f3850b")
        heading_lable.pack(pady=50)


        antiseptik = tk.Label(self, text= "Лекарство  5 500 сум", font = ('Monotype Corsiva', 25, 'bold'), fg="white", bg="#f3850b")
        antiseptik.pack()

        #-------------------------
        antiseptik_1 = tk.Label(self, text= "укажите количество", font = ('Monotype Corsiva', 15, 'bold'), fg="red", bg="#f3850b")
        antiseptik_1.pack()
        natija = tk.Label(self, text='Оплата ')
        natija.place(x=570,y=310, width=120, height=40)
        a = 5500
        miqdor = tk.Entry(self)
        miqdor.pack()

        def farq():
            narx = a
            natija.config(text=int(narx) * int(miqdor.get() ))

        tugma = tk.Button(self, text='рассчитать', command=farq)
        tugma.place(x = 570, y = 250)

        #---------------------------------
        
        dostavka_1 = tk.Label(self, text= "укажите км (1-km 1 500) ", font = ('Monotype Corsiva', 15, 'bold'), fg="red", bg="#f3850b")
        dostavka_1.place(x=790, y=190)
        natija_2 = tk.Label(self, text='Оплата за км ')
        natija_2.place(x=790, y=310, width=120, height=40)
        b = 1500
        metr = tk.Entry(self)
        metr.place(x=790, y=220)

        def farq_2():
            km = b
            natija_2.config(text=int(km) * int(metr.get() ))

        tugma_2 = tk.Button(self, text='рассчитать', command=farq_2)
        tugma_2.place(x=800, y=250)

        #---------------------------------


            
        def tabletki():
            controller.show_frame('tabletki')

        tabletki_button = tk.Button(self, text=" назад ", 
                                    command=tabletki, 
                                    bg="#f3850b",  
                                    activebackground="#f3850b", 
                                    activeforeground="red",  
                                    width = 10, 
                                    font = ('Monotype Corsiva', 15, 'bold'), 
                                    fg="white")
        tabletki_button.pack()
        tabletki_button.place(x = 575, y = 530)


        

#---------------------------------------------------

class information(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.backGroundImage = PhotoImage(file = r'img/fon_info2.png')
        self.backGroundImageLabel = Label(self, width=0, height=0,  image=self.backGroundImage)
        self.backGroundImageLabel.place(x = 0, y = 0)





        def back_menu():
            controller.show_frame('MenuPage')

        tabletki_button = tk.Button(self, text=" назад ", 
                                    command=back_menu, 
                                    bg="#dff4f0",  
                                    activebackground="#c8e3e2", 
                                    activeforeground="white",  
                                    width = 10, 
                                    font = ('Monotype Corsiva', 15, 'bold'), 
                                    fg="red")
        tabletki_button.pack()
        tabletki_button.place(x = 575, y = 450)






class Optom(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.backGroundImage = PhotoImage(file = r'img/fon_instrument.png')
        self.backGroundImageLabel = Label(self, width=0, height=0,  image=self.backGroundImage)
        self.backGroundImageLabel.place(x = 0, y = 0)







#______MenTexnika


   
class Med_instrument(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.backGroundImage = PhotoImage(file = r'img/fon_tex.png')
        self.backGroundImageLabel = Label(self, width=0, height=0,  image=self.backGroundImage)
        self.backGroundImageLabel.place(x = 0, y = 0)

        

        heading_lable = tk.Label(self, text="Выберите нужные мед инструменты", font = ('Monotype Corsiva', 30, 'bold'), fg="blue", bg="#7ed6d8")
        heading_lable.pack()
        heading_lable.place(x = 350, y = 30)


        def texnika():
            controller.show_frame('texnika')

        tabletki_button = tk.Button(self, text=" Слуховые аппараты ", activebackground="white", activeforeground="red", command=texnika, bg="#7ed6d8",  width = 17, font = ('Monotype Corsiva', 16, 'bold'), fg="blue")
        tabletki_button.pack()
        tabletki_button.place(x = 20, y = 580)



        def texnika():
            controller.show_frame('texnika')

        tabletki_button = tk.Button(self, text=" Диагностическая техника ", activebackground="white", activeforeground="red", command=texnika, bg="#7ed6d8",  width = 20, font = ('Monotype Corsiva', 16, 'bold'), fg="blue")
        tabletki_button.pack()
        tabletki_button.place(x = 260, y = 580)



        def texnika():
            controller.show_frame('texnika')

        tabletki_button = tk.Button(self, text="Кварцевые лампы", activebackground="white", activeforeground="red", command=texnika, bg="#7ed6d8",  width = 15, font = ('Monotype Corsiva', 16, 'bold'), fg="blue")
        tabletki_button.pack()
        tabletki_button.place(x = 530, y = 580)


        def texnika():
            controller.show_frame('texnika')

        tabletki_button = tk.Button(self, text=" Прочая медтехника ", activebackground="white", activeforeground="red", command=texnika, bg="#7ed6d8",  width = 15, font = ('Monotype Corsiva', 16, 'bold'), fg="blue")
        tabletki_button.pack()
        tabletki_button.place(x = 750, y = 580)



    





        def back_menu():
            controller.show_frame('MenuPage')
            
        tabletki_button = tk.Button(self, text=" назад ", activebackground="white", activeforeground="red", command=back_menu, bg="#7ed6d8",  width = 15, font = ('Monotype Corsiva', 16, 'bold'), fg="blue")
        tabletki_button.pack()
        tabletki_button.place(x = 1000, y = 580)




class texnika(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.backGroundImage = PhotoImage(file = r'img/fon_zag_tex.png')
        self.backGroundImageLabel = Label(self, width=0, height=0,  image=self.backGroundImage)
        self.backGroundImageLabel.place(x = 0, y = 0)

        heading_lable = tk.Label(self, text=" идет загрузка, пожалуйста подождите... ", font = ('Monotype Corsiva', 25, 'bold'), fg="white", bg="#297d9c")
        heading_lable.pack()
        heading_lable.place(x = 350, y = 3)

        #-----------------------------
      

         #-----------------------------

        texnika_2 = tk.Label(self, text= "Укажите количество техники (1-шт 3 500 00) ", font = ('Monotype Corsiva', 15, 'bold'), fg="red", bg="#f3850b")
        texnika_2.place(x=790, y=190)
        natija_3 = tk.Label(self, text='итого ')
        natija_3.place(x=790, y=310, width=120, height=40)
        b = 3500000
        metr = tk.Entry(self, fg='white', bg='black')
        metr.place(x=790, y=240)

        def farq_3():
            km = b
            natija_3.config(text=int(km) * int(metr.get() ))

        tugma_3 = tk.Button(self, text='рассчитать', command=farq_3)
        tugma_3.place(x=800, y=280)








        def Med_instrument():
            controller.show_frame('Med_instrument')

        tabletki_button = tk.Button(self, text=" назад ", 
                                    command=Med_instrument, 
                                    bg="#155e7c",  
                                    activebackground="white", 
                                    activeforeground="red",  
                                    width = 10, 
                                    font = ('Monotype Corsiva', 15, 'bold'), 
                                    fg="white")
        tabletki_button.pack()
        tabletki_button.place(x = 650, y = 600)





if __name__=="__main__":
    app = SampleAPP()
    app.mainloop()