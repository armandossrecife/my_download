import requests
from tqdm import tqdm  # Import for progress bar
from urllib.parse import urlparse
import os

class Util:
  def extrair_nome_extensao_url(self,url):
    # Faz o parse da URL
    parsed_url = urlparse(url)
    # Obtém o caminho do arquivo
    caminho_arquivo = parsed_url.path
    # Extrai o nome do arquivo e a extensão
    nome_arquivo, extensao = os.path.splitext(os.path.basename(caminho_arquivo))
    return nome_arquivo, extensao

class Download:
    def __init__(self, url, path_arquivo):
        self.url = url
        self.path_arquivo = path_arquivo
        self.callback = None # Function to be called for progress updates

    def set_callback(self, callback):
        self.callback = callback

    def executa(self):
        try:
            print('Aguarde...')
            response = requests.get(self.url, stream=True)  # Enable streaming for progress
            response.raise_for_status()  # Verifica se houve algum erro na requisição
            total_size = int(response.headers.get('content-length', 0))  # Get total file size
            with open(self.path_arquivo, 'wb') as file:
                with tqdm(total=total_size, unit='B', unit_scale=True, desc=self.path_arquivo) as pbar:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                            pbar.update(len(chunk))
                            if self.callback:
                                self.callback(total_size, pbar.n)  # Call the callback with total size and current progress
            print(f"Download completo. Tamanho: {total_size}, Arquivo salvo em: {self.path_arquivo}")
            return total_size
        except requests.exceptions.MissingSchema:
            print("URL inválida. Certifique-se de fornecer uma URL válida.")
            raise Exception('URL inválida. Certifique-se de fornecer uma URL válida.')
        except requests.exceptions.RequestException as e:
            print(f"Erro na conexão: {e}")
            raise Exception(f"Erro na conexão: {e}")