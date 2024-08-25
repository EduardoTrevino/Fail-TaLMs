import requests
from typing import Optional, List

BASE_URL = "https://brasilapi.com.br"

def get_banks(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Retrieves information about all banks in Brazil."""
    url = f"{BASE_URL}/banks/v1"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_bank_by_code(code: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetches information about a bank using its code."""
    url = f"{BASE_URL}/banks/v1/{code}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_cep(cep: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch address information using CEP."""
    url = f"{BASE_URL}/cep/v1/{cep}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_cep_v2(cep: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch address information using CEP version 2."""
    url = f"{BASE_URL}/cep/v2/{cep}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_cnpj(cnpj: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch company data by CNPJ."""
    url = f"{BASE_URL}/cnpj/v1/{cnpj}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_corretoras(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Retrieve information about brokers registered with CVM."""
    url = f"{BASE_URL}/cvm/corretoras/v1"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_corretora_by_cnpj(cnpj: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch a broker's information by CNPJ."""
    url = f"{BASE_URL}/cvm/corretoras/v1/{cnpj}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_cptec_cidades(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """List all cities available in CPTEC services."""
    url = f"{BASE_URL}/cptec/v1/cidade"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def search_cptec_cidade(city_name: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Search for cities in CPTEC by name."""
    url = f"{BASE_URL}/cptec/v1/cidade/{city_name}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_clima_capital(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get current weather conditions in the capitals of Brazil."""
    url = f"{BASE_URL}/cptec/v1/clima/capital"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_clima_aeroporto(icao_code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get current weather conditions at a specified airport using ICAO code."""
    url = f"{BASE_URL}/cptec/v1/clima/aeroporto/{icao_code}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_previsao_meteorologica(city_code: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch current weather forecast for a city by city code."""
    url = f"{BASE_URL}/cptec/v1/clima/previsao/{city_code}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_previsao_meteorologica_dias(city_code: int, days: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch weather forecast for a city for a period up to 6 days."""
    url = f"{BASE_URL}/cptec/v1/clima/previsao/{city_code}/{days}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_previsao_oceanica(city_code: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch oceanic forecast for a city by city code."""
    url = f"{BASE_URL}/cptec/v1/ondas/{city_code}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_previsao_oceanica_dias(city_code: int, days: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch oceanic forecast for a city for a period up to 6 days."""
    url = f"{BASE_URL}/cptec/v1/ondas/{city_code}/{days}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_ddd(ddd: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch state and city list by DDD."""
    url = f"{BASE_URL}/ddd/v1/{ddd}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_feriados(ano: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """List national holidays for a given year."""
    url = f"{BASE_URL}/feriados/v1/{ano}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_fipe_marcas(tipo_veiculo: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """List vehicle brands according to the type of vehicle."""
    url = f"{BASE_URL}/fipe/marcas/v1/{tipo_veiculo}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_fipe_preco(codigo_fipe: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get the vehicle price according to the Fipe table."""
    url = f"{BASE_URL}/fipe/preco/v1/{codigo_fipe}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_fipe_tabelas(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """List existing reference tables in FIPE."""
    url = f"{BASE_URL}/fipe/tabelas/v1"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_ibge_municipios(sigla_uf: str, providers: Optional[str] = 'dados-abertos-br,gov,wikipedia', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Returns the municipalities of the federative unit."""
    url = f"{BASE_URL}/ibge/municipios/v1/{sigla_uf}"
    params = {'providers': providers}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_ibge_uf(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Returns all states of Brazil."""
    url = f"{BASE_URL}/ibge/uf/v1"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_ibge_uf_by_code(code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch state information using its code or abbreviation."""
    url = f"{BASE_URL}/ibge/uf/v1/{code}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_isbn(isbn: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch information about a book using ISBN."""
    url = f"{BASE_URL}/isbn/v1/{isbn}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_ncms(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Returns all NCMs information."""
    url = f"{BASE_URL}/ncm/v1"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def search_ncm(code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Search NCM information by code or description."""
    url = f"{BASE_URL}/ncm/v1"
    params = {'search': code}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_ncm_by_code(code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch NCM information using a code."""
    url = f"{BASE_URL}/ncm/v1/{code}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_pix_participants(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Returns all PIX participants' information."""
    url = f"{BASE_URL}/pix/v1/participants"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_registro_br(domain: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Evaluate the status of a .br domain."""
    url = f"{BASE_URL}/registrobr/v1/{domain}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_taxas(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch interest rates and some official indices in Brazil."""
    url = f"{BASE_URL}/taxas/v1"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_taxa_by_sigla(sigla: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch information about a rate using its name or abbreviation."""
    url = f"{BASE_URL}/taxas/v1/{sigla}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}