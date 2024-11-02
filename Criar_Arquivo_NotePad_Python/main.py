import pyautogui
import time

#Tempo em que ira comecar
time.sleep(4)

#Entrar no Bloco de Notas
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write("notepad", interval=0.1)
pyautogui.press('enter')
time.sleep(3)

#Escreve no Bloco de Notas
pyautogui.write("---> Programa by Danielluiz07 <---", interval=0.1)
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write("Arquivo Criado com sucesso!", interval=0.1)
pyautogui.press('enter')

#Salva Arquivo
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write("arquivo-teste.txt", interval=0.1)
time.sleep(1)
pyautogui.press('enter')