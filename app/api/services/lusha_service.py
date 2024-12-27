import requests
from fastapi import HTTPException

API_KEY = "0550f7c4-d9a5-440b-b4bf-795c04e50800"
BASE_URL = "https://api.lusha.com/person"
LINKEDIN_URL_BASE = "https://api.lusha.com/v2/person"

def fetch_contact_info(firstName: str, lastName: str, company: str):
    """
    Business logic to fetch contact information using Lusha API.
    """
    params = {"firstName": firstName, "lastName": lastName, "company": company}
    headers = {"api_key": API_KEY}

    try:
        response = requests.get(BASE_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        email_addresses = data['data']["emailAddresses"]
        phone_numbers = data['data']["phoneNumbers"]

        return {
            "emails": [email["email"] for email in email_addresses],
            "phoneNumbers": [phone["internationalNumber"] for phone in phone_numbers],
        }
    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"API Request failed: {response.text}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")


def fetch_contact_info_by_linkedin(linkedinUrl: str):
    """
    Business logic to fetch contact information using LinkedIn URL via Lusha API.
    """
    params = {"linkedinUrl": linkedinUrl}
    headers = {"api_key": API_KEY}

    try:
        response = requests.get(LINKEDIN_URL_BASE, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        email_addresses = data.get('contact', {}).get('data', {}).get("emailAddresses", [])
        phone_numbers = data.get('contact', {}).get('data', {}).get("phoneNumbers", [])

        return {
            "emails": [email["email"] for email in email_addresses if "email" in email],
            "phoneNumbers": [
                phone.get("number", "N/A") for phone in phone_numbers
            ],
        }
    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"API Request failed: {response.text}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")