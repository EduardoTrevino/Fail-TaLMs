import requests
import json

def get_bank_holidays():
    """
    Get all bank holidays in the UK
    """
    url = "https://www.gov.uk/bank-holidays.json"
    response = requests.get(url)
    try:
        holidays = response.json()
    except json.JSONDecodeError:
        holidays = response.text
    return holidays

def get_past_bank_holidays():
    """
    Get past bank holidays in the UK
    """
    url = "https://www.gov.uk/bank-holidays.json"
    response = requests.get(url)
    try:
        holidays = response.json()
        # Process to filter past bank holidays (Example: Only return past holidays)
        past_holidays = {}
        for region, data in holidays['divisions'].items():
            past_holidays[region] = {}
            for year, events in data.items():
                if int(year) < 2024:  # Assuming 2024 is the current year
                    past_holidays[region][year] = events
    except json.JSONDecodeError:
        past_holidays = response.text
    return past_holidays
