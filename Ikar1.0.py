from Ikar_functions import *
from Ikar_Kompas_3D import *
from ikar_graphs import *
from Searching_for_component_costs import *
import customtkinter as ctk
import os
from ctypes import windll
import warnings

warnings.filterwarnings("ignore", category=UserWarning)
FR_PRIVATE = 0x10
FR_NOT_ENUM = 0x20
if os.name == 'nt':
    windll.gdi32.AddFontResourceExW("data/ofont.ru_Futura PT.ttf", FR_PRIVATE, 0) # Загрузка пользовательского шрифта
else:
    pass
class user:
    def __init__(self):
        self.nozzle_diagram=None # Схема форсуночной головки
        self.choice = None
        self.D_k = None
        self.H = None
        self.number_pr = None
        self.delta_wall = None
        self.delta = None
        self.delta_y_pr = None
        self.second_layer = None
        self.n_g_y = None
        self.n_o_y = None
        self.n_g_pr = None
        self.n_o_pr = None
        self.coord_pr_g_x = None
        self.coord_pr_g_y = None
        self.coord_y_g_x = None
        self.coord_y_g_y = None
        self.coord_y_ok_x = None
        self.coord_y_ok_y = None
class Window_1(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.font1 = ("Futura PT Book", 16)  # Настройка пользовательского шрифта 1
        self.font2 = ("Futura PT Book", 14)  # Настройка пользовательского шрифта 2
        self.title("Ikar")  # Название программы
        self.resizable(False, False)  # Запрет изменения размера окна
        self.geometry(f"{1305}x{734}+{100}+{100}")  # Установка размеров окна
        ctk.set_default_color_theme("data/dark-red.json")  # Загрузка пользовательской темы
        ctk.set_widget_scaling(1.5)  # Увеличение размера виджетов
        #ctk.deactivate_automatic_dpi_awareness()
        self.after(201, lambda: self.iconbitmap('data/sunset.ico'))  # Установка иконки окна
        self.configure(bg_color="black")  # Установка цвета фона окна

        self.global_image = None
        self.image_label = None
        self.global_image_1 = None
        self.image_label_1 = None
        self.global_image_2 = None
        self.image_label_2 = None

        self.print_label()
        self.print_radio_button()
        self.print_button()
        self.choice_1()
    def print_label(self):
        """Визуализация текста в окне"""
        self.label1 = create_label(self, "Добро пожаловавть в программу 'Икар' !", 50, 2)
        self.label2 = create_label(self, "Пожалуйста, выберите схему смесительной головки:", 35, 25)
        self.label3=create_label_red(self, "Есть ли пристеночный слой?", 5, 55)
        self.label4 = create_label_red(self, "Какие форсунки в ядре?", 5, 150)
        self.label5 = create_label_red(self, "Схема расположения форсунок в ядре?", 5, 245)
        self.label6 = create_label_red(self, "Какого типа форсунки в пристеночном слое?", 5, 370)
    def print_radio_button(self):
        """Создание дерево выбора смесительной головки (ответвлениями являются функции show_choice_1...12)"""
        self.radio_var_1 = ctk.IntVar(value=1)
        self.radio_var_2 = ctk.IntVar(value=2)
        self.radio_var_3 = ctk.IntVar(value=3)
        self.radio_var_4 = ctk.IntVar(value=1)
        self.radio_option1 = ctk.CTkRadioButton(self, text="Пристеночный слой есть", variable=self.radio_var_1,
                                                command=lambda: self.choice_1(), value=1)
        self.radio_option1.place(x=10, y=90)
        self.radio_option2 = ctk.CTkRadioButton(self, text="Пристеночного слоя нет", variable=self.radio_var_1,
                                                command=lambda: self.choice_1(), value=2)
        self.radio_option2.place(x=10, y=120)
        self.radio_option3 = ctk.CTkRadioButton(self, text="Ядро однокомпонентное", variable=self.radio_var_2,
                                                command=lambda: self.choice_1(), value=1)
        self.radio_option3.place(x=10, y=185)
        self.radio_option4 = ctk.CTkRadioButton(self, text="Ядро двухкомпонентное", variable=self.radio_var_2,
                                                command=lambda: self.choice_1(), value=2)
        self.radio_option4.place(x=10, y=215)
        self.radio_option5 = ctk.CTkRadioButton(self, text="Шахматная схема в ядре", variable=self.radio_var_3,
                                                command=lambda: self.choice_1(), value=1)
        self.radio_option5.place(x=10, y=280)
        self.radio_option6 = ctk.CTkRadioButton(self, text="Сотовая схема в ядре", variable=self.radio_var_3,
                                                command=lambda: self.choice_1(), value=2)
        self.radio_option6.place(x=10, y=310)
        self.radio_option7 = ctk.CTkRadioButton(self, text="Концентрическая схема в ядре", variable=self.radio_var_3,
                                                command=lambda: self.choice_1(), value=3)
        self.radio_option7.place(x=10, y=340)
        self.radio_option8 = ctk.CTkRadioButton(self, text="Пристенок однокомпонентный", variable=self.radio_var_4,
                                                command=lambda: self.choice_1(), value=1)
        self.radio_option8.place(x=10, y=405)
        self.radio_option9 = ctk.CTkRadioButton(self, text="Пристенок двухкомпонентный", variable=self.radio_var_4,
                                                command=lambda: self.choice_1(), value=2)
        self.radio_option9.place(x=10, y=435)

    def choice_1(self):
        """При некоторых выборах необходимо убрать определённые кнопки. Например, что при однокомпонентном ядре нет смылса реализовывать двухкомпонентный пристенок"""
        if self.radio_var_1.get() == 2:
            self.radio_option8.configure(self, state="disabled")
            self.radio_option9.configure(self, state="disabled")
            self.radio_option8.deselect(1)
            self.radio_option9.deselect(1)
        else:
            if self.radio_var_2.get() == 1:
                self.radio_option9.configure(self, state="disabled")
                self.radio_option9.deselect(1)
            else:
                self.radio_option8.configure(self, state="normal")
                self.radio_option9.configure(self, state="normal")
        self.update_json()
    def update_json(self):
        """Сопоставление выбранной схеме определённому числу (от 1 до 15 - столько у нас различных вариантов)"""
        self.current_choice = (
            self.radio_var_1.get(),
            self.radio_var_2.get(),
            self.radio_var_3.get(),
            self.radio_var_4.get()
        )
        self.number=function_1(self.current_choice)
        print(f"Выбрана схема номер: {self.number}")
        print_image(self.number,self)

    def print_button(self):
        self.close_button=create_button(self, "Выбрать", lambda: self.close_window(), self.font1,100,760,450)
        self.button_1 = create_button(self, "Общая информация", lambda: show_frame_1(self), self.font1, 220, 400, 5)
        self.button_1 = create_button(self, "Схемы расположения", lambda: show_frame_2(self), self.font1, 100, 640, 5)
        self.button_1 = create_button(self, "?", lambda: show_frame_3(self), self.font1, 50, 810, 5)
    def close_window(self):

        self.destroy()
        window_2 = Window_2(self.number)
        window_2.mainloop()
class Window_2(ctk.CTk):
    def __init__(self, choice):
        super().__init__()
        self.font1 = ("Futura PT Book", 16)  # Настройка пользовательского шрифта 1
        self.font2 = ("Futura PT Book", 14)  # Настройка пользовательского шрифта 2
        self.title("Выбор параметров")  # Название программы
        self.resizable(False, False)  # Запрет изменения размера окна
        self.geometry(f"{1305}x{734}+{100}+{100}")  # {1305}x{734}+{723}+{209}
        ctk.set_default_color_theme("data/dark-red.json")  # Загрузка пользовательской темы
        ctk.set_widget_scaling(1.5)  # Увеличение размера виджетов
        self.after(201, lambda: self.iconbitmap('data/sunset.ico'))
        self.choice = choice
        self.H=15
        self.number_pr=60
        self.delta_wall=3
        self.delta=3
        self.delta_y_pr=3
        self.place_scrollbar()
        self.setup_frame()
        self.print_label()
        self.print_entry()
        self.print_button()
        self.print_slider()
        if self.choice<10:
            self.print_radio_button()
    def place_scrollbar(self):
        self.scrollbar_frame_0 = ctk.CTkScrollableFrame(self, width=360, height=320,fg_color='#2b2b2b')  # 171717
        self.scrollbar_frame_0.place(x=10, y=100)
    def setup_frame(self):
        """--------------------Создание мини-окон--------------------"""
        self.frame1 = create_frame(self,370, 80,10,10,"#2b2b2b","transparent")
        self.frame2 = ctk.CTkFrame(master=self.scrollbar_frame_0, width=355, height=500, fg_color="#2b2b2b",bg_color="transparent")
        self.frame2.grid(row=0, column=0, sticky='w', padx=1, pady=1)
    def print_label(self):
        """Визуализация текста в окне"""
        self.label1 = create_label(self.frame1, "Введите диаметр камеры сгорания (мм) :", 20, 5)
        self.label3=create_label(self.frame1, "Рекомендуемый шаг: ", 160, 35)
        self.label2 = create_label(self.frame2, "Выберите шаг между форсунками (мм) :", 0, 0)
        self.label_3_1 = create_label(self.frame2, "12", 30, 20)
        self.label_3_2 = create_label(self.frame2, "30", 300, 20)
        self.label4 = create_label(self.frame2, "Выбранный шаг равен: 15 мм", 10, 40)
        self.label5 = create_label(self.frame2, "Выберите расстояние между форсунками (мм):", 10, 85)
        self.label_5_1 = create_label(self.frame2, "3", 40, 105)
        self.label_5_2 = create_label(self.frame2, "10", 300, 105)
        self.label6 = create_label(self.frame2, "Выбранное расстояние равно : 3 мм ", 10, 125)
        self.label7 = create_label(self.frame2, "Выберите расстояние до огневой стенки (мм):", 10, 170)
        self.label_7_1 = create_label(self.frame2, "3", 40, 190)
        self.label_7_2 = create_label(self.frame2, "10", 300, 190)
        self.label8 = create_label(self.frame2, "Выбранное расстояние равно : 3 мм", 10, 210)
        if self.choice<10:
            self.label9 = create_label(self.frame2, "Выберите расстояние от форуснок ядра и пристенка:", 10, 255)
            self.label_9_1 = create_label(self.frame2, "1", 40, 275)
            self.label_9_2 = create_label(self.frame2, "10", 300, 275)
            self.label10 = create_label(self.frame2, "Выбранное расстояние равно : 3 мм", 10, 295)
            self.label11 = create_label(self.frame2, "Выберите количество форсунок пристенка:", 10, 340)
            self.label_11_1 = create_label(self.frame2, "40", 30, 360)
            self.label_11_2 = create_label(self.frame2, "200", 300, 360)
            self.label12 = create_label(self.frame2, "Выбранное количество равно : 60", 10, 380)
            self.label13 = create_label(self.frame2, "Диаметр форсунок в ядре равен: ", 10, 450)
            self.label14 = create_label(self.frame2, "Диаметр форсунок в пристенке равен: ", 10, 480)
        else:
            self.label15 = create_label(self.frame2, "Диаметр форсунок равен: ", 10, 240)
    def print_entry(self):
        self.entry1_value = ctk.StringVar()
        self.Entry1 = create_entry(self.frame1, 70, self.entry1_value, 10, 35)
    def print_button(self):
        self.back_button = create_button(self.frame1, "Ввод", lambda: self.entry_Dk(), self.font1, 60, 90, 35)
        self.back_button = create_button(self, "Назад", lambda: self.back_window(), self.font1, 100, 10, 450)
        self.close_button = create_button(self, "Далее", lambda: self.close_window(), self.font1, 100, 120, 450)
    def print_radio_button(self):
        """Появление кнопки для создания второго пристеночного слоя, если тот нужен"""
        self.check_var = ctk.StringVar(value="off")
        self.checkbox = ctk.CTkCheckBox(self.frame2, text="2-ой пристеночный слой",command=lambda: self.on_button_change(), variable=self.check_var, onvalue="on", offvalue="off")
        self.checkbox.place(x=30, y=420)
    def back_window(self):
        self.destroy()
        app = Window_1()
        app.mainloop()
    def entry_Dk(self):
        self.D_k=float(self.entry1_value.get())
        self.H_id=round((self.D_k**0.5))
        self.label3.configure(text=f"Рекомендуемый шаг: {self.H_id} мм")
    def print_slider(self):
        self.slider1 = ctk.CTkSlider(self.frame2, from_=12, to=30, command=self.on_slider_change, number_of_steps=18,
                                    border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                    progress_color=("#D44B46"))
        self.slider1.place(x=50, y=30)
        self.slider1.set(15)
        self.slider2 = ctk.CTkSlider(self.frame2, from_=3, to=10, command=self.on_slider_change_1, number_of_steps=7,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider2.place(x=50, y=115)
        self.slider2.set(3)
        self.slider3 = ctk.CTkSlider(self.frame2, from_=3, to=10, command=self.on_slider_change_2, number_of_steps=7,
                                     border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                     progress_color=("#D44B46"))
        self.slider3.place(x=50, y=200)
        self.slider3.set(3)
        if self.choice < 10:
            self.slider4 = ctk.CTkSlider(self.frame2, from_=1, to=10, command=self.on_slider_change_3, number_of_steps=9,
                                        border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                        progress_color=("#D44B46"))
            self.slider4.place(x=50, y=285)
            self.slider4.set(3)
            self.slider5 = ctk.CTkSlider(self.frame2, from_=40, to=200, command=self.on_slider_change_4, number_of_steps=160,
                                        border_width=4, width=250, height=15, fg_color=("#5A211F"),
                                        progress_color=("#D44B46"))
            self.slider5.place(x=50, y=370)
            self.slider5.set(60)
    def on_button_change(self):
        if self.choice == 1 or self.choice == 4 or self.choice == 5:
            self.D_y,self.D_prist=chess_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta, self.delta_y_pr,
                                     self, self.choice, self.checkbox.get())
        elif self.choice == 2 or self.choice == 6 or self.choice == 7:
            self.D_y,self.D_prist=cellular_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta, self.delta_y_pr,
                                        self, self.choice, self.checkbox.get())
        elif self.choice == 3 or self.choice == 8 or self.choice == 9:
            self.D_y,self.D_prist=concentric_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta,
                                          self.delta_y_pr, self, self.choice, self.checkbox.get())
        self.label13.configure(text=f"Диаметр форсунок в ядре равен: {self.D_y:.2f} мм")
        self.label14.configure(text=f"Диаметр форсунок в пристенке равен: {self.D_prist:.2f} мм")
    def on_slider_change(self, value):
        """Обновление текста метки в соответствии со значением ползунка"""
        self.H = int(value)
        self.label4.configure(text=f"Выбранный шаг равен: {self.H} мм")
        if self.choice == 1 or self.choice == 4 or self.choice == 5:
            self.D_y,self.D_prist=chess_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta, self.delta_y_pr,self, self.choice,self.checkbox.get())
        elif self.choice == 2 or self.choice == 6 or self.choice == 7:
            self.D_y,self.D_prist=cellular_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta, self.delta_y_pr,self, self.choice,self.checkbox.get())
        elif self.choice == 3 or self.choice == 8 or self.choice == 9:
            self.D_y,self.D_prist=concentric_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta,self.delta_y_pr, self, self.choice,self.checkbox.get())
        elif self.choice == 10 or self.choice == 13 :
            self.D_y=chess_scheme(self.D_k, self.H, self.delta_wall, self.delta, self, self.choice)
        elif self.choice == 11 or self.choice == 14 :
            self.D_y=cellular_scheme(self.D_k, self.H, self.delta_wall, self.delta, self, self.choice)
        else:
            self.D_y=concentric_scheme(self.D_k, self.H, self.delta_wall, self.delta, self, self.choice)
        if self.choice<10:
            self.label13.configure(text=f"Диаметр форсунок в ядре равен: {self.D_y:.2f} мм")
            self.label14.configure(text=f"Диаметр форсунок в пристенке равен: {self.D_prist:.2f} мм")
        else:
            self.label15.configure(text=f"Диаметр форсунок равен: {self.D_y:.2f} мм")
    def on_slider_change_1(self, value):
        """Обновление текста метки в соответствии со значением ползунка"""
        self.delta = int(value)
        self.label6.configure(text=f"Выбранное расстояние равно : {self.delta} мм")
        if self.choice == 1 or self.choice == 4 or self.choice == 5:
            self.D_y,self.D_prist=chess_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta, self.delta_y_pr,self, self.choice,self.checkbox.get())
        elif self.choice == 2 or self.choice == 6 or self.choice == 7:
            self.D_y,self.D_prist=cellular_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta, self.delta_y_pr,self, self.choice,self.checkbox.get())
        elif self.choice == 3 or self.choice == 8 or self.choice == 9:
            self.D_y,self.D_prist=concentric_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta,self.delta_y_pr, self, self.choice,self.checkbox.get())
        elif self.choice == 10 or self.choice == 13 :
            self.D_y=chess_scheme(self.D_k, self.H, self.delta_wall, self.delta, self, self.choice)
        elif self.choice == 11 or self.choice == 14 :
            self.D_y=cellular_scheme(self.D_k, self.H, self.delta_wall, self.delta, self, self.choice)
        else:
            self.D_y=concentric_scheme(self.D_k, self.H, self.delta_wall, self.delta, self, self.choice)
        if self.choice<10:
            self.label13.configure(text=f"Диаметр форсунок в ядре равен: {self.D_y:.2f} мм")
            self.label14.configure(text=f"Диаметр форсунок в пристенке равен: {self.D_prist:.2f} мм")
        else:
            self.label15.configure(text=f"Диаметр форсунок равен: {self.D_y:.2f} мм")
    def on_slider_change_2(self, value):
        """Обновление текста метки в соответствии со значением ползунка"""
        self.delta_wall = int(value)
        self.label8.configure(text=f"Выбранное расстояние равно : {self.delta_wall} мм")
        if self.choice == 1 or self.choice == 4 or self.choice == 5 :
            self.D_y,self.D_prist=chess_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta, self.delta_y_pr,self, self.choice,self.checkbox.get())
        elif self.choice == 2 or self.choice == 6 or self.choice == 7:
            self.D_y,self.D_prist=cellular_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta,self.delta_y_pr, self, self.choice,self.checkbox.get())
        elif self.choice == 3 or self.choice == 8 or self.choice == 9:
            self.D_y,self.D_prist=concentric_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta,self.delta_y_pr, self, self.choice,self.checkbox.get())
        elif self.choice == 10 or self.choice == 13 :
            self.D_y=chess_scheme(self.D_k, self.H, self.delta_wall, self.delta, self, self.choice)
        elif self.choice == 11 or self.choice == 14 :
            self.D_y=cellular_scheme(self.D_k, self.H, self.delta_wall, self.delta, self, self.choice)
        else:
            self.D_y=concentric_scheme(self.D_k, self.H, self.delta_wall, self.delta, self, self.choice)
        if self.choice<10:
            self.label13.configure(text=f"Диаметр форсунок в ядре равен: {self.D_y:.2f} мм")
            self.label14.configure(text=f"Диаметр форсунок в пристенке равен: {self.D_prist:.2f} мм")
        else:
            self.label15.configure(text=f"Диаметр форсунок равен: {self.D_y:.2f} мм")
    def on_slider_change_3(self, value):
        """Обновление текста метки в соответствии со значением ползунка"""
        self.delta_y_pr = int(value)
        self.label10.configure(text=f"Выбранное расстояние равно : {self.delta_y_pr} мм")
        if self.choice == 1 or self.choice == 4 or self.choice == 5 :
            self.D_y,self.D_prist=self.n_pr,self.D_pr,self.n_2k_y,self.D_2k_y,self.koord_pr,self.koord_ok,self.koord_gor=chess_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta, self.delta_y_pr,self,self.choice,self.checkbox.get())
        elif self.choice == 2 or self.choice == 6 or self.choice == 7:
            self.D_y,self.D_prist=cellular_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta, self.delta_y_pr,self, self.choice,self.checkbox.get())
        elif self.choice == 3 or self.choice == 8 or self.choice == 9:
            self.D_y,self.D_prist=concentric_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta, self.delta_y_pr,self, self.choice,self.checkbox.get())
        self.label13.configure(text=f"Диаметр форсунок в ядре равен: {self.D_y:.2f} мм")
        self.label14.configure(text=f"Диаметр форсунок в пристенке равен: {self.D_prist:.2f} мм")
    def on_slider_change_4(self, value):
        """Обновление текста метки в соответствии со значением ползунка"""
        self.number_pr = int(value)
        self.label12.configure(text=f"Выбранное количество равно : {self.number_pr}")
        if self.choice == 1 or self.choice == 4 or self.choice == 5 :
            self.D_y,self.D_prist=chess_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta, self.delta_y_pr,self,self.choice,self.checkbox.get())
        elif self.choice == 2 or self.choice == 6 or self.choice == 7:
            self.D_y,self.D_prist=cellular_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta, self.delta_y_pr,self, self.choice,self.checkbox.get())
        elif self.choice == 3 or self.choice == 8 or self.choice == 9:
            self.D_y,self.D_prist=concentric_scheme_with_a_wall(self.D_k, self.H, self.number_pr, self.delta_wall, self.delta, self.delta_y_pr,self, self.choice,self.checkbox.get())
        self.label13.configure(text=f"Диаметр форсунок в ядре равен: {self.D_y:.2f} мм")
        self.label14.configure(text=f"Диаметр форсунок в пристенке равен: {self.D_prist:.2f} мм")
    def close_window(self):
        self.destroy()
        if self.choice<10:
            if self.checkbox.get()=="off":
                self.second_layer=1
            else:
                self.second_layer=2
        else:
            self.second_layer = 0
        user.choice=self.choice
        user.D_k =self.D_k
        user.H =self.H
        user.number_pr =self.number_pr
        user.delta_wall =self.delta_wall
        user.delta =self.delta
        user.delta_y_pr =self.delta_y_pr
        user.second_layer =self.second_layer
        window_3 = Window_3(self.choice,self.D_k, self.H, self.number_pr, self.delta_wall, self.delta, self.delta_y_pr,self.second_layer)
        window_3.mainloop()
class Window_3(ctk.CTk):
    def __init__(self, choice,D_k,H, number_pr, delta_wall, delta, delta_y_pr,second_layer):
        super().__init__()
        self.font1 = ("Futura PT Book", 16)  # Настройка пользовательского шрифта 1
        self.font2 = ("Futura PT Book", 14)  # Настройка пользовательского шрифта 2
        self.title("Результаты построения")  # Название программы
        self.resizable(False, False)  # Запрет изменения размера окна
        self.geometry(f"{1305}x{734}+{100}+{100}")  # {1305}x{734}+{723}+{209}
        ctk.set_default_color_theme("data/dark-red.json")  # Загрузка пользовательской темы
        ctk.set_widget_scaling(1.5)  # Увеличение размера виджетов
        self.after(201, lambda: self.iconbitmap('data/sunset.ico'))
        self.choice = choice
        self.D_k=D_k
        self.H=H
        self.number_pr=number_pr
        self.delta_wall=delta_wall
        self.delta=delta
        self.delta_y_pr=delta_y_pr
        self.second_layer=second_layer
        self.print_button()
        self.coord_pr_g_x=[]
        self.coord_pr_g_y=[]
        self.n_g_y = 0
        self.n_o_y = 0
        self.n_g_pr = 0
        self.n_o_pr = 0

        if self.choice < 10:
            self.n_pr_g, self.n_pr_ok, self.coord_pr_g_x, self.coord_pr_g_y, self.coord_pr_ok_x, self.coord_pr_ok_y = azmax(
                self.choice, self.D_k, self.H, self.number_pr, self.delta_wall, self.delta, self.delta_y_pr,self.second_layer)
            self.print_label_pr()
            self.print_button_pr()
        self.coord_y_g_x,self.coord_y_g_y,self.coord_y_ok_x,self.coord_y_ok_y=find_coord_core(self.choice,self.D_k,self.H, self.number_pr, self.delta_wall, self.delta, self.delta_y_pr,self.second_layer)

        self.print_label_core()


    def print_label_core(self):
        self.scrollbar_frame_1 = ctk.CTkScrollableFrame(self, width=200, height=320, fg_color='black')  # 171717
        self.scrollbar_frame_1.place(x=400, y=20)
        self.i = 2
        self.label4 = ctk.CTkLabel(master=self.scrollbar_frame_1, text='  Ядро (Горючее)  ', font=self.font1,
                                   justify='left')
        self.label4.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.label5 = ctk.CTkLabel(master=self.scrollbar_frame_1, text='X, мм', font=self.font1)
        self.label5.grid(row=1, column=0, sticky='w', padx=0, pady=0)
        self.label6 = ctk.CTkLabel(master=self.scrollbar_frame_1, text='Y, мм', font=self.font1)
        self.label6.grid(row=1, column=1, sticky='w', padx=0, pady=0)

        self.scrollbar_frame_2 = ctk.CTkScrollableFrame(self, width=200, height=320, fg_color='black')  # 171717
        self.scrollbar_frame_2.place(x=630, y=20)
        self.i_1 = 2
        self.label4 = ctk.CTkLabel(master=self.scrollbar_frame_2, text='  Ядро (Окислитель)  ', font=self.font1,
                                   justify='left')
        self.label4.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.label5 = ctk.CTkLabel(master=self.scrollbar_frame_2, text='X, мм', font=self.font1)
        self.label5.grid(row=1, column=0, sticky='w', padx=0, pady=0)
        self.label6 = ctk.CTkLabel(master=self.scrollbar_frame_2, text='Y, мм', font=self.font1)
        self.label6.grid(row=1, column=1, sticky='w', padx=0, pady=0)

        for x, y in zip(self.coord_y_g_x, self.coord_y_g_y):
            self.label6 = ctk.CTkLabel(master=self.scrollbar_frame_1, text=f'{x:.2f}', font=self.font1, justify='left')
            self.label6.grid(row=self.i, column=0, sticky='w', padx=0, pady=0)
            self.label7 = ctk.CTkLabel(master=self.scrollbar_frame_1, text=f'{y:.2f}', font=self.font1, justify='left')
            self.label7.grid(row=self.i, column=1, sticky='w', padx=0, pady=0)
            self.i += 1
        for x, y in zip(self.coord_y_ok_x, self.coord_y_ok_y):
            self.label6 = ctk.CTkLabel(master=self.scrollbar_frame_2, text=f'{x:.2f}', font=self.font1, justify='left')
            self.label6.grid(row=self.i_1, column=0, sticky='w', padx=0, pady=0)
            self.label7 = ctk.CTkLabel(master=self.scrollbar_frame_2, text=f'{y:.2f}', font=self.font1, justify='left')
            self.label7.grid(row=self.i_1, column=1, sticky='w', padx=0, pady=0)
            self.i_1 += 1

        self.label_01=create_label(self,f"Кол-во форсунок:",10,10)
        self.label_02 = create_label(self, f"Ядро:", 25, 35)
        if self.choice!=1 and self.choice!=2 and self.choice!=3 and self.choice!=10 and self.choice!=11 and self.choice!=12:
            self.label_03 = create_label(self, f"2-комп.: {len(self.coord_y_g_x)}", 40, 60)
            self.n_g_y=len(self.coord_y_g_x)
            self.n_o_y = len(self.coord_y_g_x)
        else:
            self.label_04 = create_label(self, f"Горючее: {len(self.coord_y_g_x)}", 40, 60)
            self.label_05 = create_label(self, f"Окислитель: {len(self.coord_y_ok_x)}", 40, 85)
            self.n_g_y = len(self.coord_y_g_x)
            self.n_o_y = len(self.coord_y_ok_x)
        if self.choice<10:
            self.label_06 = create_label(self, f"Пристенок:", 25, 110)
            if self.choice == 1 or self.choice == 2 or self.choice == 3 or self.choice == 4 or self.choice == 6 or self.choice == 8:
                self.label_03 = create_label(self, f"Горючее: {self.n_pr_g}", 40, 135)
                self.n_g_pr=self.n_pr_g
                self.n_o_pr = 0
            else:
                self.label_04 = create_label(self, f"2-комп.: {self.n_pr_g}", 40, 135)
                self.n_g_pr = self.n_pr_g
                self.n_o_pr = self.n_pr_g

    def print_label_pr(self):
        self.scrollbar_frame_0 = ctk.CTkScrollableFrame(self, width=200, height=320, fg_color='black')  # 171717
        self.scrollbar_frame_0.place(x=170, y=20)
        self.i=2
        if self.choice == 5 or self.choice == 7 or self.choice == 9:
            self.label4 = ctk.CTkLabel(master=self.scrollbar_frame_0, text='Прист. (2-комп.)', font=self.font1,
                                       justify='left')
        else:
            self.label4 = ctk.CTkLabel(master=self.scrollbar_frame_0, text='Прист. (Гор.)', font=self.font1,
                                       justify='left')
        self.label4.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.label5 = ctk.CTkLabel(master=self.scrollbar_frame_0, text='X, мм', font=self.font1)
        self.label5.grid(row=1, column=0, sticky='w', padx=0, pady=0)
        self.label6 = ctk.CTkLabel(master=self.scrollbar_frame_0, text='Y, мм', font=self.font1)
        self.label6.grid(row=1, column=1, sticky='w', padx=0, pady=0)

        for x,y in zip(self.coord_pr_g_x,self.coord_pr_g_y):
            self.label6 = ctk.CTkLabel(master=self.scrollbar_frame_0, text=f'{x:.4f}', font=self.font1, justify='left')
            self.label6.grid(row=self.i, column=0, sticky='w', padx=0, pady=0)
            self.label7 = ctk.CTkLabel(master=self.scrollbar_frame_0, text=f'{y:.4f}', font=self.font1, justify='left')
            self.label7.grid(row=self.i, column=1, sticky='w', padx=0, pady=0)
            self.i += 1

    def print_button_pr(self):
        self.button_1 = ctk.CTkButton(master=self, text="txt", width=40, command=lambda: save_txt_1(self.coord_pr_g_x,self.coord_pr_g_y))
        self.button_1.place(x=170, y=360)
        self.button_4 = ctk.CTkButton(master=self, text=".cdm", width=40,command=lambda: save_cdm_1(self.coord_pr_g_x, self.coord_pr_g_y,self.D_k,self.number_pr,self.delta_wall,self.delta))
        self.button_4.place(x=215, y=360)

    def print_button(self):
        self.back_button = create_button(self, "Назад", lambda: self.back_window(), self.font1, 100, 10, 450)
        self.close_button = create_button(self, "Далее", lambda: self.close_window(), self.font1, 100, 760, 450)
        self.button_2 = ctk.CTkButton(master=self, text=".txt", width=40,command=lambda: save_txt_1(self.coord_y_g_x, self.coord_y_g_y))
        self.button_2.place(x=400, y=360)
        self.button_3 = ctk.CTkButton(master=self, text=".txt", width=40,command=lambda: save_txt_1(self.coord_y_ok_x, self.coord_y_ok_y))
        self.button_3.place(x=630, y=360)

        self.button_5 = ctk.CTkButton(master=self, text=".cdm", width=40,command=lambda: save_cdm_2(self.coord_y_g_x, self.coord_y_g_y,self.H,self.delta))
        self.button_5.place(x=445, y=360)
        self.button_6 = ctk.CTkButton(master=self, text=".cdm", width=40,command=lambda: save_cdm_2(self.coord_y_ok_x, self.coord_y_ok_y,self.H,self.delta))
        self.button_6.place(x=675, y=360)

        self.button_7 = ctk.CTkButton(master=self, text="Сохранить всё в .cdm", width=150,command=lambda: save_cdm_3(self.coord_pr_g_x,self.coord_pr_g_y,self.coord_y_g_x, self.coord_y_g_y,self.coord_y_ok_x, self.coord_y_ok_y,self.H,self.delta,self.choice,self.D_k,self.delta_wall,self.number_pr) )
        self.button_7.place(x=600, y=450)
    def back_window(self):
        self.destroy()
        app = Window_2(self.choice)
        app.mainloop()

    def close_window(self):
        user.n_g_y = self.n_g_y
        user.n_o_y = self.n_o_y
        user.n_g_pr = self.n_g_pr
        user.n_o_pr = self.n_o_pr
        user.coord_pr_g_x=self.coord_pr_g_x
        user.coord_pr_g_y=self.coord_pr_g_y
        user.coord_y_g_x=self.coord_y_g_x
        user.coord_y_g_y=self.coord_y_g_y
        user.coord_y_ok_x=self.coord_y_ok_x
        user.coord_y_ok_y=self.coord_y_ok_y
        self.destroy()
        window_4 = Window_4(self.choice)
        window_4.mainloop()
class Window_4(ctk.CTk):
    def __init__(self, choice):
        super().__init__()
        self.font1 = ("Futura PT Book", 16)  # Настройка пользовательского шрифта 1
        self.font2 = ("Futura PT Book", 14)  # Настройка пользовательского шрифта 2
        self.title("Предварительные расчеты по поиску массового расхода")  # Название программы
        self.resizable(False, False)  # Запрет изменения размера окна
        self.geometry(f"{1305}x{734}+{100}+{100}")  # {1305}x{734}+{723}+{209}
        ctk.set_default_color_theme("data/dark-red.json")  # Загрузка пользовательской темы
        ctk.set_widget_scaling(1.5)  # Увеличение размера виджетов
        self.after(201, lambda: self.iconbitmap('data/sunset.ico'))
        self.choice = choice
        self.a=0
        self.b = 0
        self.c = 0
        self.d = 0
        self.f = 0
        self.g = 0
        self.global_image_4 = None
        self.image_label_4 = None
        self.global_image_5 = None
        self.image_label_5 = None
        self.print_label()
        self.print_entry()
        self.print_radio_button()
        self.print_button()
        self.place_scrollbar()
        show_frame_4(self)

    def print_label(self):
        self.label_1 = create_label(self, "Введите суммарный расход:                     кг/с", 10, 10)
        self.label_2 = create_label(self, "Введите соотношение компонентов:", 10, 40)
        self.label_3 = create_label(self, "Горючее:", 10, 70)
        self.label_4 = create_label(self, "Окислитель:", 10, 160)
        if self.choice<10:
            self.label_5 = create_label(self, "Какая доля идёт на пристенок:                      %", 10, 250)
            if self.choice==5 or self.choice==7 or self.choice==9:
                self.label_6_0 = create_label(self, "Введите соотношение компонентов в пристенке:", 10, 280)
                self.label_6 = create_label(self, "Какое горючее в пристенке?", 10, 310)
                self.label_7 = create_label(self, "Какой окислитель в пристенке?", 10, 400)
            else:
                self.label_6 = create_label(self, "Какое горючее в пристенке?", 10, 280)

    def print_entry(self):
        self.entry1_value = ctk.StringVar()
        self.entry2_value = ctk.StringVar()
        self.entry3_value = ctk.StringVar()
        self.entry4_value = ctk.StringVar()
        self.entry5_value = ctk.StringVar()
        self.entry6_value = ctk.StringVar()
        self.entry7_value = ctk.StringVar()
        self.entry8_value = ctk.StringVar()
        self.entry9_value = ctk.StringVar()
        self.Entry5 = None
        self.Entry6 = None
        self.Entry7 = None
        self.Entry8 = None
        self.Entry9 = None
        self.Entry3 = None
        self.Entry4 = None
        self.Entry1 = create_entry(self, 70, self.entry1_value, 200, 10)
        self.Entry2 = create_entry(self, 70, self.entry2_value, 250, 40)
        if self.choice < 10:
            self.Entry3 = create_entry(self, 70, self.entry3_value, 215, 250)
            if self.choice == 5 or self.choice == 7 or self.choice == 9:
                self.Entry4 = create_entry(self, 70, self.entry4_value, 330, 280)
    def print_radio_button(self):
        self.radio_var_1 = ctk.IntVar(value=8)
        self.radio_var_2 = ctk.IntVar(value=1)
        self.radio_var_3 = ctk.IntVar(value=0)
        self.radio_var_4 = ctk.IntVar(value=0)
        self.radio_var_5 = ctk.IntVar(value=0)
        self.radio_option1 = ctk.CTkRadioButton(self, text="Чистое горючее", variable=self.radio_var_1,
                                                command=lambda: self.update_entry_1(), value=8)
        self.radio_option1.place(x=30, y=100)
        self.radio_option2 = ctk.CTkRadioButton(self, text="Восстановительный ГГ", variable=self.radio_var_1,
                                                command=lambda: self.update_entry_1(), value=9)
        self.radio_option2.place(x=30, y=130)
        self.radio_option3 = ctk.CTkRadioButton(self, text="Чистый окислитель", variable=self.radio_var_2,
                                                command=lambda: self.update_entry_2(), value=1)
        self.radio_option3.place(x=30, y=190)
        self.radio_option4 = ctk.CTkRadioButton(self, text="Окислительный ГГ", variable=self.radio_var_2,
                                                command=lambda: self.update_entry_2(), value=2)
        self.radio_option4.place(x=30, y=220)
        if self.choice!=5 and self.choice!=7 and self.choice!=9 and self.choice<10:
            self.radio_var_3 = ctk.IntVar(value=2)
            self.radio_option5 = ctk.CTkRadioButton(self, text="Чистое горючее", variable=self.radio_var_3,
                                                    command=lambda: self.update_entry_3(), value=2)
            self.radio_option5.place(x=30, y=310)
            self.radio_option6 = ctk.CTkRadioButton(self, text="Восстановительный ГГ", variable=self.radio_var_3,
                                                    command=lambda: self.update_entry_3(), value=3)
            self.radio_option6.place(x=30, y=340)
        if self.choice==5 or self.choice==7 or self.choice==9:
            self.radio_var_4 = ctk.IntVar(value=4)
            self.radio_var_5 = ctk.IntVar(value=6)
            self.radio_option7 = ctk.CTkRadioButton(self, text="Чистое горючее", variable=self.radio_var_4,
                                                    command=lambda: self.update_entry_4(), value=4)
            self.radio_option7.place(x=30, y=340)
            self.radio_option8 = ctk.CTkRadioButton(self, text="Восстановительный ГГ", variable=self.radio_var_4,
                                                    command=lambda: self.update_entry_4(), value=5)
            self.radio_option8.place(x=30, y=370)
            self.radio_option9 = ctk.CTkRadioButton(self, text="Чистый окислитель", variable=self.radio_var_5,
                                                    command=lambda: self.update_entry_5(), value=6)
            self.radio_option9.place(x=30, y=430)
            self.radio_option10 = ctk.CTkRadioButton(self, text="Окислительный ГГ", variable=self.radio_var_5,
                                                    command=lambda: self.update_entry_5(), value=7)
            self.radio_option10.place(x=30, y=460)
    def update_entry_1(self):
        if self.Entry5:
            self.Entry5.destroy()
            self.Entry5 = None
            self.c=0

            # Если выбран "Восстановительный ГГ", создаем поле ввода
        if self.radio_var_1.get() == 9:
            self.Entry5 = ctk.CTkEntry(master=self, width=70, textvariable=self.entry5_value)
            self.Entry5.place(x=210, y=128)
    def update_entry_2(self):
        if self.Entry6:
            self.Entry6.destroy()
            self.Entry6 = None
            self.d =0
        if self.radio_var_2.get() == 2:
            self.Entry6 = ctk.CTkEntry(master=self, width=70, textvariable=self.entry6_value)
            self.Entry6.place(x=185, y=218)
    def update_entry_3(self):
        if self.Entry7:
            self.Entry7.destroy()
            self.Entry7 = None
            self.c = 0
        if self.radio_var_3.get() == 3:
            self.Entry7 = ctk.CTkEntry(master=self, width=70, textvariable=self.entry7_value)
            self.Entry7.place(x=210, y=338)
    def update_entry_4(self):
        if self.Entry8:
            self.Entry8.destroy()
            self.Entry8 = None
            self.c = 0
        if self.radio_var_4.get() == 5:
            self.Entry8 = ctk.CTkEntry(master=self, width=70, textvariable=self.entry8_value)
            self.Entry8.place(x=205, y=368)
    def update_entry_5(self):
        if self.Entry9:
            self.Entry9.destroy()
            self.Entry9 = None
            self.d =0
        if self.radio_var_5.get() == 7:
            self.Entry9 = ctk.CTkEntry(master=self, width=70, textvariable=self.entry9_value)
            self.Entry9.place(x=195, y=453)
    def print_button(self):
        if self.choice!=5 and self.choice!=7 and self.choice!=9:
            x=10
        else:
            x=280
        self.enter_button = create_button(self, "Ввод", lambda: self.print_options(), self.font1, 100, x, 450)
        self.back_button = create_button(self, "Назад", lambda: self.back_window(), self.font1, 100, 650, 450)
        self.close_button = create_button(self, "Далее", lambda: self.close_window(), self.font1, 100, 760, 450)
        self.button_1 = create_button(self, "?", lambda: show_frame_5(self), self.font1, 50, 580, 450)
    def print_options(self):
        if self.choice<10:
            if self.choice==5 or self.choice==7 or self.choice==9:
                self.current_choice = (
                    self.radio_var_4.get(),
                    self.radio_var_5.get(),
                    self.radio_var_1.get(),
                    self.radio_var_2.get()
                )
            else:
                self.current_choice = (
                    0,
                    self.radio_var_3.get(),
                    self.radio_var_1.get(),
                    self.radio_var_2.get()
                )
        else:
            self.current_choice = (
                0,
                1,
                self.radio_var_1.get(),
                self.radio_var_2.get()
            )
        self.number = function_2(self.current_choice)
        print(f'Выбрана система: {self.number}')
        self.a = float(self.entry1_value.get())
        self.b=float(self.entry2_value.get())
        if self.Entry5:
            self.c=float(self.entry5_value.get())
        if self.Entry7:
            self.c=float(self.entry7_value.get())
        if self.Entry8:
            self.c=float(self.entry8_value.get())
        if self.Entry6:
            self.d=float(self.entry6_value.get())
        if self.Entry9:
            self.d=float(self.entry9_value.get())
        if self.choice < 10:
            self.f=float(self.entry3_value.get())
            if self.choice == 5 or self.choice == 7 or self.choice == 9:
                self.g=float(self.entry4_value.get())
        self.x_1, self.x_2, self.x_3, self.x_4, self.x_5, self.x_6, self.x_7, self.x_8 = find_costs(self.number, self.a, self.b,self.c, self.d, self.f/100, self.g)
        self.label1 = ctk.CTkLabel(master=self.scrollbar_frame_1, text=f'm_сумм={self.a:.3f} кг/с\nk_m={self.b:.3f}\nk_m_вгг={self.c:.3f}\nk_m_огг={self.d:.3f}\nn={self.f:.3f}\nk_m_пр ={self.g:.3f}', font=self.font1, justify='left')
        self.label1.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.label2 = ctk.CTkLabel(master=self.scrollbar_frame_2,
                                   text=f'm_пр_г_вгг={self.x_1:.3f}\nm_пр_ок_вгг={self.x_2:.3f} кг/с\nm_пр_г_огг={self.x_3:.3f} кг/с\nm_пр_ок_огг={self.x_4:.3f} кг/с\nm_я_г_вгг={self.x_5:.3f} кг/с\nm_я_ок_вгг={self.x_6:.3f} кг/с\nm_я_г_огг={self.x_7:.3f} кг/с\nm_я_ок_огг={self.x_8:.3f} кг/с',
                                   font=self.font1, justify='left')
        self.label2.grid(row=0, column=0, sticky='w', padx=0, pady=0)
    def place_scrollbar(self):
        self.scrollbar_frame_1 = ctk.CTkScrollableFrame(self, width=190, height=50,fg_color='#2b2b2b')  # 171717
        self.scrollbar_frame_1.place(x=390, y=220)
        self.scrollbar_frame_2 = ctk.CTkScrollableFrame(self, width=190, height=50, fg_color='#2b2b2b')  # 171717
        self.scrollbar_frame_2.place(x=625, y=220)
    def back_window(self):
        self.destroy()
        window_3 = Window_3(user.choice, user.D_k, user.H, user.number_pr, user.delta_wall, user.delta, user.delta_y_pr,user.second_layer)
        window_3.mainloop()
    def close_window(self):
        self.destroy()
        window_5 = Window_5(user.n_g_pr, user.n_o_pr, user.n_g_y, user.n_o_y,user.choice,self.x_1, self.x_2, self.x_3, self.x_4, self.x_5, self.x_6, self.x_7, self.x_8,user.coord_pr_g_x,user.coord_pr_g_y,user.coord_y_g_x,user.coord_y_g_y,user.coord_y_ok_x,user.coord_y_ok_y)
        window_5.mainloop()
class Window_5(ctk.CTk):
    def __init__(self, n_g_pr, n_o_pr, n_g_y, n_o_y,choice,x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8,coord_pr_g_x,coord_pr_g_y,coord_y_g_x,coord_y_g_y,coord_y_ok_x,coord_y_ok_y):
        super().__init__()
        self.font1 = ("Futura PT Book", 16)  # Настройка пользовательского шрифта 1
        self.font2 = ("Futura PT Book", 14)  # Настройка пользовательского шрифта 2
        self.title("Вывод результатов расчёта массового расхода. Подготовка к методу Иевлева")  # Название программы
        self.resizable(False, False)  # Запрет изменения размера окна
        self.geometry(f"{1305}x{734}+{100}+{100}")  # {1305}x{734}+{723}+{209}
        ctk.set_default_color_theme("data/dark-red.json")  # Загрузка пользовательской темы
        ctk.set_widget_scaling(1.5)  # Увеличение размера виджетов
        self.after(201, lambda: self.iconbitmap('data/sunset.ico'))

        self.n=3
        self.n_g_pr=n_g_pr
        self.n_o_pr=n_o_pr
        self.n_g_y=n_g_y
        self.n_o_y=n_o_y
        self.choice = choice
        self.x_1 = x_1
        self.x_2 = x_2
        self.x_3 = x_3
        self.x_4 = x_4
        self.x_5 = x_5
        self.x_6 = x_6
        self.x_7 = x_7
        self.x_8 = x_8
        self.coord_pr_g_x=coord_pr_g_x
        self.coord_pr_g_y=coord_pr_g_y
        self.coord_y_g_x=coord_y_g_x
        self.coord_y_g_y=coord_y_g_y
        self.coord_y_ok_x=coord_y_ok_x
        self.coord_y_ok_y=coord_y_ok_y
        self.place_scrollbar()
        self.find_coord_sum()
        self.m_f_g_pr,self.m_f_o_pr,self.m_f_g_y,self.m_f_o_y,self.coord_gor,self.coord_ok=find_costs_2(self.x_1, self.x_2, self.x_3, self.x_4, self.x_5, self.x_6, self.x_7, self.x_8,self.choice,
                                                                                                        self.n_g_pr,self.n_o_pr,self.n_g_y,self.n_o_y,self.coord_pr_g_x,self.coord_pr_g_y,
                                                                                                        self.coord_y_g_x,self.coord_y_g_y,self.coord_y_ok_x,self.coord_y_ok_y)
        self.print_costs()
        self.input_n()
        self.print_button()
    def place_scrollbar(self):
        self.scrollbar_frame_1 = ctk.CTkScrollableFrame(self, width=180, height=200,fg_color='black')  # 171717
        self.scrollbar_frame_1.place(x=430, y=10)
        self.scrollbar_frame_2 = ctk.CTkScrollableFrame(self, width=180, height=200, fg_color='black')  # 171717
        self.scrollbar_frame_2.place(x=650, y=10)
    def print_costs(self):
        self.k=1
        self.l=1
        self.label1 = ctk.CTkLabel(master=self.scrollbar_frame_1, text=f'X гор.', font=self.font1, justify='left')
        self.label1.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.label2 = ctk.CTkLabel(master=self.scrollbar_frame_1, text=f'Y гор.', font=self.font1, justify='left')
        self.label2.grid(row=0, column=1, sticky='w', padx=0, pady=0)
        self.label3 = ctk.CTkLabel(master=self.scrollbar_frame_1, text=f'm гор.', font=self.font1, justify='left')
        self.label3.grid(row=0, column=2, sticky='w', padx=0, pady=0)
        self.label1 = ctk.CTkLabel(master=self.scrollbar_frame_2, text=f'X ок.', font=self.font1, justify='left')
        self.label1.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.label2 = ctk.CTkLabel(master=self.scrollbar_frame_2, text=f'Y ок.', font=self.font1, justify='left')
        self.label2.grid(row=0, column=1, sticky='w', padx=0, pady=0)
        self.label3 = ctk.CTkLabel(master=self.scrollbar_frame_2, text=f'm ок.', font=self.font1, justify='left')
        self.label3.grid(row=0, column=2, sticky='w', padx=0, pady=0)
        for i in range(len(self.coord_gor)):
            self.x, self.y, self.z = self.coord_gor[i]
            self.label1 = ctk.CTkLabel(master=self.scrollbar_frame_1,text=f'{self.x:.2f}',font=self.font1, justify='left')
            self.label1.grid(row=self.k, column=0, sticky='w', padx=0, pady=0)
            self.label2 = ctk.CTkLabel(master=self.scrollbar_frame_1, text=f'{self.y:.2f}', font=self.font1, justify='left')
            self.label2.grid(row=self.k, column=1, sticky='w', padx=0, pady=0)
            self.label3 = ctk.CTkLabel(master=self.scrollbar_frame_1, text=f'{self.z:.2f}', font=self.font1, justify='left')
            self.label3.grid(row=self.k, column=2, sticky='w', padx=0, pady=0)
            self.k+=1
        for i in range(len(self.coord_ok)):
            self.x, self.y, self.z = self.coord_ok[i]
            self.label1 = ctk.CTkLabel(master=self.scrollbar_frame_2,text=f'{self.x:.2f}',font=self.font1, justify='left')
            self.label1.grid(row=self.l, column=0, sticky='w', padx=0, pady=0)
            self.label2 = ctk.CTkLabel(master=self.scrollbar_frame_2, text=f'{self.y:.2f}', font=self.font1, justify='left')
            self.label2.grid(row=self.l, column=1, sticky='w', padx=0, pady=0)
            self.label3 = ctk.CTkLabel(master=self.scrollbar_frame_2, text=f'{self.z:.2f}', font=self.font1, justify='left')
            self.label3.grid(row=self.l, column=2, sticky='w', padx=0, pady=0)
            self.l+=1
    def find_coord_sum(self):
        self.coord_graph=[]
        if self.choice==1 or self.choice==2 or self.choice==3:
            for (x, y) in zip(self.coord_pr_g_x,self.coord_pr_g_y):
                self.coord_graph.append([x, y])
            for (x, y) in zip(self.coord_y_g_x,self.coord_y_g_y):
                self.coord_graph.append([x, y])
            for (x, y) in zip(self.coord_y_ok_x,self.coord_y_ok_y):
                self.coord_graph.append([x, y])
        elif self.choice==4 or self.choice==5 or self.choice==6 or self.choice==7 or self.choice==8 or self.choice==9:
            for (x, y) in zip(self.coord_pr_g_x,self.coord_pr_g_y):
                self.coord_graph.append([x, y])
            for (x, y) in zip(self.coord_y_g_x,self.coord_y_g_y):
                self.coord_graph.append([x, y])
        elif self.choice==10 or self.choice==11 or self.choice==12:
            for (x, y) in zip(self.coord_y_g_x,self.coord_y_g_y):
                self.coord_graph.append([x, y])
            for (x, y) in zip(self.coord_y_ok_x,self.coord_y_ok_y):
                self.coord_graph.append([x, y])
        else:
            for (x, y) in zip(self.coord_y_g_x,self.coord_y_g_y):
                self.coord_graph.append([x, y])
        self.n_pl,self.centers_square,self.angles_square=print_dot(self.coord_graph,user.D_k,self,user.H,self.n)
    def input_n(self):
        self.label_1 = create_label(self, "Выберите, какая часть форсунок будет рассчитываться?", 430, 260)
        self.label_2 = create_label(self, "n =", 430, 285)
        self.label_3 = create_label(self, "(каждая 2-ая, каждая 3-ья и т.д.)", 540, 285)
        self.entry1_value = ctk.StringVar()
        self.Entry1 = create_entry(self, 45, self.entry1_value, 455, 285)
        self.button_n = create_button(self, "✓", lambda: self.entry_n(), self.font1, 20, 505, 285)
    def entry_n(self):
        self.n = int(self.entry1_value.get())
        self.n_pl,self.centers_square,self.angles_square=print_dot(self.coord_graph, user.D_k, self, user.H, self.n)
    def print_button(self):
        self.button_1 = create_button(self, "txt", lambda: save_txt(self.coord_gor), self.font1, 60, 430, 235)
        self.button_2 = create_button(self, "excel", lambda: save_excel(self.coord_gor), self.font1, 60, 510, 235)
        self.button_3 = create_button(self, "txt", lambda: save_txt(self.coord_ok), self.font1, 60, 650, 235)
        self.button_4 = create_button(self, "excel", lambda: save_excel(self.coord_ok), self.font1, 60, 730, 235)
        self.back_button = create_button(self, "Назад", lambda: self.back_window(), self.font1, 100, 650, 450)
        self.close_button = create_button(self, "Далее", lambda: self.close_window(), self.font1, 100, 760, 450)
    def back_window(self):
        self.destroy()
        window_4 = Window_4()
        window_4.mainloop()

    def close_window(self):
        self.destroy()
        window_6 = Window_6(self.n_pl,self.centers_square,self.coord_graph,self.angles_square,self.coord_gor,self.coord_ok)
        window_6.mainloop()

class Window_6(ctk.CTk):
    def __init__(self,n_pl,centers_square,coord_graph,angles_square,coord_gor,coord_ok):
        super().__init__()
        self.font1 = ("Futura PT Book", 16)  # Настройка пользовательского шрифта 1
        self.font2 = ("Futura PT Book", 14)  # Настройка пользовательского шрифта 2
        self.title("Метод Иевлева")  # Название программы
        self.resizable(False, False)  # Запрет изменения размера окна
        self.geometry(f"{1305}x{734}+{100}+{100}")  # {1305}x{734}+{723}+{209}
        ctk.set_default_color_theme("data/dark-red.json")  # Загрузка пользовательской темы
        ctk.set_widget_scaling(1.5)  # Увеличение размера виджетов
        self.after(201, lambda: self.iconbitmap('data/sunset.ico'))
        self.n_pl=n_pl
        self.centers_square=centers_square
        self.coord_graph=coord_graph
        self.angles_square=angles_square
        self.coord_gor=coord_gor
        self.coord_ok=coord_ok
        self.scrollbar()
        self.print_images()
    def scrollbar(self):
        """=====Создание пролистывающегося фрейма====="""
        self.scrollbar_frame = ctk.CTkScrollableFrame(self, width=830, height=465,fg_color='#171717') #171717
        self.scrollbar_frame.place(x=10, y=10)
        self.frame0 = ctk.CTkFrame(master=self.scrollbar_frame, width=830, height=411*self.n_pl+20, fg_color="#171717",bg_color="transparent")
        self.frame0.grid(row=0, column=0, sticky='w', padx=1, pady=1)
    def print_images(self):
        self.k=0
        self.km_graph=[]
        for i, (x, y) in enumerate(self.centers_square):
            draw_circle_with_points(x, y, self.coord_graph, user.H, user.D_k,self.frame0,self.k)
            self.label = create_label(self.frame0, f"Площадка №{self.k+1}", 440, 411*self.k+40)
            if self.angles_square[i]!=361:
                self.label = create_label(self.frame0, f"Угол наклона площадки: {self.angles_square[i]:.2f}°, площадка у стенки", 440,411 * self.k + 65)
                self.m_gor_pl,self.m_ok_pl,self.n_gor,self.n_ok,self.text_programm_pl=method_by_ievlev_pr(np.deg2rad(self.angles_square[i]),x, y,self.coord_gor,self.coord_ok,user.H)
                self.label = create_label(self.frame0,f"m_гор= {self.m_gor_pl:.4f} кг/с , n={self.n_gor}",440, 411 * self.k + 90)
                self.label = create_label(self.frame0, f"m_ок= {self.m_ok_pl:.4f} кг/с , n={self.n_ok}", 440, 411 * self.k + 115)
                self.label = create_label(self.frame0, f"k_m= {self.m_ok_pl/self.m_gor_pl:.4f}", 440, 411 * self.k + 140)
                self.km_graph.append([float(x), float(y),self.m_ok_pl/self.m_gor_pl])
                self.button=create_button(self.frame0,"Программа 'Forsunki'",lambda: save_txt_fors(self.text_programm_pl),self.font1,200,440, 411 * self.k + 165)
            else:
                self.label = create_label(self.frame0, f"Угол наклона площадки: {0}°, площадка не у стенки", 440,411 * self.k + 65)
                self.m_gor_y,self.m_ok_y,self.n_gor,self.n_ok,self.text_programm_y=method_by_ievlev_core(x, y,self.coord_gor,self.coord_ok,user.H)
                self.label = create_label(self.frame0, f"m_гор= {self.m_gor_y:.4f} кг/с , n={self.n_gor}", 440, 411 * self.k + 90)
                self.label = create_label(self.frame0, f"m_ок= {self.m_ok_y:.4f} кг/с , n={self.n_ok}", 440, 411 * self.k + 115)
                self.label = create_label(self.frame0, f"k_m= {self.m_ok_y / self.m_gor_y:.4f}", 440, 411 * self.k + 140)
                self.km_graph.append([float(x), float(y), self.m_ok_y / self.m_gor_y])
            self.k+=1
        print(self.km_graph)
if __name__ == "__main__":
    app = Window_1()
    app.mainloop()