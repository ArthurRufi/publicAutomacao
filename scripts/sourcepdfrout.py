class EncontrarPastaPDF:
    def __init__(self, caminho_diretorio):
        self.caminho_pdf = caminho_diretorio

    #procura se o caminho enviado é um diretorio
    def search_directory(self):
        if os.path.isdir(self.caminho_pdf):
            print(f"Diretório encontrado: {self.caminho_pdf}")
            return str(self.caminho_pdf)
        else:
            print(f"Diretório não encontrado: {self.caminho_pdf}")
            return None