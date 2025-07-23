import os

#caminho = input("Digite o caminho da pasta: ").strip()
#caminhopro = "C:\\Users\\noteo\\Downloads"
#caminhofinal = "D:\\Automacao\\pdf"
# Garantir que o caminho termina com uma barra invertida
#if not caminhopro.endswith("\\"):
 #   caminhopro += "\\"

# Executar comando para listar PDFs


#for arquivo in caminho_pdf_add:
 #   ...


#------------------------------------------------------------------------#

class EncotrarPDF:
    def __init__(self, caminho_pdf : str):
        self.caminho_pdf = caminho_pdf


    def search_pdfs(self):
        # Implementar lógica para encontrar o PDF
        arquivos = os.listdir(f'{self.caminho_pdf}')
        caminho_pdf_add = []

        for arquivo in arquivos:
            if arquivo.endswith('.pdf'):
                caminho_pdf = os.path.join(arquivo)
                caminho_pdf_add.append(caminho_pdf)
                # Aqui você pode adicionar o código para transferir o PDF para outro local
                # Exemplo: shutil.move(caminho_pdf, destino)
        for n in caminho_pdf_add:
            print(f"PDF encontrado: {n}")

        return caminho_pdf_add