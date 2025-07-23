from scripts.sourcepdfrout import EncontrarPastaPDF
from scripts.sourcepdf import EncontrarPDF

p = EncontrarPastaPDF(input("Digite o caminho do diretório: "))



class Main:
    def __init__(self):
        pass

    def run(self):
        procura_pasta = EncontrarPastaPDF(input("Digite o caminho do diretório: "))
        caminho_encontrado = p.search_directory()
        pdf = EncontrarPDF(caminho_encontrado)
        pdf.search_pdfs()
        
        if self.caminho_pdf:
            print(f"Processando PDFs no diretório: {self.caminho_pdf}")
        else:
            print("Nenhum diretório válido encontrado.")