from entidades import Util, Download

class MyDownloadDummy:
    def __init__(self):
        self.utilidades = Util()
        self.my_var = ''
        self.filename = None
        self.progress_bar_value = 0
        self.progress_bar_maximum = 0
        self.my_msg = ''

    def set_filename(self, filename):
        self.filename = filename

    def set_msg(self, msg):
        self.my_msg = msg

    def download_with_progress_bar(self,url, path_arquivo=None):
        try:
            nome, extensao = self.utilidades.extrair_nome_extensao_url(url)
            filename = nome + extensao
            self.set_filename(filename)
            
            if path_arquivo: 
                download = Download(url, path_arquivo)
            else:
                download = Download(url, filename)

            def progress_callback(total_size, current_progress):
                percentual_avanco = int((current_progress/total_size)*100)
                self.my_var = str(int(percentual_avanco)) + '%'
                self.progress_bar_value = current_progress
                self.progress_bar_maximum = total_size

            download.set_callback(progress_callback)
            self.set_msg('Aguarde...')
            download.executa()
            self.set_msg(f'Download {self.filename} concluído com sucesso!')
        except Exception as ex:
            print(f'Erro: {str(ex)}')
            self.set_msg(f'Erro :{str(ex)}')
            self.my_var = '0%'
            self.progress_bar_value = 0