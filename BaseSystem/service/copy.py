import shutil
import os
#aqui vai para abstrações sobre routepdf.py e copy

class CopyPDF:
    def __init__(self, caminho_pdf: str, destino: str):
        self.caminho_pdf = caminho_pdf
        self.destino = destino

    def copy(self):
        if os.path.isfile(self.caminho_pdf):
            try:
                shutil.copy(self.caminho_pdf, self.destino)
                print(f"PDF copiado com sucesso para: {self.destino}")
                return True
            except Exception as e:
                print(f"Erro ao copiar o PDF: {e}")
                return False
        else:
            print(f"PDF não encontrado: {self.caminho_pdf}")
            return False