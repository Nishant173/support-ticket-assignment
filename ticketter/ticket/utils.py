def assemble_ticket_dictionary(dict_obj, request_obj):
    """Maps relevant data from Ticket model to ticket required by the API"""
    dict_obj_new = {
        "subject": dict_obj.get('subject', ''),
        "category": dict_obj.get('category', ''),
        "priority": dict_obj.get('priority', ''),
        "description": dict_obj.get('description', ''),
        "email": str(request_obj.user.email),
        "contactId": "7189000001119001",
        "departmentId": "7189000000051431",
    }
    return dict_obj_new