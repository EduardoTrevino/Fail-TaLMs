import requests
from typing import Optional, List
from xml.etree import ElementTree as ET


def get_all_transactions(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Function to download all transcribed transactions in JSON format.
    """
    url = "https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_available_disclosures(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Function to get the list of available disclosures by fetching the filemap.xml.
    """
    url = "https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/filemap.xml"
    response = requests.get(url)
    
    try:
        xml_content = response.text
        tree = ET.fromstring(xml_content)
        
        # Extract all JSON file keys from the XML
        results = [key.text for key in tree.findall('.//Key') if key.text.endswith('.json')]
        files = [file.split('/')[1] for file in results]
        
        return files
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_daily_transaction_report(date: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Function to get the JSON for a single day's disclosure.
    :param date: Date in the format 'MM_DD_YYYY'
    """
    filename = f"data/transaction_report_for_{date}.json"
    url = f"https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/{filename}"
    
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}