import requests
from typing import Optional

def is_username_available(username: str, headers: Optional[dict] = None) -> bool:
    """Return True if username is available, and False if it's taken."""

    URL_FORMAT = 'https://www.flashback.org/ajax/fb_register_username_check.php?username={username}'

    if not headers:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
        }

    session = requests.Session()
    session.headers.update(headers)

    r = session.get(URL_FORMAT.format(username = username))

    return r.text == '1'

