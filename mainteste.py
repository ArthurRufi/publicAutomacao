"""
from scripts.copy import CopyPDF
from scripts.routepdf import EncaminharPDF
from scripts.routercorrectdir import RouterCorrectDir
from scripts.sourcepdfrout import EncontrarPastaPDF
from scripts.sourcepdf import EncontrarPDF




class Main:
    def __init__(self):
        pass

    def run(self):
        procura_pasta = EncontrarPastaPDF(input("Digite o caminho do diretório: "))
        pasta_final = EncontrarPastaPDF(input("Digite o caminho do diretório final: "))
        caminho_encontrado = procura_pasta.search_directory()
        caminho_final_encontrado = pasta_final.search_directory()
        pdfs = EncontrarPDF(caminho_encontrado)
        for pdf in pdfs.search_pdfs():
            # Aqui você pode chamar a classe EncaminharPDF ou CopyPDF para processar o PDF encontrado
            # Exemplo:
            
            # ou
            #ARRUMAR LOGICA PARA ENCAMINHAR CAMINHO CORRETO
            copy_pdf = CopyPDF(f"{caminho_encontrado}\\{pdf}", caminho_final_encontrado)
            copy_pdf.copy()

m = Main()
m.run()
"""
