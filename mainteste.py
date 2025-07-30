import sys
import os
from scripts.copy import CopyPDF
from scripts.routepdf import EncaminharPDF
from scripts.routercorrectdir import RouterCorrectDir
from scripts.sourcepdfrout import EncontrarPastaPDF
from scripts.sourcepdf import EncontrarPDF



#essa classe main vai definir o funcionamento da interface grafica de forma abstraida
class Main:
    def __init__(self):
        pass

    def run_copy_pdf(self):
        procura_pasta = EncontrarPastaPDF(input("Digite o caminho do diretório: "))
        pasta_final = EncontrarPastaPDF(input("Digite o caminho do diretório final: "))
        caminho_encontrado = procura_pasta.search_directory()
        caminho_final_encontrado = pasta_final.search_directory()
        pdfs = EncontrarPDF(caminho_encontrado)
        for pdf in pdfs.search_pdfs():
            copy_pdf = CopyPDF(f"{caminho_encontrado}\\{pdf}", caminho_final_encontrado)
            copy_pdf.copy()

m = Main()
m.run_copy_pdf()

