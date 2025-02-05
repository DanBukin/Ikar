from Ikar_functions import *
from matplotlib.figure import Figure
import matplotlib.patches as patches
from matplotlib.lines import Line2D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import FuncFormatter
import numpy as np
import math
import os
from scipy.interpolate import griddata
from ctypes import windll
from matplotlib.font_manager import FontProperties
from matplotlib import font_manager


font_path = 'data/ofont.ru_Futura PT.ttf'
font_props = font_manager.FontProperties(fname=font_path)
if os.name == 'nt':
    windll.gdi32.AddFontResourceExW("data/ofont.ru_Futura PT.ttf", 0x10, 0)
else:
    pass
font1 = ("Futura PT Book", 16)
custom_font = FontProperties(fname='data/ofont.ru_Futura PT.ttf', size=16)
formatter = FuncFormatter(lambda x, _: f"{x:.2f}")


def grad_to_rad(grad):
  return grad*math.pi/180
def rad_to_grag(rad):
  return rad*180/math.pi
def chess_scheme_with_a_wall(D_k, H, edge_count,delta_wall,delta,delta_y_pr,frame,number,second_layer):

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
    fig = Figure(figsize=(6, 6), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('#242424')  # 171717

    R_k = D_k / 2  # радиус камеры сгорания
    r = H / 2  # Половина шага
    r_0 = r - (delta*0.5)
    centers = []  # Сюда будут записываться координаты форсунок
    centers_ok=[]
    centers_gor=[]

    alpha = 360 / edge_count
    i = 0
    d_wall = (2 * (D_k / 2 - delta_wall) * np.sin(np.radians(180 / edge_count))) / (
                1 + np.sin(np.radians(180 / edge_count)))

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
    fig.subplots_adjust(left=0.15, bottom=0.05, right=0.98, top=0.98)
    # Установите форматирование для осей X и Y
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)

    # Обновите параметры тиков после изменения меток, если нужно
    ax.tick_params(axis='x', colors='white', labelsize=12)  # Используйте свой размер шрифта
    ax.tick_params(axis='y', colors='white', labelsize=12)  # Используйте свой размер шрифта
    ax.set_xlim(-R_k - H, R_k + H)
    ax.set_ylim(-R_k - H, R_k + H)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=650, y=70)

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

    fig = Figure(figsize=(6, 6), dpi=100)
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
    fig.subplots_adjust(left=0.15, bottom=0.05, right=0.98, top=0.98)
    # Установите форматирование для осей X и Y
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    # Обновите параметры тиков после изменения меток, если нужно
    ax.tick_params(axis='x', colors='white', labelsize=12)  # Используйте свой размер шрифта
    ax.tick_params(axis='y', colors='white', labelsize=12)  # Используйте свой размер шрифта
    ax.set_xlim(-R_k - H, R_k + H)
    ax.set_ylim(-R_k - H, R_k + H)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=650, y=70)

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
    fig = Figure(figsize=(6, 6), dpi=100)
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
    fig.subplots_adjust(left=0.15, bottom=0.05, right=0.98, top=0.98)
    # Установите форматирование для осей X и Y
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    # Обновите параметры тиков после изменения меток, если нужно
    ax.tick_params(axis='x', colors='white', labelsize=12)  # Используйте свой размер шрифта
    ax.tick_params(axis='y', colors='white', labelsize=12)  # Используйте свой размер шрифта
    ax.set_xlim(-R_k - H, R_k + H)
    ax.set_ylim(-R_k - H, R_k + H)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=650, y=70)

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
    fig = Figure(figsize=(6, 6), dpi=100)
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
    fig.subplots_adjust(left=0.15, bottom=0.05, right=0.98, top=0.98)
    # Установите форматирование для осей X и Y
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    # Обновите параметры тиков после изменения меток, если нужно
    ax.tick_params(axis='x', colors='white', labelsize=12)  # Используйте свой размер шрифта
    ax.tick_params(axis='y', colors='white', labelsize=12)  # Используйте свой размер шрифта
    ax.set_xlim(-R_k - H, R_k + H)
    ax.set_ylim(-R_k - H, R_k + H)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=650, y=70)

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
    fig = Figure(figsize=(6, 6), dpi=100)
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
    fig.subplots_adjust(left=0.15, bottom=0.05, right=0.98, top=0.98)
    # Установите форматирование для осей X и Y
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    # Обновите параметры тиков после изменения меток, если нужно
    ax.tick_params(axis='x', colors='white', labelsize=12)  # Используйте свой размер шрифта
    ax.tick_params(axis='y', colors='white', labelsize=12)  # Используйте свой размер шрифта
    ax.set_xlim(-R_k - H, R_k + H)
    ax.set_ylim(-R_k - H, R_k + H)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=650, y=70)

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
    fig = Figure(figsize=(6, 6), dpi=100)
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
    fig.subplots_adjust(left=0.15, bottom=0.05, right=0.98, top=0.98)
    # Установите форматирование для осей X и Y
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    # Обновите параметры тиков после изменения меток, если нужно
    ax.tick_params(axis='x', colors='white', labelsize=12)  # Используйте свой размер шрифта
    ax.tick_params(axis='y', colors='white', labelsize=12)  # Используйте свой размер шрифта
    ax.set_xlim(-R_k - H, R_k + H)
    ax.set_ylim(-R_k - H, R_k + H)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=650, y=70)

    return r_0*2

def print_dot(coord,D_k,frame, H,n):
    fig = Figure(figsize=(6, 6), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('#1A1A1A')  # 171717

    arc = patches.Arc((0, 0), D_k, D_k, theta1=0, theta2=90, edgecolor='#D44B46', facecolor='#1A1A1A')
    ax.add_patch(arc)
    line = Line2D([0, 0, D_k / 2], [D_k / 2, 0, 0], color="#D44B46")
    ax.add_line(line)
    k=0
    centers_square=[]
    angles_square=[]
    for i, (x, y) in enumerate(coord):
        circle_1 = plt.Circle((x, y), 1, edgecolor='#D44B46', facecolor='#D44B46')
        ax.add_patch(circle_1)
        if i % n == 0:
            if x >= 0 and y >= 0:
                if math.sqrt((abs(x) + H / (2 ** 0.5)) ** 2 + (abs(y) + H / (2 ** 0.5)) ** 2) <= D_k / 2:
                    square = patches.Polygon([[x + H / 2, y + H / 2], [x + H / 2, y - H / 2],[x - H / 2, y - H / 2], [x - H / 2, y + H / 2]],edgecolor='#D44B46', facecolor='none', hatch='x')
                    ax.add_patch(square)
                    centers_square.append([x, y])
                    k += 1
                    angles_square.append(361)
                else:
                    angle = np.arctan2(y, x)
                    square_vertices = rotated_square(x, y, H, angle)
                    square = patches.Polygon(square_vertices, edgecolor='#D44B46', facecolor='none', hatch='x')
                    ax.add_patch(square)
                    centers_square.append([x, y])
                    k += 1
                    angles_square.append(np.rad2deg(angle))

    ax.tick_params(axis='x', colors='white', labelsize=14)
    ax.tick_params(axis='y', colors='white', labelsize=14)
    ax.grid(True, color='white', linestyle='--', linewidth=0.1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.title.set_color('white')
    fig.patch.set_facecolor('#1A1A1A')  # 171717
    fig.subplots_adjust(left=0.15, bottom=0.05, right=0.98, top=0.98)
    # Установите форматирование для осей X и Y
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    # Обновите параметры тиков после изменения меток, если нужно
    ax.tick_params(axis='x', colors='white', labelsize=12)  # Используйте свой размер шрифта
    ax.tick_params(axis='y', colors='white', labelsize=12)  # Используйте свой размер шрифта
    ax.set_xlim(- H, D_k / 2 + H)
    ax.set_ylim(- H, D_k / 2 + H)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=10, y=50)
    print(f'Количество площадок для расчёта равно: {k}')
    return k,centers_square,angles_square

def draw_circle_with_points(center_x, center_y, points_itog, H,D,frame,k):
    fig = Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('#131212')

    circle = plt.Circle((0, 0), D / 2, color='#D44B46', fill=False)
    ax.add_patch(circle)
    circle = plt.Circle((center_x, center_y), 3 * H, color='white', fill=False)
    ax.add_patch(circle)

    if math.sqrt((abs(center_x) + H / (2 ** 0.5)) ** 2 + (abs(center_y) + H / (2 ** 0.5)) ** 2) <= D / 2:
        square = patches.Polygon([[center_x + H / 2, center_y + H / 2], [center_x + H / 2, center_y - H / 2],[center_x - H / 2, center_y - H / 2], [center_x - H / 2, center_y + H / 2]],edgecolor='#D44B46', facecolor='none', hatch='x')
        ax.add_patch(square)
    else:
        angle = np.arctan2(center_y, center_x)
        square_vertices = rotated_square(center_x, center_y, H, angle)
        square = patches.Polygon(square_vertices, edgecolor='#D44B46', facecolor='none', hatch='x')
        ax.add_patch(square)
    for (x, y) in points_itog:
        if is_point_in_circle(x, y, center_x, center_y, H):
            circle = plt.Circle((x, y), 1, color='#D44B46', fill=True)
            ax.add_patch(circle)

    # Настройки графика
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim((center_x - (3 * H)) - 10, (center_x + (3 * H)) + 10)
    ax.set_ylim((center_y - (3 * H)) - 10, (center_y + (3 * H)) + 10)
    ax.tick_params(axis='x', colors='white', labelsize=10)
    ax.tick_params(axis='y', colors='white', labelsize=10)
    ax.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.title.set_color('white')
    fig.patch.set_facecolor('#131212')
    ax.set_facecolor('#131212')
    fig.subplots_adjust(left=0.07, bottom=0.05, right=0.98, top=0.98)
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.tick_params(axis='x', colors='white', labelsize=11)
    ax.tick_params(axis='y', colors='white', labelsize=11)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=10, y=560*k+10)
def rotated_square(x, y, H, angle):
    '''=====Функция, которая разворачивает площадки, находящиеся у пристенка====='''
    # Центр квадрата (x, y), угол наклона angle (в радианах)
    half_side = H / 2
    # Вершины квадрата без поворота
    vertices = np.array([
        [-half_side, -half_side],
        [half_side, -half_side],
        [half_side, half_side],
        [-half_side, half_side]
    ])

    # Поворот вершин на угол
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])

    rotated_vertices = vertices @ rotation_matrix.T
    # Смещаем вершины квадрата к точке (x, y)
    rotated_vertices += np.array([x, y])

    return rotated_vertices

def is_point_in_circle(x0, y0, x, y, H):
    '''=====Функция для проверки, находится ли точка в окружности====='''
    radius = 3.0001 * H
    distance = math.sqrt((x0 - x) ** 2 + (y0 - y) ** 2)
    return distance <= radius
def save_png_fors(center_x, center_y, points_itog, H,D):
    print(center_x, center_y)
    fig, ax = plt.subplots(figsize=(8, 8))


    circle = plt.Circle((0, 0), D / 2, color='black', fill=False)
    ax.add_patch(circle)
    circle = plt.Circle((center_x, center_y), 3 * H, color='black', fill=False)
    ax.add_patch(circle)

    if math.sqrt((abs(center_x) + H / (2 ** 0.5)) ** 2 + (abs(center_y) + H / (2 ** 0.5)) ** 2) <= D / 2:
        square = patches.Polygon([[center_x + H / 2, center_y + H / 2], [center_x + H / 2, center_y - H / 2],
                                  [center_x - H / 2, center_y - H / 2], [center_x - H / 2, center_y + H / 2]],
                                 edgecolor='black', facecolor='none', hatch='x')
        ax.add_patch(square)
    else:
        angle = np.arctan2(center_y, center_x)
        square_vertices = rotated_square(center_x, center_y, H, angle)
        square = patches.Polygon(square_vertices, edgecolor='black', facecolor='none', hatch='x')
        ax.add_patch(square)
    for (x, y) in points_itog:
        if is_point_in_circle(x, y, center_x, center_y, H):
            circle = plt.Circle((x, y), 1, color='black', fill=True)
            ax.add_patch(circle)

    # Настройки графика
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim((center_x - (3 * H)) - 10, (center_x + (3 * H)) + 10)
    ax.set_ylim((center_y - (3 * H)) - 10, (center_y + (3 * H)) + 10)
    ax.tick_params(axis='x', colors='black', labelsize=10)
    ax.tick_params(axis='y', colors='black', labelsize=10)
    ax.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.title.set_color('black')
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    fig.subplots_adjust(left=0.07, bottom=0.05, right=0.98, top=0.98)
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.tick_params(axis='x', colors='black', labelsize=11)
    ax.tick_params(axis='y', colors='black', labelsize=11)

    plt.show()
def multiply_graph(data_1):
    result = []
    data = np.array(data_1)
    for point in data:
        x, y, z = point
        result.append((x, y, z))
        result.append((-x, y, z))
        result.append((x, -y, z))
        result.append((-x, -y, z))
    result = list(set(result))
    result = np.array(result)
    return result
def points_near_line(points, P1, P2, tolerance=0.1):
    x1, y1 = P1
    x2, y2 = P2
    # Извлечение координат x, y, z из точек
    x0 = points[:, 0]  # x координаты
    y0 = points[:, 1]  # y координаты
    z0 = points[:, 2]  # z координаты (будем их сохранять в выводе)
    # Формула для расстояния до прямой, только по x и y
    numerator = np.abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    denominator = np.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    distances = numerator / denominator
    # Фильтрация точек, которые находятся ближе к прямой чем tolerance
    close_points_mask = distances <= tolerance
    close_points = points[close_points_mask]
    return close_points
def points_near_arc(points, R, tolerance=0.1):

    # Извлечение координат x, y
    x = points[:, 0]
    y = points[:, 1]
    # Рассчитываем углы для каждой точки в градусах
    angles = np.degrees(np.arctan2(y, x))
    # Рассчитываем расстояния каждой точки от центра
    distances = np.sqrt(x ** 2 + y ** 2)
    # Определяем маску для точек, которые находятся в пределах углов 0° и 90°
    angle_mask = (angles >= 0) & (angles <= 90)
    # Определяем маску для точек, которые близки к радиусу дуги с заданной точностью
    distance_mask = np.abs(distances - R) <= tolerance
    # Применяем обе маски к массиву точек
    arc_points_mask = angle_mask & distance_mask
    # Возвращаем точки, которые удовлетворяют обоим условиям
    close_points = points[arc_points_mask]
    return close_points
def three_d_graph(data_1,frame,D):
    array=multiply_graph(data_1)
    x = array[:, 0]  # Координаты X
    y = array[:, 1]  # Координаты Y
    z = array[:, 2]  # km в точках

    # Создаем сетку для интерполяции
    grid_x, grid_y = np.mgrid[min(x):max(x):100j, min(y):max(y):100j]

    # Интерполяция km по сетке
    grid_z = griddata((x, y), z, (grid_x, grid_y), method='cubic')
    # Построение графика
    fig = plt.figure(figsize=(8, 20))
    ax = fig.add_subplot(311, projection='3d')

    # Построение поверхности
    surf=ax.plot_surface(grid_x, grid_y, grid_z, cmap='hot', linewidth=0.5, edgecolors='k') #autumn_r
    ax.set_title("Распределение km по смесительной головке", fontproperties=custom_font)
    ax.title.set_color('white')
    fig.patch.set_facecolor('#171717')
    ax.set_facecolor('#171717')

    fig.subplots_adjust(left=0.1, bottom=0.03, right=0.98, top=0.98)
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.set_xlim(min(x)*1.1, max(x)*1.1)
    ax.set_ylim(min(y) * 1.1, max(y) * 1.1)
    ax.set_zlim(0, max(z) * 1.1)
    ax.grid(True, color='white', linestyle='--', linewidth=1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.set_xlabel('x, мм', color='white')  # Устанавливаем цвет текста меток осей
    ax.set_ylabel('y, мм', color='white')
    ax.set_zlabel('k_m', color='white')
    # Установите форматирование для осей X и Y
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.zaxis.set_major_formatter(formatter)
    # Получите текущие метки и примените к ним новые настройки шрифта
    ax.set_xticklabels([f"{x:.0f}" for x in ax.get_xticks()], fontproperties=font_props)
    ax.set_yticklabels([f"{x:.0f}" for x in ax.get_yticks()], fontproperties=font_props)
    ax.set_zticklabels([f"{x:.0f}" for x in ax.get_zticks()], fontproperties=font_props)
    # Обновите параметры тиков после изменения меток, если нужно
    ax.tick_params(axis='x', colors='white', labelsize=14)  # Используйте свой размер шрифта
    ax.tick_params(axis='y', colors='white', labelsize=14)  # Используйте свой размер шрифта
    ax.tick_params(axis='z', colors='white', labelsize=14)  # Используйте свой размер шрифта

    colorbar = fig.colorbar(surf, shrink=0.5, aspect=5)
    colorbar.outline.set_edgecolor('white')  # Устанавливаем цвет рамки
    colorbar.ax.tick_params(color='white', labelcolor='white')  # Устанавливаем цвет меток и текста

    array_radius_0=points_near_line(array, [-D/2, 0], [D/2, 0], tolerance=0.1)
    array_radius = array_radius_0[np.argsort(array_radius_0[:, 0])]
    x_1 = array_radius[:, 0]  # Координаты X
    z_1 = array_radius[:, 2]  # km в точках

    ax_1 = fig.add_subplot(312)
    ax_1.plot(x_1, z_1,color='#D44B46')
    ax_1.tick_params(axis='x', colors='white', labelsize=14, labelcolor='white')  # Добавляем labelcolor='white'
    ax_1.tick_params(axis='y', colors='white', labelsize=14, labelcolor='white')
    ax_1.set_xlabel('X, мм', color='white')
    ax_1.set_ylabel('k_m', color='white')
    # Установите форматирование для осей X и Y
    ax_1.xaxis.set_major_formatter(formatter)
    ax_1.yaxis.set_major_formatter(formatter)
    # Получите текущие метки и примените к ним новые настройки шрифта
    ax_1.set_xticklabels([f"{x:.0f}" for x in ax_1.get_xticks()], fontproperties=font_props)
    ax_1.set_yticklabels([f"{x:.2f}" for x in ax_1.get_yticks()], fontproperties=font_props)
    # Обновите параметры тиков после изменения меток, если нужно
    ax_1.tick_params(axis='x', colors='white', labelsize=14)  # Используйте свой размер шрифта
    ax_1.tick_params(axis='y', colors='white', labelsize=14)  # Используйте свой размер шрифта
    ax_1.set_facecolor('#171717')
    ax_1.grid(True, color='white', linestyle='--', linewidth=1)
    ax_1.grid(which='major', color='gray', linestyle='--', linewidth=1)
    ax_1.grid(which='minor', color='gray', linestyle='--', linewidth=1)
    ax_1.set_title("Распределение km по радиусу", fontproperties=custom_font, color='white')

    distances = np.sqrt(array[:, 0] ** 2 + array[:, 1] ** 2)
    max_index = np.argmax(distances)
    R=distances[max_index]
    array_angle_0=points_near_arc(array, R, tolerance=0.5)
    array_angle = array_angle_0[np.argsort(array_angle_0[:, 0])]
    angles = np.degrees(np.arctan2(array_angle[:, 1], array_angle[:, 0]))
    points_with_angles = np.column_stack((array_angle, angles))
    x_2 = points_with_angles[:, 3]  # Координаты X
    y_2 = points_with_angles[:, 2]  # km в точках
    ax_2 = fig.add_subplot(313)
    ax_2.plot(x_2, y_2,color='#D44B46')
    ax_2.tick_params(axis='x', colors='white', labelsize=11, labelcolor='white')  # Добавляем labelcolor='white'
    ax_2.tick_params(axis='y', colors='white', labelsize=11, labelcolor='white')
    ax_2.set_xlabel('Угол,°', color='white')
    ax_2.set_ylabel('k_m', color='white')
    ax_2.grid(True, color='white', linestyle='--', linewidth=1)
    ax_2.grid(which='major', color='gray', linestyle='--', linewidth=1)
    ax_2.grid(which='minor', color='gray', linestyle='--', linewidth=1)
    # Установите форматирование для осей X и Y
    ax_2.xaxis.set_major_formatter(formatter)
    ax_2.yaxis.set_major_formatter(formatter)
    # Получите текущие метки и примените к ним новые настройки шрифта
    ax_2.set_xticklabels([f"{x:.0f}" for x in ax_2.get_xticks()], fontproperties=font_props)
    ax_2.set_yticklabels([f"{x:.3f}" for x in ax_2.get_yticks()], fontproperties=font_props)
    # Обновите параметры тиков после изменения меток, если нужно
    ax_2.tick_params(axis='x', colors='white', labelsize=14)  # Используйте свой размер шрифта
    ax_2.tick_params(axis='y', colors='white', labelsize=14)  # Используйте свой размер шрифта
    ax_2.set_facecolor('#171717')
    ax_2.set_title("Распределение km по углу", fontproperties=custom_font, color='white')


    # Отображение графиков в Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=2, y=2)
def three_d_graph_T(data_1,frame,D):
    array=multiply_graph(data_1)
    x = array[:, 0]  # Координаты X
    y = array[:, 1]  # Координаты Y
    z = array[:, 2]  # km в точках

    # Создаем сетку для интерполяции
    grid_x, grid_y = np.mgrid[min(x):max(x):100j, min(y):max(y):100j]

    # Интерполяция km по сетке
    grid_z = griddata((x, y), z, (grid_x, grid_y), method='cubic')
    # Построение графика
    fig = plt.figure(figsize=(8, 20))
    ax = fig.add_subplot(311, projection='3d')

    # Построение поверхности
    surf=ax.plot_surface(grid_x, grid_y, grid_z, cmap='hot', linewidth=0.5, edgecolors='k') #autumn_r
    ax.set_title("Распределение Температуры по смесительной головке", fontproperties=custom_font)
    ax.title.set_color('white')
    fig.patch.set_facecolor('#171717')
    ax.set_facecolor('#171717')

    fig.subplots_adjust(left=0.1, bottom=0.03, right=0.98, top=0.98)
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.set_xlim(min(x)*1.1, max(x)*1.1)
    ax.set_ylim(min(y) * 1.1, max(y) * 1.1)
    ax.set_zlim(0, max(z) * 1.1)
    ax.grid(True, color='white', linestyle='--', linewidth=1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.set_xlabel('x, мм', color='white')  # Устанавливаем цвет текста меток осей
    ax.set_ylabel('y, мм', color='white')
    ax.set_zlabel('T,K', color='white')
    # Установите форматирование для осей X и Y
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.zaxis.set_major_formatter(formatter)
    # Получите текущие метки и примените к ним новые настройки шрифта
    ax.set_xticklabels([f"{x:.0f}" for x in ax.get_xticks()], fontproperties=font_props)
    ax.set_yticklabels([f"{x:.0f}" for x in ax.get_yticks()], fontproperties=font_props)
    ax.set_zticklabels([f"{x:.0f}" for x in ax.get_zticks()], fontproperties=font_props)
    # Обновите параметры тиков после изменения меток, если нужно
    ax.tick_params(axis='x', colors='white', labelsize=14)  # Используйте свой размер шрифта
    ax.tick_params(axis='y', colors='white', labelsize=14)  # Используйте свой размер шрифта
    ax.tick_params(axis='z', colors='white', labelsize=14)  # Используйте свой размер шрифта

    colorbar = fig.colorbar(surf, shrink=0.5, aspect=5)
    colorbar.outline.set_edgecolor('white')  # Устанавливаем цвет рамки
    colorbar.ax.tick_params(color='white', labelcolor='white')  # Устанавливаем цвет меток и текста

    array_radius_0=points_near_line(array, [-D/2, 0], [D/2, 0], tolerance=0.1)
    array_radius = array_radius_0[np.argsort(array_radius_0[:, 0])]
    x_1 = array_radius[:, 0]  # Координаты X
    z_1 = array_radius[:, 2]  # km в точках

    ax_1 = fig.add_subplot(312)
    ax_1.plot(x_1, z_1,color='#D44B46')
    ax_1.tick_params(axis='x', colors='white', labelsize=14, labelcolor='white')  # Добавляем labelcolor='white'
    ax_1.tick_params(axis='y', colors='white', labelsize=14, labelcolor='white')
    ax_1.set_xlabel('X, мм', color='white')
    ax_1.set_ylabel('T,K', color='white')
    # Установите форматирование для осей X и Y
    ax_1.xaxis.set_major_formatter(formatter)
    ax_1.yaxis.set_major_formatter(formatter)
    # Получите текущие метки и примените к ним новые настройки шрифта
    ax_1.set_xticklabels([f"{x:.0f}" for x in ax_1.get_xticks()], fontproperties=font_props)
    ax_1.set_yticklabels([f"{x:.0f}" for x in ax_1.get_yticks()], fontproperties=font_props)
    # Обновите параметры тиков после изменения меток, если нужно
    ax_1.tick_params(axis='x', colors='white', labelsize=14)  # Используйте свой размер шрифта
    ax_1.tick_params(axis='y', colors='white', labelsize=14)  # Используйте свой размер шрифта
    ax_1.set_facecolor('#171717')
    ax_1.grid(True, color='white', linestyle='--', linewidth=1)
    ax_1.grid(which='major', color='gray', linestyle='--', linewidth=1)
    ax_1.grid(which='minor', color='gray', linestyle='--', linewidth=1)
    ax_1.set_title("Распределение Температуры по радиусу", fontproperties=custom_font, color='white')

    distances = np.sqrt(array[:, 0] ** 2 + array[:, 1] ** 2)
    max_index = np.argmax(distances)
    R=distances[max_index]
    array_angle_0=points_near_arc(array, R, tolerance=0.5)
    array_angle = array_angle_0[np.argsort(array_angle_0[:, 0])]
    angles = np.degrees(np.arctan2(array_angle[:, 1], array_angle[:, 0]))
    points_with_angles = np.column_stack((array_angle, angles))
    x_2 = points_with_angles[:, 3]  # Координаты X
    y_2 = points_with_angles[:, 2]  # km в точках
    ax_2 = fig.add_subplot(313)
    ax_2.plot(x_2, y_2,color='#D44B46')
    ax_2.tick_params(axis='x', colors='white', labelsize=11, labelcolor='white')  # Добавляем labelcolor='white'
    ax_2.tick_params(axis='y', colors='white', labelsize=11, labelcolor='white')
    ax_2.set_xlabel('Угол,°', color='white')
    ax_2.set_ylabel('T,K', color='white')
    ax_2.grid(True, color='white', linestyle='--', linewidth=1)
    ax_2.grid(which='major', color='gray', linestyle='--', linewidth=1)
    ax_2.grid(which='minor', color='gray', linestyle='--', linewidth=1)
    # Установите форматирование для осей X и Y
    ax_2.xaxis.set_major_formatter(formatter)
    ax_2.yaxis.set_major_formatter(formatter)
    # Получите текущие метки и примените к ним новые настройки шрифта
    ax_2.set_xticklabels([f"{x:.0f}" for x in ax_2.get_xticks()], fontproperties=font_props)
    ax_2.set_yticklabels([f"{x:.0f}" for x in ax_2.get_yticks()], fontproperties=font_props)
    # Обновите параметры тиков после изменения меток, если нужно
    ax_2.tick_params(axis='x', colors='white', labelsize=14)  # Используйте свой размер шрифта
    ax_2.tick_params(axis='y', colors='white', labelsize=14)  # Используйте свой размер шрифта
    ax_2.set_facecolor('#171717')
    ax_2.set_title("Распределение температуры по углу", fontproperties=custom_font, color='white')


    # Отображение графиков в Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=2, y=2)

def print_nozzle_1(H,d_f,l,d_c,h_og,h_sr,h_ras,frame):
    fig = Figure(figsize=(7, 7), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('#131212')

    ax.plot([-0.5*(d_f),-0.5*(d_c)],[0,0], color="#D44B46")
    ax.plot([-0.5*(d_f),-0.5*(d_c)-1],[l,l], color="#D44B46")

    ax.plot([0.5*(d_c),0.5*(d_f)],[0,0], color="#D44B46")
    ax.plot([0.5*(d_c)+1,0.5*(d_f)],[l,l], color="#D44B46")

    ax.plot([-0.5*(d_f),-0.5*(d_f)],[0,l], color="#D44B46")
    ax.plot([-0.5*(d_c),-0.5*(d_c)],[0,l-1], color="#D44B46")

    ax.plot([0.5*(d_c),0.5*(d_c)],[0,l-1], color="#D44B46")
    ax.plot([0.5*(d_f),0.5*(d_f)],[0,l], color="#D44B46")

    ax.plot([-0.5*(d_c),-0.5*(d_c)-1], [l-1, l], color="#D44B46")
    ax.plot([0.5*(d_c), 0.5*(d_c)+1], [l-1, l], color="#D44B46")

    ax.plot([-0.5*H,-d_f/2],[0,0], color="#D44B46")
    ax.plot([-0.5*H,-d_f/2],[h_og,h_og], color="#D44B46")

    ax.plot([0.5*d_f,H/2],[0,0], color="#D44B46")
    ax.plot([0.5*d_f,H/2],[h_og,h_og], color="#D44B46")

    ax.plot([-0.5*H,-d_f/2],[h_og+h_ras,h_og+h_ras], color="#D44B46")
    ax.plot([-0.5*H,-d_f/2],[h_og+h_ras+h_sr,h_og+h_ras+h_sr], color="#D44B46")

    ax.plot([0.5*d_f,H/2],[h_og+h_ras,h_og+h_ras], color="#D44B46")
    ax.plot([0.5*d_f,H/2],[h_og+h_ras+h_sr,h_og+h_ras+h_sr], color="#D44B46")

    ax.plot([-0.5 * (d_c), 0.5 * (d_c)], [l - 1, l - 1], color="#D44B46")
    ax.plot([-0.5 * (d_c), 0.5 * (d_c)], [0, 0], color="#D44B46")
    ax.plot([-0.5 * (d_c)-1, 0.5 * (d_c) + 1], [l, l], color="#D44B46")

    ax.plot([0, 0], [-0.5, l+0.5], color="#D44B46",linestyle='-.')

    square = patches.Polygon(
        [[-0.5*(d_f),0 ], [-0.5*(d_f),l], [-0.5*(d_c)-1,l], [-0.5*(d_c),l-1], [-0.5*(d_c),0]],
        edgecolor='#9E3C39', facecolor='none', hatch='/')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5*d_c,0 ], [0.5*d_f,0 ], [0.5*d_f,l], [0.5*d_c+1,l], [0.5*d_c,l-1]],
        edgecolor='#9E3C39', facecolor='none', hatch='/')
    ax.add_patch(square)

    square = patches.Polygon(
        [[-H/2,0 ], [-0.5*d_f, 0], [-0.5*d_f,h_og], [-H/2,h_og ]],
        edgecolor='#9E3C39', facecolor='none', hatch="\\")
    ax.add_patch(square)

    square = patches.Polygon(
        [[-H / 2, h_og+h_ras], [-0.5 * d_f, h_og+h_ras], [-0.5 * d_f, h_og+h_ras+h_sr], [-H / 2, h_og+h_ras+h_sr]],
        edgecolor='#9E3C39', facecolor='none', hatch="\\")
    ax.add_patch(square)

    square = patches.Polygon(
        [[H / 2, 0], [0.5 * d_f, 0], [0.5 * d_f, h_og], [H / 2, h_og]],
        edgecolor='#9E3C39', facecolor='none', hatch="\\")
    ax.add_patch(square)

    square = patches.Polygon(
        [[H / 2, h_og + h_ras], [0.5 * d_f, h_og + h_ras], [0.5 * d_f, h_og + h_ras + h_sr],
         [H / 2, h_og + h_ras + h_sr]],
        edgecolor='#9E3C39', facecolor='none', hatch="\\")
    ax.add_patch(square)

    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-1.1*H/2,1.1*H/2)
    ax.set_ylim(-1, 1.1*l)
    ax.tick_params(axis='x', colors='white', labelsize=10)
    ax.tick_params(axis='y', colors='white', labelsize=10)
    ax.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.title.set_color('white')
    fig.patch.set_facecolor('#131212')
    ax.set_facecolor('#131212')
    fig.subplots_adjust(left=0.07, bottom=0.05, right=0.98, top=0.98)
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.tick_params(axis='x', colors='white', labelsize=11)
    ax.tick_params(axis='y', colors='white', labelsize=11)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=600, y=10)
def print_nozzle_2(H,d_f,d_kz,d_vh,x_st,num_copies,l_kz_otn,phi,d_c_otn,l_c_otn,h_og,h_sr,h_ras,frame):
  beta=math.acos( ((d_kz/2)-(d_vh/2))/((d_kz/2)) )
  l_1=(d_kz/2)*math.sin(beta)
  alpha=math.acos(((d_f/2)-(d_vh/2)-(x_st))/((d_f/2)))
  l_2=(d_f/2)*math.sin(alpha)
  alpha_2=math.acos(((0.5*d_f)-x_st)/(0.5*d_f))
  l_3=(d_f/2)*math.sin(alpha_2)
  alpha_3=math.acos((0.5*d_f-x_st-d_vh)/(0.5*d_f))
  l_4=0.5*d_f*math.sin(alpha_3)
  alpha_4=math.acos((0.5*d_kz-d_vh)/(0.5*d_kz))
  l_5=0.5*d_kz*math.sin(alpha_4)

  d_c=d_c_otn*d_kz
  l_c=d_c*l_c_otn
  h_phi=(d_kz/2-d_c/2)*math.tan(grad_to_rad(phi))
  l_kz=l_kz_otn*d_kz

  fig = Figure(figsize=(6, 15), dpi=100)
  ax = fig.add_subplot(211)
  ax2 = fig.add_subplot(212)
  ax.set_aspect('equal', adjustable='box')
  ax.set_facecolor('#131212')

  circle = plt.Circle((0, 0), d_f / 2, color='#D44B46', fill=False)
  ax.add_patch(circle)

  circle = plt.Circle((0, 0), d_kz / 2, color='#D44B46', fill=False)
  ax.add_patch(circle)

  for i in range(num_copies):
    angle = i* 2 * math.pi/num_copies

    x_1=(d_kz/2)*math.cos(angle+beta)
    y_1=(d_kz/2)*math.sin(angle+beta)

    x_2=(d_f/2)*math.cos(angle+alpha)
    y_2=(d_f/2)*math.sin(angle+alpha)
    ax.plot([x_1,x_2], [y_1,y_2], color="#D44B46",linestyle='-.')


    x_1=(d_kz/2)*math.cos(angle)
    y_1=(d_kz/2)*math.sin(angle)

    x_2=(d_f/2)*math.cos(angle+alpha_2)
    y_2=(d_f/2)*math.sin(angle+alpha_2)
    ax.plot([x_1,x_2], [y_1,y_2], color="#D44B46")

    x_1=(d_f/2)*math.cos(angle+alpha_3)
    y_1=(d_f/2)*math.sin(angle+alpha_3)

    x_2=(d_kz/2)*math.cos(angle+alpha_4)
    y_2=(d_kz/2)*math.sin(angle+alpha_4)
    ax.plot([x_1,x_2], [y_1,y_2], color="#D44B46")

  circle = plt.Circle((0, 0), d_c / 2, color='#D44B46', fill=False)
  ax.add_patch(circle)

  ax.plot([0, 0], [-1.1*d_f/2,1.1*d_f/2], color="#D44B46",linestyle='-.')
  ax.plot([-1.1*d_f/2,1.1*d_f/2], [0, 0], color="#D44B46",linestyle='-.')
  ax.set_xlim(-1.1*H/2,1.1*H/2)
  ax.set_ylim(-1.1*H/2,1.1*H/2)
  ax.tick_params(axis='x', colors='white', labelsize=10)
  ax.tick_params(axis='y', colors='white', labelsize=10)
  ax.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
  ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
  ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
  ax.xaxis.set_minor_locator(AutoMinorLocator())
  ax.yaxis.set_minor_locator(AutoMinorLocator())
  ax.title.set_color('white')
  fig.patch.set_facecolor('#131212')
  ax.set_facecolor('#131212')
  fig.subplots_adjust(left=0.07, bottom=0.05, right=0.98, top=0.98)
  ax.xaxis.set_major_formatter(formatter)
  ax.yaxis.set_major_formatter(formatter)
  ax.tick_params(axis='x', colors='white', labelsize=11)
  ax.tick_params(axis='y', colors='white', labelsize=11)


#------------------------------------------------------------------------------
  ax2.set_aspect('equal', adjustable='box')
  ax2.set_facecolor('#1A1A1A')  # 171717

  ax2.plot([-d_c/2, -d_c/2], [0,l_c], color="#D44B46")
  ax2.plot([d_c/2, d_c/2], [0,l_c], color="#D44B46")
  ax2.plot([d_c/2, d_kz/2], [l_c,l_c+h_phi], color="#D44B46")
  ax2.plot([-d_c/2, -d_kz/2], [l_c,l_c+h_phi], color="#D44B46")
  ax2.plot([-d_kz/2, d_kz/2], [l_c+h_phi,l_c+h_phi], color="#D44B46")
  ax2.plot([-d_c/2, d_c/2], [l_c,l_c], color="#D44B46")
  ax2.plot([d_kz/2, d_kz/2], [l_c+h_phi,l_c+h_phi+l_kz], color="#D44B46")
  ax2.plot([-d_kz/2, -d_kz/2], [l_c+h_phi,l_c+h_phi+l_kz], color="#D44B46")
  ax2.plot([-d_kz/2, d_kz/2], [l_c+h_phi+l_kz,l_c+h_phi+l_kz], color="#D44B46")
  ax2.plot([-d_kz/2-x_st, d_kz/2+x_st], [l_c+h_phi+l_kz+x_st,l_c+h_phi+l_kz+x_st], color="#D44B46")
  ax2.plot([-d_kz/2-x_st, -d_kz/2-x_st], [l_c+h_phi+l_kz+x_st,0], color="#D44B46")
  ax2.plot([d_kz/2+x_st, d_kz/2+x_st], [l_c+h_phi+l_kz+x_st,0], color="#D44B46")
  ax2.plot([-d_kz/2-x_st, -d_c/2], [0,0], color="#D44B46")
  ax2.plot([d_kz/2+x_st, d_c/2], [0,0], color="#D44B46")
  ax2.plot([-d_c/2, d_c/2], [0,0], color="#D44B46")
  square = patches.Polygon(
        [[-d_c/2,0], [-d_kz/2-x_st, 0], [-d_kz/2-x_st,l_c+h_phi+l_kz+x_st ],[d_kz/2+x_st,l_c+h_phi+l_kz+x_st ],[d_kz/2+x_st, 0],[d_c/2,0 ],[d_c/2, l_c],[d_kz/2,l_c+h_phi ],[d_kz/2, l_c+h_phi+l_kz],[-d_kz/2, l_c+h_phi+l_kz],[-d_kz/2,l_c+h_phi ],[-d_c/2, l_c]],
        edgecolor='#9E3C39', facecolor='none', hatch="/")
  ax2.add_patch(square)
  circle = plt.Circle((d_kz/2-d_vh / 2, l_c+h_phi+l_kz-d_vh / 2), d_vh / 2, color='#D44B46', fill=False)
  ax2.add_patch(circle)
  ax2.plot([d_kz/2-d_vh / 2,d_kz/2-d_vh / 2], [l_c+h_phi+l_kz-d_vh / 2+1.3*d_vh / 2,l_c+h_phi+l_kz-d_vh / 2-1.3*d_vh / 2 ], color="#D44B46",linestyle='-.')
  ax2.plot([d_kz/2- d_vh/2 + 1.3*d_vh/2 , d_kz/2 - d_vh/2 - 1.3*d_vh/2], [l_c+h_phi+l_kz-d_vh / 2, l_c+h_phi+l_kz-d_vh / 2], color="#D44B46",linestyle='-.')

  ax2.plot([0,0], [-0.5, 1.1*(l_c+h_phi+l_kz+x_st)], color="#D44B46",linestyle='-.')

  ax2.set_xlim(-1.2*H/2,1.2*H/2)
  ax2.set_ylim(-2,1.2*(l_c+h_phi+l_kz+x_st))
  ax2.tick_params(axis='x', colors='white', labelsize=10)
  ax2.tick_params(axis='y', colors='white', labelsize=10)
  ax2.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
  ax2.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
  ax2.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
  ax2.xaxis.set_minor_locator(AutoMinorLocator())
  ax2.yaxis.set_minor_locator(AutoMinorLocator())
  ax2.title.set_color('white')
  fig.patch.set_facecolor('#131212')
  ax2.set_facecolor('#131212')
  fig.subplots_adjust(left=0.07, bottom=0.05, right=0.98, top=0.98)
  ax2.xaxis.set_major_formatter(formatter)
  ax2.yaxis.set_major_formatter(formatter)
  ax2.tick_params(axis='x', colors='white', labelsize=11)
  ax2.tick_params(axis='y', colors='white', labelsize=11)

#------------------------------------------------------------------------------
  square = patches.Polygon(
        [[-H/2,0 ], [-0.5*d_f, 0], [-0.5*d_f,h_og], [-H/2,h_og ]],
        edgecolor='#9E3C39', facecolor='none', hatch="\\")
  ax2.add_patch(square)

  square = patches.Polygon(
        [[-H / 2, h_og+h_ras], [-0.5 * d_f, h_og+h_ras], [-0.5 * d_f, h_og+h_ras+h_sr], [-H / 2, h_og+h_ras+h_sr]],
        edgecolor='#9E3C39', facecolor='none', hatch="\\")
  ax2.add_patch(square)

  square = patches.Polygon(
        [[H / 2, 0], [0.5 * d_f, 0], [0.5 * d_f, h_og], [H / 2, h_og]],
        edgecolor='#9E3C39', facecolor='none', hatch="\\")
  ax2.add_patch(square)

  square = patches.Polygon(
        [[H / 2, h_og + h_ras], [0.5 * d_f, h_og + h_ras], [0.5 * d_f, h_og + h_ras + h_sr],
         [H / 2, h_og + h_ras + h_sr]],
        edgecolor='#9E3C39', facecolor='none', hatch="\\")
  ax2.add_patch(square)
  ax2.plot([-0.5*H,-d_f/2],[0,0], color="#D44B46")
  ax2.plot([-0.5*H,-d_f/2],[h_og,h_og], color="#D44B46")

  ax2.plot([0.5*d_f,H/2],[0,0], color="#D44B46")
  ax2.plot([0.5*d_f,H/2],[h_og,h_og], color="#D44B46")

  ax2.plot([-0.5*H,-d_f/2],[h_og+h_ras,h_og+h_ras], color="#D44B46")
  ax2.plot([-0.5*H,-d_f/2],[h_og+h_ras+h_sr,h_og+h_ras+h_sr], color="#D44B46")

  ax2.plot([0.5*d_f,H/2],[h_og+h_ras,h_og+h_ras], color="#D44B46")
  ax2.plot([0.5*d_f,H/2],[h_og+h_ras+h_sr,h_og+h_ras+h_sr], color="#D44B46")

  canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
  canvas_widget = canvas.get_tk_widget()
  canvas_widget.place(x=50, y=10)
def find_h_phi(d_kz,d_c,phi):
    phi_rad=grad_to_rad(phi)
    return ((0.5*d_kz)-(0.5*d_c))*math.tan(phi_rad)
def find_l_arc(x,R):
    beta=math.acos( x/R)
    l=(R)*math.sin(beta)
    return l,beta
def print_nozzle_4(frame,H,delta_st_n,l_c_n,l_kz_n,phi_n,d_c_n,d_vh_n,i_vh_n,delta_st_v,l_kz_v,l_c_v,phi_v,d_vh_v,i_vh_v,d_kz_v,d_c_v,h_og,h_sr):
    d_f = 0.75 * H
    d_kz_n = d_f - (2 * delta_st_n)
    h_1 = find_h_phi(d_kz_n, d_c_n, phi_n)
    h_2 = find_h_phi(d_kz_v, d_c_v, phi_v)
    h_max = l_c_v + h_2 + l_kz_v + delta_st_n

    fig = Figure(figsize=(6.5, 20), dpi=100)
    ax_2 = fig.add_subplot(312)
    ax = fig.add_subplot(311)
    ax_3 = fig.add_subplot(313)
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('#1A1A1A')  # 171717
# =========================Построение первого графика=========================
    square = patches.Polygon([[-0.5 * d_kz_v - delta_st_n, l_c_v + h_2 + l_kz_v + delta_st_n],
                              [0.5 * d_kz_v + delta_st_n, l_c_v + h_2 + l_kz_v + delta_st_n],
                              [0.5 * d_kz_v + delta_st_n, l_c_n + h_1 + l_kz_n + delta_st_n],
                              [0.5 * d_f, l_c_n + h_1 + l_kz_n + delta_st_n], [0.5 * d_f, 0], [0.5 * d_c_n, 0],
                              [0.5 * d_c_n, l_c_n], [0.5 * d_kz_n, l_c_n + h_1], [0.5 * d_kz_n, l_c_n + h_1 + l_kz_n],
                              [0.5 * d_kz_v + delta_st_v, l_c_n + h_1 + l_kz_n], [0.5 * d_kz_v + delta_st_v, 0],
                              [0.5 * d_c_v, 0], [0.5 * d_c_v, l_c_v], [0.5 * d_kz_v, l_c_v + h_2],
                              [0.5 * d_kz_v, l_c_v + h_2 + l_kz_v],
                              [-0.5 * d_kz_v, l_c_v + h_2 + l_kz_v], [-0.5 * d_kz_v, l_c_v + h_2],
                              [-0.5 * d_c_v, l_c_v], [-0.5 * d_c_v, 0], [-0.5 * d_kz_v - delta_st_v, 0],
                              [-0.5 * d_kz_v - delta_st_v, l_c_n + h_1 + l_kz_n], [-0.5 * d_kz_n, l_c_n + h_1 + l_kz_n],
                              [-0.5 * d_kz_n, l_c_n + h_1], [-0.5 * d_c_n, l_c_n], [-0.5 * d_c_n, 0], [-0.5 * d_f, 0],
                              [-0.5 * d_f, l_c_n + h_1 + l_kz_n + delta_st_n],
                              [-0.5 * d_kz_v - delta_st_n, l_c_n + h_1 + l_kz_n + delta_st_n]], edgecolor='#9E3C39',
                             facecolor='none', hatch="\\")
    ax.add_patch(square)

    square_1 = patches.Polygon([[-0.5 * d_kz_v - delta_st_n, l_c_v + h_2 + l_kz_v + delta_st_n],
                                [0.5 * d_kz_v + delta_st_n, l_c_v + h_2 + l_kz_v + delta_st_n],
                                [0.5 * d_kz_v + delta_st_n, l_c_n + h_1 + l_kz_n + delta_st_n],
                                [0.5 * d_f, l_c_n + h_1 + l_kz_n + delta_st_n], [0.5 * d_f, 0], [0.5 * d_c_n, 0],
                                [0.5 * d_c_n, l_c_n], [0.5 * d_kz_n, l_c_n + h_1], [0.5 * d_kz_n, l_c_n + h_1 + l_kz_n],
                                [0.5 * d_kz_v + delta_st_v, l_c_n + h_1 + l_kz_n], [0.5 * d_kz_v + delta_st_v, 0],
                                [0.5 * d_c_v, 0], [0.5 * d_c_v, l_c_v], [0.5 * d_kz_v, l_c_v + h_2],
                                [0.5 * d_kz_v, l_c_v + h_2 + l_kz_v],
                                [-0.5 * d_kz_v, l_c_v + h_2 + l_kz_v], [-0.5 * d_kz_v, l_c_v + h_2],
                                [-0.5 * d_c_v, l_c_v], [-0.5 * d_c_v, 0], [-0.5 * d_kz_v - delta_st_v, 0],
                                [-0.5 * d_kz_v - delta_st_v, l_c_n + h_1 + l_kz_n],
                                [-0.5 * d_kz_n, l_c_n + h_1 + l_kz_n],
                                [-0.5 * d_kz_n, l_c_n + h_1], [-0.5 * d_c_n, l_c_n], [-0.5 * d_c_n, 0], [-0.5 * d_f, 0],
                                [-0.5 * d_f, l_c_n + h_1 + l_kz_n + delta_st_n],
                                [-0.5 * d_kz_v - delta_st_n, l_c_n + h_1 + l_kz_n + delta_st_n]], edgecolor='#D44B46',
                               facecolor='none')
    ax.add_patch(square_1)

    square_2 = patches.Polygon([[-0.5 * H, 0], [-0.5 * H, h_og], [-0.5 * d_f, h_og], [-0.5 * d_f, 0]],
                               edgecolor='#9E3C39', facecolor='none', hatch='/')
    ax.add_patch(square_2)
    square_3 = patches.Polygon([[-0.5 * H, 0], [-0.5 * H, h_og], [-0.5 * d_f, h_og], [-0.5 * d_f, 0]],
                               edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square_3)

    square_2_1 = patches.Polygon([[0.5 * H, 0], [0.5 * H, h_og], [0.5 * d_f, h_og], [0.5 * d_f, 0]],
                                 edgecolor='#9E3C39', facecolor='none', hatch='/')
    ax.add_patch(square_2_1)
    square_3_1 = patches.Polygon([[0.5 * H, 0], [0.5 * H, h_og], [0.5 * d_f, h_og], [0.5 * d_f, 0]],
                                 edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square_3_1)

    square_4 = patches.Polygon(
        [[0.5 * H, l_c_n + h_1 + l_kz_n + delta_st_n], [0.5 * d_kz_v + delta_st_n, l_c_n + h_1 + l_kz_n + delta_st_n],
         [0.5 * d_kz_v + delta_st_n, l_c_n + h_1 + l_kz_n + delta_st_n + h_sr],
         [0.5 * H, l_c_n + h_1 + l_kz_n + delta_st_n + h_sr]], edgecolor='#9E3C39', facecolor='none', hatch='/')
    ax.add_patch(square_4)
    square_5 = patches.Polygon(
        [[0.5 * H, l_c_n + h_1 + l_kz_n + delta_st_n], [0.5 * d_kz_v + delta_st_n, l_c_n + h_1 + l_kz_n + delta_st_n],
         [0.5 * d_kz_v + delta_st_n, l_c_n + h_1 + l_kz_n + delta_st_n + h_sr],
         [0.5 * H, l_c_n + h_1 + l_kz_n + delta_st_n + h_sr]], edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square_5)

    square_4_1 = patches.Polygon(
        [[-0.5 * H, l_c_n + h_1 + l_kz_n + delta_st_n], [-0.5 * d_kz_v - delta_st_n, l_c_n + h_1 + l_kz_n + delta_st_n],
         [-0.5 * d_kz_v - delta_st_n, l_c_n + h_1 + l_kz_n + delta_st_n + h_sr],
         [-0.5 * H, l_c_n + h_1 + l_kz_n + delta_st_n + h_sr]], edgecolor='#9E3C39', facecolor='none', hatch='/')
    ax.add_patch(square_4_1)
    square_5_1 = patches.Polygon(
        [[-0.5 * H, l_c_n + h_1 + l_kz_n + delta_st_n], [-0.5 * d_kz_v - delta_st_n, l_c_n + h_1 + l_kz_n + delta_st_n],
         [-0.5 * d_kz_v - delta_st_n, l_c_n + h_1 + l_kz_n + delta_st_n + h_sr],
         [-0.5 * H, l_c_n + h_1 + l_kz_n + delta_st_n + h_sr]], edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square_4_1)

    ax.plot([-0.5 * d_kz_n, -0.5 * d_kz_v - delta_st_v], [h_1 + l_c_n, h_1 + l_c_n], color="#D44B46")
    ax.plot([0.5 * d_kz_n, 0.5 * d_kz_v + delta_st_v], [h_1 + l_c_n, h_1 + l_c_n], color="#D44B46")
    ax.plot([-0.5 * d_c_n, -0.5 * d_kz_v - delta_st_v], [l_c_n, l_c_n], color="#D44B46")
    ax.plot([0.5 * d_c_n, 0.5 * d_kz_v + delta_st_v], [l_c_n, l_c_n], color="#D44B46")
    ax.plot([-0.5 * d_kz_v, 0.5 * d_kz_v], [l_c_v + h_2, l_c_v + h_2], color="#D44B46")
    ax.plot([-0.5 * d_c_v, 0.5 * d_c_v], [l_c_v, l_c_v], color="#D44B46")

    circle = plt.Circle((0.5 * d_kz_n - 0.5 * d_vh_n, l_c_n + h_1 + l_kz_n - 0.5 * d_vh_n), d_vh_n / 2, color='#D44B46',
                        fill=False)
    ax.add_patch(circle)

    circle_1 = plt.Circle((0.5 * d_kz_v - 0.5 * d_vh_v, l_c_v + h_2 + l_kz_v - 0.5 * d_vh_v), d_vh_v / 2,
                          color='#D44B46', fill=False)
    ax.add_patch(circle_1)

    ax.plot([0.5 * d_kz_n - 0.5 * d_vh_n, 0.5 * d_kz_n - 0.5 * d_vh_n],
            [l_c_n + h_1 + l_kz_n - 0.5 * d_vh_n - 1.2 * 0.5 * d_vh_n,
             l_c_n + h_1 + l_kz_n - 0.5 * d_vh_n + 1.2 * 0.5 * d_vh_n], color="#D44B46", linestyle='-.')
    ax.plot([0.5 * d_kz_n - 0.5 * d_vh_n - 1.2 * 0.5 * d_vh_n, 0.5 * d_kz_n - 0.5 * d_vh_n + 1.2 * 0.5 * d_vh_n],
            [l_c_n + h_1 + l_kz_n - 0.5 * d_vh_n, l_c_n + h_1 + l_kz_n - 0.5 * d_vh_n], color="#D44B46", linestyle='-.')

    ax.plot([0.5 * d_kz_v - 0.5 * d_vh_v, 0.5 * d_kz_v - 0.5 * d_vh_v],
            [l_c_v + h_2 + l_kz_v - 0.5 * d_vh_v - 1.2 * 0.5 * d_vh_v,
             l_c_v + h_2 + l_kz_v - 0.5 * d_vh_v + 1.2 * 0.5 * d_vh_v], color="#D44B46", linestyle='-.')
    ax.plot([0.5 * d_kz_v - 0.5 * d_vh_v - 1.2 * 0.5 * d_vh_v, 0.5 * d_kz_v - 0.5 * d_vh_v + 1.2 * 0.5 * d_vh_v],
            [l_c_v + h_2 + l_kz_v - 0.5 * d_vh_v, l_c_v + h_2 + l_kz_v - 0.5 * d_vh_v], color="#D44B46", linestyle='-.')

    ax.plot([0, 0], [-1, 1.1 * h_max], color="#D44B46", linestyle='-.')
    ax.plot([-1.1 * d_f / 2, 1.1 * d_f / 2], [0, 0], color="#D44B46", linestyle='-.')

    ax.set_xlim(-1.1 * H / 2, 1.1 * H / 2)
    ax.set_ylim(-1, 1.1 * h_max)

# =========================Построение второго графика=========================
    ax_2.set_aspect('equal', adjustable='box')
    ax_2.set_facecolor('#1A1A1A')  # 171717

    l_1, beta_1 = find_l_arc(d_kz_n * 0.5, d_f * 0.5)
    l_2, beta_2 = find_l_arc((0.5 * d_kz_n) - 0.5 * d_vh_n, 0.5 * d_kz_n)
    l_3, beta_3 = find_l_arc((0.5 * d_kz_n) - 0.5 * d_vh_n, 0.5 * d_f)
    l_4, beta_4 = find_l_arc((0.5 * d_kz_n) - d_vh_n, 0.5 * d_kz_n)
    l_5, beta_5 = find_l_arc((0.5 * d_kz_n) - d_vh_n, 0.5 * d_f)

    circle = plt.Circle((0, 0), d_f / 2, color='#D44B46', fill=False)
    ax_2.add_patch(circle)

    circle = plt.Circle((0, 0), d_kz_n / 2, color='#D44B46', fill=False)
    ax_2.add_patch(circle)

    circle = plt.Circle((0, 0), d_kz_v / 2, color='#D44B46', fill=False)
    ax_2.add_patch(circle)

    circle = plt.Circle((0, 0), (d_kz_v / 2) + delta_st_v, color='#D44B46', fill=False)
    ax_2.add_patch(circle)

    for i in range(i_vh_n):
        angle = i * 2 * math.pi / i_vh_n

        x_1 = (d_kz_n / 2) * math.cos(angle + beta_2)
        y_1 = (d_kz_n / 2) * math.sin(angle + beta_2)

        x_2 = (d_f / 2) * math.cos(angle + beta_3)
        y_2 = (d_f / 2) * math.sin(angle + beta_3)
        ax_2.plot([x_1, x_2], [y_1, y_2], color="#D44B46", linestyle='-.')

        x_1 = (d_kz_n / 2) * math.cos(angle)
        y_1 = (d_kz_n / 2) * math.sin(angle)

        x_2 = (d_f / 2) * math.cos(angle + beta_1)
        y_2 = (d_f / 2) * math.sin(angle + beta_1)
        ax_2.plot([x_1, x_2], [y_1, y_2], color="#D44B46")

        x_1 = (d_kz_n / 2) * math.cos(angle + beta_4)
        y_1 = (d_kz_n / 2) * math.sin(angle + beta_4)

        x_2 = (d_f / 2) * math.cos(angle + beta_5)
        y_2 = (d_f / 2) * math.sin(angle + beta_5)
        ax_2.plot([x_1, x_2], [y_1, y_2], color="#D44B46")

    ax_2.plot([0, 0], [-1.1 * d_f / 2, 1.1 * d_f / 2], color="#D44B46", linestyle='-.')
    ax_2.plot([-1.1 * d_f / 2, 1.1 * d_f / 2], [0, 0], color="#D44B46", linestyle='-.')
    ax_2.set_xlim(-1.1 * H / 2, 1.1 * H / 2)
    ax_2.set_ylim(-1.1 * H / 2, 1.1 * H / 2)

    ax_3.set_aspect('equal', adjustable='box')
    ax_3.set_facecolor('#1A1A1A')  # 171717

    circle = plt.Circle((0, 0), d_kz_v / 2, color='#D44B46', fill=False)
    ax_3.add_patch(circle)
    circle = plt.Circle((0, 0), (d_kz_v / 2) + delta_st_n, color='#D44B46', fill=False)
    ax_3.add_patch(circle)

    d_f_1 = d_kz_v + 2 * delta_st_n
    l_1, beta_1 = find_l_arc(d_kz_v * 0.5, d_f_1 * 0.5)
    l_2, beta_2 = find_l_arc((0.5 * d_kz_v) - 0.5 * d_vh_v, 0.5 * d_kz_v)
    l_3, beta_3 = find_l_arc((0.5 * d_kz_v) - 0.5 * d_vh_v, 0.5 * d_f_1)
    l_4, beta_4 = find_l_arc((0.5 * d_kz_v) - d_vh_v, 0.5 * d_kz_v)
    l_5, beta_5 = find_l_arc((0.5 * d_kz_v) - d_vh_v, 0.5 * d_f_1)
    for i in range(i_vh_v):
        angle = i * 2 * math.pi / i_vh_v

        x_1 = (d_kz_v / 2) * math.cos(angle + beta_2)
        y_1 = (d_kz_v / 2) * math.sin(angle + beta_2)

        x_2 = (d_f_1 / 2) * math.cos(angle + beta_3)
        y_2 = (d_f_1 / 2) * math.sin(angle + beta_3)
        ax_3.plot([x_1, x_2], [y_1, y_2], color="#D44B46", linestyle='-.')

        x_1 = (d_kz_v / 2) * math.cos(angle)
        y_1 = (d_kz_v / 2) * math.sin(angle)

        x_2 = (d_f_1 / 2) * math.cos(angle + beta_1)
        y_2 = (d_f_1 / 2) * math.sin(angle + beta_1)
        ax_3.plot([x_1, x_2], [y_1, y_2], color="#D44B46")

        x_1 = (d_kz_v / 2) * math.cos(angle + beta_4)
        y_1 = (d_kz_v / 2) * math.sin(angle + beta_4)

        x_2 = (d_f_1 / 2) * math.cos(angle + beta_5)
        y_2 = (d_f_1 / 2) * math.sin(angle + beta_5)
        ax_3.plot([x_1, x_2], [y_1, y_2], color="#D44B46")

    ax_3.plot([0, 0], [-1.1 * ((d_kz_v / 2) + delta_st_n), 1.1 * ((d_kz_v / 2) + delta_st_n)], color="#D44B46",
              linestyle='-.')
    ax_3.plot([-1.1 * ((d_kz_v / 2) + delta_st_n), 1.1 * ((d_kz_v / 2) + delta_st_n)], [0, 0], color="#D44B46",
              linestyle='-.')
    ax_3.set_xlim(-1.1 * ((d_kz_v / 2) + delta_st_n), 1.1 * ((d_kz_v / 2) + delta_st_n))
    ax_3.set_ylim(-1.1 * ((d_kz_v / 2) + delta_st_n), 1.1 * ((d_kz_v / 2) + delta_st_n))




    ax.tick_params(axis='x', colors='white', labelsize=10)
    ax.tick_params(axis='y', colors='white', labelsize=10)
    ax.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.title.set_color('white')
    fig.patch.set_facecolor('#131212')
    ax.set_facecolor('#131212')
    fig.subplots_adjust(left=0.5, bottom=0.05, right=0.98, top=0.98)
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.tick_params(axis='x', colors='white', labelsize=11)
    ax.tick_params(axis='y', colors='white', labelsize=11)


    ax_2.tick_params(axis='x', colors='white', labelsize=10)
    ax_2.tick_params(axis='y', colors='white', labelsize=10)
    ax_2.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
    ax_2.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax_2.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax_2.xaxis.set_minor_locator(AutoMinorLocator())
    ax_2.yaxis.set_minor_locator(AutoMinorLocator())
    ax_2.title.set_color('white')
    fig.patch.set_facecolor('#131212')
    ax_2.set_facecolor('#131212')
    fig.subplots_adjust(left=0.07, bottom=0.05, right=0.98, top=0.98)
    ax_2.xaxis.set_major_formatter(formatter)
    ax_2.yaxis.set_major_formatter(formatter)
    ax_2.tick_params(axis='x', colors='white', labelsize=11)
    ax_2.tick_params(axis='y', colors='white', labelsize=11)


    ax_3.tick_params(axis='x', colors='white', labelsize=10)
    ax_3.tick_params(axis='y', colors='white', labelsize=10)
    ax_3.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
    ax_3.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax_3.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax_3.xaxis.set_minor_locator(AutoMinorLocator())
    ax_3.yaxis.set_minor_locator(AutoMinorLocator())
    ax_3.title.set_color('white')
    fig.patch.set_facecolor('#131212')
    ax_3.set_facecolor('#131212')
    fig.subplots_adjust(left=0.1, bottom=0.05, right=0.98, top=0.98)
    ax_3.xaxis.set_major_formatter(formatter)
    ax_3.yaxis.set_major_formatter(formatter)
    ax_3.tick_params(axis='x', colors='white', labelsize=11)
    ax_3.tick_params(axis='y', colors='white', labelsize=11)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=10, y=10)
def print_nozzle_5(frame,H,d_f,delta_st_n,d_kz_n,i_vh_n,d_vh_n,l_kz_n,d_f_vn,phi_n,d_c_n,l_c_n,l_c_v,i_vh_v,d_vh_v,h_vist,h_og,h_sr):
    h_1 = find_h_phi(d_kz_n, d_c_n, phi_n)
    h_max=l_c_n+h_1+l_kz_n+delta_st_n+l_c_v-h_vist
    l_1, beta_1 = find_l_arc(d_kz_n * 0.5, d_f * 0.5)
    l_2, beta_2 = find_l_arc((0.5 * d_kz_n) - 0.5 * d_vh_n, 0.5 * d_kz_n)
    l_3, beta_3 = find_l_arc((0.5 * d_kz_n) - 0.5 * d_vh_n, 0.5 * d_f)
    l_4, beta_4 = find_l_arc((0.5 * d_kz_n) - d_vh_n, 0.5 * d_kz_n)
    l_5, beta_5 = find_l_arc((0.5 * d_kz_n) - d_vh_n, 0.5 * d_f)


    fig = Figure(figsize=(6.5, 20), dpi=100)
    ax_2 = fig.add_subplot(312)
    ax = fig.add_subplot(311)
    ax_3 = fig.add_subplot(313)
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('#1A1A1A')  # 171717
    ax.plot([-0.5 * d_c_n, 0.5 * d_c_n], [0, 0], color="#9E3C39")
    ax.plot([-0.5 * d_f_vn, 0.5 * d_f_vn], [l_c_n + h_1 + l_kz_n - h_vist, l_c_n + h_1 + l_kz_n - h_vist],
            color="#9E3C39")
    ax.plot([-0.5 * d_c_n, 0.5 * d_c_n], [l_c_n, l_c_n], color="#9E3C39")
    ax.plot([-0.5 * d_kz_n, 0.5 * d_kz_n], [l_c_n+h_1, l_c_n+h_1], color="#9E3C39")
    square = patches.Polygon([[-d_f/2,0],[-d_f/2,l_c_n+h_1+l_kz_n+delta_st_n],[-d_f_vn/2,l_c_n+h_1+l_kz_n+delta_st_n],
                              [-d_f_vn/2,l_c_n+h_1+l_kz_n+delta_st_n+l_c_v-h_vist],[d_f_vn/2,l_c_n+h_1+l_kz_n+delta_st_n+l_c_v-h_vist],
                              [d_f_vn/2,l_c_n+h_1+l_kz_n+delta_st_n],[d_f/2,l_c_n+h_1+l_kz_n+delta_st_n],[d_f/2,0],[0.5*d_c_n,0],
                              [0.5*d_c_n,l_c_n],[0.5*d_kz_n,l_c_n+h_1],[0.5*d_kz_n,l_c_n+h_1+l_kz_n],[d_f_vn*0.5,l_c_n+h_1+l_kz_n],
                              [d_f_vn*0.5,l_c_n+h_1+l_kz_n-h_vist],[d_f_vn*0.5-delta_st_n,l_c_n+h_1+l_kz_n-h_vist],
                              [d_f_vn*0.5-delta_st_n,h_max-delta_st_n],[-d_f_vn*0.5+delta_st_n,h_max-delta_st_n],
                              [-d_f_vn*0.5+delta_st_n,l_c_n+h_1+l_kz_n-h_vist] ,[-d_f_vn*0.5,l_c_n+h_1+l_kz_n-h_vist],
                              [-d_f_vn*0.5,l_c_n+h_1+l_kz_n],[-0.5*d_kz_n,l_c_n+h_1+l_kz_n],[-0.5*d_kz_n,l_c_n+h_1],
                              [-0.5*d_c_n,l_c_n],[-0.5*d_c_n,0]],edgecolor='#9E3C39',facecolor='none', hatch="\\")
    ax.add_patch(square)
    square_1 = patches.Polygon([[-d_f/2,0],[-d_f/2,l_c_n+h_1+l_kz_n+delta_st_n],[-d_f_vn/2,l_c_n+h_1+l_kz_n+delta_st_n],
                              [-d_f_vn/2,l_c_n+h_1+l_kz_n+delta_st_n+l_c_v-h_vist],[d_f_vn/2,l_c_n+h_1+l_kz_n+delta_st_n+l_c_v-h_vist],
                              [d_f_vn/2,l_c_n+h_1+l_kz_n+delta_st_n],[d_f/2,l_c_n+h_1+l_kz_n+delta_st_n],[d_f/2,0],[0.5*d_c_n,0],
                              [0.5*d_c_n,l_c_n],[0.5*d_kz_n,l_c_n+h_1],[0.5*d_kz_n,l_c_n+h_1+l_kz_n],[d_f_vn*0.5,l_c_n+h_1+l_kz_n],
                              [d_f_vn*0.5,l_c_n+h_1+l_kz_n-h_vist],[d_f_vn*0.5-delta_st_n,l_c_n+h_1+l_kz_n-h_vist],
                              [d_f_vn*0.5-delta_st_n,h_max-delta_st_n],[-d_f_vn*0.5+delta_st_n,h_max-delta_st_n],
                              [-d_f_vn*0.5+delta_st_n,l_c_n+h_1+l_kz_n-h_vist] ,[-d_f_vn*0.5,l_c_n+h_1+l_kz_n-h_vist],
                              [-d_f_vn*0.5,l_c_n+h_1+l_kz_n],[-0.5*d_kz_n,l_c_n+h_1+l_kz_n],[-0.5*d_kz_n,l_c_n+h_1],
                              [-0.5*d_c_n,l_c_n],[-0.5*d_c_n,0]], edgecolor='#D44B46',facecolor='none')
    ax.add_patch(square_1)
    square = patches.Polygon([[-0.5*H,0],[-0.5*H,h_og],[-0.5*d_f,h_og],[-0.5*d_f,0]],edgecolor='#9E3C39',facecolor='none', hatch='/')
    ax.add_patch(square)
    square = patches.Polygon([[0.5 * H, 0], [0.5 * H, h_og], [0.5 * d_f, h_og], [0.5 * d_f, 0]],edgecolor='#9E3C39', facecolor='none', hatch='/')
    ax.add_patch(square)
    square = patches.Polygon([[-0.5 * H, l_c_n+h_1+l_kz_n+delta_st_n], [-0.5*d_f_vn, l_c_n+h_1+l_kz_n+delta_st_n], [-0.5*d_f_vn, l_c_n+h_1+l_kz_n+delta_st_n+h_sr], [-0.5 * H, l_c_n+h_1+l_kz_n+delta_st_n+h_sr]], edgecolor='#9E3C39',facecolor='none', hatch='/')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * H, l_c_n + h_1 + l_kz_n + delta_st_n], [0.5 * d_f_vn, l_c_n + h_1 + l_kz_n + delta_st_n],
         [0.5 * d_f_vn, l_c_n + h_1 + l_kz_n + delta_st_n + h_sr],
         [0.5 * H, l_c_n + h_1 + l_kz_n + delta_st_n + h_sr]], edgecolor='#9E3C39', facecolor='none', hatch='/')
    ax.add_patch(square)

    square = patches.Polygon([[-0.5 * H, 0], [-0.5 * H, h_og], [-0.5 * d_f, h_og], [-0.5 * d_f, 0]],edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon([[0.5 * H, 0], [0.5 * H, h_og], [0.5 * d_f, h_og], [0.5 * d_f, 0]], edgecolor='#D44B46',facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5 * H, l_c_n + h_1 + l_kz_n + delta_st_n], [-0.5 * d_f_vn, l_c_n + h_1 + l_kz_n + delta_st_n],
         [-0.5 * d_f_vn, l_c_n + h_1 + l_kz_n + delta_st_n + h_sr],
         [-0.5 * H, l_c_n + h_1 + l_kz_n + delta_st_n + h_sr]], edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * H, l_c_n + h_1 + l_kz_n + delta_st_n], [0.5 * d_f_vn, l_c_n + h_1 + l_kz_n + delta_st_n],
         [0.5 * d_f_vn, l_c_n + h_1 + l_kz_n + delta_st_n + h_sr],
         [0.5 * H, l_c_n + h_1 + l_kz_n + delta_st_n + h_sr]], edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    ax.plot([0.5*d_kz_n-0.5*d_vh_n, 0.5*d_kz_n-0.5*d_vh_n], [0.98*(-0.5*d_vh_n+l_c_n + h_1 + l_kz_n-0.5*d_vh_n),1.02*(0.5*d_vh_n+l_c_n + h_1 + l_kz_n-0.5*d_vh_n)], color="#D44B46",linestyle='-.')
    ax.plot([0.5 * d_f_vn - delta_st_n-(0.5*d_vh_v), 0.5 * d_f_vn - delta_st_n-(0.5*d_vh_v)], [0.98*(-0.5*d_vh_v+l_c_n + h_1 + l_kz_n-h_vist+l_c_v-(0.5 * d_vh_v)),1.02*(0.5*d_vh_v+l_c_n + h_1 + l_kz_n-h_vist+l_c_v-(0.5 * d_vh_v))], color="#D44B46", linestyle='-.')
    ax.plot([0.98*(-0.5*d_vh_n+0.5*d_kz_n-0.5*d_vh_n),1.02*(0.5*d_vh_n+0.5*d_kz_n-0.5*d_vh_n)], [l_c_n + h_1 + l_kz_n-0.5*d_vh_n,l_c_n + h_1 + l_kz_n-0.5*d_vh_n], color="#D44B46",linestyle='-.')
    ax.plot([0.98*(-0.5*d_vh_v+0.5 * d_f_vn - delta_st_n-(0.5*d_vh_v)),1.02*(0.5*d_vh_v+0.5 * d_f_vn - delta_st_n-(0.5*d_vh_v))], [l_c_n + h_1 + l_kz_n-h_vist+l_c_v-(0.5 * d_vh_v),l_c_n + h_1 + l_kz_n-h_vist+l_c_v-(0.5 * d_vh_v) ], color="#D44B46", linestyle='-.')
    ax.plot([0, 0], [-0.5, 1.05 * h_max], color="#D44B46", linestyle='-.')
    circle = plt.Circle((0.5*d_kz_n-0.5*d_vh_n, l_c_n + h_1 + l_kz_n-0.5*d_vh_n), 0.5*d_vh_n, color='#D44B46', fill=False)
    ax.add_patch(circle)
    circle = plt.Circle((0.5 * d_f_vn - delta_st_n-(0.5*d_vh_v), l_c_n + h_1 + l_kz_n-h_vist+l_c_v-(0.5 * d_vh_v)), 0.5 * d_vh_v, color='#D44B46', fill=False)
    ax.add_patch(circle)


    ax.set_xlim(-1.1 * H / 2, 1.1 * H / 2)
    ax.set_ylim(-1, 1.1 * h_max)
    ax.tick_params(axis='x', colors='white', labelsize=10)
    ax.tick_params(axis='y', colors='white', labelsize=10)
    ax.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.title.set_color('white')
    fig.patch.set_facecolor('#131212')
    ax.set_facecolor('#131212')
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.tick_params(axis='x', colors='white', labelsize=11)
    ax.tick_params(axis='y', colors='white', labelsize=11)


    ax_2.set_aspect('equal', adjustable='box')
    ax_2.set_facecolor('#1A1A1A')  # 171717
    circle = plt.Circle((0,0),0.5*d_f,color='#632525', fill='#632525')
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_kz_n, color='#131212', fill='#131212')
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_c_n, color='#D44B46', fill=False)
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_f_vn, color='#632525', fill='#632525')
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_f_vn-delta_st_n, color='#131212', fill='#131212')
    ax_2.add_patch(circle)
    for i in range(i_vh_n):
        angle = i * 2 * math.pi / i_vh_n

        x_1_0 = (d_kz_n / 2) * math.cos(angle + beta_2)
        y_1_0 = (d_kz_n / 2) * math.sin(angle + beta_2)

        x_2_0 = (d_f / 2) * math.cos(angle + beta_3)
        y_2_0 = (d_f / 2) * math.sin(angle + beta_3)

        x_1 = (d_kz_n / 2) * math.cos(angle)
        y_1 = (d_kz_n / 2) * math.sin(angle)

        x_2 = (d_f / 2) * math.cos(angle + beta_1)
        y_2 = (d_f / 2) * math.sin(angle + beta_1)

        x_1_1 = (d_kz_n / 2) * math.cos(angle + beta_4)
        y_1_1 = (d_kz_n / 2) * math.sin(angle + beta_4)

        x_2_1 = (d_f / 2) * math.cos(angle + beta_5)
        y_2_1 = (d_f / 2) * math.sin(angle + beta_5)
        square = patches.Polygon([[x_1,y_1 ], [x_2,y_2],[x_2_1,y_2_1],[x_1_1,y_1_1 ]],
                                 color='#131212', fill='#131212')
        ax_2.add_patch(square)
        ax_2.plot([x_1, x_2], [y_1, y_2], color="#D44B46")
        ax_2.plot([x_1_1, x_2_1], [y_1_1, y_2_1], color="#D44B46")
        ax_2.plot([x_1_0, x_2_0], [y_1_0, y_2_0], color="#D44B46", linestyle='-.')
    circle = plt.Circle((0, 0), 0.5 * d_f, color='#D44B46', fill=None)
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_kz_n, color='#D44B46', fill=None)
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_f_vn, color='#D44B46', fill=None)
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_f_vn - delta_st_n, color='#D44B46', fill=None)
    ax_2.add_patch(circle)
    ax_2.plot([0, 0], [-0.5 * H, 0.5 * H], color="#D44B46", linestyle='-.')
    ax_2.plot([-0.5 * H, 0.5 * H], [0, 0], color="#D44B46", linestyle='-.')
    ax_2.set_xlim(-1.1*H / 2, 1.1*H / 2)
    ax_2.set_ylim(-1.1*H / 2, 1.1*H / 2)
    ax_2.tick_params(axis='x', colors='white', labelsize=10)
    ax_2.tick_params(axis='y', colors='white', labelsize=10)
    ax_2.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
    ax_2.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax_2.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax_2.xaxis.set_minor_locator(AutoMinorLocator())
    ax_2.yaxis.set_minor_locator(AutoMinorLocator())
    ax_2.title.set_color('white')
    ax_2.set_facecolor('#131212')
    ax_2.xaxis.set_major_formatter(formatter)
    ax_2.yaxis.set_major_formatter(formatter)
    ax_2.tick_params(axis='x', colors='white', labelsize=11)
    ax_2.tick_params(axis='y', colors='white', labelsize=11)



    ax_3.set_aspect('equal', adjustable='box')
    ax_3.set_facecolor('#1A1A1A')  # 171717
    ax_3.set_xlim(-1.1 * d_f_vn / 2, 1.1 * d_f_vn / 2)
    ax_3.set_ylim(-1.1 * d_f_vn / 2, 1.1 * d_f_vn / 2)
    d_kz_v=d_f_vn-(2*delta_st_n)
    d_f_1=d_f_vn
    l_1, beta_1 = find_l_arc(d_kz_v * 0.5, d_f_1 * 0.5)
    l_2, beta_2 = find_l_arc((0.5 * d_kz_v) - 0.5 * d_vh_v, 0.5 * d_kz_v)
    l_3, beta_3 = find_l_arc((0.5 * d_kz_v) - 0.5 * d_vh_v, 0.5 * d_f_1)
    l_4, beta_4 = find_l_arc((0.5 * d_kz_v) - d_vh_v, 0.5 * d_kz_v)
    l_5, beta_5 = find_l_arc((0.5 * d_kz_v) - d_vh_v, 0.5 * d_f_1)

    circle = plt.Circle((0, 0), 0.5 * d_f_vn, color='#632525', fill='#632525')
    ax_3.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_kz_v, color='#131212', fill='#131212')
    ax_3.add_patch(circle)
    for i in range(i_vh_v):
        angle = i * 2 * math.pi / i_vh_v

        x_1_0 = (d_kz_v / 2) * math.cos(angle + beta_2)
        y_1_0 = (d_kz_v / 2) * math.sin(angle + beta_2)

        x_2_0 = (d_f_1 / 2) * math.cos(angle + beta_3)
        y_2_0 = (d_f_1 / 2) * math.sin(angle + beta_3)
        ax_3.plot([x_1_0, x_2_0], [y_1_0, y_2_0], color="#D44B46", linestyle='-.')

        x_1 = (d_kz_v / 2) * math.cos(angle)
        y_1 = (d_kz_v / 2) * math.sin(angle)

        x_2 = (d_f_1 / 2) * math.cos(angle + beta_1)
        y_2 = (d_f_1 / 2) * math.sin(angle + beta_1)
        ax_3.plot([x_1, x_2], [y_1, y_2], color="#D44B46")

        x_1_1 = (d_kz_v / 2) * math.cos(angle + beta_4)
        y_1_1 = (d_kz_v / 2) * math.sin(angle + beta_4)

        x_2_1 = (d_f_1 / 2) * math.cos(angle + beta_5)
        y_2_1 = (d_f_1 / 2) * math.sin(angle + beta_5)
        ax_3.plot([x_1_1, x_2_1], [y_1_1, y_2_1], color="#D44B46")

        square = patches.Polygon([[x_1, y_1], [x_2, y_2], [x_2_1, y_2_1], [x_1_1, y_1_1]],
                                 color='#131212', fill='#131212')
        ax_3.add_patch(square)
        ax_3.plot([x_1, x_2], [y_1, y_2], color="#D44B46")
        ax_3.plot([x_1_1, x_2_1], [y_1_1, y_2_1], color="#D44B46")
        ax_3.plot([x_1_0, x_2_0], [y_1_0, y_2_0], color="#D44B46", linestyle='-.')
    circle = plt.Circle((0, 0), 0.5 * d_f_vn, color='#D44B46', fill=None)
    ax_3.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_kz_v, color='#D44B46', fill=None)
    ax_3.add_patch(circle)
    ax_3.plot([0, 0], [-0.55 * d_f_vn, 0.55 * d_f_vn], color="#D44B46", linestyle='-.')
    ax_3.plot([-0.55 * d_f_vn, 0.55 * d_f_vn], [0, 0], color="#D44B46", linestyle='-.')
    ax_3.tick_params(axis='x', colors='white', labelsize=10)
    ax_3.tick_params(axis='y', colors='white', labelsize=10)
    ax_3.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
    ax_3.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax_3.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax_3.xaxis.set_minor_locator(AutoMinorLocator())
    ax_3.yaxis.set_minor_locator(AutoMinorLocator())
    ax_3.title.set_color('white')
    ax_3.set_facecolor('#131212')
    ax_3.xaxis.set_major_formatter(formatter)
    ax_3.yaxis.set_major_formatter(formatter)
    ax_3.tick_params(axis='x', colors='white', labelsize=11)
    ax_3.tick_params(axis='y', colors='white', labelsize=11)
    fig.patch.set_facecolor('#131212')
    fig.subplots_adjust(left=0.1, bottom=0.05, right=0.98, top=0.98)
    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=10, y=10)
def print_nozzle_6(frame,H,d_f,delta_st_n,d_c_n,phi_n,l_c_n,l_k_z,d_c_v,delta_st_v,l_c_v,d_vh_n,h_og,h_sr,i_vh_n):
    d_kz_n=d_f-(2*delta_st_n)
    h_1 = find_h_phi(d_kz_n, d_c_n, phi_n)

    fig = Figure(figsize=(6.5, 14), dpi=100)
    ax_2 = fig.add_subplot(212)
    ax = fig.add_subplot(211)
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('#1A1A1A')  # 171717

    square = patches.Polygon(
        [[-0.5*d_c_n,0],[-0.5*d_f,0],[-0.5*d_f,l_c_n+h_1+l_k_z+delta_st_n],[-0.5*d_c_v-delta_st_v,l_c_n+h_1+l_k_z+delta_st_n],
         [-0.5*d_c_v-delta_st_v,l_c_v],[-0.5*d_c_v-(0.5*delta_st_v),l_c_v],[-0.5*d_c_v,l_c_v-(0.5*delta_st_v)],[-0.5*d_c_v,0],[-0.5*d_c_v-delta_st_v,0],
         [-0.5*d_c_v-delta_st_v,l_c_n+h_1+l_k_z],[-0.5*d_kz_n,l_c_n+h_1+l_k_z],[-0.5*d_kz_n,l_c_n+h_1],[-0.5*d_c_n,l_c_n],[-0.5*d_c_n,0]],
        edgecolor='#9E3C39',facecolor='none', hatch='/')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_c_n, 0], [0.5 * d_f, 0], [0.5 * d_f, l_c_n + h_1 + l_k_z + delta_st_n],
         [0.5 * d_c_v + delta_st_v, l_c_n + h_1 + l_k_z + delta_st_n],
         [0.5 * d_c_v + delta_st_v, l_c_v], [0.5 * d_c_v + (0.5*delta_st_v), l_c_v], [0.5 * d_c_v, l_c_v - (0.5*delta_st_v)], [0.5 * d_c_v, 0],
         [0.5 * d_c_v + delta_st_v, 0],
         [0.5 * d_c_v + delta_st_v, l_c_n + h_1 + l_k_z], [0.5 * d_kz_n, l_c_n + h_1 + l_k_z],
         [0.5 * d_kz_n, l_c_n + h_1], [0.5 * d_c_n, l_c_n], [0.5 * d_c_n, 0]],
        edgecolor='#9E3C39', facecolor='none', hatch='/')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5 * d_c_n, 0], [-0.5 * d_f, 0], [-0.5 * d_f, l_c_n + h_1 + l_k_z + delta_st_n],
         [-0.5 * d_c_v - delta_st_v, l_c_n + h_1 + l_k_z + delta_st_n],
         [-0.5 * d_c_v - delta_st_v, l_c_v], [-0.5 * d_c_v - (0.5*delta_st_v), l_c_v], [-0.5 * d_c_v, l_c_v - (0.5*delta_st_v)], [-0.5 * d_c_v, 0],
         [-0.5 * d_c_v - delta_st_v, 0],
         [-0.5 * d_c_v - delta_st_v, l_c_n + h_1 + l_k_z], [-0.5 * d_kz_n, l_c_n + h_1 + l_k_z],
         [-0.5 * d_kz_n, l_c_n + h_1], [-0.5 * d_c_n, l_c_n], [-0.5 * d_c_n, 0]],
        edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_c_n, 0], [0.5 * d_f, 0], [0.5 * d_f, l_c_n + h_1 + l_k_z + delta_st_n],
         [0.5 * d_c_v + delta_st_v, l_c_n + h_1 + l_k_z + delta_st_n],
         [0.5 * d_c_v + delta_st_v, l_c_v], [0.5 * d_c_v + (0.5*delta_st_v), l_c_v], [0.5 * d_c_v, l_c_v - (0.5*delta_st_v)], [0.5 * d_c_v, 0],
         [0.5 * d_c_v + delta_st_v, 0],
         [0.5 * d_c_v + delta_st_v, l_c_n + h_1 + l_k_z], [0.5 * d_kz_n, l_c_n + h_1 + l_k_z],
         [0.5 * d_kz_n, l_c_n + h_1], [0.5 * d_c_n, l_c_n], [0.5 * d_c_n, 0]],
        edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    ax.plot([-0.5 * d_c_v - delta_st_v, -0.5 * d_c_v - delta_st_v], [l_c_n + h_1 + l_k_z, l_c_n + h_1 + l_k_z + delta_st_n], color="#D44B46")
    ax.plot([0.5 * d_c_v + delta_st_v, 0.5 * d_c_v + delta_st_v],
            [l_c_n + h_1 + l_k_z, l_c_n + h_1 + l_k_z + delta_st_n], color="#D44B46")
    ax.plot([-0.5*d_f, 0.5 * d_f],[0, 0], color="#D44B46")
    ax.plot([-0.5 * d_c_v - delta_st_v, 0.5 * d_c_v + delta_st_v], [l_c_v, l_c_v], color="#D44B46")
    ax.plot([-0.5 * d_kz_n, -0.5 * d_c_v - delta_st_v], [l_c_n + h_1, l_c_n + h_1], color="#9E3C39")
    ax.plot([0.5 * d_kz_n, 0.5 * d_c_v + delta_st_v], [l_c_n + h_1, l_c_n + h_1], color="#9E3C39")
    ax.plot([0.5 * d_c_n, 0.5 * d_c_v + delta_st_v], [l_c_n, l_c_n], color="#9E3C39")
    ax.plot([-0.5 * d_c_n, -0.5 * d_c_v - delta_st_v], [l_c_n, l_c_n], color="#9E3C39")
    ax.plot([-0.5 * d_c_v, 0.5 * d_c_v ], [l_c_v-(0.5*delta_st_v), l_c_v-(0.5*delta_st_v)], color="#9E3C39")
    center_circ_x = 0.5 * d_kz_n - (0.5 * d_vh_n)
    center_circ_y = l_c_n + h_1 + l_k_z - (0.5 * d_vh_n)
    circle = plt.Circle((center_circ_x, center_circ_y), 0.5*d_vh_n, color='#D44B46', fill=None)
    ax.add_patch(circle)
    ax.plot([0, 0], [-0.5, 1.1 *l_c_v], color="#D44B46", linestyle='-.')
    square = patches.Polygon(
        [[-0.5*H,0],[-0.5*H,h_og],[-0.5*d_f,h_og],[-0.5*d_f,0]],
        edgecolor='#9E3C39', facecolor='none', hatch='\\')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * H, 0], [0.5 * H, h_og], [0.5 * d_f, h_og], [0.5 * d_f, 0]],
        edgecolor='#9E3C39', facecolor='none', hatch='\\')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5 * H, l_c_n+h_1+l_k_z+delta_st_n], [-0.5 * H, l_c_n+h_1+l_k_z+delta_st_n+h_sr],
         [-0.5 * d_c_v-delta_st_v, l_c_n+h_1+l_k_z+delta_st_n+h_sr], [-0.5 * d_c_v-delta_st_v, l_c_n+h_1+l_k_z+delta_st_n]],
        edgecolor='#9E3C39', facecolor='none', hatch='\\')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * H, l_c_n + h_1 + l_k_z + delta_st_n], [0.5 * H, l_c_n + h_1 + l_k_z + delta_st_n + h_sr],
         [0.5 * d_c_v + delta_st_v, l_c_n + h_1 + l_k_z + delta_st_n + h_sr],
         [0.5 * d_c_v + delta_st_v, l_c_n + h_1 + l_k_z + delta_st_n]],
        edgecolor='#9E3C39', facecolor='none', hatch='\\')
    ax.add_patch(square)

    square = patches.Polygon(
        [[-0.5 * H, 0], [-0.5 * H, h_og], [-0.5 * d_f, h_og], [-0.5 * d_f, 0]],
        edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * H, 0], [0.5 * H, h_og], [0.5 * d_f, h_og], [0.5 * d_f, 0]],
        edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5 * H, l_c_n + h_1 + l_k_z + delta_st_n], [-0.5 * H, l_c_n + h_1 + l_k_z + delta_st_n + h_sr],
         [-0.5 * d_c_v - delta_st_v, l_c_n + h_1 + l_k_z + delta_st_n + h_sr],
         [-0.5 * d_c_v - delta_st_v, l_c_n + h_1 + l_k_z + delta_st_n]],
        edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * H, l_c_n + h_1 + l_k_z + delta_st_n], [0.5 * H, l_c_n + h_1 + l_k_z + delta_st_n + h_sr],
         [0.5 * d_c_v + delta_st_v, l_c_n + h_1 + l_k_z + delta_st_n + h_sr],
         [0.5 * d_c_v + delta_st_v, l_c_n + h_1 + l_k_z + delta_st_n]],
        edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)

    ax.plot([center_circ_x, center_circ_x], [center_circ_y-(1.2*0.5*d_vh_n),center_circ_y+(1.2*0.5*d_vh_n) ], color="#D44B46", linestyle='-.')
    ax.plot([center_circ_x-(1.2*0.5*d_vh_n), center_circ_x+(1.2*0.5*d_vh_n)], [center_circ_y,center_circ_y], color="#D44B46", linestyle='-.')

    ax.set_xlim(-1.1 * H / 2, 1.1 * H / 2)
    ax.set_ylim(-1, 1.1 *l_c_v)
    ax.tick_params(axis='x', colors='white', labelsize=10)
    ax.tick_params(axis='y', colors='white', labelsize=10)
    ax.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.title.set_color('white')
    fig.patch.set_facecolor('#131212')
    ax.set_facecolor('#131212')
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.tick_params(axis='x', colors='white', labelsize=11)
    ax.tick_params(axis='y', colors='white', labelsize=11)


    ax_2.set_aspect('equal', adjustable='box')
    ax_2.set_facecolor('#1A1A1A')  # 171717

    circle = plt.Circle((0, 0), 0.5 * d_f, color='#632525', fill='#632525')
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_kz_n, color='#131212', fill='#131212')
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_c_v + delta_st_v, color='#632525', fill='#632525')
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_c_v, color='#131212', fill='#131212')
    ax_2.add_patch(circle)

    l_1, beta_1 = find_l_arc(d_kz_n * 0.5, d_f * 0.5)
    l_2, beta_2 = find_l_arc((0.5 * d_kz_n) - 0.5 * d_vh_n, 0.5 * d_kz_n)
    l_3, beta_3 = find_l_arc((0.5 * d_kz_n) - 0.5 * d_vh_n, 0.5 * d_f)
    l_4, beta_4 = find_l_arc((0.5 * d_kz_n) - d_vh_n, 0.5 * d_kz_n)
    l_5, beta_5 = find_l_arc((0.5 * d_kz_n) - d_vh_n, 0.5 * d_f)

    for i in range(i_vh_n):
        angle = i * 2 * math.pi / i_vh_n

        x_1_0 = (d_kz_n / 2) * math.cos(angle + beta_2)
        y_1_0 = (d_kz_n / 2) * math.sin(angle + beta_2)

        x_2_0 = (d_f / 2) * math.cos(angle + beta_3)
        y_2_0 = (d_f / 2) * math.sin(angle + beta_3)

        x_1 = (d_kz_n / 2) * math.cos(angle)
        y_1 = (d_kz_n / 2) * math.sin(angle)

        x_2 = (d_f / 2) * math.cos(angle + beta_1)
        y_2 = (d_f / 2) * math.sin(angle + beta_1)

        x_1_1 = (d_kz_n / 2) * math.cos(angle + beta_4)
        y_1_1 = (d_kz_n / 2) * math.sin(angle + beta_4)

        x_2_1 = (d_f / 2) * math.cos(angle + beta_5)
        y_2_1 = (d_f / 2) * math.sin(angle + beta_5)
        square = patches.Polygon([[x_1,y_1 ], [x_2,y_2],[x_2_1,y_2_1],[x_1_1,y_1_1 ]],
                                 color='#131212', fill='#131212')
        ax_2.add_patch(square)
        ax_2.plot([x_1, x_2], [y_1, y_2], color="#D44B46")
        ax_2.plot([x_1_1, x_2_1], [y_1_1, y_2_1], color="#D44B46")
        ax_2.plot([x_1_0, x_2_0], [y_1_0, y_2_0], color="#D44B46", linestyle='-.')

    circle = plt.Circle((0, 0), 0.5 * d_f, color='#D44B46', fill=None)
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_kz_n, color='#D44B46', fill=None)
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_c_n, color='#D44B46', fill=None)
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_c_v + delta_st_v, color='#D44B46', fill=None)
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_c_v, color='#D44B46', fill=None)
    ax_2.add_patch(circle)
    ax_2.plot([0, 0], [-0.5 * H, 0.5 * H], color="#D44B46", linestyle='-.')
    ax_2.plot([-0.5 * H, 0.5 * H], [0, 0], color="#D44B46", linestyle='-.')

    ax_2.set_xlim(-1.1*H / 2, 1.1*H / 2)
    ax_2.set_ylim(-1.1*H / 2, 1.1*H / 2)
    ax_2.tick_params(axis='x', colors='white', labelsize=10)
    ax_2.tick_params(axis='y', colors='white', labelsize=10)
    ax_2.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
    ax_2.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax_2.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax_2.xaxis.set_minor_locator(AutoMinorLocator())
    ax_2.yaxis.set_minor_locator(AutoMinorLocator())
    ax_2.title.set_color('white')
    ax_2.set_facecolor('#131212')
    ax_2.xaxis.set_major_formatter(formatter)
    ax_2.yaxis.set_major_formatter(formatter)
    ax_2.tick_params(axis='x', colors='white', labelsize=11)
    ax_2.tick_params(axis='y', colors='white', labelsize=11)




    fig.patch.set_facecolor('#131212')
    fig.subplots_adjust(left=0.1, bottom=0.05, right=0.98, top=0.98)
    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=10, y=10)

def print_nozzle_7(frame,H,delta_st,l_c_n,l_c_v,d_c_v,delta_og,delta_sr,d_vh,i_vh):
    d_f=H*0.75
    d_c_n=d_f-(2*delta_st)


    fig = Figure(figsize=(6.5, 14), dpi=100)
    ax_2 = fig.add_subplot(212)
    ax = fig.add_subplot(211)
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('#1A1A1A')  # 171717
    d_f_v=d_c_v+2*delta_st
    square = patches.Polygon(
        [[-0.5*d_f,0],[-0.5*d_f,l_c_n+delta_st],[-0.5*d_f_v,l_c_n+delta_st],[-0.5*d_f_v,l_c_n+l_c_v],
         [-0.5*d_c_v-(0.5*delta_st),l_c_n+l_c_v],[-0.5*d_c_v,l_c_n+l_c_v-(0.5*delta_st)],[-0.5*d_c_v,l_c_n],[-0.5*d_c_n,l_c_n],
         [-0.5*d_c_n,0]],
        edgecolor='#9E3C39', facecolor='none', hatch='/')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5 * d_f, 0], [-0.5 * d_f, l_c_n + delta_st], [-0.5 * d_f_v, l_c_n + delta_st],
         [-0.5 * d_f_v, l_c_n + l_c_v],
         [-0.5 * d_c_v - (0.5 * delta_st), l_c_n + l_c_v], [-0.5 * d_c_v, l_c_n + l_c_v - (0.5 * delta_st)],
         [-0.5 * d_c_v, l_c_n], [-0.5 * d_c_n, l_c_n],
         [-0.5 * d_c_n, 0]],
        edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_f, 0], [0.5 * d_f, l_c_n + delta_st], [0.5 * d_f_v, l_c_n + delta_st],
         [0.5 * d_f_v, l_c_n + l_c_v],
         [0.5 * d_c_v + (0.5 * delta_st), l_c_n + l_c_v], [0.5 * d_c_v, l_c_n + l_c_v - (0.5 * delta_st)],
         [0.5 * d_c_v, l_c_n], [0.5 * d_c_n, l_c_n],
         [0.5 * d_c_n, 0]],
        edgecolor='#9E3C39', facecolor='none', hatch='/')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_f, 0], [0.5 * d_f, l_c_n + delta_st], [0.5 * d_f_v, l_c_n + delta_st],
         [0.5 * d_f_v, l_c_n + l_c_v],
         [0.5 * d_c_v + (0.5 * delta_st), l_c_n + l_c_v], [0.5 * d_c_v, l_c_n + l_c_v - (0.5 * delta_st)],
         [0.5 * d_c_v, l_c_n], [0.5 * d_c_n, l_c_n],
         [0.5 * d_c_n, 0]],
        edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5*d_f,0],[-0.5*H,0],[-0.5*H,delta_og],[-0.5*d_f,delta_og]],
        edgecolor='#9E3C39', facecolor='none', hatch='\\')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5 * d_f_v, l_c_n+delta_st], [-0.5 * H, l_c_n+delta_st], [-0.5 * H, l_c_n+delta_st+delta_sr], [-0.5 * d_f_v, l_c_n+delta_st+delta_sr]],
        edgecolor='#9E3C39', facecolor='none', hatch='\\')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_f, 0], [0.5 * H, 0], [0.5 * H, delta_og], [0.5 * d_f, delta_og]],
        edgecolor='#9E3C39', facecolor='none', hatch='\\')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_f_v, l_c_n + delta_st], [0.5 * H, l_c_n + delta_st], [0.5 * H, l_c_n + delta_st + delta_sr],
         [0.5 * d_f_v, l_c_n + delta_st + delta_sr]],
        edgecolor='#9E3C39', facecolor='none', hatch='\\')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5 * d_f, 0], [-0.5 * H, 0], [-0.5 * H, delta_og], [-0.5 * d_f, delta_og]],
        edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5 * d_f_v, l_c_n + delta_st], [-0.5 * H, l_c_n + delta_st], [-0.5 * H, l_c_n + delta_st + delta_sr],
         [-0.5 * d_f_v, l_c_n + delta_st + delta_sr]],
        edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_f, 0], [0.5 * H, 0], [0.5 * H, delta_og], [0.5 * d_f, delta_og]],
        edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_f_v, l_c_n + delta_st], [0.5 * H, l_c_n + delta_st], [0.5 * H, l_c_n + delta_st + delta_sr],
         [0.5 * d_f_v, l_c_n + delta_st + delta_sr]],
        edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    ax.plot([-0.5 * d_c_n, 0.5 * d_c_n], [0, 0], color="#9E3C39")
    ax.plot([-0.5 * d_c_v, 0.5 * d_c_v], [l_c_n, l_c_n], color="#9E3C39")
    ax.plot([-0.5 * d_c_v, 0.5 * d_c_v], [l_c_n+l_c_v-(0.5*delta_st), l_c_n+l_c_v-(0.5*delta_st)], color="#9E3C39")
    ax.plot([-0.5 * d_c_v-(0.5 * delta_st), 0.5 * d_c_v+(0.5 * delta_st)], [l_c_n + l_c_v, l_c_n + l_c_v ],color="#9E3C39")
    ax.plot([0, 0], [-0.2, 1.1*(l_c_n + l_c_v)], color="#D44B46", linestyle='-.')
    x_circ = 0.5 * d_c_n - (0.5 * d_vh)
    y_circ = l_c_n - (0.5 * d_vh)
    circle = plt.Circle((x_circ, y_circ), 0.5*d_vh, color='#D44B46', fill=None)
    ax.add_patch(circle)
    ax.plot([x_circ, x_circ], [y_circ-(0.55*d_vh), y_circ+(0.55*d_vh)], color="#D44B46", linestyle='-.')
    ax.plot([x_circ-(0.55*d_vh), x_circ+(0.55*d_vh)], [y_circ, y_circ], color="#D44B46", linestyle='-.')

    ax.set_xlim(-1.1 * H / 2, 1.1 * H / 2)
    ax.set_ylim(-0.5, 1.1*(l_c_v+l_c_n))
    ax.tick_params(axis='x', colors='white', labelsize=10)
    ax.tick_params(axis='y', colors='white', labelsize=10)
    ax.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.title.set_color('white')
    ax.set_facecolor('#131212')
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.tick_params(axis='x', colors='white', labelsize=11)
    ax.tick_params(axis='y', colors='white', labelsize=11)

    circle = plt.Circle((0, 0), 0.5 * d_f, color='#632525', fill='#632525')
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_c_n, color='#131212', fill='#131212')
    ax_2.add_patch(circle)

    l_1, beta_1 = find_l_arc(d_c_n * 0.5, d_f * 0.5)
    l_2, beta_2 = find_l_arc((0.5 * d_c_n) - 0.5 * d_vh, 0.5 * d_c_n)
    l_3, beta_3 = find_l_arc((0.5 * d_c_n) - 0.5 * d_vh, 0.5 * d_f)
    l_4, beta_4 = find_l_arc((0.5 * d_c_n) - d_vh, 0.5 * d_c_n)
    l_5, beta_5 = find_l_arc((0.5 * d_c_n) - d_vh, 0.5 * d_f)
    i_vh_n=i_vh
    d_kz_n=d_c_n
    for i in range(i_vh_n):
        angle = i * 2 * math.pi / i_vh_n

        x_1_0 = (d_kz_n / 2) * math.cos(angle + beta_2)
        y_1_0 = (d_kz_n / 2) * math.sin(angle + beta_2)

        x_2_0 = (d_f / 2) * math.cos(angle + beta_3)
        y_2_0 = (d_f / 2) * math.sin(angle + beta_3)

        x_1 = (d_kz_n / 2) * math.cos(angle)
        y_1 = (d_kz_n / 2) * math.sin(angle)

        x_2 = (d_f / 2) * math.cos(angle + beta_1)
        y_2 = (d_f / 2) * math.sin(angle + beta_1)

        x_1_1 = (d_kz_n / 2) * math.cos(angle + beta_4)
        y_1_1 = (d_kz_n / 2) * math.sin(angle + beta_4)

        x_2_1 = (d_f / 2) * math.cos(angle + beta_5)
        y_2_1 = (d_f / 2) * math.sin(angle + beta_5)
        square = patches.Polygon([[x_1,y_1 ], [x_2,y_2],[x_2_1,y_2_1],[x_1_1,y_1_1 ]],
                                 color='#131212', fill='#131212')
        ax_2.add_patch(square)
        ax_2.plot([x_1, x_2], [y_1, y_2], color="#D44B46")
        ax_2.plot([x_1_1, x_2_1], [y_1_1, y_2_1], color="#D44B46")
        ax_2.plot([x_1_0, x_2_0], [y_1_0, y_2_0], color="#D44B46", linestyle='-.')
    circle = plt.Circle((0, 0), 0.5 * d_f, color='#D44B46', fill=None)
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_c_n, color='#D44B46', fill=None)
    ax_2.add_patch(circle)
    ax_2.plot([0, 0], [-0.5*H, 0.5*H], color="#D44B46", linestyle='-.')
    ax_2.plot([-0.5 * H, 0.5 * H], [0, 0], color="#D44B46", linestyle='-.')
    ax_2.set_xlim(-1.1 * H / 2, 1.1 * H / 2)
    ax_2.set_ylim(-1.1 * H / 2, 1.1 * H / 2)
    ax_2.tick_params(axis='x', colors='white', labelsize=10)
    ax_2.tick_params(axis='y', colors='white', labelsize=10)
    ax_2.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
    ax_2.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax_2.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax_2.xaxis.set_minor_locator(AutoMinorLocator())
    ax_2.yaxis.set_minor_locator(AutoMinorLocator())
    ax_2.title.set_color('white')
    ax_2.set_facecolor('#131212')
    ax_2.xaxis.set_major_formatter(formatter)
    ax_2.yaxis.set_major_formatter(formatter)
    ax_2.tick_params(axis='x', colors='white', labelsize=11)
    ax_2.tick_params(axis='y', colors='white', labelsize=11)





    fig.patch.set_facecolor('#131212')
    fig.subplots_adjust(left=0.1, bottom=0.05, right=0.98, top=0.98)
    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=10, y=10)

def print_nozzle_8(frame,H,d_z,h_otv,d_c_n,d_c_v,delta_st_v,l_c_n,h_og,h_sr,l_otv,l_c_v):
    d_f=H*0.75
    x_f_otv=math.sqrt(0.5*d_f*0.5*d_f-(0.5*0.5*h_otv*h_otv))
    y_f_otv=x_f_otv
    x_z_otv = math.sqrt(0.5*d_z * 0.5*d_z - (0.5 * 0.5 * h_otv * h_otv))
    y_z_otv = x_z_otv

    fig = Figure(figsize=(6.5, 14), dpi=100)
    ax_2 = fig.add_subplot(212)
    ax = fig.add_subplot(211)
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('#1A1A1A')  # 171717


    ax.set_xlim(-1.1 * H / 2, 1.1 * H / 2)
    ax.set_ylim(-0.5, 1.1*l_c_v)
    ax.tick_params(axis='x', colors='white', labelsize=10)
    ax.tick_params(axis='y', colors='white', labelsize=10)
    ax.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.title.set_color('white')
    ax.set_facecolor('#131212')
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.tick_params(axis='x', colors='white', labelsize=11)
    ax.tick_params(axis='y', colors='white', labelsize=11)

    square = patches.Polygon(
        [[-0.5*d_c_n,0], [-0.5*0.5*(d_f+d_c_n),0],[-0.5*0.5*(d_f+d_c_n),h_og],[-0.5*d_f,h_og],[-0.5*d_f,l_c_n],
         [-0.5*d_c_n-0.5,l_c_n],[-0.5*d_c_n,l_c_n-0.5]],edgecolor='#9E3C39', facecolor='none', hatch='/')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_c_n, 0], [0.5 * 0.5 * (d_f + d_c_n), 0], [0.5 * 0.5 * (d_f + d_c_n), h_og], [0.5 * d_f, h_og],
         [0.5 * d_f, l_c_n],
         [0.5 * d_c_n + 0.5, l_c_n], [0.5 * d_c_n, l_c_n - 0.5]], edgecolor='#9E3C39', facecolor='none', hatch='/')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5 * d_c_n, 0], [-0.5 * 0.5 * (d_f + d_c_n), 0], [-0.5 * 0.5 * (d_f + d_c_n), h_og], [-0.5 * d_f, h_og],
         [-0.5 * d_f, l_c_n],
         [-0.5 * d_c_n - 0.5, l_c_n], [-0.5 * d_c_n, l_c_n - 0.5]], edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_c_n, 0], [0.5 * 0.5 * (d_f + d_c_n), 0], [0.5 * 0.5 * (d_f + d_c_n), h_og], [0.5 * d_f, h_og],
         [0.5 * d_f, l_c_n],
         [0.5 * d_c_n + 0.5, l_c_n], [0.5 * d_c_n, l_c_n - 0.5]], edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5*0.5*(d_f+d_c_n),0], [-0.5*0.5*(d_f+d_c_n),h_og],[-0.5*H,h_og],[-0.5*H,0]], edgecolor='#9E3C39', facecolor='none', hatch='\\')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * 0.5 * (d_f + d_c_n), 0], [0.5 * 0.5 * (d_f + d_c_n), h_og], [0.5 * H, h_og], [0.5 * H, 0]],
        edgecolor='#9E3C39', facecolor='none', hatch='\\')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5 * 0.5 * (d_f + d_c_n), 0], [-0.5 * 0.5 * (d_f + d_c_n), h_og], [-0.5 * H, h_og], [-0.5 * H, 0]],
        edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * 0.5 * (d_f + d_c_n), 0], [0.5 * 0.5 * (d_f + d_c_n), h_og], [0.5 * H, h_og], [0.5 * H, 0]],
        edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    #---------------------------------------------------------
    square = patches.Polygon(
        [[-0.5*d_f,l_c_n+l_otv], [-0.5*d_f,l_c_n+l_otv+delta_st_v],[-0.5*d_c_v-delta_st_v,l_c_n+l_otv+delta_st_v],
         [-0.5*d_c_v-delta_st_v,l_c_n+l_otv]], edgecolor='#9E3C39', facecolor='none', hatch='/')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_f, l_c_n + l_otv], [0.5 * d_f, l_c_n + l_otv + delta_st_v],
         [0.5 * d_c_v + delta_st_v, l_c_n + l_otv + delta_st_v],
         [0.5 * d_c_v + delta_st_v, l_c_n + l_otv]], edgecolor='#9E3C39', facecolor='none', hatch='/')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5 * d_f, l_c_n + l_otv], [-0.5 * d_f, l_c_n + l_otv + delta_st_v],
         [-0.5 * d_c_v - delta_st_v, l_c_n + l_otv + delta_st_v],
         [-0.5 * d_c_v - delta_st_v, l_c_n + l_otv]], edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_f, l_c_n + l_otv], [0.5 * d_f, l_c_n + l_otv + delta_st_v],
         [0.5 * d_c_v + delta_st_v, l_c_n + l_otv + delta_st_v],
         [0.5 * d_c_v + delta_st_v, l_c_n + l_otv]], edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    #---------------------------------------------------------------
    square = patches.Polygon(
        [[-0.5*d_c_v-delta_st_v,l_c_n+l_otv+delta_st_v], [-0.5*d_c_v-(1.5*delta_st_v),l_c_n+l_otv+delta_st_v],
         [-0.5*d_c_v-(1.5*delta_st_v),l_c_v],[-0.5*d_c_v-(0.5*delta_st_v),l_c_v],[-0.5*d_c_v,l_c_v-(0.5*delta_st_v)],
         [-0.5*d_c_v,0],[-0.5*d_c_v-delta_st_v,0]], edgecolor='#9E3C39', facecolor='none', hatch='\\')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_c_v + delta_st_v, l_c_n + l_otv + delta_st_v],
         [0.5 * d_c_v + (1.5 * delta_st_v), l_c_n + l_otv + delta_st_v],
         [0.5 * d_c_v + (1.5 * delta_st_v), l_c_v], [0.5 * d_c_v + (0.5 * delta_st_v), l_c_v],
         [0.5 * d_c_v, l_c_v - (0.5 * delta_st_v)], [0.5 * d_c_v, 0], [0.5 * d_c_v + delta_st_v, 0]],
        edgecolor='#9E3C39', facecolor='none', hatch='\\')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5 * d_c_v - delta_st_v, l_c_n + l_otv + delta_st_v],
         [-0.5 * d_c_v - (1.5 * delta_st_v), l_c_n + l_otv + delta_st_v],
         [-0.5 * d_c_v - (1.5 * delta_st_v), l_c_v], [-0.5 * d_c_v - (0.5 * delta_st_v), l_c_v],
         [-0.5 * d_c_v, l_c_v - (0.5 * delta_st_v)],
         [-0.5 * d_c_v, 0], [-0.5 * d_c_v - delta_st_v, 0]], edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_c_v + delta_st_v, l_c_n + l_otv + delta_st_v],
         [0.5 * d_c_v + (1.5 * delta_st_v), l_c_n + l_otv + delta_st_v],
         [0.5 * d_c_v + (1.5 * delta_st_v), l_c_v], [0.5 * d_c_v + (0.5 * delta_st_v), l_c_v],
         [0.5 * d_c_v, l_c_v - (0.5 * delta_st_v)], [0.5 * d_c_v, 0], [0.5 * d_c_v + delta_st_v, 0]],
        edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    if x_f_otv>(0.5*d_c_v+delta_st_v):
        ax.plot([-x_f_otv, -x_f_otv], [l_c_n, l_c_n + l_otv], color="#D44B46")
        ax.plot([x_f_otv, x_f_otv], [l_c_n, l_c_n + l_otv], color="#D44B46")
    if x_z_otv > (0.5 * d_c_v + delta_st_v):
        ax.plot([-x_z_otv, -x_z_otv], [l_c_n, l_c_n + l_otv], color="#D44B46")
        ax.plot([x_z_otv, x_z_otv], [l_c_n, l_c_n + l_otv], color="#D44B46")
    if 0.5*h_otv > (0.5 * d_c_v + delta_st_v):
        ax.plot([-0.5*h_otv, -0.5*h_otv], [l_c_n, l_c_n + l_otv], color="#D44B46")
        ax.plot([0.5 * h_otv, 0.5 * h_otv], [l_c_n, l_c_n + l_otv], color="#D44B46")
    ax.plot([-0.5 * d_c_n, 0.5 * d_c_n], [0, 0], color="#9E3C39")
    ax.plot([-0.5 * d_c_v-0.5*delta_st_v, 0.5 * d_c_v+0.5*delta_st_v], [l_c_v, l_c_v], color="#9E3C39")
    ax.plot([-0.5 * d_c_v, 0.5 * d_c_v ], [l_c_v-0.5*delta_st_v, l_c_v-0.5*delta_st_v], color="#9E3C39")
    ax.plot([-0.5*d_c_n-0.5, -0.5*d_c_v-delta_st_v], [l_c_n, l_c_n], color="#9E3C39")
    ax.plot([-0.5 * d_c_n, -0.5 * d_c_v - delta_st_v], [l_c_n-0.5, l_c_n-0.5], color="#9E3C39")
    ax.plot([0.5 * d_c_n + 0.5, 0.5 * d_c_v + delta_st_v], [l_c_n, l_c_n], color="#9E3C39")
    ax.plot([0.5 * d_c_n, 0.5 * d_c_v + delta_st_v], [l_c_n - 0.5, l_c_n - 0.5], color="#9E3C39")
    ax.plot([0, 0], [-0.1, 1.1 * l_c_v], color="#D44B46", linestyle='-.')
    square = patches.Polygon(
        [[-0.5*d_c_v-(1.5*delta_st_v),l_c_n+l_otv+delta_st_v],[-0.5*d_c_v-(1.5*delta_st_v),l_c_n+l_otv+delta_st_v+h_sr],
         [-0.5*H,l_c_n+l_otv+delta_st_v+h_sr],[-0.5*H,l_c_n+l_otv+delta_st_v]], edgecolor='#9E3C39', facecolor='none', hatch='/')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_c_v + (1.5 * delta_st_v), l_c_n + l_otv + delta_st_v],
         [0.5 * d_c_v + (1.5 * delta_st_v), l_c_n + l_otv + delta_st_v + h_sr],
         [0.5 * H, l_c_n + l_otv + delta_st_v + h_sr], [0.5 * H, l_c_n + l_otv + delta_st_v]], edgecolor='#9E3C39',
        facecolor='none', hatch='/')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5 * d_c_v - (1.5 * delta_st_v), l_c_n + l_otv + delta_st_v],
         [-0.5 * d_c_v - (1.5 * delta_st_v), l_c_n + l_otv + delta_st_v + h_sr],
         [-0.5 * H, l_c_n + l_otv + delta_st_v + h_sr], [-0.5 * H, l_c_n + l_otv + delta_st_v]], edgecolor='#D44B46',
        facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_c_v + (1.5 * delta_st_v), l_c_n + l_otv + delta_st_v],
         [0.5 * d_c_v + (1.5 * delta_st_v), l_c_n + l_otv + delta_st_v + h_sr],
         [0.5 * H, l_c_n + l_otv + delta_st_v + h_sr], [0.5 * H, l_c_n + l_otv + delta_st_v]], edgecolor='#D44B46',
        facecolor='none')
    ax.add_patch(square)


    ax_2.set_xlim(-1.1 * H / 2, 1.1 * H / 2)
    ax_2.set_ylim(-1.1 * H / 2, 1.1 * H / 2)
    ax_2.tick_params(axis='x', colors='white', labelsize=10)
    ax_2.tick_params(axis='y', colors='white', labelsize=10)
    ax_2.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
    ax_2.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax_2.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax_2.xaxis.set_minor_locator(AutoMinorLocator())
    ax_2.yaxis.set_minor_locator(AutoMinorLocator())
    ax_2.title.set_color('white')
    ax_2.set_facecolor('#131212')
    ax_2.xaxis.set_major_formatter(formatter)
    ax_2.yaxis.set_major_formatter(formatter)
    ax_2.tick_params(axis='x', colors='white', labelsize=11)
    ax_2.tick_params(axis='y', colors='white', labelsize=11)

    circle = plt.Circle((0, 0), 0.5 * d_f, color='#632525', fill='#632525')
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_z, color='#131212', fill='#131212')
    ax_2.add_patch(circle)
    square = patches.Polygon(
        [[-0.5*h_otv,0.5*d_f],[0.5*h_otv,0.5*d_f],[0.5*h_otv,-0.5*d_f],[-0.5*h_otv,-0.5*d_f]],
        edgecolor='#131212', facecolor='#131212')
    ax_2.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_f,-0.5 * h_otv], [0.5 * d_f,0.5 * h_otv], [-0.5 * d_f,0.5 * h_otv], [-0.5 * d_f,-0.5 * h_otv]],
        edgecolor='#131212', facecolor='#131212')
    ax_2.add_patch(square)
    circle = plt.Circle((0, 0), 0.5 * d_f, color='#D44B46', fill=None)
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_c_n, color='#D44B46', fill=None)
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_c_n+0.5, color='#D44B46', fill=None)
    ax_2.add_patch(circle)

    circle = plt.Circle((0, 0), 0.5 * d_c_v + delta_st_v, color='#632525', fill='#632525')
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_c_v, color='#131212', fill='#131212')
    ax_2.add_patch(circle)

    circle = plt.Circle((0, 0), 0.5 * d_c_v+delta_st_v, color='#D44B46', fill=None)
    ax_2.add_patch(circle)
    circle = plt.Circle((0, 0), 0.5 * d_c_v, color='#D44B46', fill=None)
    ax_2.add_patch(circle)
    for i in range(4):

        arc = patches.Arc((0, 0), d_z, d_z, theta1=(90 * i) - math.acos(h_otv / d_z) * 180 / math.pi,
                          theta2=(90 * i) - math.asin(h_otv / d_z) * 180 / math.pi, color="#D44B46")
        ax_2.add_patch(arc)
    ax_2.plot([-0.5*h_otv, -0.5*h_otv], [y_f_otv, y_z_otv], color="#D44B46")
    ax_2.plot([0.5 * h_otv, 0.5 * h_otv], [y_f_otv, y_z_otv], color="#D44B46")
    ax_2.plot([-0.5 * h_otv, -0.5 * h_otv], [-y_f_otv, -y_z_otv], color="#D44B46")
    ax_2.plot([0.5 * h_otv, 0.5 * h_otv], [-y_f_otv, -y_z_otv], color="#D44B46")
    ax_2.plot([-x_f_otv, -x_z_otv], [0.5 * h_otv, 0.5 * h_otv], color="#D44B46")
    ax_2.plot([x_f_otv, x_z_otv], [0.5 * h_otv, 0.5 * h_otv], color="#D44B46")
    ax_2.plot([-x_f_otv, -x_z_otv], [-0.5 * h_otv, -0.5 * h_otv], color="#D44B46")
    ax_2.plot([x_f_otv, x_z_otv], [-0.5 * h_otv, -0.5 * h_otv], color="#D44B46")

    ax_2.plot([0, 0], [-0.5 * H, 0.5 * H], color="#D44B46", linestyle='-.')
    ax_2.plot([-0.5 * H, 0.5 * H], [0, 0], color="#D44B46", linestyle='-.')



    fig.patch.set_facecolor('#131212')
    fig.subplots_adjust(left=0.1, bottom=0.05, right=0.98, top=0.98)
    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=10, y=10)
def print_nozzle_9(frame,H,delta_st_n,delta_st_v,d_c_v,l_c_n,l_c_v,h_og,h_sr,phi,d_vh,h_ot):
    d_f=H*0.75
    d_c_n=d_f-(2*delta_st_n)
    x_otv = 0.5 * d_vh / (math.cos(phi * math.pi / 180))
    h_kon_otv=h_ot-(delta_st_n*math.tan(phi*math.pi/180))
    fig = Figure(figsize=(6.5, 6.5), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('#1A1A1A')  # 171717

    square = patches.Polygon(
        [[-0.5*d_c_n,0],[-0.5*d_f,0],[-0.5*d_f,l_c_n+delta_st_n],[-0.5*d_c_v-delta_st_v,l_c_n+delta_st_n],
         [-0.5*d_c_v-delta_st_v,l_c_n+l_c_v],[-0.5*d_c_v-(0.5*delta_st_v),l_c_n+l_c_v],[-0.5*d_c_v,l_c_n+l_c_v-(0.5*delta_st_v)],
         [-0.5*d_c_v,l_c_n],[-0.5*d_c_n,l_c_n]], edgecolor='#9E3C39',facecolor='none', hatch='/')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_c_n, 0], [0.5 * d_f, 0], [0.5 * d_f, l_c_n + delta_st_n],
         [0.5 * d_c_v + delta_st_v, l_c_n + delta_st_n],
         [0.5 * d_c_v + delta_st_v, l_c_n + l_c_v], [0.5 * d_c_v + (0.5 * delta_st_v), l_c_n + l_c_v],
         [0.5 * d_c_v, l_c_n + l_c_v - (0.5 * delta_st_v)],
         [0.5 * d_c_v, l_c_n], [0.5 * d_c_n, l_c_n]], edgecolor='#9E3C39', facecolor='none', hatch='/')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5 * d_c_n, 0], [-0.5 * d_f, 0], [-0.5 * d_f, l_c_n + delta_st_n],
         [-0.5 * d_c_v - delta_st_v, l_c_n + delta_st_n],
         [-0.5 * d_c_v - delta_st_v, l_c_n + l_c_v], [-0.5 * d_c_v - (0.5 * delta_st_v), l_c_n + l_c_v],
         [-0.5 * d_c_v, l_c_n + l_c_v - (0.5 * delta_st_v)],
         [-0.5 * d_c_v, l_c_n], [-0.5 * d_c_n, l_c_n]], edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_c_n, 0], [0.5 * d_f, 0], [0.5 * d_f, l_c_n + delta_st_n],
         [0.5 * d_c_v + delta_st_v, l_c_n + delta_st_n],
         [0.5 * d_c_v + delta_st_v, l_c_n + l_c_v], [0.5 * d_c_v + (0.5 * delta_st_v), l_c_n + l_c_v],
         [0.5 * d_c_v, l_c_n + l_c_v - (0.5 * delta_st_v)],
         [0.5 * d_c_v, l_c_n], [0.5 * d_c_n, l_c_n]], edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)


    square = patches.Polygon(
        [[-0.5*d_f,h_ot-x_otv],[-0.5*d_f,h_ot+x_otv],[-0.5*d_c_n,h_kon_otv+x_otv],[-0.5*d_c_n,h_kon_otv-x_otv]], edgecolor='#D44B46', facecolor='#131212')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_f, h_ot - x_otv], [0.5 * d_f, h_ot + x_otv], [0.5 * d_c_n, h_kon_otv + x_otv],
         [0.5 * d_c_n, h_kon_otv - x_otv]], edgecolor='#D44B46', facecolor='#131212')
    ax.add_patch(square)

    ax.plot([-0.5 * d_f, -0.5 * d_c_n], [h_ot, h_kon_otv], color="#D44B46", linestyle='-.')
    ax.plot([0.5* d_f,0.5 * d_c_n], [h_ot, h_kon_otv], color="#D44B46", linestyle='-.')

    ellipse = patches.Ellipse((0, h_kon_otv), d_vh, 2*x_otv, edgecolor='#D44B46', facecolor='none')
    ax.add_patch(ellipse)
    ax.plot([0, 0], [1.1*(h_kon_otv + x_otv), 0.9*(h_kon_otv - x_otv)], color="#D44B46", linestyle='-.')
    ax.plot([-1.1*x_otv, 1.1*x_otv], [h_kon_otv, h_kon_otv], color="#D44B46", linestyle='-.')

    ax.plot([-0.5*d_c_n, 0.5*d_c_n], [0, 0], color="#9E3C39")
    ax.plot([-0.5 * d_c_v, 0.5 * d_c_v], [l_c_n, l_c_n], color="#9E3C39")
    ax.plot([-0.5 * d_c_v, 0.5 * d_c_v], [l_c_n + l_c_v - (0.5 * delta_st_v), l_c_n + l_c_v - (0.5 * delta_st_v)], color="#9E3C39")
    ax.plot([-0.5 * d_c_v- (0.5 * delta_st_v), 0.5 * d_c_v + (0.5 * delta_st_v)], [l_c_n + l_c_v, l_c_n + l_c_v], color="#9E3C39")
    ax.plot([0, 0], [-0.1, 1.1*(l_c_n + l_c_v)], color="#D44B46", linestyle='-.')

    square = patches.Polygon(
        [[-0.5*d_f,0],[-0.5*H,0],[-0.5*H,h_og],[-0.5*d_f,h_og]], edgecolor='#9E3C39', facecolor='none', hatch='\\')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_f, 0], [0.5 * H, 0], [0.5 * H, h_og], [0.5 * d_f, h_og]], edgecolor='#9E3C39', facecolor='none',hatch='\\')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5*d_c_v-delta_st_v,l_c_n+delta_st_n], [-0.5*H,l_c_n+delta_st_n],[-0.5*H,l_c_n+delta_st_n+h_sr],[-0.5*d_c_v-delta_st_v,l_c_n+delta_st_n+h_sr]], edgecolor='#9E3C39', facecolor='none',
        hatch='\\')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_c_v + delta_st_v, l_c_n + delta_st_n], [0.5 * H, l_c_n + delta_st_n],
         [0.5 * H, l_c_n + delta_st_n + h_sr], [0.5 * d_c_v + delta_st_v, l_c_n + delta_st_n + h_sr]],
        edgecolor='#9E3C39', facecolor='none',
        hatch='\\')
    ax.add_patch(square)
#-------------------------------
    square = patches.Polygon(
        [[-0.5 * d_f, 0], [-0.5 * H, 0], [-0.5 * H, h_og], [-0.5 * d_f, h_og]], edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_f, 0], [0.5 * H, 0], [0.5 * H, h_og], [0.5 * d_f, h_og]], edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[-0.5 * d_c_v - delta_st_v, l_c_n + delta_st_n], [-0.5 * H, l_c_n + delta_st_n],
         [-0.5 * H, l_c_n + delta_st_n + h_sr], [-0.5 * d_c_v - delta_st_v, l_c_n + delta_st_n + h_sr]],
        edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)
    square = patches.Polygon(
        [[0.5 * d_c_v + delta_st_v, l_c_n + delta_st_n], [0.5 * H, l_c_n + delta_st_n],
         [0.5 * H, l_c_n + delta_st_n + h_sr], [0.5 * d_c_v + delta_st_v, l_c_n + delta_st_n + h_sr]],
        edgecolor='#D44B46', facecolor='none')
    ax.add_patch(square)


    ax.set_xlim(-1.1 * H / 2, 1.1 * H / 2)
    ax.set_ylim(-0.5, 1.1*(l_c_n+l_c_v))
    ax.tick_params(axis='x', colors='white', labelsize=10)
    ax.tick_params(axis='y', colors='white', labelsize=10)
    ax.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
    ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.title.set_color('white')
    ax.set_facecolor('#131212')
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.tick_params(axis='x', colors='white', labelsize=11)
    ax.tick_params(axis='y', colors='white', labelsize=11)
    fig.patch.set_facecolor('#131212')
    fig.subplots_adjust(left=0.1, bottom=0.05, right=0.98, top=0.98)
    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=10, y=10)