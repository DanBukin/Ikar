import customtkinter as ctk
import os
from PIL import Image, ImageTk
from ctypes import windll, byref, create_string_buffer
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import FuncFormatter
import tkinter as tk
from tkinter import filedialog
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
        resized_image = original_image.resize((round(905 * 1), round(766 * 1)), Image.Resampling.LANCZOS)
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
        resized_image_1 = original_image_1.resize((round(905 * 1), round(766 * 1)),Image.Resampling.LANCZOS)  # Изменяем размер
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
        resized_image_2 = original_image_2.resize((round(905 * 1), round(766 * 1)),Image.Resampling.LANCZOS)  # Изменяем размер
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
    resized_image_4 = original_image_4.resize((round(2213 * 0.45), round(840 * 0.45)),Image.Resampling.LANCZOS)  # Изменяем размер
    app.global_image_4 = ImageTk.PhotoImage(resized_image_4)

    app.image_label_4 = ctk.CTkLabel(app, image=app.global_image_4)
    app.image_label_4.place(x=325, y=8)  # Размещаем метку в координатах x=220, y=150
    app.image_label_4.configure(text="")
def show_frame_5(app):
    if app.global_image_5 is None:
        # Сначала изменяем размер изображения с помощью Pillow
        original_image_5 = Image.open("data/frame_5.png")  # Замените на путь к вашему изображению
        resized_image_5 = original_image_5.resize((round(2191 * 0.46), round(825 * 0.46)),Image.Resampling.LANCZOS)  # Изменяем размер
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
def chess_scheme_with_a_wall(D_k, H, edge_count,delta_wall,delta,delta_y_pr,frame,number,second_layer):
    n_pr_g=0
    n_pr_ok=0
    n_y_g=0
    n_y_ok=0

    coord_pr_g=[]
    coord_pr_ok=[]
    coord_y_g=[]
    coord_y_ok=[]

    number_0=number
    color_g='#D44B46'
    color_o='white'
    color_y_1='#D44B46'
    color_f='#242424'
    if second_layer=="off":
        dop_sloy=1
    else:
        dop_sloy=2
    if number_0==4:
        color_pr=color_g
        color_pr_1 = color_g
        color_y_1=color_g
        color_y_1_1 = color_f
        color_y_2=color_g
        color_y_2_1 = color_f
    if number_0==5:
        color_pr = color_g
        color_pr_1 = color_f
        color_y_1 = color_g
        color_y_1_1 = color_f
        color_y_2 = color_g
        color_y_2_1 = color_f
    if number_0==1:
        color_pr = color_g
        color_pr_1 = color_g
        color_y_1 = color_g
        color_y_1_1 = color_g
        color_y_2 = color_o
        color_y_2_1 = color_f
    fig = Figure(figsize=(7.7, 7.7), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('#242424')  # 171717

    R_k = D_k / 2  # радиус камеры сгорания
    r = H / 2  # Половина шага
    r_0 = r - (delta*0.5)
    centers = []  # Сюда будут записываться координаты форсунок
    centers_ok=[]
    centers_gor=[]
    centers_pr=[]
    centers_y_2=[]

    alpha = 360 / edge_count
    i = 0
    d_wall = (2 * (D_k / 2 - delta_wall) * np.sin(np.radians(180 / edge_count))) / (
                1 + np.sin(np.radians(180 / edge_count)))
    d_itog = 2 * (D_k / 2 - delta_wall - d_wall - delta_y_pr)

    while i < 360:
        x = (D_k / 2 - delta_wall - d_wall / 2) * np.cos(np.radians(i))
        y = (D_k / 2 - delta_wall - d_wall / 2) * np.sin(np.radians(i))
        i += alpha
        circle = plt.Circle((x, y), d_wall / 2, edgecolor=color_pr, facecolor=color_f, linestyle='--')
        circle_1 = plt.Circle((x, y), d_wall / 2 - delta / 2, edgecolor=color_pr, facecolor=color_pr_1)
        circle_2 = plt.Circle((x, y), 0.5, edgecolor=color_pr, facecolor=color_pr)
        ax.add_patch(circle)
        ax.add_patch(circle_1)
        ax.add_patch(circle_2)
    edge_radius = d_wall/2
    # Границы сетки, чтобы покрыть всю большую окружность
    max_index = int((R_k-2*edge_radius-delta_wall-delta_y_pr) // H) + 1

    if dop_sloy == 2:
        alpha_2 = 360 / (edge_count - 6)
        i = 0
        d_wall_2 = d_wall

        while i < 360:
            x = (R_k - delta_wall - d_wall - d_wall / 2) * np.cos(np.radians(i))
            y = (R_k - delta_wall - d_wall - d_wall / 2) * np.sin(np.radians(i))
            i += alpha_2
            circle = plt.Circle((x, y), d_wall_2 / 2, edgecolor=color_pr, facecolor=color_f, linestyle='--')
            circle_1 = plt.Circle((x, y), d_wall_2 / 2 - delta / 2, edgecolor=color_pr, facecolor=color_pr_1)
            circle_2 = plt.Circle((x, y), 0.5, edgecolor=color_pr, facecolor=color_pr)
            ax.add_patch(circle)
            ax.add_patch(circle_1)
            ax.add_patch(circle_2)
        max_index = int((R_k - 4 * edge_radius - delta_wall - delta_y_pr) // H) + 1

    # Сетка
    for i in range(-max_index, max_index + 1):
        for j in range(-max_index, max_index + 1):
            x = i * H
            y = j * H
            if dop_sloy == 1:
                # Проверяем, что окружность не выходит за границы
                if np.sqrt(x ** 2 + y ** 2) + r <= (R_k-2*edge_radius-delta_wall-delta_y_pr):
                    centers.append((x, y))
            else:
                if np.sqrt(x ** 2 + y ** 2) + r <= (R_k-4*edge_radius-delta_wall-delta_y_pr):
                    centers.append((x, y))

    # Рисуем большую окружность
    big_circle = plt.Circle((0, 0), R_k, fill=False, color=color_g)
    ax.add_artist(big_circle)

    # Рисуем маленькие окружности
    n_gor_0=0
    n_ok_0=0
    for (x, y) in centers:
        if (int((x / H) + (y / H)) % 2) == 0:
            n_ok_0+=1
            color = color_y_1 # Цвет окислительных форсунок, если они однокомпонентные (white)
            color_1=color_y_1_1
            centers_ok.append((x, y))
        else:
            n_gor_0 +=1
            color = color_y_2
            color_1=color_y_2_1
            centers_gor.append((x, y))
        small_circle = plt.Circle((x, y), r, fill=False, linestyle="--", color=color)
        small_circle_0 = plt.Circle((x, y), r_0, fill=True, edgecolor=color, facecolor=color_1)
        dot_0 = plt.Circle((x, y), 0.5, fill=True, edgecolor=color, facecolor=color_1)
        ax.add_artist(small_circle)
        ax.add_artist(small_circle_0)
        ax.add_artist(dot_0)

    ax.tick_params(axis='x', colors='white', labelsize=14)
    ax.tick_params(axis='y', colors='white', labelsize=14)
    ax.grid(True, color='white', linestyle='--', linewidth=0.1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.title.set_color('white')
    fig.patch.set_facecolor('#242424')  # 171717
    fig.subplots_adjust(left=0.07, bottom=0.05, right=0.98, top=0.98)
    # Установите форматирование для осей X и Y
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    # Обновите параметры тиков после изменения меток, если нужно
    ax.tick_params(axis='x', colors='white', labelsize=15)  # Используйте свой размер шрифта
    ax.tick_params(axis='y', colors='white', labelsize=15)  # Используйте свой размер шрифта
    ax.set_xlim(-R_k - H, R_k + H)
    ax.set_ylim(-R_k - H, R_k + H)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=760, y=70)

    return r_0*2,d_wall-delta
def cellular_scheme_with_a_wall(D_k, H, edge_count,delta_wall,delta,delta_y_pr,frame,number,second_layer):
    number_0=number
    color_g='#D44B46'
    color_o='white'
    color_f='#242424'

    if second_layer=="off":
        dop_sloy=1
    else:
        dop_sloy=2

    if number_0==6:
        color_pr=color_g
        color_pr_1 = color_g
        color_y_1=color_f
        color_y_2=color_g
        color_y_1_0=color_f
    if number_0==7:
        color_pr = color_g
        color_pr_1 = color_f
        color_y_1 = color_f
        color_y_2 = color_g

    if number_0==2:
        color_pr = color_g
        color_pr_1 = color_g
        color_y_1 = color_g
        color_y_2 = color_o

    fig = Figure(figsize=(7.7, 7.7), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('#242424')  # 171717

    R_k = D_k / 2  # радиус камеры сгорания
    r = H / 2  # Половина шага


    circle_0 = plt.Circle((0, 0), D_k / 2, edgecolor=color_g, facecolor=color_f)
    ax.add_patch(circle_0)

    alpha = 360 / edge_count
    i = 0
    d_wall = (2 * (D_k / 2 - delta_wall) * np.sin(np.radians(180 / edge_count))) / (1 + np.sin(np.radians(180 / edge_count)))
    d_itog = 2 * (D_k / 2 - delta_wall - d_wall - delta_y_pr)

    while i < 360:
        x = (D_k / 2 - delta_wall - d_wall / 2) * np.cos(np.radians(i))
        y = (D_k / 2 - delta_wall - d_wall / 2) * np.sin(np.radians(i))
        i += alpha
        circle = plt.Circle((x, y), d_wall / 2, edgecolor=color_pr, facecolor=color_f, linestyle='--')
        circle_1 = plt.Circle((x, y), d_wall / 2 - delta / 2, edgecolor=color_pr, facecolor=color_pr_1)
        circle_2 = plt.Circle((x, y), 0.5, edgecolor=color_pr, facecolor=color_pr)
        ax.add_patch(circle)
        ax.add_patch(circle_1)
        ax.add_patch(circle_2)

    if dop_sloy == 2:
        alpha_2 = 360 / (edge_count - 6)
        i = 0
        d_wall_2 = d_wall

        while i < 360:
            x = (R_k - delta_wall - d_wall - d_wall / 2) * np.cos(np.radians(i))
            y = (R_k - delta_wall - d_wall - d_wall / 2) * np.sin(np.radians(i))
            i += alpha_2
            circle = plt.Circle((x, y), d_wall_2 / 2, edgecolor=color_pr, facecolor=color_f, linestyle='--')
            circle_1 = plt.Circle((x, y), d_wall_2 / 2 - delta / 2, edgecolor=color_pr, facecolor=color_pr_1)
            circle_2 = plt.Circle((x, y), 0.5, edgecolor=color_pr, facecolor=color_pr)
            ax.add_patch(circle)
            ax.add_patch(circle_1)
            ax.add_patch(circle_2)

        d_itog = 2 * (R_k - delta_wall - 2 * d_wall - delta_y_pr)
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
                if (abs(i)) % 3 == 0 and j % 2 == 0:
                    circle = plt.Circle((x, y), H / 2, edgecolor=color_g, facecolor=color_f, linestyle='--')
                    ax.add_patch(circle)
                    circle_1 = plt.Circle((x, y), H / 2 - delta / 2, edgecolor=color_g, facecolor=color_y_1)
                    ax.add_patch(circle_1)
                    circle_2 = plt.Circle((x, y), 0.5, edgecolor=color_g, facecolor=color_y_1)
                    ax.add_patch(circle_2)
                elif ((i)) % 3 == 1 and j % 2 == 1:
                    circle = plt.Circle((x, y), H / 2, edgecolor=color_g, facecolor=color_f, linestyle='--')
                    ax.add_patch(circle)
                    circle_1 = plt.Circle((x, y), H / 2 - delta / 2, edgecolor=color_g, facecolor=color_y_1)
                    ax.add_patch(circle_1)
                    circle_2 = plt.Circle((x, y), 0.5, edgecolor=color_g, facecolor=color_y_1)
                    ax.add_patch(circle_2)
                else:
                    circle = plt.Circle((x, y), H / 2, edgecolor=color_y_2, facecolor=color_f, linestyle='--')
                    ax.add_patch(circle)
                    circle_1 = plt.Circle((x, y), H / 2 - delta / 2, edgecolor=color_y_2, facecolor=color_f)
                    ax.add_patch(circle_1)
                    circle_2 = plt.Circle((x, y), 0.5, edgecolor=color_y_2, facecolor=color_f)
                    ax.add_patch(circle_2)

    ax.tick_params(axis='x', colors='white', labelsize=14)
    ax.tick_params(axis='y', colors='white', labelsize=14)
    ax.grid(True, color='white', linestyle='--', linewidth=0.1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.title.set_color('white')
    fig.patch.set_facecolor('#242424')  # 171717
    fig.subplots_adjust(left=0.07, bottom=0.05, right=0.98, top=0.98)
    # Установите форматирование для осей X и Y
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    # Обновите параметры тиков после изменения меток, если нужно
    ax.tick_params(axis='x', colors='white', labelsize=15)  # Используйте свой размер шрифта
    ax.tick_params(axis='y', colors='white', labelsize=15)  # Используйте свой размер шрифта
    ax.set_xlim(-R_k - H, R_k + H)
    ax.set_ylim(-R_k - H, R_k + H)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=760, y=70)

    return (H-delta),d_wall-delta
def concentric_scheme_with_a_wall(D_k, H, edge_count,delta_wall,delta,delta_y_pr,frame,number,second_layer):
    number_0=number
    color_g='#D44B46'
    color_o='white'
    color_f='#242424'

    if second_layer=="off":
        dop_sloy=1
    else:
        dop_sloy=2

    if number_0==8:
        color_pr=color_g
        color_pr_1 = color_g
        color_y_1=color_g
        color_y_2=color_g
        color_y_1_0=color_f
    if number_0==9:
        color_pr = color_g
        color_pr_1 = color_f
        color_y_1 = color_g
        color_y_2 = color_g
        color_y_1_0 = color_f
    if number_0==3:
        color_pr = color_g
        color_pr_1 = color_g
        color_y_1 = color_g
        color_y_2 = color_o
        color_y_1_0 = color_g
    fig = Figure(figsize=(7.7, 7.7), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('#242424')  # 171717

    R_k = D_k / 2  # радиус камеры сгорания
    r = H / 2  # Половина шага
    r_0 = r - (delta*0.5)
    sin_60 = np.sin(np.radians(60))
    centers = []  # Сюда будут записываться координаты форсунок

    alpha = 360 / edge_count
    i = 0
    d_wall = (2 * (D_k / 2 - delta_wall) * np.sin(np.radians(180 / edge_count))) / (
                1 + np.sin(np.radians(180 / edge_count)))
    d_itog = 2 * (D_k / 2 - delta_wall - d_wall - delta_y_pr)

    while i < 360:
        x = (D_k / 2 - delta_wall - d_wall / 2) * np.cos(np.radians(i))
        y = (D_k / 2 - delta_wall - d_wall / 2) * np.sin(np.radians(i))
        i += alpha
        circle = plt.Circle((x, y), d_wall / 2, edgecolor=color_pr, facecolor=color_f, linestyle='--')
        circle_1 = plt.Circle((x, y), d_wall / 2 - delta / 2, edgecolor=color_pr, facecolor=color_pr_1)
        circle_2 = plt.Circle((x, y), 0.5, edgecolor=color_pr, facecolor=color_pr)
        ax.add_patch(circle)
        ax.add_patch(circle_1)
        ax.add_patch(circle_2)
    edge_radius=d_wall/2
    # Границы сетки, чтобы покрыть всю большую окружность
    max_index = int((R_k - 2 * edge_radius - delta_wall - delta_y_pr) // H) + 1
    x = 0
    y = 0
    small_circle = plt.Circle((x, y), r, fill=False, linestyle="--", color=color_y_1)
    small_circle_0 = plt.Circle((x, y), r_0, fill=True, edgecolor=color_y_1, facecolor=color_y_1_0)
    dot_0 = plt.Circle((x, y), 0.5, fill=True, edgecolor=color_y_1, facecolor=color_y_1_0)
    ax.add_artist(small_circle)
    ax.add_artist(small_circle_0)
    ax.add_artist(dot_0)

    if dop_sloy == 2:
        alpha_2 = 360 / (edge_count - 6)
        i = 0
        d_wall_2 = d_wall

        while i < 360:
            x = (R_k - delta_wall - d_wall - d_wall / 2) * np.cos(np.radians(i))
            y = (R_k - delta_wall - d_wall - d_wall / 2) * np.sin(np.radians(i))
            i += alpha_2
            circle = plt.Circle((x, y), d_wall_2 / 2, edgecolor=color_pr, facecolor=color_f, linestyle='--')
            circle_1 = plt.Circle((x, y), d_wall_2 / 2 - delta / 2, edgecolor=color_pr, facecolor=color_pr_1)
            circle_2 = plt.Circle((x, y), 0.5, edgecolor=color_pr, facecolor=color_pr)
            ax.add_patch(circle)
            ax.add_patch(circle_1)
            ax.add_patch(circle_2)

        max_index = int((R_k - 4 * edge_radius - delta_wall - delta_y_pr) // H) + 1

    for k in range(0, max_index + 1):
        theta = np.linspace(0, 2 * np.pi, 6 * k, endpoint=False)
        for angle in theta:
            x = (k * H) * np.cos(angle)
            y = (k * H) * np.sin(angle)
            if dop_sloy==1 and np.sqrt(x ** 2 + y ** 2) + r <= (R_k - 2 * edge_radius - delta_wall - delta_y_pr):
                centers.append((x, y,k))
            if dop_sloy==2 and np.sqrt(x ** 2 + y ** 2) + r <= (R_k - 4 * edge_radius - delta_wall - delta_y_pr):
                centers.append((x, y,k))
    for (x, y,k) in centers:
        if k % 2 == 0:
            small_circle = plt.Circle((x, y), r, fill=False, linestyle="--", color=color_y_1)
            small_circle_0 = plt.Circle((x, y), r_0, fill=True, edgecolor=color_y_1, facecolor=color_y_1_0)
            dot_0 = plt.Circle((x, y), 0.5, fill=True, edgecolor=color_y_1, facecolor=color_y_1_0)
        else:
            small_circle = plt.Circle((x, y), r, fill=False, linestyle="--", color=color_y_2)
            small_circle_0 = plt.Circle((x, y), r_0, fill=True, edgecolor=color_y_2, facecolor=color_f)
            dot_0 = plt.Circle((x, y), 0.5, fill=True, edgecolor=color_y_2, facecolor=color_y_2)
        ax.add_artist(small_circle)
        ax.add_artist(small_circle_0)
        ax.add_artist(dot_0)
    # Рисуем большую окружность
    big_circle = plt.Circle((0, 0), R_k, fill=False, color=color_g)
    ax.add_artist(big_circle)

    ax.tick_params(axis='x', colors='white', labelsize=14)
    ax.tick_params(axis='y', colors='white', labelsize=14)
    ax.grid(True, color='white', linestyle='--', linewidth=0.1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.title.set_color('white')
    fig.patch.set_facecolor('#242424')  # 171717
    fig.subplots_adjust(left=0.07, bottom=0.05, right=0.98, top=0.98)
    # Установите форматирование для осей X и Y
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    # Обновите параметры тиков после изменения меток, если нужно
    ax.tick_params(axis='x', colors='white', labelsize=15)  # Используйте свой размер шрифта
    ax.tick_params(axis='y', colors='white', labelsize=15)  # Используйте свой размер шрифта
    ax.set_xlim(-R_k - H, R_k + H)
    ax.set_ylim(-R_k - H, R_k + H)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=760, y=70)

    return r_0*2, d_wall-delta
def chess_scheme(D_k, H,delta_wall,delta,frame,number):
    number_0=number
    color_g='#D44B46'
    color_o='white'
    color_y_1='#D44B46'
    color_f='#242424'
    if number_0==13:
        color_y_1=color_g
        color_y_1_1 = color_f
        color_y_2=color_g
        color_y_2_1 = color_f
    if number_0==10:
        color_y_1 = color_g
        color_y_1_1 = color_g
        color_y_2 = color_o
        color_y_2_1 = color_f
    fig = Figure(figsize=(7.7, 7.7), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('#242424')  # 171717

    R_k = D_k / 2  # радиус камеры сгорания
    r = H / 2  # Половина шага
    r_0 = r - (delta*0.5)
    centers = []  # Сюда будут записываться координаты форсунок

    # Границы сетки, чтобы покрыть всю большую окружность
    max_index = int((R_k-delta_wall) // H) + 1
    # Сетка
    for i in range(-max_index, max_index + 1):
        for j in range(-max_index, max_index + 1):
            x = i * H
            y = j * H
            # Проверяем, что окружность не выходит за границы
            if np.sqrt(x ** 2 + y ** 2) + r <= (R_k-delta_wall):
                centers.append((x, y))

    # Рисуем большую окружность
    big_circle = plt.Circle((0, 0), R_k, fill=False, color=color_g)
    ax.add_artist(big_circle)

    # Рисуем маленькие окружности
    for (x, y) in centers:
        if (int((x / H) + (y / H)) % 2) == 0:
            color = color_y_1 # Цвет окислительных форсунок, если они однокомпонентные (white)
            color_1=color_y_1_1
        else:
            color = color_y_2
            color_1=color_y_2_1
        small_circle = plt.Circle((x, y), r, fill=False, linestyle="--", color=color)
        small_circle_0 = plt.Circle((x, y), r_0, fill=True, edgecolor=color, facecolor=color_1)
        dot_0 = plt.Circle((x, y), 0.5, fill=True, edgecolor=color, facecolor=color_1)
        ax.add_artist(small_circle)
        ax.add_artist(small_circle_0)
        ax.add_artist(dot_0)

    ax.tick_params(axis='x', colors='white', labelsize=14)
    ax.tick_params(axis='y', colors='white', labelsize=14)
    ax.grid(True, color='white', linestyle='--', linewidth=0.1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.title.set_color('white')
    fig.patch.set_facecolor('#242424')  # 171717
    fig.subplots_adjust(left=0.07, bottom=0.05, right=0.98, top=0.98)
    # Установите форматирование для осей X и Y
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    # Обновите параметры тиков после изменения меток, если нужно
    ax.tick_params(axis='x', colors='white', labelsize=15)  # Используйте свой размер шрифта
    ax.tick_params(axis='y', colors='white', labelsize=15)  # Используйте свой размер шрифта
    ax.set_xlim(-R_k - H, R_k + H)
    ax.set_ylim(-R_k - H, R_k + H)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=760, y=70)

    return r_0*2
def cellular_scheme(D_k, H,delta_wall,delta,frame,number):
    number_0=number
    color_g='#D44B46'
    color_o='white'
    color_f='#242424'
    if number_0==14:
        color_y_1 = color_g
        color_y_2 = color_g
        color_y_1_0 = color_f
    if number_0==11:
        color_y_1 = color_g
        color_y_2 = color_o
        color_y_1_0 = color_g
    fig = Figure(figsize=(7.7, 7.7), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('#242424')  # 171717

    R_k = D_k / 2  # радиус камеры сгорания
    r = H / 2  # Половина шага
    r_0 = r - (delta*0.5)
    sin_60 = np.sin(np.radians(60))


    n_1 = int((R_k - delta_wall-r) // H)
    n_2 = int((R_k -delta_wall- r) // (H * np.sin(np.radians(60))))
    circle_0 = plt.Circle((0, 0), R_k, edgecolor=color_g, facecolor='#242424')
    ax.add_patch(circle_0)

    for i in range(-n_1, n_1 + 1):
        for j in range(-n_2, n_2 + 1):
            if j % 2 == 0:
                x = i * H
                y = j * H * sin_60
            else:
                x = i * H + r
                y = j * H * sin_60
            if np.sqrt(x ** 2 + y ** 2) + r <= R_k-delta_wall:
                if (abs(i)) % 3 == 0 and j % 2 == 0:
                    small_circle = plt.Circle((x, y), H / 2, fill=False, edgecolor=color_y_1, linestyle="--")
                    small_circle_0 = plt.Circle((x, y), r_0, fill=True, edgecolor=color_y_1, facecolor=color_y_1_0)
                    dot_0 = plt.Circle((x, y), 0.5, fill=True, color=color_y_1)
                    ax.add_patch(small_circle)
                    ax.add_patch(small_circle_0)
                    ax.add_patch(dot_0)
                elif ((i)) % 3 == 1 and j % 2 == 1:
                    small_circle = plt.Circle((x, y), H / 2, fill=False, edgecolor=color_y_1, linestyle="--")
                    small_circle_0 = plt.Circle((x, y), r_0, fill=True, edgecolor=color_y_1, facecolor=color_y_1_0)
                    dot_0 = plt.Circle((x, y), 0.5, fill=True, color=color_y_1)
                    ax.add_patch(small_circle)
                    ax.add_patch(small_circle_0)
                    ax.add_patch(dot_0)
                else:
                    small_circle = plt.Circle((x, y), H / 2, fill=False, edgecolor=color_y_2, linestyle="--")
                    small_circle_0 = plt.Circle((x, y), r_0, fill=True, edgecolor=color_y_2, facecolor=color_f)
                    dot_0 = plt.Circle((x, y), 0.5, fill=True, color=color_y_2)
                    ax.add_patch(small_circle)
                    ax.add_patch(small_circle_0)
                    ax.add_patch(dot_0)

    ax.tick_params(axis='x', colors='white', labelsize=14)
    ax.tick_params(axis='y', colors='white', labelsize=14)
    ax.grid(True, color='white', linestyle='--', linewidth=0.1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.title.set_color('white')
    fig.patch.set_facecolor('#242424')  # 171717
    fig.subplots_adjust(left=0.07, bottom=0.05, right=0.98, top=0.98)
    # Установите форматирование для осей X и Y
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    # Обновите параметры тиков после изменения меток, если нужно
    ax.tick_params(axis='x', colors='white', labelsize=15)  # Используйте свой размер шрифта
    ax.tick_params(axis='y', colors='white', labelsize=15)  # Используйте свой размер шрифта
    ax.set_xlim(-R_k - H, R_k + H)
    ax.set_ylim(-R_k - H, R_k + H)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=760, y=70)

    return r_0*2
def concentric_scheme(D_k, H,delta_wall,delta,frame,number):
    number_0=number
    color_g='#D44B46'
    color_o='white'
    color_f='#242424'
    if number_0==15:
        color_pr = color_g
        color_pr_1 = color_f
        color_y_1 = color_g
        color_y_2 = color_g
        color_y_1_0 = color_f
    if number_0==12:
        color_pr = color_g
        color_pr_1 = color_g
        color_y_1 = color_g
        color_y_2 = color_o
        color_y_1_0 = color_g
    fig = Figure(figsize=(7.7, 7.7), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('#242424')  # 171717

    R_k = D_k / 2  # радиус камеры сгорания
    r = H / 2  # Половина шага
    r_0 = r - (delta*0.5)
    sin_60 = np.sin(np.radians(60))
    centers = []  # Сюда будут записываться координаты форсунок

    # Границы сетки, чтобы покрыть всю большую окружность
    max_index = int((R_k  - delta_wall ) // H) + 1
    x = 0
    y = 0
    small_circle = plt.Circle((x, y), r, fill=False, linestyle="--", color=color_y_1)
    small_circle_0 = plt.Circle((x, y), r_0, fill=True, edgecolor=color_y_1, facecolor=color_y_1_0)
    dot_0 = plt.Circle((x, y), 0.5, fill=True, edgecolor=color_y_1, facecolor=color_y_1_0)
    ax.add_artist(small_circle)
    ax.add_artist(small_circle_0)
    ax.add_artist(dot_0)
    for k in range(0, max_index + 1):
        theta = np.linspace(0, 2 * np.pi, 6 * k, endpoint=False)
        for angle in theta:
            x = (k * H) * np.cos(angle)
            y = (k * H) * np.sin(angle)
            if np.sqrt(x ** 2 + y ** 2) + r <= (R_k  - delta_wall):
                centers.append((x, y,k))
    for (x, y,k) in centers:
        if k % 2 == 0:
            small_circle = plt.Circle((x, y), r, fill=False, linestyle="--", color=color_y_1)
            small_circle_0 = plt.Circle((x, y), r_0, fill=True, edgecolor=color_y_1, facecolor=color_y_1_0)
            dot_0 = plt.Circle((x, y), 0.5, fill=True, edgecolor=color_y_1, facecolor=color_y_1_0)
        else:
            small_circle = plt.Circle((x, y), r, fill=False, linestyle="--", color=color_y_2)
            small_circle_0 = plt.Circle((x, y), r_0, fill=True, edgecolor=color_y_2, facecolor=color_f)
            dot_0 = plt.Circle((x, y), 0.5, fill=True, edgecolor=color_y_2, facecolor=color_y_2)
        ax.add_artist(small_circle)
        ax.add_artist(small_circle_0)
        ax.add_artist(dot_0)
    # Рисуем большую окружность
    big_circle = plt.Circle((0, 0), R_k, fill=False, color=color_g)
    ax.add_artist(big_circle)

    ax.tick_params(axis='x', colors='white', labelsize=14)
    ax.tick_params(axis='y', colors='white', labelsize=14)
    ax.grid(True, color='white', linestyle='--', linewidth=0.1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.title.set_color('white')
    fig.patch.set_facecolor('#242424')  # 171717
    fig.subplots_adjust(left=0.07, bottom=0.05, right=0.98, top=0.98)
    # Установите форматирование для осей X и Y
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    # Обновите параметры тиков после изменения меток, если нужно
    ax.tick_params(axis='x', colors='white', labelsize=15)  # Используйте свой размер шрифта
    ax.tick_params(axis='y', colors='white', labelsize=15)  # Используйте свой размер шрифта
    ax.set_xlim(-R_k - H, R_k + H)
    ax.set_ylim(-R_k - H, R_k + H)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=760, y=70)

    return r_0*2
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
    if choice == 5 or choice == 7 or choice == 9:
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
    return m_f_g_pr,m_f_o_pr,m_f_g_y,m_f_o_y,coord_gor,coord_ok
