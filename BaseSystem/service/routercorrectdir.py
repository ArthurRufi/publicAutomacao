from pathlib import Path
import platform

class ValidateOS:
    def __init__(self):
        self.os_name = platform.system()

    def this_os(self):
        if self.os_name not in ['Windows', 'Linux', 'Darwin']:
            raise ValueError("Unsupported OS name. Use 'Windows', 'Linux', or 'Darwin'.")
        return self.os_name

class RouterCorrectDir:
    def __init__(self, caminho_pdf: str):
        caminho_pdf = caminho_pdf.replace('"', '').replace("'", '')  # remove aspas da string
        self.caminho_pdf = Path(caminho_pdf)
        self.validate_os = ValidateOS()

        
    def get_correct_path(self):
        os_name = self.validate_os.this_os()
        if os_name in ['Windows', 'Linux', 'Darwin']:
            # Retorna a string do caminho formatada para o SO atual (ainda nao testado no MacOS)
            return str(self.caminho_pdf)
        else:
            raise ValueError("Unsupported OS for path correction.")

