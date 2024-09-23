import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def get_geolocation(ip_address):
    """
    Fetches geolocation data from the IP API service for a given IP address.
    """
    # Load the Geolocation API URL from .env
    GEO_API_URL = os.getenv('GEO_API_URL', 'http://ip-api.com/json/')

    response = requests.get(f"{GEO_API_URL}{ip_address}")

    if response.status_code == 200:
        geo_data = response.json()
        return {
            "country": geo_data.get("country", "Unknown"),
            "region": geo_data.get("regionName", "Unknown"),
            "city": geo_data.get("city", "Unknown"),
            "isp": geo_data.get("isp", "Unknown"),
        }
    else:
        return {"error": "Geolocation API error or invalid response."}

def log_geolocation(ip_address):
    """
    Logs the geolocation information for a given IP address.
    """
    geo_info = get_geolocation(ip_address)
    print(f"IP Address: {ip_address}, Geolocation Info: {geo_info}")
    return geo_info
