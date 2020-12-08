from typing import Dict, List, Optional, Union
import pandas as pd


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