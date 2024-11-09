import math
import cantera as ct


def return_condition(gas, S, P):
    """--------------------Возвращает состояние газа при заданных P и S--------------------"""
    gas.SP = S, P * 10 ** 6
    gas.equilibrate('SP')
    return gas

def options_ks(choice, p_k, alpha, fuel, oxidizer, H_gor, H_ok, km0):
    """--------------------Поиск всех основных параметров в камере сгорания--------------------"""
    k0 = km0
    gas = ct.Solution('gri30_highT.yaml')
    # gas = ct.Solution('gri30.yaml')
    km = k0 * alpha
    # Расчёт энтальпии смеси
    m_gor = (1 / (1 + km))
    m_ok = 1 * km / (1 + km)
    H_sum = ((m_gor * H_gor) + (m_ok * H_ok)) * 1000
    # Задаём смешивание компонентов
    gas.set_equivalence_ratio(1 / (alpha), fuel, oxidizer)
    # Уравновешиваем состав при 300 К (иначе выдаёт ошибку в итерациях):
    gas.TP = 300, p_k * 10 ** 6
    gas.equilibrate('TP')
    # Уравновешиваем состав при заданной энатльпии смеси и заданном давлении:
    gas.HP = H_sum, p_k * 10 ** 6
    gas.equilibrate('HP')
    # Запоминаем параметры в камере для удобства использования в последующих расчётах
    T_k = gas.T
    R_k = gas.cp - gas.cv
    S_k = gas.s
    H_k = gas.h
    doc_excel = []
    properties = f"""Давление (p) = {gas.P / 10 ** 6:.5} МПа
Температура (T) = {gas.T:.2f} К
Удельный объём (v) = {gas.v:.2f} м3/кг
Энтропия (S) = {gas.s:.2f} Дж/кг*К
Полная энтальпия (I) = {gas.enthalpy_mass * 0.001:.2f} кДж/кг
Полная внутренняя энергия (U) = {gas.int_energy_mass * 0.001:.2f} кДж/кг
Молярная масса газовой фазы (MMg): {gas.mean_molecular_weight:.2f} г/моль
Газовая постоянная: {gas.cp - gas.cv:.2f} Дж/кг*К
"""
    doc_excel.append(str(gas.P / 10 ** 6))
    doc_excel.append(str(gas.T))
    doc_excel.append(str(gas.v))
    doc_excel.append(str(gas.s))
    doc_excel.append(str(gas.enthalpy_mass * 0.001))
    doc_excel.append(str(gas.int_energy_mass * 0.001))
    doc_excel.append(str(gas.mean_molecular_weight))
    doc_excel.append(str(gas.cp - gas.cv))
    if choice == 0:
        return_condition(gas, S_k, p_k)
        T_1 = gas.T
        P_1 = gas.P
        V_1 = gas.v
        S_1 = S_k
        # расчёт равновесной Cv
        gas.TD = T_1 * 1.00001, 1 / V_1
        gas.equilibrate('TV')
        U2 = gas.int_energy_mass
        gas.TD = T_1, 1 / V_1
        gas.equilibrate('TV')
        U1 = gas.int_energy_mass
        CVEQ = (U2 - U1) / (0.00001 * T_1)
        # Возвращаем всё, как было
        return_condition(gas, S_1, P_1 / 10 ** 6)
        # расчёт равновесной Cp
        gas.TP = T_1 * 1.01, P_1
        gas.equilibrate('TP')
        H2 = gas.enthalpy_mass
        gas.TP = T_1 * 0.99, P_1
        gas.equilibrate('TP')
        H1 = gas.enthalpy_mass
        CPEQ = (H2 - H1) / (0.02 * T_1)
        # Возвращаем всё, как было
        return_condition(gas, S_1, P_1 / 10 ** 6)
        properties += f"""------------Равновеснные параметры------------
Удельная теплоёмкость при постоянном давлении (Cp\'\') = {CPEQ:.2f} Дж/кг*К
Удельная теплоёмкость при постоянном объёме (Cv\'\') =  {CVEQ:.2f} Дж/кг*К
Показатель адиабаты (k\'\'): {CPEQ / CVEQ:.3f}
"""
        k_k = CPEQ / CVEQ
        doc_excel.append(str(CPEQ))
        doc_excel.append(str(CVEQ))
        doc_excel.append(str(CPEQ / CVEQ))
    else:
        properties += f"""------------Замороженные параметры------------
Удельная теплоёмкость при постоянном давлении (Cp) = {gas.cp:.2f} Дж/кг*К
Удельная теплоёмкость при постоянном объёме (Cv) = {gas.cv:.2f} Дж/кг*К
Показатель адиабаты (k): {gas.cp / gas.cv:.3f}
"""
        k_k = gas.cp / gas.cv
        doc_excel.append(str(gas.cp))
        doc_excel.append(str(gas.cv))
        doc_excel.append(str(gas.cp / gas.cv))
    # Получение и вывод массовых и мольных долей компонентов смеси
    mass_fractions = gas.Y
    mole_fractions = gas.X
    species_names = gas.species_names
    return properties, species_names, mass_fractions, mole_fractions, R_k, T_k, k_k, doc_excel

def find_temperature(p_k, alpha, fuel, oxidizer, H_gor, H_ok, km0):
    k0 = km0
    gas = ct.Solution('gri30_highT.yaml')
    km = k0 * alpha
    # Расчёт энтальпии смеси
    m_gor = (1 / (1 + km))
    m_ok = 1 * km / (1 + km)
    H_sum = ((m_gor * H_gor) + (m_ok * H_ok)) * 1000
    # Задаём смешивание компонентов
    gas.set_equivalence_ratio(1 / (alpha), fuel, oxidizer)
    # Уравновешиваем состав при 300 К (иначе выдаёт ошибку в итерациях):
    gas.TP = 300, p_k * 10 ** 6
    gas.equilibrate('TP')
    # Уравновешиваем состав при заданной энатльпии смеси и заданном давлении:
    gas.HP = H_sum, p_k * 10 ** 6
    gas.equilibrate('HP')
    # Запоминаем параметры в камере для удобства использования в последующих расчётах
    T_k = gas.T
    return T_k