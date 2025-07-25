from pathlib import Path
from tkinter import Tk, filedialog

def selecionar_pasta():
    root = Tk()
    root.withdraw()  # esconde a janela principal
    caminho = filedialog.askdirectory(title="Selecione uma pasta")
    root.destroy()  # fecha o Tk depois da escolha
    # Se o usuário cancelar, retorna None
    return Path(caminho) if caminho else None

