import unittest
import requests_mock
from entidades import Download
from unittest.mock import MagicMock
import tqdm

class TestDownload(unittest.TestCase):

    @requests_mock.Mocker()
    def test_executa_invalid_url(self, mock):
        url = 'invalid_url'  # Missing scheme
        path_arquivo = 'downloaded_file.txt'
        with self.assertRaises(Exception) as context:
            download = Download(url, path_arquivo)
            download.executa()
        self.assertEqual(str(context.exception), "URL inválida. Certifique-se de fornecer uma URL válida.")

    @requests_mock.Mocker()
    def test_executa_network_error(self, mock):
        url = 'https://example.com/file'
        path_arquivo = 'downloaded_file.txt'
        mock.get(url, status_code=500)  # Simulate a network error
        with self.assertRaises(Exception) as context:
            download = Download(url, path_arquivo)
            download.executa()
        self.assertIn("Erro na conexão", str(context.exception))

    @requests_mock.Mocker()
    def test_executa_file_saving_error(self, mock):
        url = 'https://example.com/file'
        path_arquivo = '/unwritable/path/file.txt'  # Unwritable path
        mock.get(url, content=b'Some content\nSome content\nSome content\nSome content\nSome content\nSome content\nSome content\nSome content\nSome content\nSome content')
        with self.assertRaises(Exception) as context:
            download = Download(url, path_arquivo)
            download.executa()
        self.assertIn("No such file or directory:", str(context.exception))

    def test_executa_download_com_sucesso(self):
        url = 'https://raw.githubusercontent.com/armandossrecife/teste/main/my_file.txt'
        path_arquivo = 'downloaded_file.txt'
        download = Download(url, path_arquivo)
        download.executa()