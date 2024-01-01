import unittest
from entidades import Util

class TestUtil(unittest.TestCase):
    def setUp(self):
        self.util = Util()
        
    def test_extrair_nome_extensao_url_valid_url_with_filename_and_extension(self):
        url = 'https://example.com/path/to/file.txt'
        nome, extensao = self.util.extrair_nome_extensao_url(url)
        self.assertEqual(nome, 'file')
        self.assertEqual(extensao, '.txt')

    def test_extrair_nome_extensao_url_url_without_extension(self):
        url = 'https://example.com/path/to/file'
        nome, extensao = self.util.extrair_nome_extensao_url(url)
        self.assertEqual(nome, 'file')
        self.assertEqual(extensao, '')

    def test_extrair_nome_extensao_url_url_with_query_string(self):
        url = 'https://example.com/path/to/file?query=value'
        nome, extensao = self.util.extrair_nome_extensao_url(url)
        self.assertEqual(nome, 'file')
        self.assertEqual(extensao, '')

    def test_extrair_nome_extensao_url_missing_file_path(self):
        url = 'https://example.com'
        with self.assertRaises(ValueError) as context:
            self.util.extrair_nome_extensao_url(url)
        self.assertEqual(str(context.exception), "Missing file path in URL")

    def test_extrair_nome_extensao_url_unsupported_protocol(self):
        url = 'mailto:someone@example.com'
        with self.assertRaises(ValueError) as context:
            self.util.extrair_nome_extensao_url(url)
        self.assertIn("Unsupported protocol:", str(context.exception))