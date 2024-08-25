import pytest
import api

def test_get_banks():
    response = api.get_banks()
    assert isinstance(response, list), "Response should be a list of banks"

def test_get_bank_by_code():
    response = api.get_bank_by_code(code=1)
    assert isinstance(response, dict), "Response should be a dictionary with bank information"

def test_get_cep():
    response = api.get_cep(89010025)
    assert isinstance(response, dict) and "cep" in response, "Response should be a dictionary with CEP information"

def test_get_cep_v2():
    response = api.get_cep_v2(89010025)
    assert isinstance(response, dict) and "cep" in response, "Response should be a dictionary with CEP V2 information"

def test_get_cnpj():
    response = api.get_cnpj("19131243000197")
    assert isinstance(response, dict) and "cnpj" in response, "Response should be a dictionary with CNPJ information"

def test_get_corretoras():
    response = api.get_corretoras()
    assert isinstance(response, list), "Response should be a list of brokers"

def test_get_corretora_by_cnpj():
    response = api.get_corretora_by_cnpj("02332886000104")
    assert isinstance(response, dict), "Response should be a dictionary with broker information"

def test_get_cptec_cidades():
    response = api.get_cptec_cidades()
    assert isinstance(response, list), "Response should be a list of cities"

def test_search_cptec_cidade():
    response = api.search_cptec_cidade("São Paulo")
    assert isinstance(response, list), "Response should be a list of cities"

def test_get_clima_capital():
    response = api.get_clima_capital()
    assert isinstance(response, list), "Response should be a list of weather conditions for capitals"

def test_get_clima_aeroporto():
    response = api.get_clima_aeroporto("SBGR")
    assert isinstance(response, dict), "Response should be a dictionary with airport weather information"

def test_get_previsao_meteorologica():
    response = api.get_previsao_meteorologica(999)
    assert isinstance(response, dict), "Response should be a dictionary with weather forecast for a city"

def test_get_previsao_meteorologica_dias():
    response = api.get_previsao_meteorologica_dias(999, 3)
    assert isinstance(response, dict), "Response should be a dictionary with weather forecast for a period"

def test_get_previsao_oceanica():
    response = api.get_previsao_oceanica(241)
    assert isinstance(response, dict), "Response should be a dictionary with ocean forecast information"

def test_get_previsao_oceanica_dias():
    response = api.get_previsao_oceanica_dias(241, 2)
    assert isinstance(response, dict), "Response should be a dictionary with extended ocean forecast information"

def test_get_ddd():
    response = api.get_ddd(11)
    assert isinstance(response, dict), "Response should be a dictionary with DDD information"

def test_get_feriados():
    response = api.get_feriados(2022)
    assert isinstance(response, list), "Response should be a list of holidays"

def test_get_fipe_marcas():
    response = api.get_fipe_marcas('carros')
    assert isinstance(response, list), "Response should be a list of vehicle brands"

def test_get_fipe_preco():
    response = api.get_fipe_preco('001004-9')
    assert isinstance(response, list), "Response should be a list with vehicle price information"

def test_get_fipe_tabelas():
    response = api.get_fipe_tabelas()
    assert isinstance(response, list), "Response should be a list of FIPE tables"

def test_get_ibge_municipios():
    response = api.get_ibge_municipios('SP')
    assert isinstance(response, list), "Response should be a list of municipalities"

def test_get_ibge_uf():
    response = api.get_ibge_uf()
    assert isinstance(response, list), "Response should be a list of states"

def test_get_ibge_uf_by_code():
    response = api.get_ibge_uf_by_code('SP')
    assert isinstance(response, dict), "Response should be a dictionary with state information"

def test_get_isbn():
    response = api.get_isbn('9788545702870')
    assert isinstance(response, dict) and "isbn" in response, "Response should be a dictionary with ISBN information"

def test_get_ncms():
    response = api.get_ncms()
    assert isinstance(response, list), "Response should be a list of NCMs"

def test_search_ncm():
    response = api.search_ncm('3305.10.00')
    assert isinstance(response, list), "Response should be a list of NCMs"

def test_get_ncm_by_code():
    response = api.get_ncm_by_code('3305.10.00')
    assert isinstance(response, dict), "Response should be a dictionary with NCM information"

def test_get_pix_participants():
    response = api.get_pix_participants()
    assert isinstance(response, list), "Response should be a list of PIX participants"

def test_get_registro_br():
    response = api.get_registro_br('brasilapi.com.br')
    assert isinstance(response, dict), "Response should be a dictionary with domain status"

def test_get_taxas():
    response = api.get_taxas()
    assert isinstance(response, list), "Response should be a list of interest rates"

def test_get_taxa_by_sigla():
    response = api.get_taxa_by_sigla('CDI')
    assert isinstance(response, dict), "Response should be a dictionary with rate information"