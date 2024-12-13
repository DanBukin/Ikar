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
    # elif i==2:
    #     app = Window_2()
    #     app.mainloop()
    # elif i==3:
    #     app = Window_3()
    #     app.mainloop()
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
        self.frame2 = ctk.CTkFrame(master=self.scrollbar_frame_0, width=355, height=1000, fg_color="#2b2b2b",bg_color="transparent")
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
        self.label_11_2 = create_label(self.frame2, f"- давление на входе в форсунку (МПа)", 90, 510)
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
        self.button_1 = create_button(self.frame2, "Расчёт при выбранных значениях", lambda: self.entry_m(), self.font1, 25, 10, 475+self.x)
    def entry_m(self):
        self.m_f = float(self.entry1_value.get())
        self.nu = float(self.entry2_value.get())/1000
        self.rho = float(self.entry3_value.get())
        self.p_k = float(self.entry4_value.get())*(10**6)
        self.p_vh = float(self.entry5_value.get()) * (10 ** 6)
        self.R_gg = float(self.entry6_value.get())
        self.T_vh = float(self.entry7_value.get())
        self.n = float(self.entry8_value.get())
        self.configure_label()
    def configure_label(self):
        self.F_f = (math.pi * self.d_c * self.d_c / 4)
        self.label_12 = create_label_left(self.frame2, f'•Площадь сопла форсунки:\n{self.F_f:.2f} мм^2', 10, 505+self.x)
        self.Re=(4*self.m_f)/(math.pi*self.d_c/1000*self.nu)
        self.label_13 = create_label_left(self.frame2, f'•Число Рейнольдса:\n{self.Re:.1f}', 10, 550+self.x)
        self.W=self.m_f*1000000/(self.rho*self.F_f)
        self.label_14 = create_label_left(self.frame2, f'•Средняя скорость компонента на выходе:\n{self.W:.2f} м/с', 10, 595+self.x)

        self.mu= ( (math.sqrt( (1.23**2)+(232*self.l/(self.Re*self.d_c)) ))-1.23 )/(116*self.l/(self.Re*self.d_c))
        self.label_17 = create_label_left(self.frame2, f'•Коэффициент расхода форсунки:\n{self.mu:.6f}', 10, 595 + self.x+45)
        self.F_f_1=(self.m_f)/(self.mu*self.rho*((self.p_k/self.p_vh)**(1/self.n))*math.sqrt(2*(self.n/(self.n-1))*self.R_gg*self.T_vh*(1-((self.p_k/self.p_vh)**((self.n-1)/self.n)))) )
        self.delta_p=(self.m_f*self.m_f*(10**(12)))/(2*self.rho*self.mu*self.mu*self.F_f*self.F_f)
        self.label_18 = create_label_left(self.frame2, f'•Площадь сопла форсунки на выходе:\n{self.F_f_1*(10**(6)):.2f} мм^2', 10,
                                          595 + self.x+90)

if __name__ == "__main__":
    app = Window_1()
    app.mainloop()