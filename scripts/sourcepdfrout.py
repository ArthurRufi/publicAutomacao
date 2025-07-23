import os
from scripts.routercorrectdir import RouterCorrectDir

class EncontrarPastaPDF:
    def __init__(self, caminho_diretorio):
        self._caminho_diretorio = caminho_diretorio

    #procura se o caminho enviado é um diretorio
    def search_directory(self):
        caminhocorrigido = RouterCorrectDir(self._caminho_diretorio).get_correct_path()

        if os.path.isdir(caminhocorrigido):
            print(f"Diretório encontrado: {caminhocorrigido}")
            return str(caminhocorrigido)
        else:
            print(f"Diretório não encontrado: {caminhocorrigido}")
            return None