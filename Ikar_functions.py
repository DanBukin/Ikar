from ikar_graphs import *
import customtkinter as ctk
import os
from PIL import Image, ImageTk
from ctypes import windll
import math
import numpy as np
from matplotlib.ticker import FuncFormatter
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from scipy.integrate import quad
import json

formatter = FuncFormatter(lambda x, _: f"{x:.0f}")

FR_PRIVATE = 0x10
FR_NOT_ENUM = 0x20
if os.name == 'nt':
    windll.gdi32.AddFontResourceExW("data/ofont.ru_Futura PT.ttf", FR_PRIVATE, 0)
else:
    pass

font0 = ("Futura PT Book", 18)  # Настройка пользовательского шрифта 1
font1 = ("Futura PT Book", 16)  # Настройка пользовательского шрифта 2
font2 = ("Futura PT Book", 14)  # Настройка пользовательского шрифта 3
canvas_widget = None
k_1=0
FR_PRIVATE = 0x10
FR_NOT_ENUM = 0x20
if os.name == 'nt':
    windll.gdi32.AddFontResourceExW("data/ofont.ru_Futura PT.ttf", FR_PRIVATE, 0) # Загрузка пользовательского шрифта
else:
    pass
def create_frame(parent,wight, height, x, y, fg_color, bg_color):
    frame = ctk.CTkFrame(master=parent,width=wight, height=height, fg_color=fg_color, bg_color=bg_color)
    frame.place(x=x, y=y)
    return frame
def create_entry(parent, wight, textvariable, x, y):
    Entry = ctk.CTkEntry(master=parent, width=wight, textvariable=textvariable)
    Entry.place(x=x, y=y)
def create_label(parent, text, x, y):
    label = ctk.CTkLabel(parent, text=text, font=font1)
    label.place(x=x, y=y)
    return label
def create_label_left(parent, text, x, y):
    label = ctk.CTkLabel(parent, text=text, font=font1, justify='left')
    label.place(x=x, y=y)
    return label
def create_label_red(parent, text, x, y):
    label = ctk.CTkLabel(parent, text=text, font=font1,fg_color="#B62626", corner_radius=10)
    label.place(x=x, y=y)
    return label
def create_button(parent, text, command, font, width, x, y):
    button = ctk.CTkButton(master=parent, text=text, command=command, font=font, width=width)
    button.place(x=x, y=y)
    return button
def show_frame_1(app):
    # Если изображение еще не было загружено, загружаем его
    if app.global_image is None:
        original_image = Image.open("data/frame_1.png")  # Путь к изображению
        resized_image = original_image.resize((round(905 * 1*0.8), round(766 * 1*0.8)), Image.Resampling.LANCZOS)
        app.global_image = ImageTk.PhotoImage(resized_image)

    # Если метка изображения еще не была создана, создаем ее
    if app.image_label is None:
        app.image_label = ctk.CTkLabel(app, image=app.global_image)
        app.image_label.place(x=380, y=38)
        app.image_label.configure(text="")
    else:
        app.image_label.configure(image=app.global_image)
        app.image_label.place(x=380, y=38)
        app.image_label.configure(text="")
        app.image_label.place_forget()
        app.image_label=None
    if app.image_label_1 is not None:
        app.image_label_1.place_forget()
    if app.image_label_2 is not None:
        app.image_label_2.place_forget()
def show_frame_2(app):
    if app.global_image_1 is None:
        # Сначала изменяем размер изображения с помощью Pillow
        original_image_1 = Image.open("data/frame_2.png")  # Замените на путь к вашему изображению
        resized_image_1 = original_image_1.resize((round(905 * 1*0.8), round(766 * 1*0.8)),Image.Resampling.LANCZOS)  # Изменяем размер
        app.global_image_1 = ImageTk.PhotoImage(resized_image_1)

    # Если метка изображения еще не была создана, создаем ее
    if app.image_label_1 is None:
        app.image_label_1 = ctk.CTkLabel(app, image=app.global_image_1)
        app.image_label_1.place(x=380, y=38)  # Размещаем метку в координатах x=220, y=150
        app.image_label_1.configure(text="")
    else:
        # Просто обновляем изображение метки
        app.image_label_1.configure(image=app.global_image_1)
        app.image_label_1.place(x=380, y=38)
        app.image_label_1.configure(text="")
        app.image_label_1.place_forget()
        app.image_label_1 = None
    if app.image_label is not None:
        app.image_label.place_forget()  # Скрываем метку изображения
    if app.image_label_2 is not None:
        app.image_label_2.place_forget()
def show_frame_3(app):
    if app.global_image_2 is None:
        # Сначала изменяем размер изображения с помощью Pillow
        original_image_2 = Image.open("data/frame_3.png")  # Замените на путь к вашему изображению
        resized_image_2 = original_image_2.resize((round(905 * 1*0.8), round(766 * 1*0.8)),Image.Resampling.LANCZOS)  # Изменяем размер
        app.global_image_2 = ImageTk.PhotoImage(resized_image_2)

    # Если метка изображения еще не была создана, создаем ее
    if app.image_label_2 is None:
        app.image_label_2 = ctk.CTkLabel(app, image=app.global_image_2)
        app.image_label_2.place(x=380, y=38)  # Размещаем метку в координатах x=220, y=150
        app.image_label_2.configure(text="")
    else:
        # Просто обновляем изображение метки
        app.image_label_2.configure(image=app.global_image_2)
        app.image_label_2.place(x=380, y=38)
        app.image_label_2.configure(text="")
        app.image_label_2.place_forget()
        app.image_label_2 = None
    if app.image_label is not None:
        app.image_label.place_forget()  # Скрываем метку изображения
    if app.image_label_1 is not None:
        app.image_label_1.place_forget()  # Скрываем метку изображения
def show_frame_4(app):
    original_image_4 = Image.open("data/frame_4.png")  # Замените на путь к вашему изображению
    resized_image_4 = original_image_4.resize((round(2213 * 0.45*0.8), round(840 * 0.45*0.8)),Image.Resampling.LANCZOS)  # Изменяем размер
    app.global_image_4 = ImageTk.PhotoImage(resized_image_4)

    app.image_label_4 = ctk.CTkLabel(app, image=app.global_image_4)
    app.image_label_4.place(x=325, y=8)  # Размещаем метку в координатах x=220, y=150
    app.image_label_4.configure(text="")
def show_frame_5(app):
    if app.global_image_5 is None:
        # Сначала изменяем размер изображения с помощью Pillow
        original_image_5 = Image.open("data/frame_5.png")  # Замените на путь к вашему изображению
        resized_image_5 = original_image_5.resize((round(2191 * 0.46*0.8), round(825 * 0.46*0.8)),Image.Resampling.LANCZOS)  # Изменяем размер
        app.global_image_5 = ImageTk.PhotoImage(resized_image_5)

    # Если метка изображения еще не была создана, создаем ее
    if app.image_label_5 is None:
        app.image_label_5 = ctk.CTkLabel(app, image=app.global_image_5)
        app.image_label_5.place(x=325, y=7)  # Размещаем метку в координатах x=220, y=150
        app.image_label_5.configure(text="")
    else:
        # Просто обновляем изображение метки
        app.image_label_5.configure(image=app.global_image_5)
        app.image_label_5.place(x=325, y=7)
        app.image_label_5.configure(text="")
        app.image_label_5.place_forget()
        app.image_label_5 = None

def show_oxigen_properties(app):
    """=====Создание изображения с параметрами окислителей====="""
    # Если изображение еще не было загружено, загружаем его
    if app.global_image is None:
        original_image = Image.open("data/oxigen.png")  # Путь к изображению
        resized_image = original_image.resize((round(1205 * 0.8), round(763 * 0.8)), Image.Resampling.LANCZOS)
        app.global_image = ImageTk.PhotoImage(resized_image)

    # Если метка изображения еще не была создана, создаем ее
    if app.image_label is None:
        app.image_label = ctk.CTkLabel(app, image=app.global_image)
        app.image_label.place(x=216, y=41)
        app.image_label.configure(text="")
    else:
        app.image_label.configure(image=app.global_image)
        app.image_label.place(x=216, y=41)
        app.image_label.configure(text="")
    if app.image_label_1 is not None:
        app.image_label_1.place_forget()
    if app.image_label_2 is not None:
        app.image_label_2.place_forget()

def show_fuel_properties(app):
    """=====Создание изображения с параметрами горючих====="""
    if app.global_image_1 is None:
        # Сначала изменяем размер изображения с помощью Pillow
        original_image_1 = Image.open("data/fuel.png")  # Замените на путь к вашему изображению
        resized_image_1 = original_image_1.resize((round(1205 * 0.8), round(763 * 0.8)),Image.Resampling.LANCZOS)  # Изменяем размер
        app.global_image_1 = ImageTk.PhotoImage(resized_image_1)

    # Если метка изображения еще не была создана, создаем ее
    if app.image_label_1 is None:
        app.image_label_1 = ctk.CTkLabel(app, image=app.global_image_1)
        app.image_label_1.place(x=216, y=41)  # Размещаем метку в координатах x=220, y=150
        app.image_label_1.configure(text="")
    else:
        # Просто обновляем изображение метки
        app.image_label_1.configure(image=app.global_image_1)
        app.image_label_1.place(x=216, y=41)
        app.image_label_1.configure(text="")
    if app.image_label is not None:
        app.image_label.place_forget()  # Скрываем метку изображения
    if app.image_label_2 is not None:
        app.image_label_2.place_forget()

def show_alpha_properties(app):
    """=====Создание изображения с параметрами смешения компонентов====="""
    if app.global_image_2 is None:
        # Сначала изменяем размер изображения с помощью Pillow
        original_image_2 = Image.open("data/alpha_105.png")  # Замените на путь к вашему изображению
        resized_image_2 = original_image_2.resize((round(1205 * 0.8), round(763 * 0.8)),Image.Resampling.LANCZOS)  # Изменяем размер
        app.global_image_2 = ImageTk.PhotoImage(resized_image_2)

    # Если метка изображения еще не была создана, создаем ее
    if app.image_label_2 is None:
        app.image_label_2 = ctk.CTkLabel(app, image=app.global_image_2)
        app.image_label_2.place(x=216, y=41)  # Размещаем метку в координатах x=220, y=150
        app.image_label_2.configure(text="")
    else:
        # Просто обновляем изображение метки
        app.image_label_2.configure(image=app.global_image_2)
        app.image_label_2.place(x=216, y=41)
        app.image_label_2.configure(text="")
    if app.image_label is not None:
        app.image_label.place_forget()  # Скрываем метку изображения
    if app.image_label_1 is not None:
        app.image_label_1.place_forget()  # Скрываем метку изображения

def hide_images(app):
    if app.image_label is not None:
        app.image_label.place_forget()  # Скрываем метку изображения
    if app.image_label_2 is not None:
        app.image_label_2.place_forget()
    if app.image_label_1 is not None:
        app.image_label_1.place_forget()  # Скрываем метку изображения

def function_1(array):
    choice_mapping = {
        (1, 1, 1, 1): 1,  # Есть пристенок, ядро однокомпонентное, шахматная, прист. одн.
        (1, 1, 1, 2): 1,
        (1, 1, 2, 1): 2,  # Есть пристенок, ядро однокомпонентное, сотовая, прист. одн.
        (1, 1, 2, 2): 2,
        (1, 1, 3, 1): 3,  # Есть пристенок, ядро однокомпонентное, концентрическая, прист. одн.
        (1, 1, 3, 2): 3,
        (1, 2, 1, 1): 4,  # Есть пристенок, ядро двухкомпонентное, шахматная, прист. одн.
        (1, 2, 1, 2): 5,  # Есть пристенок, ядро двухкомпонентное, шахматная, прист. двух.
        (1, 2, 2, 1): 6,  # Есть пристенок, ядро двухкомпонентное, сотовая, прист. одн.
        (1, 2, 2, 2): 7, # Есть пристенок, ядро двухкомпонентное, сотовая, прист. двух.
        (1, 2, 3, 1): 8, # Есть пристенок, ядро двухкомпонентное, концентрическая, прист. одн.
        (1, 2, 3, 2): 9, # Есть пристенок, ядро двухкомпонентное, концентрическая, прист. двух.
        (2, 1, 1, 1): 10, # Нет пристенка, ядро однокомпонентное, шахматная, прист. одн.
        (2, 1, 1, 2): 10,
        (2, 1, 2, 1): 11, # Нет пристенка, ядро однокомпонентное, сотовая, прист. одн.
        (2, 1, 2, 2): 11,
        (2, 1, 3, 1): 12, # Нет пристенка, ядро однокомпонентное, концентрическая, прист. одн.
        (2, 1, 3, 2): 12,
        (2, 2, 1, 1): 13, # Нет пристенка, ядро двухкомпонентное, шахматная, прист. одн.
        (2, 2, 1, 2): 13,
        (2, 2, 2, 1): 14, # Нет пристенка, ядро двухкомпонентное, сотовая, прист. одн.
        (2, 2, 2, 2): 14,
        (2, 2, 3, 1): 15, # Нет пристенка, ядро двухкомпонентное, концентрическая, прист. одн.
        (2, 2, 3, 2): 15
    }
    number = choice_mapping.get(array, "Неверный выбор")
    return number
def print_image(number,frame):
    if number==1 or number==4 or number==5:
        chess_scheme_with_a_wall(350, 19, 60, 5, 3, 3, frame, number,"off")
    elif number==2 or number==6 or number==7:
        cellular_scheme_with_a_wall(345, 25, 60, 5, 6, 3, frame, number,"off")
    elif number==3 or number==8 or number==9:
        concentric_scheme_with_a_wall(350, 19, 60, 3, 3, 3, frame, number,"off")
    elif number==10 or number==13:
        chess_scheme(350,19,3,6,frame,number)
    elif number==11 or number==14:
        cellular_scheme(345,25,3,6,frame,number)
    elif number==12 or number==15:
        concentric_scheme(350,22,3,6,frame,number)
def save_txt(array):
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно tkinter
    file_path = filedialog.asksaveasfilename(defaultextension='.txt',
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:  # Если путь был выбран
        with open(file_path, 'w') as f:
            for x,y,z in array:
                f.write(f'{x}\t{y}\t{z}\n')
def save_excel(array):
    """=====Сохранение результатов в формате excel (2 параметра)====="""
    X=[]
    Y=[]
    Z=[]
    for x,y,z in array:
       X.append(x)
       Y.append(y)
       Z.append(z)
    df = pd.DataFrame({"X": X,"Y": Y,"m": Z})
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно tkinter
    file_path = filedialog.asksaveasfilename(defaultextension='.xlsx',filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    if file_path:  # Если путь был выбран
        df.to_excel(file_path, index=False)

def azmax(choice,D_k,H, number_pr, delta_wall, delta, delta_y_pr,second_layer):
    n_pr_g=0
    n_pr_ok=0
    n_y_g=0
    n_y_ok=0

    coord_pr_g_x=[]
    coord_pr_g_y=[]

    coord_pr_ok_x=[]
    coord_pr_ok_y=[]

    coord_y_g_x=[]
    coord_y_g_y=[]

    coord_y_ok_x=[]
    coord_y_ok_y=[]


    if choice <10:
        if second_layer==1:
            n_pr_g=number_pr
            if choice==5 or choice==7 or choice==9:
                n_pr_ok=n_pr_g
            alpha = 360 / number_pr
            i = 0
            d_wall = (2 * (D_k / 2 - delta_wall) * np.sin(np.radians(180 / number_pr))) / (
                    1 + np.sin(np.radians(180 / number_pr)))

            while i < 360:
                x = (D_k / 2 - delta_wall - d_wall / 2) * np.cos(np.radians(i))
                y = (D_k / 2 - delta_wall - d_wall / 2) * np.sin(np.radians(i))
                i += alpha
                coord_pr_g_x.append(x)
                coord_pr_g_y.append(y)

            if choice==5 or choice==7 or choice==9:
                coord_pr_ok_x=coord_pr_g_x
                coord_pr_ok_y=coord_pr_g_y

        else:
            n_pr_g=2*number_pr-6
            if choice==5 or choice==7 or choice==9:
                n_pr_ok=n_pr_g
            alpha = 360 / number_pr
            i = 0
            d_wall = (2 * (D_k / 2 - delta_wall) * np.sin(np.radians(180 / number_pr))) / (
                    1 + np.sin(np.radians(180 / number_pr)))

            while i < 360:
                x = (D_k / 2 - delta_wall - d_wall / 2) * np.cos(np.radians(i))
                y = (D_k / 2 - delta_wall - d_wall / 2) * np.sin(np.radians(i))
                i += alpha
                coord_pr_g_x.append(x)
                coord_pr_g_y.append(y)


            alpha_2 = 360 / (number_pr - 6)
            i = 0

            while i < 360:
                x = (D_k / 2 - delta_wall - d_wall - d_wall / 2) * np.cos(np.radians(i))
                y = (D_k / 2 - delta_wall - d_wall - d_wall / 2) * np.sin(np.radians(i))
                i += alpha_2
                coord_pr_g_x.append(x)
                coord_pr_g_y.append(y)

            if choice==5 or choice==7 or choice==9:
                coord_pr_ok_x=coord_pr_g_x
                coord_pr_ok_y=coord_pr_g_y
    return n_pr_g,n_pr_ok,coord_pr_g_x,coord_pr_g_y,coord_pr_ok_x,coord_pr_ok_y
def save_txt_1(X, Y):
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно tkinter
    file_path = filedialog.asksaveasfilename(defaultextension='.txt',
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:  # Если путь был выбран
        with open(file_path, 'w') as f:
            for x,y in zip(X, Y):
                f.write(f'{x}\t{y}\n')
def save_txt_3(array):
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно tkinter
    file_path = filedialog.asksaveasfilename(defaultextension='.txt',
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:  # Если путь был выбран
        with open(file_path, 'w') as f:
            f.write(f'X\tY\tk_m\n')
            for i in range(len(array)):
                X, Y, Z = array[i]
                f.write(f'{X}\t{Y}\t{Z}\n')
def save_to_excel(array):
    """=====Сохранение результатов в формате excel (2 параметра)====="""
    X = []
    Y = []
    Z = []
    for row in array:
        X.append(row[0])
    for row in array:
        Y.append(row[1])
    for row in array:
        Z.append(row[2])
    df = pd.DataFrame({"X": X,"Y": Y,"k_m": Z})
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно tkinter
    file_path = filedialog.asksaveasfilename(defaultextension='.xlsx',
                                             filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    if file_path:  # Если путь был выбран
        df.to_excel(file_path, index=False)
def save_txt_fors(text):
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно tkinter
    file_path = filedialog.asksaveasfilename(defaultextension='.txt',
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:  # Если путь был выбран
        with open(file_path, 'w') as f:
            f.write(f'{text}')
def find_coord_core(choice,D_k,H,number_pr,delta_wall, delta, delta_y_pr,second_layer):
    """Поиск координат центров окружностей в ядре смесительной головки"""
    if choice == 1 or choice == 4 or choice == 5 or choice == 10 or choice == 13: # 1,4,5,10,13 - шахматная

        centers=[]
        coord_y_g_x=[]
        coord_y_g_y = []
        coord_y_ok_x=[]
        coord_y_ok_y = []
        R_k=D_k / 2
        r = H / 2
        d_wall = (2 * (D_k / 2 - delta_wall) * np.sin(np.radians(180 / number_pr))) / (1 + np.sin(np.radians(180 / number_pr)))

        if second_layer==1: # Один пристеночный слой
            max_index = int((R_k - d_wall - delta_wall - delta_y_pr) // H) + 1
        elif second_layer==2:  # Два пристеночного слоя
            max_index = int((R_k - 2*d_wall - delta_wall - delta_y_pr) // H) + 1
        else:
            max_index = int((R_k - delta_wall ) // H) + 1

        for i in range(-max_index, max_index + 1):
            for j in range(-max_index, max_index + 1):
                x = i * H
                y = j * H
                if second_layer == 1:
                    # Проверяем, что окружность не выходит за границы
                    if np.sqrt(x ** 2 + y ** 2) + r <= (R_k - d_wall - delta_wall - delta_y_pr):
                        centers.append((x, y))
                else:
                    if np.sqrt(x ** 2 + y ** 2) + r <= (R_k - 2 * d_wall - delta_wall - delta_y_pr):
                        centers.append((x, y))

        for (x, y) in centers:
            if choice==4 or choice==5 or choice==13:
                coord_y_g_x.append(x)
                coord_y_g_y.append(y)
                coord_y_ok_x.append(x)
                coord_y_ok_y.append(y)
            else:
                if (int((x / H) + (y / H)) % 2) == 0:
                    coord_y_g_x.append(x)
                    coord_y_g_y.append(y)
                else:
                    coord_y_ok_x.append(x)
                    coord_y_ok_y.append(y)
        return coord_y_g_x,coord_y_g_y,coord_y_ok_x,coord_y_ok_y
#____________________________________________________________________________________________________________________
    elif choice == 2 or choice == 6 or choice == 7 or choice == 11 or choice == 14: # 2,6,7,11,14 - сотовая

        R_k = D_k / 2  # радиус камеры сгорания
        d_wall = (2 * (D_k / 2 - delta_wall) * np.sin(np.radians(180 / number_pr))) / (
                1 + np.sin(np.radians(180 / number_pr)))
        coord_y_g_x = []
        coord_y_g_y = []
        coord_y_ok_x = []
        coord_y_ok_y = []


        if second_layer==1:
            d_itog = 2 * (R_k - delta_wall - d_wall - delta_y_pr)
        elif second_layer==2:
            d_itog = 2 * (R_k - delta_wall - 2 * d_wall - delta_y_pr)
        else:
            d_itog = 2 * (R_k - delta_wall)

        n_1 = int((d_itog / 2 - H / 2) // H)
        n_2 = int((d_itog / 2 - H / 2) // (H * np.sin(np.radians(60))))

        for i in range(-n_1 - 1, n_1 + 2):
            for j in range(-n_2, n_2 + 1):
                if j % 2 == 0:
                    x = i * H
                    y = j * H * np.sin(np.radians(60))
                else:
                    x = i * H + H / 2
                    y = j * H * np.sin(np.radians(60))
                if np.sqrt(x ** 2 + y ** 2) + H / 2 <= d_itog / 2:
                    if choice==2 or choice==11:
                        if (abs(i)) % 3 == 0 and j % 2 == 0: #Горючее
                            coord_y_g_x.append(x)
                            coord_y_g_y.append(y)
                        elif ((i)) % 3 == 1 and j % 2 == 1: #Горючее
                            coord_y_g_x.append(x)
                            coord_y_g_y.append(y)
                        else: #Окислитель
                            coord_y_ok_x.append(x)
                            coord_y_ok_y.append(y)
                    else:
                        coord_y_g_x.append(x)
                        coord_y_g_y.append(y)
                        coord_y_ok_x.append(x)
                        coord_y_ok_y.append(y)
        return coord_y_g_x,coord_y_g_y,coord_y_ok_x,coord_y_ok_y
# ____________________________________________________________________________________________________________________
    else: # 3,8,9,12,15 - концентрическая

        R_k = D_k / 2  # радиус камеры сгорания
        r = H / 2  # Половина шага
        r_0 = r - (delta * 0.5)
        sin_60 = np.sin(np.radians(60))
        centers = []  # Сюда будут записываться координаты форсунок
        edge_count=number_pr
        coord_y_g_x = []
        coord_y_g_y = []
        coord_y_ok_x = []
        coord_y_ok_y = []

        d_wall = (2 * (D_k / 2 - delta_wall) * np.sin(np.radians(180 / edge_count))) / (
                1 + np.sin(np.radians(180 / edge_count)))

        if second_layer==1:
            d_itog = 2 * (R_k - delta_wall - d_wall - delta_y_pr)
        elif second_layer==2:
            d_itog = 2 * (R_k - delta_wall - 2 * d_wall - delta_y_pr)
        else:
            d_itog = 2 * (R_k - delta_wall)

        edge_radius = d_wall / 2
        # Границы сетки, чтобы покрыть всю большую окружность
        max_index = int((d_itog/2) // H) + 1
        x = 0
        y = 0
        for k in range(0, max_index + 1):
            theta = np.linspace(0, 2 * np.pi, 6 * k, endpoint=False)
            for angle in theta:
                x = (k * H) * np.cos(angle)
                y = (k * H) * np.sin(angle)
                if np.sqrt(x ** 2 + y ** 2) + r <= d_itog/2:
                    centers.append((x, y, k))

        for (x, y, k) in centers:
            if choice==3 or choice==12:
                if k % 2 == 0:
                    coord_y_g_x.append(x)
                    coord_y_g_y.append(y)
                else:
                    coord_y_ok_x.append(x)
                    coord_y_ok_y.append(y)
            else:
                coord_y_g_x.append(x)
                coord_y_g_y.append(y)
                coord_y_ok_x.append(x)
                coord_y_ok_y.append(y)
        if choice == 3 or choice == 12:
            coord_y_g_x.append(0)
            coord_y_g_y.append(0)
        else:
            coord_y_g_x.append(0)
            coord_y_g_y.append(0)
            coord_y_ok_x.append(0)
            coord_y_ok_y.append(0)
        return coord_y_g_x, coord_y_g_y, coord_y_ok_x, coord_y_ok_y
def function_2(array):
    choice_mapping = {
        (0,1,8,1): 1,  # Есть пристенок, ядро однокомпонентное, шахматная, прист. одн.
        (0,1,8,2):2,
        (0,1,9,1):3,
        (0,1,9,2): 4,
        (0,2,8,1):5,
        (0,2,8,2): 6,
        (0,2,9,1):7,
        (0,2,9,2): 8,
        (0,3,8,1):9,
        (0,3,8,2): 10,
        (0,3,9,1):11,
        (0,3,9,2): 12,
        (4,6,8,1):13,
        (4,6,8,2): 14,
        (4,6,9,1):15,
        (4,6,9,2): 16,
        (4,7,8,1):17,
        (4,7,8,2): 18,
        (4,7,9,1):19,
        (4,7,9,2): 20,
        (5,6,8,1):21,
        (5,6,8,2): 22,
        (5,6,9,1):23,
        (5,6,9,2): 24,
        (5,7,8,1):25,
        (5,7,8,2): 26,
        (5,7,9,1):27,
        (5,7,9,2):28
    }
    number = choice_mapping.get(array, "Неверный выбор")
    return number
def find_costs_2(x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, choice,n_g_pr,n_o_pr,n_g_y,n_o_y,coord_pr_g_x,coord_pr_g_y,coord_y_g_x,coord_y_g_y,coord_y_ok_x,coord_y_ok_y):

    coord_gor=[]
    coord_ok = []
    m_f_o_pr=0
    m_f_g_y=(x_5+x_6)/n_g_y
    m_f_o_y = (x_7 + x_8) / n_o_y

    m_f_g_y_1=(x_5)/n_g_y
    m_f_g_y_2=(x_7) / n_o_y
    m_f_o_y_1 = (x_6) / n_g_y
    m_f_o_y_2 = (x_8) / n_o_y
    for x,y in zip(coord_y_g_x,coord_y_g_y):
        if m_f_g_y_1!=0:
            coord_gor.append((x,y,m_f_g_y_1))
        if m_f_o_y_1 != 0:
            coord_ok.append((x,y,m_f_o_y_1))
    for x, y in zip(coord_y_ok_x, coord_y_ok_y):
        if m_f_g_y_2 != 0:
            coord_gor.append((x, y, m_f_g_y_2))
        if m_f_o_y_2 != 0:
            coord_ok.append((x, y, m_f_o_y_2))
    if choice==1 or choice==2 or choice==3 or choice==4 or choice==6 or choice==8:
        m_f_g_pr = (x_1 + x_2) / n_g_pr

        m_f_g_pr_1 = (x_1) / n_g_pr
        m_f_ok_pr_1 = (x_2) / n_g_pr
        for x, y in zip(coord_pr_g_x, coord_pr_g_y):
            if m_f_g_pr_1 != 0:
                coord_gor.append((x, y, m_f_g_pr_1))
            if m_f_ok_pr_1 != 0:
                coord_ok.append((x, y, m_f_ok_pr_1))
    elif choice == 5 or choice == 7 or choice == 9:
        m_f_g_pr = (x_1 + x_2) / n_g_y
        m_f_o_pr = (x_3 + x_4) / n_o_y

        m_f_g_pr_1 = (x_1) / n_g_pr
        m_f_g_pr_2 = (x_3) / n_o_pr
        m_f_o_pr_1 = (x_2) / n_g_pr
        m_f_o_pr_2 = (x_4) / n_o_pr
        for x, y in zip(coord_pr_g_x, coord_pr_g_y):
            if m_f_g_pr_1 != 0:
                coord_gor.append((x, y, m_f_g_pr_1))
            if m_f_g_pr_2 != 0:
                coord_gor.append((x, y, m_f_g_pr_2))
            if m_f_o_pr_1 != 0:
                coord_ok.append((x, y, m_f_o_pr_1))
            if m_f_o_pr_2 != 0:
                coord_ok.append((x, y, m_f_o_pr_2))
    else:
        m_f_g_pr=0
        m_f_o_pr=0
    return m_f_g_pr,m_f_o_pr,m_f_g_y,m_f_o_y,coord_gor,coord_ok
def is_point_in_circle(x0, y0, x, y, H):
    '''=====Функция для проверки, находится ли точка в окружности====='''
    radius = 3.0001 * H
    distance = math.sqrt((x0 - x) ** 2 + (y0 - y) ** 2)
    return distance <= radius

def phi(t):
    # Определяем функцию под интегралом
    integrand = lambda z: np.exp(-z ** 2)

    # Численное интегрирование от 0 до t
    integral_value, _ = quad(integrand, 0, t)

    # Вычисляем результат
    return (2 / math.sqrt(math.pi)) * integral_value
def method_by_ievlev_pr(angle,x_0,y_0,coord_gor,coord_ok,H):
    text_programm='[x_1] [x_2] [y_1] [y_2] [Комп.]=[Расход]\n'
    points_gor=[]
    points_ok = []
    dx_1_g=[]
    dx_2_g=[]
    dy_1_g=[]
    dx_1_ok = []
    dx_2_ok = []
    dy_1_ok = []
    m_gor_0=[]
    m_gor_1=0
    m_ok_0 = []
    m_ok_1 = 0
    n_gor=0
    n_ok=0
    for x,y,z in coord_gor:
        if is_point_in_circle(x, y, x_0, y_0, H):
            points_gor.append([x, y])
            m_gor_0.append(z)
            n_gor+=1
    for x,y,z in coord_ok:
        if is_point_in_circle(x, y, x_0, y_0, H):
            points_ok.append([x, y])
            m_ok_0.append(z)
            n_ok+=1
    for (x_1, y_1) in points_gor:
        H_0 = (x_1 - x_0) * math.cos(angle) + (y_1 - y_0) * math.sin(angle)
        L_0 = (x_1 - x_0) * math.sin(angle) - (y_1 - y_0) * math.cos(angle)
        h_1 = -(L_0 + H / 2)
        h_2 = -(L_0 - H / 2)
        l_1 = H_0 + H / 2
        if h_1>h_2:
            dx_1_g.append(h_2)
            dx_2_g.append(h_1)
        else:
            dx_1_g.append(h_1)
            dx_2_g.append(h_2)
        dy_1_g.append(-l_1)
    for (x_1, y_1) in points_ok:
        H_0 = (x_1 - x_0) * math.cos(angle) + (y_1 - y_0) * math.sin(angle)
        L_0 = (x_1 - x_0) * math.sin(angle) - (y_1 - y_0) * math.cos(angle)
        h_1 = -(L_0 + H / 2)
        h_2 = -(L_0 - H / 2)
        l_1 = H_0 + H / 2
        if h_1>h_2:
            dx_1_ok.append(h_2)
            dx_2_ok.append(h_1)
        else:
            dx_1_ok.append(h_1)
            dx_2_ok.append(h_2)
        dy_1_ok.append(-l_1)
    for x_1,x_2,y_1,m in zip(dx_1_g,dx_2_g,dy_1_g,m_gor_0):
        z_x_1_g=(x_1/(math.sqrt(2)*H))
        z_x_2_g=(x_2 / (math.sqrt(2) * H))
        z_y_1_g=(y_1 / (math.sqrt(2) * H))
        Phi_x_1_g=(phi(z_x_1_g))
        Phi_x_2_g=(phi(z_x_2_g))
        Phi_y_1_g=(phi(z_y_1_g))
        text_programm+=(f'{x_1:.3f},{x_2:.3f},{y_1:.3f},inf mFuel={m:.3f}\n')
        m_gor_1+=m*((Phi_x_2_g-Phi_x_1_g)*(1-Phi_y_1_g))
    for x_1,x_2,y_1,m in zip(dx_1_ok,dx_2_ok,dy_1_ok,m_ok_0):
        z_x_1_ok=(x_1/(math.sqrt(2)*H))
        z_x_2_ok=(x_2 / (math.sqrt(2) * H))
        z_y_1_ok=(y_1 / (math.sqrt(2) * H))
        Phi_x_1_ok=(phi(z_x_1_ok))
        Phi_x_2_ok=(phi(z_x_2_ok))
        Phi_y_1_ok=(phi(z_y_1_ok))
        m_ok_1+=m*((Phi_x_2_ok-Phi_x_1_ok)*(1-Phi_y_1_ok))
        text_programm+=(f'{x_1:.3f},{x_2:.3f},{y_1:.3f},inf mOx={m:.3f}\n')

    return 0.25*m_gor_1,0.25*m_ok_1,n_gor,n_ok,text_programm
def method_by_ievlev_core(x_0,y_0,coord_gor,coord_ok,H):
    text_programm='[x_1] [x_2] [y_1] [y_2] [Комп.]=[Расход]\n'
    x_10 = x_0 + H / 2
    x_20 = x_0 - H / 2
    y_10 = y_0 + H / 2
    y_20 = y_0 - H / 2
    points_gor=[]
    points_ok = []
    n_gor=0
    n_ok=0
    m_gor_0=[]
    m_ok_0=[]
    dx_1_g = []
    dx_2_g = []
    dy_1_g = []
    dy_2_g = []
    dx_1_ok = []
    dx_2_ok = []
    dy_1_ok = []
    dy_2_ok = []
    m_gor_1 = 0
    m_ok_1 = 0
    for x, y, z in coord_gor:
        if is_point_in_circle(x, y, x_0, y_0, H):
            points_gor.append([x, y])
            m_gor_0.append(z)
            n_gor += 1
    for x,y,z in coord_ok:
        if is_point_in_circle(x, y, x_0, y_0, H):
            points_ok.append([x, y])
            m_ok_0.append(z)
            n_ok+=1
    for (x_1, y_1) in points_gor:
        dx_1_g.append(x_1 - x_10)
        dx_2_g.append(x_1 - x_20)
        dy_1_g.append(y_1 - y_10)
        dy_2_g.append(y_1 - y_20)
    for (x_1, y_1) in points_ok:
        dx_1_ok.append(x_1 - x_10)
        dx_2_ok.append(x_1 - x_20)
        dy_1_ok.append(y_1 - y_10)
        dy_2_ok.append(y_1 - y_20)

    for x_1,x_2,y_1,y_2,m in zip(dx_1_g,dx_2_g,dy_1_g,dy_2_g,m_gor_0):
        z_x_1_g=(x_1/(math.sqrt(2)*H))
        z_x_2_g=(x_2 / (math.sqrt(2) * H))
        z_y_1_g=(y_1 / (math.sqrt(2) * H))
        z_y_2_g = (y_2 / (math.sqrt(2) * H))
        Phi_x_1_g=(phi(z_x_1_g))
        Phi_x_2_g=(phi(z_x_2_g))
        Phi_y_1_g=(phi(z_y_1_g))
        Phi_y_2_g = (phi(z_y_2_g))
        text_programm+=(f'{x_1:.3f},{x_2:.3f},{y_1:.3f},{y_2:.3f}, mFuel={m:.3f}\n')
        m_gor_1+=m*((Phi_x_2_g-Phi_x_1_g)*(Phi_y_2_g-Phi_y_1_g))
    for x_1,x_2,y_1,y_2,m in zip(dx_1_ok,dx_2_ok,dy_1_ok,dy_2_ok,m_ok_0):
        z_x_1_ok=(x_1/(math.sqrt(2)*H))
        z_x_2_ok=(x_2 / (math.sqrt(2) * H))
        z_y_1_ok=(y_1 / (math.sqrt(2) * H))
        z_y_2_ok = (y_2 / (math.sqrt(2) * H))
        Phi_x_1_ok=(phi(z_x_1_ok))
        Phi_x_2_ok=(phi(z_x_2_ok))
        Phi_y_1_ok=(phi(z_y_1_ok))
        Phi_y_2_ok = (phi(z_y_2_ok))
        m_ok_1+=m*((Phi_x_2_ok-Phi_x_1_ok)*(Phi_y_2_ok-Phi_y_1_ok))
        text_programm+=(f'{x_1:.3f},{x_2:.3f},{y_1:.3f},{y_2:.3f}, mOx={m:.3f}\n')
    return 0.25 * m_gor_1, 0.25 * m_ok_1, n_gor, n_ok,text_programm

def find_value(first, second,data):
    # Преобразуем числа в строки для поиска в JSON
    first = str(first)
    second = str(second)

    # Проверяем, есть ли ключи в верхнем уровне
    if first in data:
        sub_dict = data[first]
        # Проверяем, есть ли второй ключ во вложенном словаре
        if second in sub_dict:
            return sub_dict[second]
    return None
def find_l_otn_kz(D_kz,D_f,d_vh,x_st):
    beta=math.acos((0.5*(D_kz-d_vh))/(0.5*D_kz))
    alpha=math.acos(((0.5*D_f)-(x_st)-(0.5*d_vh))/(0.5*D_f))
    l_1=(D_kz/2)*math.sin(beta)
    l_2=(D_f/2)*math.sin(alpha)
    return l_2-l_1
