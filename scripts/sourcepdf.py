import os

#criar futura abstração para receber mais que um tipo de arquivo
class EncontrarPDF:
    def __init__(self, caminho_pdf : str):
        self.caminho_pdf = caminho_pdf


    def search_pdfs(self):
        #lembrete: lógica para encontrar o PDF
        arquivos = os.listdir(f'{self.caminho_pdf}')
        caminho_pdf_add = []

        for arquivo in arquivos:
            if arquivo.endswith('.pdf'):
                caminho_pdf = os.path.join(arquivo)
                caminho_pdf_add.append(caminho_pdf)
        for n in caminho_pdf_add:
            print(f"PDF encontrado: {n}")

        return caminho_pdf_add