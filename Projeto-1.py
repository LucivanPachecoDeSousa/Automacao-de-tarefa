# AUTOMAÇÃO DE TAREFAS, AGENDA


import pyautogui
import time
import pandas as pd
import os
time.sleep(2)
os.system("C:\Tecnobyte\Agenda\Agenda.exe")
time.sleep(1)

pyautogui.hotkey("alt", "space")
pyautogui.press("down")
pyautogui.press("down")
pyautogui.press("down")
pyautogui.press("down")
time.sleep(1)
pyautogui.press("enter")

time.sleep(1)

tabela = pd.read_csv("tabela.csv")
dados = tabela.to_dict(orient="records")
tamanho_tabela = tabela.index

for linha in tamanho_tabela:
    print(dados[linha]["entidade"])
    entidade = dados[linha]
    pyautogui.click(x=51, y=125)

    time.sleep(0.8)

    pyautogui.write(entidade["entidade"])
    pyautogui.press("Tab")

    time.sleep(0.8)
    print(dados[linha]["nascimento"])
    nascimento = dados[linha]
    
    pyautogui.write(str(nascimento["nascimento"]))
    pyautogui.press("Tab")

    print(dados[linha]["endereco"])
    endereco = dados[linha]
    time.sleep(0.8)
    pyautogui.write(str(endereco["endereco"]))
    pyautogui.press("Tab")

    print(dados[linha]["bairro"])
    bairro = dados[linha]

    time.sleep(0.8)
    pyautogui.write(bairro['bairro'])
    pyautogui.press(["Tab"])

    print(dados[linha]["cep"])
    cep = dados[linha]

    time.sleep(0.8)
    pyautogui.write(str(cep["cep"]))
    pyautogui.press("Tab")


    print(dados[linha]["cidade"])
    cidade = dados[linha]

    time.sleep(0.8)
    pyautogui.write(cidade["cidade"])
    pyautogui.press("Tab")

    print(dados[linha]["estado"])
    estado = dados[linha]

    time.sleep(0.8)
    pyautogui.write(estado["estado"])
    pyautogui.press("Tab")
    pyautogui.press("Tab")

    time.sleep(0.8)

    print(dados[linha]["telefone"])
    telefone = dados[linha]
    pyautogui.write(str(telefone["telefone"]))
    pyautogui.press("Tab")
    pyautogui.press("Tab")
    pyautogui.press("Tab")
    pyautogui.press("enter")