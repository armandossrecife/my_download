import tkinter as tk
from tkinter import ttk
from entidades import Util, Download

class MyWindow:
    def __init__(self, app) -> None:
        self.utilidades = Util()
        self.app = app
        self.filename = None

        # URL label
        self.ulr_label = ttk.Label(self.app, text='Informe a URL do arquivo')
        self.ulr_label.pack()

        # URL Entry
        self.url_var = tk.StringVar()
        self.url_entry = ttk.Entry(self.app, textvariable=self.url_var, width=90)
        self.url_entry.pack()

        # Label to message
        self.my_msg = tk.StringVar()
        self.label_msg = ttk.Label(self.app, textvariable=self.my_msg)
        self.label_msg.pack()

        # Label to show progress
        self.my_var= tk.StringVar()
        self.label = ttk.Label(self.app, textvariable=self.my_var)
        self.label.pack()

        # Progress bar
        self.progress_bar = ttk.Progressbar(self.app, orient="horizontal", length=400, mode="determinate")
        self.progress_bar.pack()
        
        # Download button
        self.download_button = ttk.Button(self.app, text="Download", command=lambda: self.download_with_progress_bar(self.url_var.get()))
        self.download_button.pack()

    def set_title(self, title):
        self.app.title(title)

    def set_filename(self, filename):
        self.filename = filename

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
                self.my_var.set(str(int(percentual_avanco)) + '%')
                self.progress_bar["value"] = current_progress
                self.progress_bar["maximum"] = total_size
                self.progress_bar.update_idletasks()

            download.set_callback(progress_callback)
            self.my_msg.set('Aguarde...')
            download.executa()
            self.my_msg.set(f'Download {self.filename} concluído com sucesso!')
        except Exception as ex:
            print(f'Erro: {str(ex)}')
            self.my_msg.set(f'Erro :{str(ex)}')
            self.my_var.set('0%')
            self.progress_bar['value'] = 0
