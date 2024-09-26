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

formatter = FuncFormatter(lambda x, _: f"{x:.0f}")
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

def print_dot(coord,D_k,frame, H,n):
    fig = Figure(figsize=(7.7, 7.7), dpi=100)
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
    fig.subplots_adjust(left=0.07, bottom=0.05, right=0.98, top=0.98)
    # Установите форматирование для осей X и Y
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    # Обновите параметры тиков после изменения меток, если нужно
    ax.tick_params(axis='x', colors='white', labelsize=15)  # Используйте свой размер шрифта
    ax.tick_params(axis='y', colors='white', labelsize=15)  # Используйте свой размер шрифта
    ax.set_xlim(- H, D_k / 2 + H)
    ax.set_ylim(- H, D_k / 2 + H)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=10, y=50)
    print(f'Количетво площадок для расчёта равно: {k}')
    return k,centers_square,angles_square

def draw_circle_with_points(center_x, center_y, points_itog, H,D,frame,k):
    fig = Figure(figsize=(7.7, 7.7), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('#171717')

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
    fig.patch.set_facecolor('#171717')
    ax.set_facecolor('#171717')
    fig.subplots_adjust(left=0.07, bottom=0.05, right=0.98, top=0.98)
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.tick_params(axis='x', colors='white', labelsize=11)
    ax.tick_params(axis='y', colors='white', labelsize=11)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame - это контейнер, где должен быть размещен график
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=10, y=770*k+10)
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