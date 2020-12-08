from typing import Dict, List, Optional, Union
import json
import requests
import pandas as pd
import config


def get_tickets() -> Union[List[Dict], List]:
    """Gets list of tickets"""
    response = requests.get(url=config.URL_TICKETS,
                            headers=config.AUTH_CREDENTIALS)
    if response.status_code not in [200, 201]:
        raise Exception(f"Error with API request. Status code: {response.status_code}")
    tickets = response.json()['data']
    return tickets


def post_ticket(dict_obj: Dict) -> Dict:
    """Posts one ticket to API, and returns response containing what was posted"""
    response = requests.post(url=config.URL_TICKETS,
                             headers=config.AUTH_CREDENTIALS,
                             data=json.dumps(dict_obj))
    response = response.json()
    return response


def is_valid_post_ticket(response: Dict,
                         dict_obj_sent: Dict) -> bool:
    """
    Checks if POST request made was valid. Returns True if valid; False otherwise.
    Parameters:
        - response (dict): Response received on making POST request.
        - dict_obj_sent (dict): Python dictionary object sent (posted) to the API.
    """
    subject_exists = (True if response.get('subject', None) else False)
    if not subject_exists:
        return False
    is_same_subject = (response.get('subject', '') == dict_obj_sent.get('subject', ''))
    is_same_email = (response.get('email', '') == dict_obj_sent.get('email', ''))
    if is_same_subject and is_same_email:
        return True
    return False


def filter_tickets(tickets: Union[List[Dict], List],
                   email: Optional[str] = None,
                   status: Optional[str] = None) -> Union[List[Dict], List]:
    """Filters list of tickets based on certain parameters"""
    df = pd.DataFrame(data=tickets)
    if email:
        df = df[df['email'].str.lower() == str(email).lower().strip()]
    if status:
        df = df[df['status'].str.lower() == str(status).lower().strip()]
    return df.to_dict(orient='records')


if __name__ == "__main__":
    # GET
    tickets = get_tickets()
    tickets = filter_tickets(tickets=tickets, email=None, status=None)
    print(pd.DataFrame(tickets)[['subject', 'email']])

    # POST
    dict_obj = {
        "subject": "Some subject",
        "departmentId": "7189000000051431",
        "contactId": "7189000001119001",
        "email": "nishant@gmail.com",
    }
    response = post_ticket(dict_obj=dict_obj)
    is_valid = is_valid_post_ticket(response=response,
                                    dict_obj_sent=dict_obj)
    print(is_valid)