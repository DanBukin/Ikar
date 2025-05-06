import numpy as np
import tkinter as tk
from tkinter import filedialog

def print_circle(k,x,y,r_0,r_1,c_1,c_2):
    text=f"""
x_center_{k} = {x}  # X-координата центра
y_center_{k} = {y}  # Y-координата центра
radius_{k} = {r_0}     # Радиус окружности
radius_1_{k} = {r_1}     # Радиус окружности

iDocument2D.ksCircle(x_center_{k}, y_center_{k}, radius_{k}, {c_1})
iDocument2D.ksCircle(x_center_{k}, y_center_{k}, radius_1_{k}, {c_2})
"""
    return text
script_content = """# -*- coding: utf-8 -*-
#|Макрос_1

import pythoncom
from win32com.client import Dispatch, gencache

import LDefin2D
import MiscellaneousHelpers as MH

#  Подключим константы API Компас
kompas6_constants = gencache.EnsureModule("{75C9F5D0-B5B8-4526-8681-9903C567D2ED}", 0, 1, 0).constants
kompas6_constants_3d = gencache.EnsureModule("{2CAF168C-7961-4B90-9DA2-701419BEEFE3}", 0, 1, 0).constants

#  Подключим описание интерфейсов API5
kompas6_api5_module = gencache.EnsureModule("{0422828C-F174-495E-AC5D-D31014DBBE87}", 0, 1, 0)
kompas_object = kompas6_api5_module.KompasObject(Dispatch("Kompas.Application.5")._oleobj_.QueryInterface(kompas6_api5_module.KompasObject.CLSID, pythoncom.IID_IDispatch))
MH.iKompasObject = kompas_object

#  Подключим описание интерфейсов API7
kompas_api7_module = gencache.EnsureModule("{69AC2981-37C0-4379-84FD-5DD2F3C0A520}", 0, 1, 0)
application = kompas_api7_module.IApplication(Dispatch("Kompas.Application.7")._oleobj_.QueryInterface(kompas_api7_module.IApplication.CLSID, pythoncom.IID_IDispatch))
MH.iApplication = application

# Получаем активный документ
kompas_document = application.ActiveDocument
kompas_document_2d = kompas_api7_module.IKompasDocument2D(kompas_document)

# Получаем интерфейс для работы с 2D документом
iDocument2D = kompas_object.ActiveDocument2D()

"""
def save_cdm_1(X,Y,D_k,number_pr,delta_wall,delta):
    d_wall = (2 * (D_k / 2 - delta_wall) * np.sin(np.radians(180 / number_pr))) / (1 + np.sin(np.radians(180 / number_pr)))
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно tkinter
    file_path = filedialog.asksaveasfilename(defaultextension='.txt',
                                             filetypes=[("Text files", "*.cdm"), ("All files", "*.*")])
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(script_content)
        k = 1
        for x, y in zip(X, Y):
            file.write(print_circle(k,x,y,d_wall / 2,d_wall / 2 - delta / 2,4,5))
            k += 1
def save_cdm_2(X,Y,H,delta):
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно tkinter
    file_path = filedialog.asksaveasfilename(defaultextension='.txt',
                                             filetypes=[("Text files", "*.cdm"), ("All files", "*.*")])
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(script_content)
        k = 1
        for x, y in zip(X, Y):
            file.write(print_circle(k, x, y, H / 2, H / 2 - delta / 2, 4, 5))
            k += 1
def save_cdm_3(pr_x,pr_y,core_g_x,core_g_y,core_ok_x,core_ok_y,H,delta,choice,D_k,delta_wall,number_pr):
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно tkinter
    file_path = filedialog.asksaveasfilename(defaultextension='.txt',
                                             filetypes=[("Text files", "*.cdm"), ("All files", "*.*")])
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(script_content)
        file.write(f"""
x_center = 0
y_center = 0 
radius = {D_k/2} 
iDocument2D.ksCircle(x_center, y_center, radius, 1)
""")
        if choice<10:
            d_wall = (2 * (D_k / 2 - delta_wall) * np.sin(np.radians(180 / number_pr))) / (1 + np.sin(np.radians(180 / number_pr)))
            if choice==5 or choice==7 or choice==9:
                k = 1
                for x, y in zip(pr_x,pr_y):
                    file.write(print_circle(k, x, y, d_wall / 2, d_wall / 2 - delta / 2, 6, 7))
                    k += 1
            else:
                k = 1
                for x, y in zip(pr_x, pr_y):
                    file.write(print_circle(k, x, y, d_wall / 2, d_wall / 2 - delta / 2, 6, 1))
                    k += 1
        if choice==1 or choice==2 or choice==3 or choice==10 or choice==11 or choice==12:
            k = 1
            for x, y in zip(core_g_x, core_g_y):
                file.write(print_circle(k, x, y, H / 2, H / 2 - delta / 2, 6, 1))
                k += 1
            k = 1
            for x, y in zip(core_ok_x, core_ok_y):
                file.write(print_circle(k, x, y, H / 2, H / 2 - delta / 2, 6, 2))
                k += 1
        else:
            k = 1
            for x, y in zip(core_g_x, core_g_y):
                file.write(print_circle(k, x, y, H / 2, H / 2 - delta / 2, 6, 7))
                k += 1
