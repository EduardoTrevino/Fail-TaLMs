import requests
from typing import Optional

def search_npi(
    number: Optional[str] = None, 
    enumeration_type: Optional[str] = None,
    taxonomy_description: Optional[str] = None,
    name_purpose: Optional[str] = None,
    first_name: Optional[str] = None,
    use_first_name_alias: bool = True,
    last_name: Optional[str] = None,
    organization_name: Optional[str] = None,
    address_purpose: Optional[str] = None,
    city: Optional[str] = None,
    state: Optional[str] = None,
    postal_code: Optional[str] = None,
    country_code: Optional[str] = None,
    limit: int = 10,
    skip: int = 0,
    pretty: bool = False,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
):
    """
    Endpoint to search NPI registry.
    Parameters:
    - number: Optional[str] = NPI Number, a unique 10-digit identifier.
    - enumeration_type: Optional[str] = Type of NPI (Individual or Organizational) (NPI-1/NPI-2).
    - taxonomy_description: Optional[str] = Description related to provider's taxonomy.
    - name_purpose: Optional[str] = Specifies if the name pertains to AO (Authorized Official) or Provider.
    - first_name: Optional[str] = First name of the provider (for Individual providers).
    - use_first_name_alias: bool = If True, includes similar First Names.
    - last_name: Optional[str] = Last name of the provider (for Individual providers).
    - organization_name: Optional[str] = Organization name (for Organizational providers).
    - address_purpose: Optional[str] = Address type filter (LOCATION/MAILING/PRIMARY/SECONDARY).
    - city: Optional[str] = City associated with the provider's address.
    - state: Optional[str] = State abbreviation for the provider's address.
    - postal_code: Optional[str] = Postal code for the provider's address.
    - country_code: Optional[str] = Country associated with the provider's address.
    - limit: int = Maximum number of results to return. Default is 10.
    - skip: int = Number of results to skip. Default is 0.
    - pretty: bool = Display in an easy to read format. Default is False.
    - toolbench_rapidapi_key: str = API key for access.
    """
    url = "https://npiregistry.cms.hhs.gov/api/"
    params = {
        'version': '2.1',
        'number': number,
        'enumeration_type': enumeration_type,
        'taxonomy_description': taxonomy_description,
        'name_purpose': name_purpose,
        'first_name': first_name,
        'use_first_name_alias': str(use_first_name_alias).lower(),
        'last_name': last_name,
        'organization_name': organization_name,
        'address_purpose': address_purpose,
        'city': city,
        'state': state,
        'postal_code': postal_code,
        'country_code': country_code,
        'limit': limit,
        'skip': skip,
        'pretty': str(pretty).lower(),
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}