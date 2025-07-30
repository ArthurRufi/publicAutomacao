import os


class DeletePDF:
    def __init__(self, caminho_pdf):
        self.caminho_pdf = caminho_pdf

    def delete(self):
        try:
            os.remove(self.caminho_pdf)
            print(f"Arquivo {self.caminho_pdf} deletado com sucesso.")
        except Exception as e:
            print(f"Erro ao deletar o arquivo {self.caminho_pdf}: {e}")