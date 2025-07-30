#aqui vai o caminho para o qual o script vai transferir o PDF
from scripts.routercorrectdir import RouterCorrectDir
import os


#verificar possivel abstração futura para receber mais tipos de arquivos
class EncaminharPDF:
    def __init__(self, caminho_pdf: str):
        self.caminho_pdf = caminho_pdf

    def encaminhar(self):
        caminho_corrigido = RouterCorrectDir(self.caminho_pdf).get_correct_path()
        
        if os.path.isfile(caminho_corrigido):
            print(f"PDF encontrado e pronto para ser transferido: {caminho_corrigido}")
            return caminho_corrigido
        else:
            print(f"PDF não encontrado: {caminho_corrigido}")
            return None