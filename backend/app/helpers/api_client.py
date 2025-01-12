import httpx
import os
from dotenv import load_dotenv
import os
from typing import List, Dict
# Load environment variables
load_dotenv()


BING_API_KEY = os.getenv("BING_SEARCH_API_KEY")
BING_SEARCH_ENDPOINT = os.getenv("BING_SEARCH_ENDPOINT")

def bing_search(query: str, count: int = 5) -> dict:
    """Fetch search results from Bing for the given query."""
    headers = {"Ocp-Apim-Subscription-Key": BING_API_KEY}
    params = {"q": query, "count": count}
    print(f"BING_SEARCH_ENDPOINT: {BING_SEARCH_ENDPOINT}")  # Debugging
    
    try:
        response = httpx.get(BING_SEARCH_ENDPOINT, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except httpx.RequestError as e:
        raise ValueError(f"Error making request to Bing Search API: {e}")
    except httpx.HTTPStatusError as e:
        raise ValueError(f"HTTP error from Bing Search API: {e.response.status_code}")
    
def fetch_realtime_data(query: str, search_type: str = "general") -> List[Dict[str, str]]:
    """Fetch real-time data using Bing Search."""
    try:
        results = bing_search(query, count=5)
        return [
            {"title": item["name"], "snippet": item["snippet"], "url": item["url"]}
            for item in results.get("webPages", {}).get("value", [])
        ]
    except Exception as e:
        logger.error(f"Failed to fetch {search_type} data: {e}")
        raise ValueError(f"Error fetching {search_type} data")