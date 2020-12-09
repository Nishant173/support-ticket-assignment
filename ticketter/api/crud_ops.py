from typing import Dict, List, Union
import json
import requests
from . import config
from .errors import BadApiRequestError


def get_tickets() -> Union[List[Dict], List]:
    """Gets list of tickets"""
    response = requests.get(url=config.URL_TICKETS,
                            headers=config.AUTH_CREDENTIALS)
    if response.status_code not in [200, 201]:
        raise BadApiRequestError(f"Error with API request. Status code: {response.status_code}")
    tickets = response.json()['data']
    return tickets


def post_ticket(dict_obj: Dict) -> Dict:
    """Posts one ticket to API, and returns dictionary containing `status_code`"""
    response = requests.post(url=config.URL_TICKETS,
                             headers=config.AUTH_CREDENTIALS,
                             data=json.dumps(dict_obj))
    return {'status_code': response.status_code}


# def is_valid_post_ticket(response: Dict,
#                          dict_obj_sent: Dict) -> bool:
#     """
#     Checks if POST request made was valid. Returns True if valid; False otherwise.
#     Parameters:
#         - response (dict): Response received on making POST request.
#         - dict_obj_sent (dict): Python dictionary object sent (posted) to the API.
#     """
#     subject_exists = (True if response.get('subject', None) else False)
#     if not subject_exists:
#         return False
#     is_same_subject = (response.get('subject', '') == dict_obj_sent.get('subject', ''))
#     is_same_email = (response.get('email', '') == dict_obj_sent.get('email', ''))
#     if is_same_subject and is_same_email:
#         return True
#     return False


# if __name__ == "__main__":
#     # GET
#     tickets = get_tickets()
#     print(tickets)

#     # POST
#     dict_obj = {
#         "subject": "Some random subject",
#         "departmentId": "7189000000051431",
#         "contactId": "7189000001119001",
#         "email": "nishant@yahoo.com",
#     }
#     response = post_ticket(dict_obj=dict_obj)
#     if response.get('status_code', '') in [200, 201]:
#         print("VALID")
#     else:
#         print("INVALID")