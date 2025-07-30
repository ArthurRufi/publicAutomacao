import shutil
import os


class DeletePDF:
    def __init__(self, caminho_pdf: str):
        self.caminho_pdf = caminho_pdf

    def delete(self):
        if os.path.isfile(self.caminho_pdf):
            try:
                os.remove(self.caminho_pdf)
                print(f"PDF deletado com sucesso: {self.caminho_pdf}")
                return True
            except Exception as e:
                print(f"Erro ao deletar o PDF: {e}")
                return False
        else:
            print(f"PDF não encontrado: {self.caminho_pdf}")
            return False