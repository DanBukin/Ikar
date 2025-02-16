import xlsxwriter
import tkinter as tk
from tkinter import filedialog


def save_all_properties(user):
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно tkinter
    file_path = filedialog.asksaveasfilename(defaultextension='.xlsx',
                                             filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    if file_path:  # Если путь был выбран

        workbook = xlsxwriter.Workbook(file_path)
        worksheet = workbook.add_worksheet()
        data_format = workbook.add_format({'bg_color': '#C44642'})
        for i in range(0, 15):
            worksheet.write_string(i, 3, "", cell_format=data_format)  # Столбец
            worksheet.write_string(i, 0, "", cell_format=data_format)  # Столбец
        for i in range(0, 5):
            worksheet.write_string(i, 6, "", cell_format=data_format)  # Столбец
            worksheet.write_string(i, 9, "", cell_format=data_format)  # Столбец
        for i in range(0, 4):
            worksheet.write_string(15, i, "", cell_format=data_format)  # Строка
        for i in range(0, 10):
            worksheet.write_string(0, i, "", cell_format=data_format)  # Строка
        for i in range(4, 10):
            worksheet.write_string(5, i, "", cell_format=data_format)  # Строка
        worksheet.write(1, 1, 'Ядро:')
        if user.choice==1 or user.choice==2 or user.choice==3 or user.choice==10 or user.choice==11 or user.choice==12:
            worksheet.write(1, 2, 'Однокомпонентное')
        else:
            worksheet.write(1, 2, 'Двухкомпонентное')
        worksheet.write(2, 1, 'Пристенок:')
        if user.choice==1 or user.choice==2 or user.choice==3 or user.choice==4 or user.choice==6 or user.choice==8:
            worksheet.write(2, 2, 'Однокомпонентный')
        elif user.choice==5 or user.choice==7 or user.choice==9:
            worksheet.write(2, 2, 'Двухкомпонентный')
        else:
            worksheet.write(2, 2, 'Отсутствует')
        worksheet.write(3, 1, 'Схема:')
        if user.choice==1 or user.choice==4 or user.choice==5 or user.choice==13 or user.choice==10:
            worksheet.write(3, 2, 'Шахматная')
        elif user.choice==2 or user.choice==6 or user.choice==7 or user.choice==14 or user.choice==11:
            worksheet.write(3, 2, 'Сотовая')
        else:
            worksheet.write(3, 2, 'Концентрическая')
        worksheet.write(4, 1, 'Диаметр камеры, мм:')
        worksheet.write(4, 2, float(user.D_k))
        worksheet.write(6, 1, 'Рекомендуемый шаг, мм:')
        worksheet.write(6, 2, float(round((user.D_k**0.5))))
        worksheet.write(7, 1, 'Выбранный шаг, мм:')
        worksheet.write(7, 2, float(user.H))
        worksheet.write(8, 1, 'Расстояние между форсунками, мм:')
        worksheet.write(8, 2, float(user.delta))
        worksheet.write(9, 1, 'Расстояние до огневой стенки, мм:')
        worksheet.write(9, 2, float(user.delta_wall))
        worksheet.write(10, 1, 'Расстояние от шага ядра до пристенка, мм:')
        if user.choice==13 or user.choice==14 or user.choice==15 or user.choice==11 or user.choice==12 or user.choice==10:
            worksheet.write(10, 2, "нет пристенка")
        else:
            worksheet.write(10, 2, float(user.delta_y_pr))
        worksheet.write(11, 1, 'Количество форсунок пристенка:')
        if user.choice==13 or user.choice==14 or user.choice==15 or user.choice==11 or user.choice==12 or user.choice==10:
            worksheet.write(11, 2, "нет пристенка")
        else:
            worksheet.write(11, 2, float(user.number_pr))
        worksheet.write(12, 1, '2-ой пристеночный слой:')
        if user.second_layer==1 or user.second_layer==0:
            worksheet.write(12, 2, 'Отсутствует')
        else:
            worksheet.write(12, 2, 'Есть')
        worksheet.write(13, 1, 'Диаметр форсунок в ядре, мм:')
        worksheet.write(13, 2, float(user.D_y))
        worksheet.write(14, 1, 'Диаметр форсунок в пристенке, мм:')
        if user.choice==13 or user.choice==14 or user.choice==15 or user.choice==11 or user.choice==12 or user.choice==10:
            worksheet.write(14, 2, "нет пристенка")
        else:
            worksheet.write(14, 2, float(user.D_prist))
        worksheet.write(1, 4, 'Количество форсунок:')
        worksheet.write(2, 4, 'Ядро:')
        worksheet.write(3, 4, 'Горючее:')
        worksheet.write(3, 5, int(user.n_g_y))
        worksheet.write(4, 4, 'Окислитель:')
        worksheet.write(4, 5, int(user.n_o_y))
        worksheet.write(2, 7, 'Пристенок:')
        worksheet.write(3, 7, 'Горючее:')
        worksheet.write(3, 8, int(user.n_g_pr))
        worksheet.write(4, 7, 'Окислитель:')
        worksheet.write(4, 8, int(user.n_o_pr))

        worksheet.write(16, 1, 'Ядро (Горючее)')
        worksheet.write(17, 1, 'X,мм')
        worksheet.write(17, 2, 'Y, мм')
        worksheet.write(16, 4, 'Ядро (Окислитель)')
        worksheet.write(17, 4, 'X,мм')
        worksheet.write(17, 5, 'Y, мм')
        i_1=18
        for x, y in zip(user.coord_y_g_x, user.coord_y_g_y):
            worksheet.write(i_1, 1, float(x))
            worksheet.write(i_1, 2, float(y))
            i_1+=1
        i_2=18
        for x, y in zip(user.coord_y_ok_x, user.coord_y_ok_y):
            worksheet.write(i_2, 4, float(x))
            worksheet.write(i_2, 5, float(y))
            i_2+=1
        if user.choice==5 or user.choice==7 or user.choice==9:
            worksheet.write(16, 7, 'Пристенок (2-комп.)')
            worksheet.write(17, 7, 'X,мм')
            worksheet.write(17, 8, 'Y, мм')
            i_3=18
            for x, y in zip(user.coord_pr_g_x, user.coord_pr_g_y):
                worksheet.write(i_3, 7, float(x))
                worksheet.write(i_3, 8, float(y))
                i_3 += 1
            i_4 = max(i_1, i_2, i_3)
        elif user.choice==1 or user.choice==2 or user.choice==3 or user.choice==4 or user.choice==6 or user.choice==8:
            worksheet.write(16, 7, 'Пристенок (Горючее)')
            worksheet.write(17, 7, 'X,мм')
            worksheet.write(17, 8, 'Y, мм')
            i_3 = 18
            for x, y in zip(user.coord_pr_g_x, user.coord_pr_g_y):
                worksheet.write(i_3, 7, float(x))
                worksheet.write(i_3, 8, float(y))
                i_3 += 1
            i_4 = max(i_1, i_2, i_3)
        else:
            i_4 = max(i_1, i_2)

        for i in range(0, 7):
            worksheet.write_string(15, i, "", cell_format=data_format)  # Строка
        for i in range(0, 7):
            worksheet.write_string(i_4, i, "", cell_format=data_format)  # Строка
        for i in range(16, i_4):
            worksheet.write_string(i, 0, "", cell_format=data_format)  # Столбец
            worksheet.write_string(i, 3, "", cell_format=data_format)  # Столбец
            worksheet.write_string(i, 6, "", cell_format=data_format)  # Столбец
        if user.choice!=10 and user.choice!=11 and user.choice!=12 and user.choice!=13 and user.choice!=14 and user.choice!=15:
            for i in range(16, i_4):
                worksheet.write_string(i, 9, "", cell_format=data_format)  # Столбец
            for i in range(0, 10):
                worksheet.write_string(15, i, "", cell_format=data_format)  # Строка
            for i in range(0, 10):
                worksheet.write_string(i_4, i, "", cell_format=data_format)  # Строка

        worksheet.write(i_4 + 1, 1, 'Суммарный расход, кг/с')
        worksheet.write(i_4 + 2, 1, 'Соотношение компонентов в ядре')
        worksheet.write(i_4 + 3, 1, 'Соотношение компонентов в ВГГ')
        worksheet.write(i_4 + 4, 1, 'Соотношение компонентов в ОГГ')
        worksheet.write(i_4 + 5, 1, 'Доля расхода на пристенок, %')
        worksheet.write(i_4 + 6, 1, 'Соотношение компонентов в пристенке')

        worksheet.write(i_4 + 1, 2, float(user.a))
        worksheet.write(i_4 + 2, 2, float(user.b))
        worksheet.write(i_4 + 3, 2, float(user.c))
        worksheet.write(i_4 + 4, 2, float(user.d))
        worksheet.write(i_4 + 5, 2, float(user.f))
        worksheet.write(i_4 + 6, 2, float(user.g))

        worksheet.write(i_4 + 1, 4, 'm_пр_г_вгг, кг/с')
        worksheet.write(i_4 + 2, 4, 'm_пр_ок_вгг, кг/с')
        worksheet.write(i_4 + 3, 4, 'm_пр_г_огг, кг/с')
        worksheet.write(i_4 + 4, 4, 'm_пр_ок_огг, кг/с')
        worksheet.write(i_4 + 5, 4, 'm_я_г_вгг, кг/с')
        worksheet.write(i_4 + 6, 4, 'm_я_ок_вгг, кг/с')
        worksheet.write(i_4 + 7, 4, 'm_я_г_огг, кг/с')
        worksheet.write(i_4 + 8, 4, 'm_я_ок_огг, кг/с')

        worksheet.write(i_4 + 1, 5, float(user.x_1))
        worksheet.write(i_4 + 2, 5, float(user.x_2))
        worksheet.write(i_4 + 3, 5, float(user.x_3))
        worksheet.write(i_4 + 4, 5, float(user.x_4))
        worksheet.write(i_4 + 5, 5, float(user.x_5))
        worksheet.write(i_4 + 6, 5, float(user.x_6))
        worksheet.write(i_4 + 7, 5, float(user.x_7))
        worksheet.write(i_4 + 8, 5, float(user.x_8))
        i_5 = i_4 + 9
        for i in range(i_4, i_5):
            worksheet.write_string(i, 0, "", cell_format=data_format)  # Столбец
            worksheet.write_string(i, 3, "", cell_format=data_format)  # Столбец
            worksheet.write_string(i, 6, "", cell_format=data_format)  # Столбец
        for i in range(0, 13):
            worksheet.write_string(i_5, i, "", cell_format=data_format)  # Строка

        worksheet.write(i_5 + 1, 1, 'Расчетные площадки (Метод Иевлева)')
        worksheet.write(i_5 + 2, 1, 'X (горючее), мм')
        worksheet.write(i_5 + 2, 2, 'Y (горючее), мм')
        worksheet.write(i_5 + 2, 4, 'm (горючее), кг/с')
        worksheet.write(i_5 + 2, 7, 'X (окислитель), мм')
        worksheet.write(i_5 + 2, 8, 'Y (окислитель), мм')
        worksheet.write(i_5 + 2, 10, 'm (окислитель), кг/с')

        for i in range(len(user.coord_gor)):
            x, y, z = user.coord_gor[i]
            worksheet.write(i_5 + 3+i, 1, float(x))
            worksheet.write(i_5 + 3 + i, 2, float(y))
            worksheet.write(i_5 + 3 + i, 4, float(z))
        i_6=i_5 +len(user.coord_gor)+3
        for i in range(len(user.coord_ok)):
            x, y, z = user.coord_ok[i]
            worksheet.write(i_5 + 3+i, 7, float(x))
            worksheet.write(i_5 + 3 + i, 8, float(y))
            worksheet.write(i_5 + 3 + i, 10, float(z))
        i_7=i_5 +len(user.coord_ok)+3
        i_8=max(i_6,i_7)
        for i in range(0, 13):
            worksheet.write_string(i_8, i, "", cell_format=data_format)  # Строка
        for i in range(i_5, i_8):
            worksheet.write_string(i, 0, "", cell_format=data_format)  # Столбец
            worksheet.write_string(i, 6, "", cell_format=data_format)  # Столбец
            worksheet.write_string(i, 12, "", cell_format=data_format)  # Столбец

        worksheet.write(i_8 + 1, 1, 'Расход ф-ки гор. в ядре, кг/с')
        worksheet.write(i_8 + 2, 1, 'Расход ф-ки ок. в ядре, кг/с')
        worksheet.write(i_8 + 3, 1, 'Расход ф-ки гор. в пристенке, кг/с')
        worksheet.write(i_8 + 4, 1, 'Расход ф-ки ок. в пристенке, кг/с')

        worksheet.write(i_8 + 1, 2, float(user.m_f_g_y))
        worksheet.write(i_8 + 2, 2, float(user.m_f_o_y))
        worksheet.write(i_8 + 3, 2, float(user.m_f_g_pr))
        worksheet.write(i_8 + 4, 2, float(user.m_f_o_pr))
        i_9=i_8 + 5
        for i in range(0, 13):
            worksheet.write_string(i_9, i, "", cell_format=data_format)  # Строка
        for i in range(i_8, i_9):
            worksheet.write_string(i, 0, "", cell_format=data_format)  # Столбец
            worksheet.write_string(i, 3, "", cell_format=data_format)  # Столбец
        worksheet.write(i_9 + 1, 1, 'Распределение km')
        worksheet.write(i_9 + 2, 1, 'X, мм')
        worksheet.write(i_9 + 2, 2, 'Y, мм')
        worksheet.write(i_9 + 2, 4, 'km')
        k=1
        for x,y,z in zip(user.graph_x_1,user.graph_y_1,user.graph_z_1):
            worksheet.write(i_9 + 2+k, 1, float(x))
            worksheet.write(i_9 + 2 + k, 2, float(y))
            worksheet.write(i_9 + 2 + k, 4, float(z))
            k+=1
        i_10=i_9+2+k
        worksheet.write(i_9 + 1, 7, 'По радиусу')
        worksheet.write(i_9 + 2, 7, 'R, мм')
        worksheet.write(i_9 + 2, 8, 'km')
        k = 1
        for x, y in zip(user.graph_x_2, user.graph_y_2):
            worksheet.write(i_9 + 2+k, 7, float(x))
            worksheet.write(i_9 + 2 + k, 8, float(y))
            k+=1
        i_11 = i_9 + 2 + k
        worksheet.write(i_9 + 1, 10, 'По углу')
        worksheet.write(i_9 + 2, 10, 'угол, град')
        worksheet.write(i_9 + 2, 11, 'km')
        k=1
        for x, y in zip(user.graph_x_3, user.graph_y_3):
            worksheet.write(i_9 + 2+k, 10, float(x))
            worksheet.write(i_9 + 2 + k, 11, float(y))
            k+=1
        i_12=i_9 + 2 + k
        i_13=max(i_10,i_11,i_12)
        for i in range(0, 13):
            worksheet.write_string(i_13, i, "", cell_format=data_format)  # Строка
        for i in range(i_9, i_13):
            worksheet.write_string(i, 0, "", cell_format=data_format)  # Столбец
            worksheet.write_string(i, 6, "", cell_format=data_format)  # Столбец
            worksheet.write_string(i, 9, "", cell_format=data_format)  # Столбец
            worksheet.write_string(i, 12, "", cell_format=data_format)  # Столбец
        for i in range(0, 13):
            worksheet.write_string(i_13+4, i, "", cell_format=data_format)  # Строка
        for i in range(i_13, i_13+4):
            worksheet.write_string(i, 0, "", cell_format=data_format)  # Столбец
            worksheet.write_string(i, 3, "", cell_format=data_format)  # Столбец
        worksheet.write(i_13 + 1, 1, 'Окислитель:')
        worksheet.write(i_13 + 1, 2, str(user.formula_ox))
        worksheet.write(i_13 + 2, 1, 'Горючее:')
        worksheet.write(i_13 + 2, 2, str(user.formula_gor))
        worksheet.write(i_13 + 3, 1, 'Давление в КС, МПа:')
        worksheet.write(i_13 + 3, 2, float(user.p_k))
        worksheet.write(i_13 + 5, 1, 'Распределение температуры')
        worksheet.write(i_13 + 6, 1, 'X, мм')
        worksheet.write(i_13 + 6, 2, 'Y, мм')
        worksheet.write(i_13 + 6, 4, 'T, К')
        k = 1
        for x, y, z in zip(user.x_1_T, user.y_1_T, user.z_1_T):
            worksheet.write(i_13 + 6 + k, 1, float(x))
            worksheet.write(i_13 + 6 + k, 2, float(y))
            worksheet.write(i_13 + 6 + k, 4, float(z))
            k += 1
        i_14=i_13+6+k
        worksheet.write(i_13 + 5, 7, 'По радиусу')
        worksheet.write(i_13 + 6, 7, 'R, мм')
        worksheet.write(i_13 + 6, 8, 'T, К')
        k = 1
        for x, y in zip(user.x_2_T, user.y_2_T):
            worksheet.write(i_13 + 6 + k, 7, float(x))
            worksheet.write(i_13 + 6 + k, 8, float(y))
            k += 1
        i_15 = i_13 + 6 + k
        worksheet.write(i_13 + 5, 10, 'По углу')
        worksheet.write(i_13 + 6, 10, 'угол, град')
        worksheet.write(i_13 + 6, 11, 'Т, К')
        k = 1
        for x, y in zip(user.x_3_T, user.y_3_T):
            worksheet.write(i_13 + 6 + k, 10, float(x))
            worksheet.write(i_13 + 6 + k, 11, float(y))
            k += 1
        i_16 = i_13 + 6 + k
        i_17=max(i_14,i_15,i_16)
        for i in range(0, 13):
            worksheet.write_string(i_17, i, "", cell_format=data_format)  # Строка
        for i in range(i_13+4, i_17):
            worksheet.write_string(i, 0, "", cell_format=data_format)  # Столбец
            worksheet.write_string(i, 6, "", cell_format=data_format)  # Столбец
            worksheet.write_string(i, 9, "", cell_format=data_format)  # Столбец
            worksheet.write_string(i, 12, "", cell_format=data_format)  # Столбец
#----------------------Настройка высоты строк---------------------------
        worksheet.set_row(0, 7)
        worksheet.set_row(5, 7)
        worksheet.set_row(15, 7)
        worksheet.set_row(i_4, 7)
        worksheet.set_row(i_5, 7)
        worksheet.set_row(i_8, 7)
        worksheet.set_row(i_9, 7)
        worksheet.set_row(i_13, 7)
        worksheet.set_row(i_13+4, 7)
        worksheet.set_row(i_17, 7)
# ----------------------Настройка ширины столбцов---------------------------
        worksheet.set_column(0, 0, 0.7)
        worksheet.set_column(1, 1, 34.44)
        worksheet.set_column(2, 2, 18.11)
        worksheet.set_column(3, 3, 0.7)
        worksheet.set_column(4, 4, 19.67)
        worksheet.set_column(5, 5, 11.9)
        worksheet.set_column(6, 6, 0.7)
        worksheet.set_column(7, 7, 18.44)
        worksheet.set_column(8, 8, 16.22)
        worksheet.set_column(9, 9, 0.7)
        worksheet.set_column(10, 10, 14.11)
        worksheet.set_column(11, 11, 13.33)
        worksheet.set_column(12, 12, 0.7)
        workbook.close()