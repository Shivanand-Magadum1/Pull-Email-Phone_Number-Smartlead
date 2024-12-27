from fastapi import APIRouter, HTTPException
from app.api.services.lusha_service import fetch_contact_info, fetch_contact_info_by_linkedin

router = APIRouter()

@router.get("/get-contact-info")
def get_contact_info(firstName: str, lastName: str, company: str):
    """
    API endpoint to fetch email and phone number using Lusha API.
    """
    try:
        return fetch_contact_info(firstName, lastName, company)
    except HTTPException as e:
        raise e


@router.get("/get-contact-info-linkedin")
def get_contact_info_linkedin(linkedinUrl: str):
    """
    API endpoint to fetch email and phone number using LinkedIn URL via Lusha API.
    """
    try:
        return fetch_contact_info_by_linkedin(linkedinUrl)
    except HTTPException as e:
        raise e
