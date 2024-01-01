import unittest
from entidades import Util

class TestUtil(unittest.TestCase):

    def test_extrair_nome_extensao_url_valid_url_with_filename_and_extension(self):
        util = Util()
        url = 'https://example.com/path/to/file.txt'
        nome, extensao = util.extrair_nome_extensao_url(url)
        self.assertEqual(nome, 'file')
        self.assertEqual(extensao, '.txt')

    def test_extrair_nome_extensao_url_url_without_extension(self):
        util = Util()
        url = 'https://example.com/path/to/file'
        nome, extensao = util.extrair_nome_extensao_url(url)
        self.assertEqual(nome, 'file')
        self.assertEqual(extensao, '')

    def test_extrair_nome_extensao_url_url_with_query_string(self):
        util = Util()
        url = 'https://example.com/path/to/file?query=value'
        nome, extensao = util.extrair_nome_extensao_url(url)
        self.assertEqual(nome, 'file')
        self.assertEqual(extensao, '')

    def test_extrair_nome_extensao_url_missing_file_path(self):
        util = Util()
        url = 'https://example.com'
        with self.assertRaises(ValueError) as context:
            util.extrair_nome_extensao_url(url)
        print(f'str(context.exception): {str(context.exception)}')
        self.assertEqual(str(context.exception), "Missing file path in URL")

    def test_extrair_nome_extensao_url_unsupported_protocol(self):
        util = Util()
        url = 'mailto:someone@example.com'
        with self.assertRaises(ValueError) as context:
            util.extrair_nome_extensao_url(url)
        print(f'str(context.exception): {str(context.exception)}')            
        self.assertIn("Unsupported protocol:", str(context.exception))