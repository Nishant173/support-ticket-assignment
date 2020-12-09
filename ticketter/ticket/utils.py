def map_model2api(dict_obj, email):
    """
    Maps data object obtained from Ticket model to Ticket required by the API.
    Note: The API requires certain keys like ['email', 'contactId', 'departmentId']
    """
    dict_obj_new = {
        "subject": dict_obj.get('subject', ''),
        "category": dict_obj.get('category', ''),
        "priority": dict_obj.get('priority', ''),
        "description": dict_obj.get('description', ''),
        "email": str(email),
        "contactId": "7189000001119001",
        "departmentId": "7189000000051431",
    }
    return dict_obj_new