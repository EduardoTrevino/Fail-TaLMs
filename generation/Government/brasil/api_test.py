import unittest
import api

class TestAPI(unittest.TestCase):

    def test_get_banks(self):
        response = api.get_banks()
        self.assertIsInstance(response, list, "Response should be a list of banks")

    def test_get_bank_by_code(self):
        response = api.get_bank_by_code(code=1)
        self.assertIsInstance(response, dict, "Response should be a dictionary with bank information")

    def test_get_cep(self):
        response = api.get_cep(89010025)
        self.assertIsInstance(response, dict, "Response should be a dictionary with CEP information")
        self.assertIn("cep", response, "Response should contain 'cep' key")

    def test_get_cep_v2(self):
        response = api.get_cep_v2(89010025)
        self.assertIsInstance(response, dict, "Response should be a dictionary with CEP V2 information")
        self.assertIn("cep", response, "Response should contain 'cep' key")

    def test_get_cnpj(self):
        response = api.get_cnpj("19131243000197")
        self.assertIsInstance(response, dict, "Response should be a dictionary with CNPJ information")
        self.assertIn("cnpj", response, "Response should contain 'cnpj' key")

    def test_get_corretoras(self):
        response = api.get_corretoras()
        self.assertIsInstance(response, list, "Response should be a list of brokers")

    def test_get_corretora_by_cnpj(self):
        response = api.get_corretora_by_cnpj("02332886000104")
        self.assertIsInstance(response, dict, "Response should be a dictionary with broker information")

    def test_get_cptec_cidades(self):
        response = api.get_cptec_cidades()
        self.assertIsInstance(response, list, "Response should be a list of cities")

    def test_search_cptec_cidade(self):
        response = api.search_cptec_cidade("São Paulo")
        self.assertIsInstance(response, list, "Response should be a list of cities")

    def test_get_clima_aeroporto(self):
        response = api.get_clima_aeroporto("SBGR")
        self.assertIsInstance(response, dict, "Response should be a dictionary with airport weather information")

    def test_get_previsao_meteorologica(self):
        response = api.get_previsao_meteorologica(999)
        self.assertIsInstance(response, dict, "Response should be a dictionary with weather forecast for a city")

    def test_get_previsao_meteorologica_dias(self):
        response = api.get_previsao_meteorologica_dias(999, 3)
        self.assertIsInstance(response, dict, "Response should be a dictionary with weather forecast for a period")

    def test_get_previsao_oceanica(self):
        response = api.get_previsao_oceanica(241)
        self.assertIsInstance(response, dict, "Response should be a dictionary with ocean forecast information")

    def test_get_previsao_oceanica_dias(self):
        response = api.get_previsao_oceanica_dias(241, 2)
        self.assertIsInstance(response, dict, "Response should be a dictionary with extended ocean forecast information")

    def test_get_ddd(self):
        response = api.get_ddd(11)
        self.assertIsInstance(response, dict, "Response should be a dictionary with DDD information")

    def test_get_feriados(self):
        response = api.get_feriados(2022)
        self.assertIsInstance(response, list, "Response should be a list of holidays")

    def test_get_fipe_marcas(self):
        response = api.get_fipe_marcas('carros')
        self.assertIsInstance(response, list, "Response should be a list of vehicle brands")

    def test_get_fipe_preco(self):
        response = api.get_fipe_preco('001004-9')
        self.assertIsInstance(response, list, "Response should be a list with vehicle price information")

    def test_get_fipe_tabelas(self):
        response = api.get_fipe_tabelas()
        self.assertIsInstance(response, list, "Response should be a list of FIPE tables")

    def test_get_ibge_municipios(self):
        response = api.get_ibge_municipios('SP')
        self.assertIsInstance(response, list, "Response should be a list of municipalities")

    def test_get_ibge_uf(self):
        response = api.get_ibge_uf()
        self.assertIsInstance(response, list, "Response should be a list of states")

    def test_get_ibge_uf_by_code(self):
        response = api.get_ibge_uf_by_code('SP')
        self.assertIsInstance(response, dict, "Response should be a dictionary with state information")

    def test_get_isbn(self):
        response = api.get_isbn('9788545702870')
        self.assertIsInstance(response, dict, "Response should be a dictionary with ISBN information")
        self.assertIn("isbn", response, "Response should contain 'isbn' key")

    def test_get_ncms(self):
        response = api.get_ncms()
        self.assertIsInstance(response, list, "Response should be a list of NCMs")

    def test_search_ncm(self):
        response = api.search_ncm('3305.10.00')
        self.assertIsInstance(response, list, "Response should be a list of NCMs")

    def test_get_ncm_by_code(self):
        response = api.get_ncm_by_code('3305.10.00')
        self.assertIsInstance(response, dict, "Response should be a dictionary with NCM information")

    def test_get_pix_participants(self):
        response = api.get_pix_participants()
        self.assertIsInstance(response, list, "Response should be a list of PIX participants")

    def test_get_registro_br(self):
        response = api.get_registro_br('brasilapi.com.br')
        self.assertIsInstance(response, dict, "Response should be a dictionary with domain status")

    def test_get_taxas(self):
        response = api.get_taxas()
        self.assertIsInstance(response, dict, "Response should be a dict of interest rates")

    def test_get_taxa_by_sigla(self):
        response = api.get_taxa_by_sigla('CDI')
        self.assertIsInstance(response, dict, "Response should be a dictionary with rate information")

if __name__ == '__main__':
    unittest.main()
