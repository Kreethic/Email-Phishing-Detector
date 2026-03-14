
import requests
import base64
import re

def check_url_virustotal(email_body):
    api_key = "api key".strip() #Add your virustotal API key
    urls = re.findall(r'https?://[^\s]+', email_body)  # Extract URLs

    for url in urls:
        url_id = base64.urlsafe_b64encode(url.encode()).decode().rstrip("=")
        headers = {"x-apikey": api_key}
        # Ensure no whitespace in header value
        for k, v in headers.items():
            headers[k] = v.strip()
        response = requests.get(f"https://www.virustotal.com/api/v3/urls/{url_id}", headers=headers)

        if response.status_code == 200:
            result = response.json()
            print("VirusTotal Analysis Result:", result)  # Print the result for debugging

            # Check for malicious indicators
            if result.get('data', {}).get('attributes', {}).get('last_analysis_stats', {}).get('malicious', 0) > 0:
                return url  # Return the actual suspicious URL

    return None  # No phishing detected

# New function to detect HTTP (not HTTPS) links
def contains_http_link(email_body):
    """
    Returns the first HTTP (not HTTPS) link found in the email body, or None if not found.
    """
    http_links = re.findall(r'http://[^\s]+', email_body)
    return http_links[0] if http_links else None
