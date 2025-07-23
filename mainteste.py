from scripts.sourcepdfrout import EncontrarPastaPDF
from scripts.sourcepdf import EncotrarPDF

p = EncontrarPastaPDF(input("Digite o caminho do diretório: "))

caminho_encontrado = p.search_directory()

pdf = EncotrarPDF(caminho_encontrado)
pdf.search_pdfs()