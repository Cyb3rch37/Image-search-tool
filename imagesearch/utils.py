import requests
from django.conf import settings

def search_with_image_tool(image_url):
    """Search for an image using the custom reverse image search tool API"""
    api_key = settings.IMAGE_SEARCH_TOOL_API_KEY
    api_url = "https://your-image-search-tool.com/api/search"
    
    params = {"image_url": image_url, "api_key": api_key}
    response = requests.get(api_url, params=params)

    return response.json() if response.status_code == 200 else {"error": response.text}


def search_on_social_media(platform, image_url):
    """Search for an image using a specific social media platform's API"""
    api_key = settings.SOCIAL_MEDIA_API_KEYS.get(platform)

    if not api_key:
        return {"error": f"API key for {platform} not found"}

    # Example URL (adjust based on the platform’s API documentation)
    api_url = f"https://api.{platform}.com/v1/search"

    headers = {"Authorization": f"Bearer {api_key}"}
    params = {"image_url": image_url}

    response = requests.get(api_url, headers=headers, params=params)

    return response.json() if response.status_code == 200 else {"error": response.text}

def search_image_everywhere(image_url):
    """Search for an image using both the custom tool and social media APIs"""
    results = {}

    # Search on web using your reverse image tool
    results["web_search"] = search_with_image_tool(image_url)

    # Search on social media (Facebook, Instagram, Twitter)
    social_media_platforms = ["facebook", "instagram", "twitter", "linkedin", "pinterest", "tiktok", "tumblr"]
    results["social_media"] = {platform: search_on_social_media(platform, image_url) for platform in social_media_platforms}

    return results
