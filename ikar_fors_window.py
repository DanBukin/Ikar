import math

from Ikar_functions import *
import warnings
import sys

warnings.filterwarnings("ignore", category=UserWarning)
ctk.deactivate_automatic_dpi_awareness()
FR_PRIVATE = 0x10
FR_NOT_ENUM = 0x20
if os.name == 'nt':
    windll.gdi32.AddFontResourceExW("data/ofont.ru_Futura PT.ttf", FR_PRIVATE, 0) # Загрузка пользовательского шрифта
else:
    pass
def open_window_fors(i):
    if i==1:
        app = Window_1()
        app.mainloop()
    elif i==2:
        app = Window_2()
        app.mainloop()
    elif i==3:
        app = Window_3()
        app.mainloop()
    # elif i==4:
    #     app = Window_4()
    #     app.mainloop()
    # elif i==5:
    #     app = Window_5()
    #     app.mainloop()
    # elif i==6:
    #     app = Window_6()
    #     app.mainloop()
    # elif i==7:
    #     app = Window_7()
    #     app.mainloop()
    # elif i==8:
    #     app = Window_8()
    #     app.mainloop()
    # elif i==9:
    #     app = Window_9()
    #     app.mainloop()
    # else:
    #     app = Window_10()
    #     app.mainloop()

class Window_1(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.font1 = ("Futura PT Book", 16)  # Настройка пользовательского шрифта 1
        self.font2 = ("Futura PT Book", 14)  # Настройка пользовательского шрифта 2
        self.title("Однокомпонентная струйная жидкостная форсунка")  # Название программы
        self.resizable(False, False)  # Запрет изменения размера окна
        self.geometry(f"{1305}x{734}+{100}+{100}")  # Установка размеров окна
        ctk.set_default_color_theme("data/dark-red.json")  # Загрузка пользовательской темы
        self.fg_color = 'white'
        ctk.set_widget_scaling(1.5)  # Увеличение размера виджетов
        #ctk.deactivate_automatic_dpi_awareness()
        self.after(201, lambda: self.iconbitmap('data/sunset.ico'))  # Установка иконки окна
        self.configure(bg_color="black")  # Установка цвета фона окна

        self.label_17_1=None
        self.label_18_1 = None
        self.label_19_1 = None
        self.label_20_1 = None
        self.label_15 = None
        self.label_15 = None
        self.label_16 = None
        self.label_17 = None
        self.label_18 = None
        self.label_19 = None
        self.label_20 = None

        self.l=20
        self.H=17
        self.D_f=12.75
        self.d_c=3
        self.h_og = 2.5
        self.h_sr = 2.5
        self.h_ras = 10
        self.x = 50+35
        self.choice_ist = 1

        self.place_scrollbar()
        self.setup_frame()
        self.print_label()
        self.print_slider()
        self.print_entry()
        self.print_button()
        self.print_radio_button()
        print_nozzle_1(self.H,self.D_f,self.l,self.d_c,self.h_og,self.h_sr,self.h_ras,self)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
    def on_closing(self):
        """=====Действие при нажатии на крестик закрытия окна====="""
        self.destroy()
        sys.exit()  # Завершает работу программы
    def place_scrollbar(self):
        self.scrollbar_frame_0 = ctk.CTkScrollableFrame(self, width=360, height=455,fg_color='#2b2b2b')  # 171717
        self.scrollbar_frame_0.place(x=10, y=10)
    def setup_frame(self):
        """--------------------Создание мини-окон--------------------"""
        self.frame2 = ctk.CTkFrame(master=self.scrollbar_frame_0, width=355, height=1030, fg_color="#2b2b2b",bg_color="transparent")
        self.frame2.grid(row=0, column=0, sticky='w', padx=1, pady=1)
    def print_label(self):
        self.label_1=create_label(self.frame2,"Выбери шаг между форсунками: 17 мм",2,2)
        self.label_1_0 = create_label(self.frame2, "12", 25, 26)
        self.label_1_1 = create_label(self.frame2, "30", 300, 26)
        self.label_2=create_label(self.frame2,"Диаметр форсунки равен: 12.75 мм",2,60)
        self.label_3=create_label(self.frame2,"Выбери длину форсунки: 20 мм",2,85)
        self.label_3_0 = create_label(self.frame2, "1", 35, 112)
        self.label_3_1 = create_label(self.frame2, "50", 300, 112)
        self.label_4=create_label(self.frame2,"Выберите диаметр сопла форсунки: 3 мм",2,140)
        self.label_4_0 = create_label(self.frame2, "0", 35, 163)
        self.label_4_1 = create_label(self.frame2, "10", 300, 163)
        self.label_5=create_label(self.frame2,"Относительная длина форсунки: 6.67",2,185)
        self.label_6 = create_label(self.frame2, "Выберите толщину огневого днища: 2.5 мм", 2, 215)
        self.label_6_0 = create_label(self.frame2, "2", 35, 242)
        self.label_6_1 = create_label(self.frame2, "3", 300, 242)
        self.label_7 = create_label(self.frame2, "Выберите толщину среднего днища: 2.5 мм", 2, 265)
        self.label_7_0 = create_label(self.frame2, "2", 35, 292)
        self.label_7_1 = create_label(self.frame2, "3", 300, 292)
        self.label_8 = create_label(self.frame2, "Выберите расстояние между днищами: 10 мм", 2, 315)
        self.label_8_0 = create_label(self.frame2, "8", 35, 338)
        self.label_8_1 = create_label(self.frame2, "12", 300, 338)
        self.label_9 = create_label(self.frame2, "- расход через форсунку (кг/с)", 90, 370)
        self.label_10 = create_label(self.frame2, f"- динамическая вязкость (Па*с*1000)", 90, 405)
        self.label_11 = create_label(self.frame2, f"- плотность компонента (кг/м^3)", 90, 440)
        self.label_12 = create_label(self.frame2, f"- коэф. поверхн. натяжения (Н/м)", 90, 475)

    def print_slider(self):
        self.slider1 = ctk.CTkSlider(self.frame2, from_=12, to=30, command=self.on_slider_change, number_of_steps=18,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider1.place(x=50, y=35)
        self.slider1.set(17)
        self.slider2 = ctk.CTkSlider(self.frame2, from_=1, to=50, command=self.on_slider_change_1, number_of_steps=50,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider2.place(x=50, y=120)
        self.slider2.set(20)
        self.slider3 = ctk.CTkSlider(self.frame2, from_=0, to=10, command=self.on_slider_change_2, number_of_steps=20,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider3.place(x=50, y=170)
        self.slider3.set(3)
        self.slider4 = ctk.CTkSlider(self.frame2, from_=2, to=3, command=self.on_slider_change_3, number_of_steps=10,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider4.place(x=50, y=250)
        self.slider4.set(2.5)
        self.slider5 = ctk.CTkSlider(self.frame2, from_=2, to=3, command=self.on_slider_change_4, number_of_steps=10,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider5.place(x=50, y=300)
        self.slider5.set(2.5)
        self.slider6 = ctk.CTkSlider(self.frame2, from_=8, to=12, command=self.on_slider_change_5, number_of_steps=16,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider6.place(x=50, y=347)
        self.slider6.set(10)
    def on_slider_change(self, value):
        """Обновление текста метки в соответствии со значением ползунка"""
        self.H = int(value)
        self.label_1.configure(text=f"Выбери шаг между форсунками: {self.H} мм")
        self.D_f=0.75*self.H
        if self.D_f<10:
            self.D_f=10
        self.label_2.configure(text=f"Диаметр форсунки равен: {self.D_f} мм")
        print_nozzle_1(self.H, self.D_f, self.l, self.d_c, self.h_og, self.h_sr, self.h_ras, self)
    def on_slider_change_1(self, value):
        self.l = int(value)
        self.label_3.configure(text=f"Выбери длину форсунки: {self.l} мм")
        self.label_5.configure(text=f"Относительная длина форсунки: {(self.l / self.d_c):.2f}")
        print_nozzle_1(self.H, self.D_f, self.l, self.d_c, self.h_og, self.h_sr, self.h_ras, self)
    def on_slider_change_2(self, value):
        self.d_c = float(value)
        self.label_4.configure(text=f"Выберите диаметр сопла форсунки: {self.d_c} мм")
        self.label_5.configure(text=f"Относительная длина форсунки: {(self.l / self.d_c):.2f}")
        print_nozzle_1(self.H, self.D_f, self.l, self.d_c, self.h_og, self.h_sr, self.h_ras, self)
    def on_slider_change_3(self, value):
        self.h_og = float(value)
        self.label_6.configure(text=f"Выберите толщину огневого днища: {self.h_og} мм")
        print_nozzle_1(self.H, self.D_f, self.l, self.d_c, self.h_og, self.h_sr, self.h_ras, self)
    def on_slider_change_4(self, value):
        self.h_sr = float(value)
        self.label_7.configure(text=f"Выберите толщину среднего днища: {self.h_sr} мм")
        print_nozzle_1(self.H, self.D_f, self.l, self.d_c, self.h_og, self.h_sr, self.h_ras, self)
    def on_slider_change_5(self, value):
        self.h_ras = float(value)
        self.label_8.configure(text=f"Выберите расстояние между днищами: {self.h_ras} мм")
        print_nozzle_1(self.H, self.D_f, self.l, self.d_c, self.h_og, self.h_sr, self.h_ras, self)
    def print_entry(self):
        self.entry1_value = ctk.StringVar()
        self.Entry1 = create_entry(self.frame2, 80, self.entry1_value, 2, 370)
        self.entry2_value = ctk.StringVar()
        self.Entry2 = create_entry(self.frame2, 80, self.entry2_value, 2, 405)
        self.entry3_value = ctk.StringVar()
        self.Entry3 = create_entry(self.frame2, 80, self.entry3_value, 2, 440)
        self.entry4_value = ctk.StringVar()
        self.Entry4 = create_entry(self.frame2, 80, self.entry4_value, 2, 475)
    def print_button(self):
        self.button_1 = create_button(self.frame2, "Расчёт при выбранных значениях", lambda: self.entry_m(), self.font1, 25, 10, 475+self.x)
    def print_radio_button(self):
        self.radio_var_1 = ctk.IntVar(value=1)
        self.radio_option1 = ctk.CTkRadioButton(self.frame2, text="Безотрывный режим истечения", variable=self.radio_var_1,font=self.font1,
                                                command=lambda: self.choice_1(), value=1)
        self.radio_option1.place(x=10, y=475+35)
        self.radio_option2 = ctk.CTkRadioButton(self.frame2, text="Отрывной режим истечения", variable=self.radio_var_1,font=self.font1,
                                                command=lambda: self.choice_1(), value=2)
        self.radio_option2.place(x=10, y=500+35)
    def choice_1(self):
        if self.radio_var_1.get() == 1:
            self.choice_ist=1
        else:
            self.choice_ist = 2
    def entry_m(self):
        self.m_f = float(self.entry1_value.get())
        self.nu = float(self.entry2_value.get())/1000
        self.rho = float(self.entry3_value.get())
        self.sigma=float(self.entry4_value.get())
        self.configure_label()
    def configure_label(self):
        """Создание кнопок сохранения и выхода и обновление расчётов"""
        self.button_2 = create_button(self.frame2, "Сохранить", lambda: save_txt_fors(self.text_f), self.font1, 25, 10,
                                      910 + self.x)
        self.button_3 = create_button(self.frame2, "Выход", lambda: self.destroy(), self.font1, 25, 100,
                                      910 + self.x)
        self.text_f = ''
        self.text_f += f'Форсунка жидкостная однокомпонентная струйная\nШаг между форсунками: {self.H} мм\nДиаметр форсунки: {self.D_f} мм\nДлина форсунки: {self.l} мм\nДиаметр сопла форсунки: {self.d_c} мм\n'
        self.text_f += f'Толщина огневого днища: {self.h_og} мм\nТолщина среднего днища:{self.h_sr} мм \nРасстояние между днищами: {self.h_ras} мм\n'
        self.text_f +=f'Расход через форсунку: {self.m_f} кг/с \nДинамическая вязкость: {self.nu} Па*с \nПлотность компонента: {self.rho} кг/м^3 \nКоэффициент поверхностного натяжения: {self.sigma} Н/м\n'


        self.F_f = (math.pi * self.d_c * self.d_c / 4)
        self.label_12 = create_label_left(self.frame2, f'•Площадь сопла форсунки:\n{self.F_f:.2f} мм^2', 10, 505+self.x)
        self.Re=(4*self.m_f)/(math.pi*self.d_c/1000*self.nu)
        self.label_13 = create_label_left(self.frame2, f'•Число Рейнольдса:\n{self.Re:.1f}', 10, 550+self.x)
        self.W=self.m_f*1000000/(self.rho*self.F_f)
        self.label_14 = create_label_left(self.frame2, f'•Средняя скорость компонента на выходе:\n{self.W:.2f} м/с', 10,
                                          595 + self.x)
        self.text_f += f'Площадь сопла форсунки: {self.F_f} мм^2 \nЧисло Рейнольдса: {self.Re}\nСредняя скорость компонента на выходе: {self.W} м/с\n'

        if self.choice_ist==1:
            if self.label_17_1 is not None:
                self.label_17_1.place_forget()
                self.label_18_1.place_forget()
                self.label_19_1.place_forget()
                self.label_20_1.place_forget()
            if self.Re<2000:
                self.lambda_0=64/self.Re
                self.K=2.2-(0.726*math.exp((-74.5)*((self.nu*self.l/1000)/(self.m_f))))
            elif self.Re>10000:
                self.lambda_0=0.031
                self.K =1+2.65*self.lambda_0
            else:
                self.lambda_0=0.3164*(self.Re**(-0.25))
                self.K = 1 + 2.65 * self.lambda_0
            self.mu=1/math.sqrt(self.K+(self.lambda_0*self.l / self.d_c))
            self.delta_p=(self.m_f*self.m_f*(10**(12)))/(2*self.rho*self.mu*self.mu*self.F_f*self.F_f)
            self.We = self.rho * self.W * self.W * self.d_c * 0.001 / self.sigma
            self.d_m=self.d_c*0.001*((27*math.pi/4)**(1/3))*(self.We**(-0.333))

            self.label_15 = create_label_left(self.frame2, f'•Коэффициент линейн. гидравл. сопрот-ия:\n{self.lambda_0:.6f}', 10,640+self.x)
            self.label_16 = create_label_left(self.frame2,f'•Потери на входе струйной форсунки:\n{self.K:.4f}', 10, 685 + self.x)
            self.label_17 = create_label_left(self.frame2, f'•Коэффициент расхода форсунки:\n{self.mu:.6f}', 10, 685 + self.x+45)
            self.label_18 = create_label_left(self.frame2, f'•Перепад давления на форсунке:\n{self.delta_p/10**(6):.3f} МПа', 10,685 + self.x+90)
            self.label_19 = create_label_left(self.frame2, f'•Критерий Вебера:\n{self.We:.2f}', 10,685 + self.x + 90+45)
            self.label_20 = create_label_left(self.frame2, f'•Медианный диаметр капель:\n{self.d_m*1000:.2f} мм', 10,685 + self.x + 90 + 90)

            self.text_f +="Течение безотрывное\n"
            self.text_f += f'Коэффициент линейного гидравлического сопротивления: {self.lambda_0}\n'
            self.text_f += f'Потери на входе струйной форсунки: {self.K}\n'
            self.text_f += f'Коэффициент расхода форсунки: {self.mu}\n'
            self.text_f += f'Перепад давления на форсунке: {self.delta_p/10**(6)} МПа\n'
            self.text_f += f'Критерий Вебера: {self.We}\n'
            self.text_f += f'Медианный диаметр капель: {self.d_m*1000} мм\n'
        else:
            if self.label_15 is not None:
                self.label_15.place_forget()
                self.label_16.place_forget()
                self.label_17.place_forget()
                self.label_18.place_forget()
                self.label_19.place_forget()
                self.label_20.place_forget()
            self.mu =0.63
            self.delta_p = (self.m_f * self.m_f * (10 ** (12))) / (2 * self.rho * self.mu * self.mu * self.F_f * self.F_f)
            self.We = self.rho * self.W * self.W * self.d_c * 0.001 / self.sigma
            self.d_m = self.d_c * 0.001 * ((27 * math.pi / 4) ** (1 / 3)) * (self.We ** (-0.333))

            self.label_17_1 = create_label_left(self.frame2, f'•Коэффициент расхода форсунки:\n{0.63}', 10, 640 + self.x)
            self.label_18_1 = create_label_left(self.frame2,f'•Перепад давления на форсунке:\n{self.delta_p / 10 ** (6):.3f} МПа', 10,640 + self.x + 45)
            self.label_19_1 = create_label_left(self.frame2, f'•Критерий Вебера:\n{self.We:.2f}', 10,640 + self.x + 90)
            self.label_20_1 = create_label_left(self.frame2, f'•Медианный диаметр капель:\n{self.d_m * 1000:.2f} мм', 10,640 + self.x + 90 + 45)

            self.text_f += "Течение отрывное"
            self.text_f += f'Коэффициент расхода форсунки: {0.63}\n'
            self.text_f += f'Перепад давления на форсунке: {self.delta_p / 10 ** (6)} МПа\n'
            self.text_f += f'Критерий Вебера: {self.We}\n'
            self.text_f += f'Медианный диаметр капель: {self.d_m * 1000} мм\n'

class Window_2(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.font1 = ("Futura PT Book", 16)  # Настройка пользовательского шрифта 1
        self.font2 = ("Futura PT Book", 14)  # Настройка пользовательского шрифта 2
        self.title("Однокомпонентная струйная газовая форсунка")  # Название программы
        self.resizable(False, False)  # Запрет изменения размера окна
        self.geometry(f"{1305}x{734}+{100}+{100}")  # Установка размеров окна
        ctk.set_default_color_theme("data/dark-red.json")  # Загрузка пользовательской темы
        self.fg_color = 'white'
        ctk.set_widget_scaling(1.5)  # Увеличение размера виджетов
        #ctk.deactivate_automatic_dpi_awareness()
        self.after(201, lambda: self.iconbitmap('data/sunset.ico'))  # Установка иконки окна
        self.configure(bg_color="black")  # Установка цвета фона окна

        self.l=20
        self.H=17
        self.D_f=12.75
        self.d_c=3
        self.h_og = 2.5
        self.h_sr = 2.5
        self.h_ras = 10
        self.x = 200
        self.choice_ist = 1

        self.place_scrollbar()
        self.setup_frame()
        self.print_label()
        self.print_slider()
        self.print_entry()
        self.print_button()
        print_nozzle_1(self.H,self.D_f,self.l,self.d_c,self.h_og,self.h_sr,self.h_ras,self)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
    def on_closing(self):
        """=====Действие при нажатии на крестик закрытия окна====="""
        self.destroy()
        sys.exit()  # Завершает работу программы
    def place_scrollbar(self):
        self.scrollbar_frame_0 = ctk.CTkScrollableFrame(self, width=360, height=455,fg_color='#2b2b2b')  # 171717
        self.scrollbar_frame_0.place(x=10, y=10)
    def setup_frame(self):
        """--------------------Создание мини-окон--------------------"""
        self.frame2 = ctk.CTkFrame(master=self.scrollbar_frame_0, width=355, height=1050, fg_color="#2b2b2b",bg_color="transparent")
        self.frame2.grid(row=0, column=0, sticky='w', padx=1, pady=1)
    def print_label(self):
        self.label_1=create_label(self.frame2,"Выбери шаг между форсунками: 17 мм",2,2)
        self.label_1_0 = create_label(self.frame2, "12", 25, 26)
        self.label_1_1 = create_label(self.frame2, "30", 300, 26)
        self.label_2=create_label(self.frame2,"Диаметр форсунки равен: 12.75 мм",2,60)
        self.label_3=create_label(self.frame2,"Выбери длину форсунки: 20 мм",2,85)
        self.label_3_0 = create_label(self.frame2, "1", 35, 112)
        self.label_3_1 = create_label(self.frame2, "50", 300, 112)
        self.label_4=create_label(self.frame2,"Выберите диаметр сопла форсунки: 3 мм",2,140)
        self.label_4_0 = create_label(self.frame2, "0", 35, 163)
        self.label_4_1 = create_label(self.frame2, f"{round(self.D_f)}", 300, 163)
        self.label_5=create_label(self.frame2,"Относительная длина форсунки: 6.67",2,185)
        self.label_6 = create_label(self.frame2, "Выберите толщину огневого днища: 2.5 мм", 2, 215)
        self.label_6_0 = create_label(self.frame2, "2", 35, 242)
        self.label_6_1 = create_label(self.frame2, "3", 300, 242)
        self.label_7 = create_label(self.frame2, "Выберите толщину среднего днища: 2.5 мм", 2, 265)
        self.label_7_0 = create_label(self.frame2, "2", 35, 292)
        self.label_7_1 = create_label(self.frame2, "3", 300, 292)
        self.label_8 = create_label(self.frame2, "Выберите расстояние между днищами: 10 мм", 2, 315)
        self.label_8_0 = create_label(self.frame2, "8", 35, 338)
        self.label_8_1 = create_label(self.frame2, "12", 300, 338)
        self.label_9 = create_label(self.frame2, f"- расход через форсунку (кг/с)", 90, 370)
        self.label_10 = create_label(self.frame2, f"- динамическая вязкость (Па*с*1000)", 90, 405)
        self.label_11 = create_label(self.frame2, f"- плотность компонента (кг/м^3)", 90, 440)
        self.label_11_1 = create_label(self.frame2, f"- давление в КС (МПа)", 90, 475)
        self.label_11_2 = create_label(self.frame2, f"- перепад давления в форсунке (МПа)", 90, 510)
        self.label_11_3 = create_label(self.frame2, f"- газовая постоянная (Дж/кг*К)", 90, 545)
        self.label_11_4 = create_label(self.frame2, f"- температура на входе (К)", 90, 580)
        self.label_11_5 = create_label(self.frame2, f"- показатель адиабаты", 90, 615)


    def print_slider(self):
        self.slider1 = ctk.CTkSlider(self.frame2, from_=12, to=30, command=self.on_slider_change, number_of_steps=18,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider1.place(x=50, y=35)
        self.slider1.set(17)
        self.slider2 = ctk.CTkSlider(self.frame2, from_=1, to=50, command=self.on_slider_change_1, number_of_steps=50,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider2.place(x=50, y=120)
        self.slider2.set(20)
        self.slider3 = ctk.CTkSlider(self.frame2, from_=0.5, to=round(self.D_f), command=self.on_slider_change_2, number_of_steps=round(self.D_f)*2-1,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider3.place(x=50, y=170)
        self.slider3.set(3)
        self.slider4 = ctk.CTkSlider(self.frame2, from_=2, to=3, command=self.on_slider_change_3, number_of_steps=10,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider4.place(x=50, y=250)
        self.slider4.set(2.5)
        self.slider5 = ctk.CTkSlider(self.frame2, from_=2, to=3, command=self.on_slider_change_4, number_of_steps=10,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider5.place(x=50, y=300)
        self.slider5.set(2.5)
        self.slider6 = ctk.CTkSlider(self.frame2, from_=8, to=12, command=self.on_slider_change_5, number_of_steps=16,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider6.place(x=50, y=347)
        self.slider6.set(10)
    def on_slider_change(self, value):
        """Обновление текста метки в соответствии со значением ползунка"""
        self.H = int(value)
        self.label_1.configure(text=f"Выбери шаг между форсунками: {self.H} мм")
        self.D_f=0.75*self.H
        if self.D_f<10:
            self.D_f=10
        self.label_2.configure(text=f"Диаметр форсунки равен: {self.D_f} мм")
        print_nozzle_1(self.H, self.D_f, self.l, self.d_c, self.h_og, self.h_sr, self.h_ras, self)
    def on_slider_change_1(self, value):
        self.l = int(value)
        self.label_3.configure(text=f"Выбери длину форсунки: {self.l} мм")
        self.label_5.configure(text=f"Относительная длина форсунки: {(self.l / self.d_c):.2f}")
        print_nozzle_1(self.H, self.D_f, self.l, self.d_c, self.h_og, self.h_sr, self.h_ras, self)
    def on_slider_change_2(self, value):
        self.d_c = float(value)
        self.label_4.configure(text=f"Выберите диаметр сопла форсунки: {self.d_c} мм")
        self.label_5.configure(text=f"Относительная длина форсунки: {(self.l / self.d_c):.2f}")
        print_nozzle_1(self.H, self.D_f, self.l, self.d_c, self.h_og, self.h_sr, self.h_ras, self)
    def on_slider_change_3(self, value):
        self.h_og = float(value)
        self.label_6.configure(text=f"Выберите толщину огневого днища: {self.h_og} мм")
        print_nozzle_1(self.H, self.D_f, self.l, self.d_c, self.h_og, self.h_sr, self.h_ras, self)
    def on_slider_change_4(self, value):
        self.h_sr = float(value)
        self.label_7.configure(text=f"Выберите толщину среднего днища: {self.h_sr} мм")
        print_nozzle_1(self.H, self.D_f, self.l, self.d_c, self.h_og, self.h_sr, self.h_ras, self)
    def on_slider_change_5(self, value):
        self.h_ras = float(value)
        self.label_8.configure(text=f"Выберите расстояние между днищами: {self.h_ras} мм")
        print_nozzle_1(self.H, self.D_f, self.l, self.d_c, self.h_og, self.h_sr, self.h_ras, self)
    def print_entry(self):
        self.entry1_value = ctk.StringVar()
        self.Entry1 = create_entry(self.frame2, 80, self.entry1_value, 2, 370)
        self.entry2_value = ctk.StringVar()
        self.Entry2 = create_entry(self.frame2, 80, self.entry2_value, 2, 405)
        self.entry3_value = ctk.StringVar()
        self.Entry3 = create_entry(self.frame2, 80, self.entry3_value, 2, 440)
        self.entry4_value = ctk.StringVar()
        self.Entry4 = create_entry(self.frame2, 80, self.entry4_value, 2, 475)
        self.entry5_value = ctk.StringVar()
        self.Entry5 = create_entry(self.frame2, 80, self.entry5_value, 2, 510)
        self.entry6_value = ctk.StringVar()
        self.Entry6 = create_entry(self.frame2, 80, self.entry6_value, 2, 545)
        self.entry7_value = ctk.StringVar()
        self.Entry7 = create_entry(self.frame2, 80, self.entry7_value, 2, 580)
        self.entry8_value = ctk.StringVar()
        self.Entry8 = create_entry(self.frame2, 80, self.entry8_value, 2, 615)
    def print_button(self):
        self.button_1 = create_button(self.frame2, "Расчёт при выбранных значениях", lambda: self.entry_m(), self.font1, 25, 10, 470+self.x)
    def entry_m(self):
        self.m_f = float(self.entry1_value.get())
        self.nu = float(self.entry2_value.get())/1000
        self.rho = float(self.entry3_value.get())
        self.p_k = float(self.entry4_value.get())*(10**6)
        self.delta_p = float(self.entry5_value.get()) * (10 ** 6)
        self.R_gg = float(self.entry6_value.get())
        self.T_vh = float(self.entry7_value.get())
        self.n = float(self.entry8_value.get())



        self.configure_label()
    def configure_label(self):
        self.button_2 = create_button(self.frame2, "Сохранить", lambda: save_txt_fors(self.text_f), self.font1, 25, 10,1020)
        self.button_3 = create_button(self.frame2, "Выход", lambda: self.destroy(), self.font1, 25, 100,1020)

        self.F_f = (math.pi * self.d_c * self.d_c / 4)
        self.Re=(4*self.m_f)/(math.pi*self.d_c/1000*self.nu)
        self.W=self.m_f*1000000/(self.rho*self.F_f)
        self.mu= ( (math.sqrt( (1.23**2)+(232*self.l/(self.Re*self.d_c)) ))-1.23 )/(116*self.l/(self.Re*self.d_c))
        self.F_f_1=(self.m_f)/(self.mu*self.rho*((self.p_k/(self.p_k+self.delta_p))**(1/self.n))*math.sqrt(2*(self.n/(self.n-1))*self.R_gg*self.T_vh*(1-((self.p_k/(self.p_k+self.delta_p))**((self.n-1)/self.n)))) )
        self.d_c_1=math.sqrt((4*self.F_f_1)/math.pi)*1000
        self.delta_d_c=((abs(self.d_c-self.d_c_1))*100/(self.d_c))

        self.label_12 = create_label_left(self.frame2, f'•Площадь сопла форсунки:\n{self.F_f:.2f} мм^2', 10, 505+self.x)
        self.label_13 = create_label_left(self.frame2, f'•Число Рейнольдса:\n{self.Re:.1f}', 10, 550+self.x)
        self.label_14 = create_label_left(self.frame2, f'•Средняя скорость компонента на выходе:\n{self.W:.2f} м/с', 10, 595+self.x)
        self.label_17 = create_label_left(self.frame2, f'•Коэффициент расхода форсунки:\n{self.mu:.6f}', 10, 595 + self.x+45)
        self.label_18 = create_label_left(self.frame2, f'•Площадь сопла форсунки на выходе:\n{self.F_f_1*(10**(6)):.2f} мм^2', 10,595 + self.x+90)
        self.label_19 = create_label_left(self.frame2, f'•Требуемый диаметр сопла форсунки:\n{self.d_c_1:.2f} мм',10, 595 + self.x + 90+45)
        self.label_20 = create_label_left(self.frame2,f'•Разница в диаметрах:\n{self.delta_d_c:.2f} %', 10, 595 + self.x + 180)

        self.text_f = ''
        self.text_f += f'Однокомпонентная струйная газовая форсунка\n'
        self.text_f += f'Расход через форсунку: {self.m_f} кг/с\n'
        self.text_f += f'Динамическая вязкость: {self.nu} Па*с\n'
        self.text_f += f'Плотность компонента: {self.rho} кг/м^3\n'
        self.text_f += f'Давление в КС: {self.p_k} МПа\n'
        self.text_f += f'Перепад давления в форсунке: {self.delta_p} МПа\n'
        self.text_f += f'Газовая постоянная: {self.R_gg} Дж/кг*К\n'
        self.text_f += f'Температура на входе: {self.T_vh} К\n'
        self.text_f += f'Показатель адиабаты: {self.n}\n'
        self.text_f += f'Площадь сопла форсунки: {self.F_f} мм^2\n'
        self.text_f += f'Число Рейнольдса: {self.Re}\n'
        self.text_f += f'Средняя скорость компонента на выходе: {self.W} м/с\n'
        self.text_f += f'Коэффициент расхода форсунки: {self.mu}\n'
        self.text_f += f'Площадь сопла форсунки на выходе: {self.F_f_1*(10**(6))} мм^2\n'
        self.text_f += f'Требуемый диаметр сопла форсунки: {self.d_c_1} мм\n'
        self.text_f += f'Разница в диаметрах: {self.delta_d_c} %\n'

class Window_3(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.font1 = ("Futura PT Book", 16)  # Настройка пользовательского шрифта 1
        self.font2 = ("Futura PT Book", 14)  # Настройка пользовательского шрифта 2
        self.title("Однокомпонентная центробежная жидкостная форсунка")  # Название программы
        self.resizable(False, False)  # Запрет изменения размера окна
        self.geometry(f"{1305}x{734}+{100}+{100}")  # Установка размеров окна
        ctk.set_default_color_theme("data/dark-red.json")  # Загрузка пользовательской темы
        self.fg_color = 'white'
        ctk.set_widget_scaling(1.5)  # Увеличение размера виджетов
        #ctk.deactivate_automatic_dpi_awareness()
        self.after(201, lambda: self.iconbitmap('data/sunset.ico'))  # Установка иконки окна
        self.configure(bg_color="black")  # Установка цвета фона окна

        self.H = 17
        self.d_f = 0.75 * self.H
        self.D_f=self.d_f
        self.x_st = 1.5
        self.d_kz = self.d_f - (2 * self.x_st)
        self.d_vh = 2
        self.num_copies = 4
        self.l_kz_otn = 1.5
        self.phi = 45
        self.d_c_otn = 0.5
        self.l_c_otn = 0.5
        self.h_og = 2.5
        self.h_sr = 2.5
        self.h_ras = 10

        self.place_scrollbar()
        self.setup_frame()
        self.print_label()
        self.print_entry()
        self.print_button()
        self.print_slider()
        print_nozzle_2(self.H, self.d_f, self.d_kz, self.d_vh, self.x_st, self.num_copies, self.l_kz_otn, self.phi, self.d_c_otn, self.l_c_otn, self.h_og, self.h_sr, self.h_ras,self.frame2_1)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
    def on_closing(self):
        """=====Действие при нажатии на крестик закрытия окна====="""
        self.destroy()
        sys.exit()  # Завершает работу программы
    def place_scrollbar(self):
        self.scrollbar_frame_0 = ctk.CTkScrollableFrame(self, width=360, height=455,fg_color='#2b2b2b')  # 171717
        self.scrollbar_frame_0.place(x=10, y=10)
        self.scrollbar_frame_1 = ctk.CTkScrollableFrame(self, width=445, height=455, fg_color='#131212')  # 171717
        self.scrollbar_frame_1.place(x=400, y=10)
    def setup_frame(self):
        """--------------------Создание мини-окон--------------------"""
        self.frame2 = ctk.CTkFrame(master=self.scrollbar_frame_0, width=355, height=1660, fg_color="#2b2b2b",bg_color="transparent")
        self.frame2.grid(row=0, column=0, sticky='w', padx=1, pady=1)
        self.frame2_1 = ctk.CTkFrame(master=self.scrollbar_frame_1, width=445, height=1030, fg_color="#131212",
                                   bg_color="transparent")
        self.frame2_1.grid(row=0, column=0, sticky='w', padx=1, pady=1)
    def print_label(self):
        self.x_1=240-215+50+25+25
        self.label_1=create_label(self.frame2,"Выбери шаг между форсунками: 17 мм",2,2)
        self.label_1_0 = create_label(self.frame2, "12", 25, 26)
        self.label_1_1 = create_label(self.frame2, "30", 300, 26)
        self.label_2=create_label(self.frame2,"Диаметр форсунки равен: 12.75 мм",2,60)
        self.label_3=create_label(self.frame2,"Выберите толщину стенок: 1.50 мм",2,85)
        self.label_3_0 = create_label(self.frame2, "0", 35, 112)
        self.label_3_1 = create_label(self.frame2, "5", 300, 112)
        self.label_4=create_label(self.frame2,"Выберите число отверстий: 4",2,140)
        self.label_4_0 = create_label(self.frame2, "2", 35, 163)
        self.label_4_1 = create_label(self.frame2, f"6", 300, 163)
        self.label_5 = create_label(self.frame2, "Выберите входной диаметр отверстия: 2.0 мм", 2, 190)
        self.label_5_0 = create_label(self.frame2, "0.5", 26, 215)
        self.label_5_1 = create_label(self.frame2, f"2.5", 305, 215)
        self.label_5_2_1 = create_label(self.frame2, "Длина входного отверстия: 2.10 мм", 2, 240)
        self.label_5_2_2 = create_label(self.frame2, "Отношение l_вх/d_вх: 1.05", 2, 265)

        self.label_12 = create_label(self.frame2, "Выберите относит. длину камеры закручивания: 1.5", 2, 215 + self.x_1-50)
        self.label_12_0 = create_label(self.frame2, "0.5", 26, 242 + self.x_1-50)
        self.label_12_1 = create_label(self.frame2, "3.0", 305, 242 + self.x_1-50)

        self.label_6 = create_label(self.frame2, "Выберите толщину огневого днища: 2.5 мм", 2, 215+self.x_1)
        self.label_6_0 = create_label(self.frame2, "2", 35, 242+self.x_1)
        self.label_6_1 = create_label(self.frame2, "3", 300, 242+self.x_1)
        self.label_7 = create_label(self.frame2, "Выберите толщину среднего днища: 2.5 мм", 2, 265+self.x_1)
        self.label_7_0 = create_label(self.frame2, "2", 35, 292+self.x_1)
        self.label_7_1 = create_label(self.frame2, "3", 300, 292+self.x_1)
        self.label_8 = create_label(self.frame2, "Выберите расстояние между днищами: 10 мм", 2, 315+self.x_1)
        self.label_8_0 = create_label(self.frame2, "8", 35, 338+self.x_1)
        self.label_8_1 = create_label(self.frame2, "12", 300, 338+self.x_1)
        self.label_9 = create_label(self.frame2, "Выберите угол наклона конической части: 45°", 2, 365 + self.x_1)
        self.label_9_0 = create_label(self.frame2, "30", 30, 365+27 + self.x_1)
        self.label_9_1 = create_label(self.frame2, "85", 300, 365+27 + self.x_1)
        self.label_10 = create_label(self.frame2, "Выберите относит. диаметр сопла форсунки: 0.5", 2, 415 + self.x_1)
        self.label_10_0 = create_label(self.frame2, "0.2", 26, 415 + 27 + self.x_1)
        self.label_10_1 = create_label(self.frame2, "1.0", 305, 415 + 27 + self.x_1)
        self.label_11 = create_label(self.frame2, "Выберите относит. длину сопла: 0.5", 2, 465 + self.x_1)
        self.label_11_0 = create_label(self.frame2, "0.2", 26, 465 + 27 + self.x_1)
        self.label_11_1 = create_label(self.frame2, "1.0", 305, 492 + self.x_1)

        self.label_13 = create_label(self.frame2, "- расход через форсунку (кг/с)", 90, 492 + self.x_1+32)
        self.label_14 = create_label(self.frame2, f"- динамическая вязкость (Па*с*1000)", 90, 492 + self.x_1+32+35)
        self.label_15 = create_label(self.frame2, f"- плотность компонента (кг/м^3)", 90, 492 + self.x_1+32+70)
        self.label_16 = create_label(self.frame2, f"- коэф. поверхн. натяжения (Н/м)", 90, 492 + self.x_1+32+105)
        self.label_17 = create_label(self.frame2, f"- плотность компонента в КС (кг/м^3)", 90, 492 + self.x_1 + 32 + 140)

        self.x_2=629 + self.x_1+70+35
        self.label_2_1=create_label_left(self.frame2, "•Геометрическая хар-ка форсунки:\nA=", 10, self.x_2)
        self.label_2_2 = create_label_left(self.frame2, "•Число Рейнольдса на входе в форсунку:\nRe_вх=", 10, self.x_2+45)
        self.label_2_3 = create_label_left(self.frame2, "•Коэффициент трения:\nλ=", 10,self.x_2 + 90)
        self.label_2_4 = create_label_left(self.frame2, "•Эквивалентная геом. хар-ка форсунки:\nА_э=", 10, self.x_2 + 135)
        self.label_2_5 = create_label_left(self.frame2, "•Коэффициент живого сечения:\nφ=", 10,self.x_2 + 180)
        self.label_2_6 = create_label_left(self.frame2, "•Коэффициент расхода:\nμ=", 10, self.x_2 + 225)
        self.label_2_7 = create_label_left(self.frame2, "•Средний угол факела распыла:\n2α=", 10, self.x_2 + 270)
        self.label_2_8 = create_label_left(self.frame2, "•Площадь сопла форсунки:\nF_ф=", 10, self.x_2 + 315)
        self.label_2_9 = create_label_left(self.frame2, "•Перепад давления на форсунке:\nΔp=", 10, self.x_2 + 360)
        self.label_2_10 = create_label_left(self.frame2, "•Радиус вихря жидкости:\nr_ж=", 10, self.x_2 + 360+45)
        self.label_2_11 = create_label_left(self.frame2, "•Площадь живого сечения сопла:\nF_ж=", 10, self.x_2 + 450)
        self.label_2_12 = create_label_left(self.frame2, "•Среднее значение осевой скорости:\nW_a=", 10, self.x_2 + 450+45)
        self.label_2_13 = create_label_left(self.frame2, "•Среднее значение абсолютной скорости:\nW=", 10, self.x_2 + 540)
        self.label_2_14 = create_label_left(self.frame2, "•Толщина пелены на выходе:\nδ_n=", 10, self.x_2 + 540+45)
        self.label_2_15 = create_label_left(self.frame2, "•Критерий Вебера:\nWe=", 10, self.x_2 + 630)
        self.label_2_16 = create_label_left(self.frame2, "•Критерий Лапласа:\nL_p=", 10, self.x_2 + 630+45)
        self.label_2_17 = create_label_left(self.frame2, "•Медианный диаметр капель:\nd_м=", 10, self.x_2 + 720)

        self.button_2 = create_button(self.frame2, "Сохранить", lambda: save_txt_fors(self.text_f), self.font1, 25, 10,
                                      self.x_2 + 720+50)
        self.button_3 = create_button(self.frame2, "Выход", lambda: self.destroy(), self.font1, 25, 100, self.x_2 + 720+50)

    def print_entry(self):
        self.entry1_value = ctk.StringVar()
        self.Entry1 = create_entry(self.frame2, 80, self.entry1_value, 2, 492 + self.x_1+32)
        self.entry2_value = ctk.StringVar()
        self.Entry2 = create_entry(self.frame2, 80, self.entry2_value, 2, 492 + self.x_1+32+35)
        self.entry3_value = ctk.StringVar()
        self.Entry3 = create_entry(self.frame2, 80, self.entry3_value, 2, 492 + self.x_1+32+70)
        self.entry4_value = ctk.StringVar()
        self.Entry4 = create_entry(self.frame2, 80, self.entry4_value, 2, 492 + self.x_1+32+105)
        self.entry5_value = ctk.StringVar()
        self.Entry5 = create_entry(self.frame2, 80, self.entry5_value, 2, 492 + self.x_1 + 32 + 140)
    def print_button(self):
        self.button_1 = create_button(self.frame2, "Расчёт при выбранных значениях", lambda: self.entry_m(), self.font1,25, 10, 629 + self.x_1+70)
    def entry_m(self):
        self.m_f = float(self.entry1_value.get())
        self.nu = float(self.entry2_value.get())/1000
        self.rho = float(self.entry3_value.get())
        self.sigma = float(self.entry4_value.get())
        self.rho_ks = float(self.entry5_value.get())
        self.configure_label()
    def configure_label(self):
        self.text_f=''
        self.R_vh=(0.5*self.d_kz)-(0.5*self.d_vh)
        self.d_c = self.d_c_otn * self.d_kz

        self.A=(self.R_vh*0.5*self.d_c)/(self.num_copies*0.5*self.d_vh*0.5*self.d_vh)
        self.Re_vh=(4*self.m_f)/(math.pi*self.nu*self.d_vh*0.001*math.sqrt(self.num_copies))
        self.lambda_1=10**(((25.8)/((math.log(self.Re_vh,10))**(2.58)))-2)
        self.A_e=(self.A)/(1+(0.5*self.lambda_1*self.R_vh*0.001)*((self.R_vh*0.001)+(self.d_vh*0.001)-(self.d_c*0.5*0.001)))
        self.phi_zh=1/(( ( ((self.A_e/(2*math.sqrt(2)))+(math.sqrt((self.A_e*self.A_e/8)-(1/27))))**(1/3) )+( ((self.A_e/(2*math.sqrt(2)))-(math.sqrt((self.A_e*self.A_e/8)-(1/27))))**(1/3)) )**2)
        self.mu=self.phi_zh*math.sqrt((self.phi_zh)/(2-self.phi_zh))
        self.alpha_rasp=(math.atan( (2*self.mu*self.A_e)/(math.sqrt( ((1+math.sqrt(1-self.phi_zh))**2)-(4*self.mu*self.mu*self.A_e*self.A_e) )) ))*180/math.pi
        self.F_f=math.pi*self.d_c*self.d_c*0.001*0.001/4
        self.delta_p=(self.m_f**2)/(2*self.rho*self.mu*self.mu*self.F_f*self.F_f)
        self.r_zh=self.d_c*0.5*math.sqrt(1-self.phi_zh)
        self.F_zh=self.phi_zh*self.F_f
        self.W_a=(self.m_f/(self.rho*self.F_zh))
        self.W=self.W_a/math.cos(self.alpha_rasp*math.pi/180)
        self.delta_pelen=0.5*self.d_c-self.r_zh
        self.We=(self.rho_ks*self.W*self.W*self.d_c*0.001)/(self.sigma)
        self.L_p=(self.rho*self.delta_pelen*0.001*self.sigma)/(self.nu)
        self.d_m=269*((self.L_p)**(-0.35))*(((self.We*self.rho_ks)/(self.rho))**(-0.483))


        self.label_2_1.configure(text=f"•Геометрическая хар-ка форсунки:\nA= {self.A:.3f}")
        self.label_2_2.configure(text=f"•Число Рейнольдса на входе в форсунку:\nRe_вх= {self.Re_vh:.1f}")
        self.label_2_3.configure(text=f"•Коэффициент трения:\nλ= {self.lambda_1:.3f}")
        self.label_2_4.configure(text=f"•Эквивалентная геом. хар-ка форсунки:\nА_э= {self.A_e:.3f}")
        self.label_2_5.configure(text=f"•Коэффициент живого сечения:\nφ= {self.phi_zh:.3f}")
        self.label_2_6.configure(text=f"•Коэффициент расхода:\nμ= {self.mu:.3f}")
        self.label_2_7.configure(text=f"•Средний угол факела распыла:\n2α= {2*self.alpha_rasp:.1f}°")
        self.label_2_8.configure(text=f"•Площадь сопла форсунки:\nF_ф= {self.F_f*1000000:.2f} мм^2")
        self.label_2_9.configure(text=f"•Перепад давления на форсунке:\nΔp= {self.delta_p*(10**(-6)):.3f}")
        self.label_2_10.configure(text=f"•Радиус вихря жидкости:\nr_ж= {self.r_zh:.3f}")
        self.label_2_11.configure(text=f"•Площадь живого сечения сопла:\nF_ж= {self.F_zh*1000000:.3f}")
        self.label_2_12.configure(text=f"•Среднее значение осевой скорости:\nW_a= {self.W_a:.3f}")
        self.label_2_13.configure(text=f"•Среднее значение абсолютной скорости:\nW= {self.W:.3f}")
        self.label_2_14.configure(text=f"•Толщина пелены на выходе:\nδ_n= {self.delta_pelen:.3f}")
        self.label_2_15.configure(text=f"•Критерий Вебера:\nWe= {self.We:.3f}")
        self.label_2_16.configure(text=f"•Критерий Лапласа:\nL_p= {self.L_p:.3f}")
        self.label_2_17.configure(text=f"•Медианный диаметр капель:\nd_м= {self.d_m:.3f}")


    def print_slider(self):
        self.slider1 = ctk.CTkSlider(self.frame2, from_=12, to=30, command=self.on_slider_change, number_of_steps=18,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider1.place(x=50, y=35)
        self.slider1.set(17)
        self.slider2 = ctk.CTkSlider(self.frame2, from_=0, to=5, command=self.on_slider_change_1, number_of_steps=20,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider2.place(x=50, y=120)
        self.slider2.set(1.5)
        self.slider3 = ctk.CTkSlider(self.frame2, from_=2, to=6, command=self.on_slider_change_2, number_of_steps=4,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider3.place(x=50, y=170)
        self.slider3.set(4)
        self.slider4 = ctk.CTkSlider(self.frame2, from_=0.5, to=2.5, command=self.on_slider_change_2_1, number_of_steps=20,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider4.place(x=50, y=223)
        self.slider4.set(2)
        self.slider8 = ctk.CTkSlider(self.frame2, from_=0.5, to=3.0, command=self.on_slider_change_6, number_of_steps=25,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider8.place(x=50, y=200 + self.x_1)
        self.slider8.set(1.5)
        self.slider5 = ctk.CTkSlider(self.frame2, from_=2, to=3, command=self.on_slider_change_3, number_of_steps=10,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider5.place(x=50, y=250+self.x_1)
        self.slider5.set(2.5)
        self.slider6 = ctk.CTkSlider(self.frame2, from_=2, to=3, command=self.on_slider_change_4, number_of_steps=10,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider6.place(x=50, y=300+self.x_1)
        self.slider6.set(2.5)
        self.slider7 = ctk.CTkSlider(self.frame2, from_=8, to=12, command=self.on_slider_change_5, number_of_steps=16,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider7.place(x=50, y=350+self.x_1)
        self.slider7.set(10)
        self.slider9 = ctk.CTkSlider(self.frame2, from_=30, to=85, command=self.on_slider_change_7, number_of_steps=11,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider9.place(x=50, y=400 + self.x_1)
        self.slider9.set(45)
        self.slider10 = ctk.CTkSlider(self.frame2, from_=0.2, to=1.0, command=self.on_slider_change_8, number_of_steps=16,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider10.place(x=50, y=450 + self.x_1)
        self.slider10.set(0.5)
        self.slider11 = ctk.CTkSlider(self.frame2, from_=0.2, to=1.0, command=self.on_slider_change_9,
                                      number_of_steps=16,
                                      border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                      progress_color=("#D44B46"))
        self.slider11.place(x=50, y=500 + self.x_1)
        self.slider11.set(0.5)

    def on_slider_change(self, value):
        """Обновление текста метки в соответствии со значением ползунка"""
        self.H = int(value)
        self.label_1.configure(text=f"Выбери шаг между форсунками: {self.H} мм")
        self.d_f=0.75*self.H
        self.d_kz = self.d_f - (2 * self.x_st)
        if self.d_f<10:
            self.d_f=10
        self.label_2.configure(text=f"Диаметр форсунки равен: {self.d_f} мм")
        self.l_otn=find_l_otn_kz(self.d_kz,self.d_f,self.d_vh,self.x_st)
        self.label_5_2_1.configure(text=f"Длина входного отверстия: {self.l_otn:.2f} мм")
        self.label_5_2_2.configure(text=f"Отношение l_вх/d_вх: {self.l_otn/self.d_vh:.2f}")
        print_nozzle_2(self.H, self.d_f, self.d_kz, self.d_vh, self.x_st, self.num_copies, self.l_kz_otn, self.phi,
                       self.d_c_otn, self.l_c_otn, self.h_og, self.h_sr, self.h_ras, self.frame2_1)
    def on_slider_change_1(self, value):
        self.x_st = float(value)
        self.d_kz = self.d_f - (2 * self.x_st)
        self.label_3.configure(text=f"Выберите толщину стенок: {self.x_st:.2f} мм")
        self.l_otn = find_l_otn_kz(self.d_kz, self.d_f, self.d_vh, self.x_st)
        self.label_5_2_1.configure(text=f"Длина входного отверстия: {self.l_otn:.2f} мм")
        self.label_5_2_2.configure(text=f"Отношение l_вх/d_вх: {self.l_otn / self.d_vh:.2f}")

        print_nozzle_2(self.H, self.d_f, self.d_kz, self.d_vh, self.x_st, self.num_copies, self.l_kz_otn, self.phi,
                   self.d_c_otn, self.l_c_otn, self.h_og, self.h_sr, self.h_ras, self.frame2_1)
    def on_slider_change_2(self, value):
        self.num_copies = int(value)
        self.label_4.configure(text=f"Выберите число отверстий: {self.num_copies}")
        print_nozzle_2(self.H, self.d_f, self.d_kz, self.d_vh, self.x_st, self.num_copies, self.l_kz_otn, self.phi,
                       self.d_c_otn, self.l_c_otn, self.h_og, self.h_sr, self.h_ras, self.frame2_1)
    def on_slider_change_2_1(self, value):
        self.d_vh = float(value)
        self.label_5.configure(text=f"Выберите входной диаметр отверстия: {self.d_vh:.1f} мм")
        self.l_otn = find_l_otn_kz(self.d_kz, self.d_f, self.d_vh, self.x_st)
        self.label_5_2_1.configure(text=f"Длина входного отверстия: {self.l_otn:.2f} мм")
        self.label_5_2_2.configure(text=f"Отношение l_вх/d_вх: {self.l_otn / self.d_vh:.2f}")
        print_nozzle_2(self.H, self.d_f, self.d_kz, self.d_vh, self.x_st, self.num_copies, self.l_kz_otn, self.phi,
                       self.d_c_otn, self.l_c_otn, self.h_og, self.h_sr, self.h_ras, self.frame2_1)

    def on_slider_change_3(self, value):
        self.h_og = float(value)
        self.label_6.configure(text=f"Выберите толщину огневого днища: {self.h_og} мм")
        print_nozzle_2(self.H, self.d_f, self.d_kz, self.d_vh, self.x_st, self.num_copies, self.l_kz_otn, self.phi,
                       self.d_c_otn, self.l_c_otn, self.h_og, self.h_sr, self.h_ras, self.frame2_1)
    def on_slider_change_4(self, value):
        self.h_sr = float(value)
        self.label_7.configure(text=f"Выберите толщину среднего днища: {self.h_sr} мм")
        print_nozzle_2(self.H, self.d_f, self.d_kz, self.d_vh, self.x_st, self.num_copies, self.l_kz_otn, self.phi,
                       self.d_c_otn, self.l_c_otn, self.h_og, self.h_sr, self.h_ras, self.frame2_1)

    def on_slider_change_5(self, value):
        self.h_ras = float(value)
        self.label_8.configure(text=f"Выберите расстояние между днищами: {self.h_ras} мм")
        print_nozzle_2(self.H, self.d_f, self.d_kz, self.d_vh, self.x_st, self.num_copies, self.l_kz_otn, self.phi,
                       self.d_c_otn, self.l_c_otn, self.h_og, self.h_sr, self.h_ras, self.frame2_1)
    def on_slider_change_6(self, value):
        self.l_kz_otn = float(value)
        self.label_12.configure(text=f"Выберите относит. длину камеры закручивания: {self.l_kz_otn:.1f}")
        print_nozzle_2(self.H, self.d_f, self.d_kz, self.d_vh, self.x_st, self.num_copies, self.l_kz_otn, self.phi,
                       self.d_c_otn, self.l_c_otn, self.h_og, self.h_sr, self.h_ras, self.frame2_1)
    def on_slider_change_7(self, value):
        self.phi = int(value)
        self.label_9.configure(text=f"Выберите угол наклона конической части: {self.phi}°")
        print_nozzle_2(self.H, self.d_f, self.d_kz, self.d_vh, self.x_st, self.num_copies, self.l_kz_otn, self.phi,
                       self.d_c_otn, self.l_c_otn, self.h_og, self.h_sr, self.h_ras, self.frame2_1)
    def on_slider_change_8(self, value):
        self.d_c_otn = float(value)
        self.label_10.configure(text=f"Выберите относит. диаметр сопла форсунки: {self.d_c_otn:.2f}")
        print_nozzle_2(self.H, self.d_f, self.d_kz, self.d_vh, self.x_st, self.num_copies, self.l_kz_otn, self.phi,
                       self.d_c_otn, self.l_c_otn, self.h_og, self.h_sr, self.h_ras, self.frame2_1)
    def on_slider_change_9(self, value):
        self.l_c_otn = float(value)
        self.label_11.configure(text=f"Выберите относит. длину сопла: {self.l_c_otn:.2f}")
        print_nozzle_2(self.H, self.d_f, self.d_kz, self.d_vh, self.x_st, self.num_copies, self.l_kz_otn, self.phi,
                       self.d_c_otn, self.l_c_otn, self.h_og, self.h_sr, self.h_ras, self.frame2_1)
class Window_4(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.font1 = ("Futura PT Book", 16)  # Настройка пользовательского шрифта 1
        self.font2 = ("Futura PT Book", 14)  # Настройка пользовательского шрифта 2
        self.title("Двухкомпонентная центробежно-центробежная жидкостная форсунка")  # Название программы
        self.resizable(False, False)  # Запрет изменения размера окна
        self.geometry(f"{1305}x{734}+{100}+{100}")  # Установка размеров окна
        ctk.set_default_color_theme("data/dark-red.json")  # Загрузка пользовательской темы
        self.fg_color = 'white'
        ctk.set_widget_scaling(1.5)  # Увеличение размера виджетов
        #ctk.deactivate_automatic_dpi_awareness()
        self.after(201, lambda: self.iconbitmap('data/sunset.ico'))  # Установка иконки окна
        self.configure(bg_color="black")  # Установка цвета фона окна

        self.H = 24
        self.d_f = 18
        self.delta_st_n=1.5
        self.l_c_n=1.5
        self.d_c_n=12
        self.l_kz_n=7
        self.phi_n=45
        self.d_vh_n=1.5
        self.i_vh_n=4
        self.delta_st_v=1.5
        self.d_kz_v=4
        self.l_kz_v=13
        self.d_c_v=2
        self.l_c_v =1
        self.phi_v=45
        self.d_vh_v=1
        self.i_vh_v=4
        self.h_og = 2
        self.h_sr = 2


        self.place_scrollbar()
        self.setup_frame()
        self.print_label()
        self.print_slider()
        print_nozzle_4(self.frame2_1, self.H, self.delta_st_n, self.l_c_n, self.l_kz_n, self.phi_n, self.d_c_n, self.d_vh_n,
                       self.i_vh_n, self.delta_st_v, self.l_kz_v, self.l_c_v,self.phi_v, self.d_vh_v,
                       self.i_vh_v, self.d_kz_v, self.d_c_v, self.h_og, self.h_sr)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
    def on_closing(self):
        """=====Действие при нажатии на крестик закрытия окна====="""
        self.destroy()
        sys.exit()  # Завершает работу программы
    def place_scrollbar(self):
        self.scrollbar_frame_0 = ctk.CTkScrollableFrame(self, width=360, height=455,fg_color='#2b2b2b')  # 171717
        self.scrollbar_frame_0.place(x=10, y=10)
        self.scrollbar_frame_1 = ctk.CTkScrollableFrame(self, width=445, height=455, fg_color='#131212')  # 171717
        self.scrollbar_frame_1.place(x=400, y=10)
    def setup_frame(self):
        """--------------------Создание мини-окон--------------------"""
        self.frame2 = ctk.CTkFrame(master=self.scrollbar_frame_0, width=355, height=1660, fg_color="#2b2b2b",bg_color="transparent")
        self.frame2.grid(row=0, column=0, sticky='w', padx=1, pady=1)
        self.frame2_1 = ctk.CTkFrame(master=self.scrollbar_frame_1, width=445, height=1600, fg_color="#131212",
                                   bg_color="transparent")
        self.frame2_1.grid(row=0, column=0, sticky='w', padx=1, pady=1)
    def print_label(self):
        self.label_1 = create_label(self.frame2, "Выбери шаг между форсунками: 24 мм", 2, 2)
        self.label_1_0 = create_label(self.frame2, "12", 25, 26)
        self.label_1_1 = create_label(self.frame2, "30", 300, 26)
        self.label_2 = create_label(self.frame2, "Диаметр форсунки равен: 18.00 мм", 2, 60)
        self.label_3 = create_label(self.frame2, "Выберите толщину стенок: 1.50 мм", 2, 85)
        self.label_3_0 = create_label(self.frame2, "0.5", 25, 112)
        self.label_3_1 = create_label(self.frame2, "3.0", 300, 112)
        self.label_4 = create_label(self.frame2, "Выберите длину наружнего сопла: 1.50 мм", 2, 140)
        self.label_4_0 = create_label(self.frame2, "0.5", 25, 167)
        self.label_4_1 = create_label(self.frame2, f"5.0", 300, 167)
        self.label_5 = create_label(self.frame2, "Выберите наружний диаметр сопла: 12.00 мм", 2, 140+55)
        self.label_5_0 = create_label(self.frame2, "5", 35, 167+55)
        self.label_5_1 = create_label(self.frame2, f"20", 300, 167+55)
        self.label_6 = create_label(self.frame2, "Выберите длину наруж. камеры закруч-ия: 7.00 мм", 2, 140 + 2*55)
        self.label_6_0 = create_label(self.frame2, "1", 35, 167 + 2*55)
        self.label_6_1 = create_label(self.frame2, f"20", 300, 167 + 2*55)
        self.label_7 = create_label(self.frame2, "Выберите наружний угол сужения: 45°", 2, 140 + 3*55)
        self.label_7_0 = create_label(self.frame2, "30", 30, 167 + 3*55)
        self.label_7_1 = create_label(self.frame2, f"85", 300, 167 + 3*55)
        self.label_8 = create_label(self.frame2, "Выберите диаметр наружних отверстий: 1.5 мм", 2, 140 + 4 * 55)
        self.label_8_0 = create_label(self.frame2, "0.2", 25, 167 + 4 * 55)
        self.label_8_1 = create_label(self.frame2, f"6.0", 300, 167 + 4 * 55)
        self.label_9 = create_label(self.frame2, "Выберите число наружних отверстий: 4", 2, 140 + 5 * 55)
        self.label_9_0 = create_label(self.frame2, "2", 35, 167 + 5 * 55)
        self.label_9_1 = create_label(self.frame2, f"6", 300, 167 + 5 * 55)
        self.label_10 = create_label(self.frame2, "Выберите внутреннюю толщину стенок: 1.5 мм", 2, 140 + 6 * 55)
        self.label_10_0 = create_label(self.frame2, "0.5", 25, 167 + 6 * 55)
        self.label_10_1 = create_label(self.frame2, f"3.0", 300, 167 + 6 * 55)
        self.label_11 = create_label(self.frame2, "Выберите внутр. диаметр камеры закруч-ия: 4.0 мм", 2, 140 + 7 * 55)
        self.label_11_0 = create_label(self.frame2, "0.5", 25, 167 + 7 * 55)
        self.label_11_1 = create_label(self.frame2, f"12.5", 300, 167 + 7 * 55)
        self.label_12 = create_label(self.frame2, "Выберите длину внутр. камеры закруч-ия: 13 мм ", 2, 140 + 8 * 55)
        self.label_12_0 = create_label(self.frame2, "1", 35, 167 + 8 * 55)
        self.label_12_1 = create_label(self.frame2, f"40", 300, 167 + 8 * 55)
        self.label_13 = create_label(self.frame2, "Выберите внутренний диаметр сопла: 2.0 мм", 2, 140 + 9 * 55)
        self.label_13_0 = create_label(self.frame2, "0.2", 25, 167 + 9 * 55)
        self.label_13_1 = create_label(self.frame2, f"8.0", 300, 167 + 9 * 55)
        self.label_14 = create_label(self.frame2, "Выберите длину внутреннего сопла: 1.00 мм ", 2, 140 + 10 * 55)
        self.label_14_0 = create_label(self.frame2, "0.5", 25, 167 + 10 * 55)
        self.label_14_1 = create_label(self.frame2, f"5.0", 300, 167 + 10 * 55)
        self.label_15 = create_label(self.frame2, "Выберите внутренний угол сужения: 45°", 2, 140 + 11 * 55)
        self.label_15_0 = create_label(self.frame2, "30", 25, 167 + 11 * 55)
        self.label_15_1 = create_label(self.frame2, f"85", 300, 167 + 11 * 55)
        self.label_16 = create_label(self.frame2, "Выберите диаметр внутренних отверстий: 1.0 мм", 2, 140 + 12 * 55)
        self.label_16_0 = create_label(self.frame2, "0.2", 25, 167 + 12 * 55)
        self.label_16_1 = create_label(self.frame2, f"8.0", 300, 167 + 12 * 55)
        self.label_17 = create_label(self.frame2, "Выберите число внутренних отверстий: 4", 2, 140 + 13 * 55)
        self.label_17_0 = create_label(self.frame2, "2", 35, 167 + 13 * 55)
        self.label_17_1 = create_label(self.frame2, f"6", 300, 167 + 13 * 55)

    def print_slider(self):
        self.slider1 = ctk.CTkSlider(self.frame2, from_=12, to=30, command=self.on_slider_change_1, number_of_steps=18,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider1.place(x=50, y=35)
        self.slider1.set(24)
        self.slider2 = ctk.CTkSlider(self.frame2, from_=0.5, to=3, command=self.on_slider_change_2, number_of_steps=25,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider2.place(x=50, y=120)
        self.slider2.set(1.5)
        self.slider3 = ctk.CTkSlider(self.frame2, from_=0.5, to=5, command=self.on_slider_change_3, number_of_steps=18,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider3.place(x=50, y=120+55)
        self.slider3.set(1.5)
        self.slider4 = ctk.CTkSlider(self.frame2, from_=5, to=20, command=self.on_slider_change_4, number_of_steps=30,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider4.place(x=50, y=120 + 2*55)
        self.slider4.set(12)
        self.slider5 = ctk.CTkSlider(self.frame2, from_=1, to=20, command=self.on_slider_change_5, number_of_steps=38,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider5.place(x=50, y=120 + 3 * 55)
        self.slider5.set(7)
        self.slider6 = ctk.CTkSlider(self.frame2, from_=30, to=85, command=self.on_slider_change_6, number_of_steps=11,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider6.place(x=50, y=120 + 4 * 55)
        self.slider6.set(45)
        self.slider7 = ctk.CTkSlider(self.frame2, from_=0.2, to=6, command=self.on_slider_change_7, number_of_steps=29,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider7.place(x=50, y=120 + 5 * 55)
        self.slider7.set(1.5)
        self.slider8 = ctk.CTkSlider(self.frame2, from_=2, to=6, command=self.on_slider_change_8, number_of_steps=4,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider8.place(x=50, y=120 + 6 * 55)
        self.slider8.set(4)
        self.slider9 = ctk.CTkSlider(self.frame2, from_=0.5, to=3.0, command=self.on_slider_change_9, number_of_steps=25,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider9.place(x=50, y=120 + 7 * 55)
        self.slider9.set(1.5)
        self.slider10 = ctk.CTkSlider(self.frame2, from_=0.5, to=12.5, command=self.on_slider_change_10,number_of_steps=24,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider10.place(x=50, y=120 + 8 * 55)
        self.slider10.set(4)
        self.slider11 = ctk.CTkSlider(self.frame2, from_=1, to=40, command=self.on_slider_change_11,number_of_steps=39,
                                      border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                      progress_color=("#D44B46"))
        self.slider11.place(x=50, y=120 + 9 * 55)
        self.slider11.set(13)
        self.slider12 = ctk.CTkSlider(self.frame2, from_=0.2, to=8, command=self.on_slider_change_12,number_of_steps=39,
                                      border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                      progress_color=("#D44B46"))
        self.slider12.place(x=50, y=120 + 10 * 55)
        self.slider12.set(2)
        self.slider13 = ctk.CTkSlider(self.frame2, from_=0.5, to=5.0, command=self.on_slider_change_13,number_of_steps=18,
                                      border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                      progress_color=("#D44B46"))
        self.slider13.place(x=50, y=120 + 11 * 55)
        self.slider13.set(1)
        self.slider14 = ctk.CTkSlider(self.frame2, from_=30, to=85, command=self.on_slider_change_14,number_of_steps=11,
                                      border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                      progress_color=("#D44B46"))
        self.slider14.place(x=50, y=120 + 12 * 55)
        self.slider14.set(45)
        self.slider15 = ctk.CTkSlider(self.frame2, from_=0.2, to=8.0, command=self.on_slider_change_15,
                                      number_of_steps=39,
                                      border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                      progress_color=("#D44B46"))
        self.slider15.place(x=50, y=120 + 13 * 55)
        self.slider15.set(1)
        self.slider16 = ctk.CTkSlider(self.frame2, from_=2, to=6, command=self.on_slider_change_16,
                                      number_of_steps=4,
                                      border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                      progress_color=("#D44B46"))
        self.slider16.place(x=50, y=120 + 14 * 55)
        self.slider16.set(4)
    def on_slider_change_1(self, value):
        self.H = float(value)
        self.d_f=0.75*self.H
        self.d_kz_n = self.d_f - (2 * self.delta_st_n)
        self.label_1.configure(text=f"Выбери шаг между форсунками: {self.H:.0f} мм")
        self.label_2.configure(text=f"Диаметр форсунки равен: {self.d_f:.2f} мм")
        print_nozzle_4(self.frame2_1, self.H, self.delta_st_n, self.l_c_n, self.l_kz_n, self.phi_n, self.d_c_n,
                       self.d_vh_n,
                       self.i_vh_n, self.delta_st_v, self.l_kz_v, self.l_c_v, self.phi_v, self.d_vh_v,
                       self.i_vh_v, self.d_kz_v, self.d_c_v, self.h_og, self.h_sr)
    def on_slider_change_2(self, value):
        self.delta_st_n = float(value)
        self.d_kz_n = self.d_f - (2 * self.delta_st_n)
        self.label_3.configure(text=f"Выберите толщину стенок: {self.delta_st_n:.2f} мм")
        print_nozzle_4(self.frame2_1, self.H, self.delta_st_n, self.l_c_n, self.l_kz_n, self.phi_n, self.d_c_n,
                       self.d_vh_n,
                       self.i_vh_n, self.delta_st_v, self.l_kz_v, self.l_c_v, self.phi_v, self.d_vh_v,
                       self.i_vh_v, self.d_kz_v, self.d_c_v, self.h_og, self.h_sr)
    def on_slider_change_3(self, value):
        self.l_c_n = float(value)
        self.label_4.configure(text=f"Выберите длину наружнего сопла: {self.l_c_n:.2f} мм")
        print_nozzle_4(self.frame2_1, self.H, self.delta_st_n, self.l_c_n, self.l_kz_n, self.phi_n, self.d_c_n,
                       self.d_vh_n,
                       self.i_vh_n, self.delta_st_v, self.l_kz_v, self.l_c_v, self.phi_v, self.d_vh_v,
                       self.i_vh_v, self.d_kz_v, self.d_c_v, self.h_og, self.h_sr)
    def on_slider_change_4(self, value):
        self.d_c_n = float(value)
        self.label_5.configure(text=f"Выберите наружний диаметр сопла: {self.d_c_n:.2f} мм")
        print_nozzle_4(self.frame2_1, self.H, self.delta_st_n, self.l_c_n, self.l_kz_n, self.phi_n, self.d_c_n,
                       self.d_vh_n,
                       self.i_vh_n, self.delta_st_v, self.l_kz_v, self.l_c_v, self.phi_v, self.d_vh_v,
                       self.i_vh_v, self.d_kz_v, self.d_c_v, self.h_og, self.h_sr)
    def on_slider_change_5(self, value):
        self.l_kz_n = float(value)
        self.label_6.configure(text=f"Выберите длину наруж. камеры закруч-ия: {self.l_kz_n:.2f} мм")
        print_nozzle_4(self.frame2_1, self.H, self.delta_st_n, self.l_c_n, self.l_kz_n, self.phi_n, self.d_c_n,
                       self.d_vh_n,
                       self.i_vh_n, self.delta_st_v, self.l_kz_v, self.l_c_v, self.phi_v, self.d_vh_v,
                       self.i_vh_v, self.d_kz_v, self.d_c_v, self.h_og, self.h_sr)
    def on_slider_change_6(self, value):
        self.phi_n = float(value)
        self.label_7.configure(text=f"Выберите наружний угол сужения: {self.phi_n:.0f}°")
        print_nozzle_4(self.frame2_1, self.H, self.delta_st_n, self.l_c_n, self.l_kz_n, self.phi_n, self.d_c_n,
                       self.d_vh_n,
                       self.i_vh_n, self.delta_st_v, self.l_kz_v, self.l_c_v, self.phi_v, self.d_vh_v,
                       self.i_vh_v, self.d_kz_v, self.d_c_v, self.h_og, self.h_sr)
    def on_slider_change_7(self, value):
        self.d_vh_n = float(value)
        self.label_8.configure(text=f"Выберите диаметр наружних отверстий: {self.d_vh_n:.1f} мм")
        print_nozzle_4(self.frame2_1, self.H, self.delta_st_n, self.l_c_n, self.l_kz_n, self.phi_n, self.d_c_n,
                       self.d_vh_n,
                       self.i_vh_n, self.delta_st_v, self.l_kz_v, self.l_c_v, self.phi_v, self.d_vh_v,
                       self.i_vh_v, self.d_kz_v, self.d_c_v, self.h_og, self.h_sr)
    def on_slider_change_8(self, value):
        self.i_vh_n = int(value)
        self.label_9.configure(text=f'Выберите число наружних отверстий: {self.i_vh_n:.0f}')
        print_nozzle_4(self.frame2_1, self.H, self.delta_st_n, self.l_c_n, self.l_kz_n, self.phi_n, self.d_c_n,
                       self.d_vh_n,
                       self.i_vh_n, self.delta_st_v, self.l_kz_v, self.l_c_v, self.phi_v, self.d_vh_v,
                       self.i_vh_v, self.d_kz_v, self.d_c_v, self.h_og, self.h_sr)
    def on_slider_change_9(self, value):
        self.delta_st_v = float(value)
        self.label_10.configure(text=f'Выберите внутреннюю толщину стенок: {self.delta_st_v:.1f} мм')
        print_nozzle_4(self.frame2_1, self.H, self.delta_st_n, self.l_c_n, self.l_kz_n, self.phi_n, self.d_c_n,
                       self.d_vh_n,
                       self.i_vh_n, self.delta_st_v, self.l_kz_v, self.l_c_v, self.phi_v, self.d_vh_v,
                       self.i_vh_v, self.d_kz_v, self.d_c_v, self.h_og, self.h_sr)
    def on_slider_change_10(self, value):
        self.d_kz_v=float(value)
        self.label_11.configure(text=f'Выберите внутр. диаметр камеры закруч-ия: {self.d_kz_v:.1f} мм')
        print_nozzle_4(self.frame2_1, self.H, self.delta_st_n, self.l_c_n, self.l_kz_n, self.phi_n, self.d_c_n,
                       self.d_vh_n,
                       self.i_vh_n, self.delta_st_v, self.l_kz_v, self.l_c_v, self.phi_v, self.d_vh_v,
                       self.i_vh_v, self.d_kz_v, self.d_c_v, self.h_og, self.h_sr)
    def on_slider_change_11(self, value):
        self.l_kz_v=float(value)
        self.label_12.configure(text=f'Выберите длину внутр. камеры закруч-ия: {self.l_kz_v:.0f} мм')
        print_nozzle_4(self.frame2_1, self.H, self.delta_st_n, self.l_c_n, self.l_kz_n, self.phi_n, self.d_c_n,
                       self.d_vh_n,
                       self.i_vh_n, self.delta_st_v, self.l_kz_v, self.l_c_v, self.phi_v, self.d_vh_v,
                       self.i_vh_v, self.d_kz_v, self.d_c_v, self.h_og, self.h_sr)
    def on_slider_change_12(self, value):
        self.d_c_v=float(value)
        self.label_13.configure(text=f"Выберите внутренний диаметр сопла: {self.d_c_v:.1f} мм")
        print_nozzle_4(self.frame2_1, self.H, self.delta_st_n, self.l_c_n, self.l_kz_n, self.phi_n, self.d_c_n,
                       self.d_vh_n,
                       self.i_vh_n, self.delta_st_v, self.l_kz_v, self.l_c_v, self.phi_v, self.d_vh_v,
                       self.i_vh_v, self.d_kz_v, self.d_c_v, self.h_og, self.h_sr)
    def on_slider_change_13(self, value):
        self.l_c_v=float(value)
        self.label_14.configure(text=f"Выберите длину внутреннего сопла: {self.l_c_v:.2f} мм ")
        print_nozzle_4(self.frame2_1, self.H, self.delta_st_n, self.l_c_n, self.l_kz_n, self.phi_n, self.d_c_n,
                       self.d_vh_n,
                       self.i_vh_n, self.delta_st_v, self.l_kz_v, self.l_c_v, self.phi_v, self.d_vh_v,
                       self.i_vh_v, self.d_kz_v, self.d_c_v, self.h_og, self.h_sr)
    def on_slider_change_14(self, value):
        self.phi_v=float(value)
        self.label_15.configure(text=f'Выберите внутренний угол сужения: {self.phi_v:.0f}°')
        print_nozzle_4(self.frame2_1, self.H, self.delta_st_n, self.l_c_n, self.l_kz_n, self.phi_n, self.d_c_n,
                       self.d_vh_n,
                       self.i_vh_n, self.delta_st_v, self.l_kz_v, self.l_c_v, self.phi_v, self.d_vh_v,
                       self.i_vh_v, self.d_kz_v, self.d_c_v, self.h_og, self.h_sr)
    def on_slider_change_15(self, value):
        self.d_vh_v=float(value)
        self.label_16.configure(text=f'Выберите диаметр внутренних отверстий: {self.d_vh_v:.1f} мм')
        print_nozzle_4(self.frame2_1, self.H, self.delta_st_n, self.l_c_n, self.l_kz_n, self.phi_n, self.d_c_n,
                       self.d_vh_n,
                       self.i_vh_n, self.delta_st_v, self.l_kz_v, self.l_c_v, self.phi_v, self.d_vh_v,
                       self.i_vh_v, self.d_kz_v, self.d_c_v, self.h_og, self.h_sr)
    def on_slider_change_16(self, value):
        self.i_vh_v=int(value)
        self.label_17.configure(text=f"Выберите число внутренних отверстий: {self.i_vh_v:.0f}")
        print_nozzle_4(self.frame2_1, self.H, self.delta_st_n, self.l_c_n, self.l_kz_n, self.phi_n, self.d_c_n,
                       self.d_vh_n,
                       self.i_vh_n, self.delta_st_v, self.l_kz_v, self.l_c_v, self.phi_v, self.d_vh_v,
                       self.i_vh_v, self.d_kz_v, self.d_c_v, self.h_og, self.h_sr)
if __name__ == "__main__":
    app = Window_4()
    app.mainloop()