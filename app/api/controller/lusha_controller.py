from fastapi import APIRouter, HTTPException, Query
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
def get_contact_info_linkedin(linkedinUrl: list[str] = Query(...)):
    """
    API endpoint to fetch email and phone number using LinkedIn URLs via Lusha API.
    """
    try:
        # Debug log to check the incoming URLs
        print("Received LinkedIn URLs:", linkedinUrl)
        
        # Loop through the list of LinkedIn URLs and fetch contact info
        results = []

        try:
            result = fetch_contact_info_by_linkedin(linkedinUrl)
            results.append({"linkedinUrl": linkedinUrl, "contactInfo": result})
        except HTTPException as e:
            # Log and include failed URL info
            results.append({"linkedinUrl": linkedinUrl, "error": str(e.detail)})
        
        return {"results": results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
