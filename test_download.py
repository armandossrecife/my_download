import unittest
import requests_mock
from entidades import Download
import os

class TestDownload(unittest.TestCase):

    @requests_mock.Mocker()
    def test_executa(self, mock):
        url = 'https://raw.githubusercontent.com/armandossrecife/teste/main/my_file.txt'
        path_arquivo = 'downloaded_file.txt'
        mock.get(url, content=b'Some file content')

        download = Download(url, path_arquivo)
        download.executa()

        self.assertTrue(os.path.exists(path_arquivo))
        with open(path_arquivo, 'rb') as f:
            content = f.read()
        self.assertEqual(content, b'Some file content')