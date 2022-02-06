# Standard library imports...
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports...
import requests

# Local imports...
from constants import BASE_URL

QR_CODES_URL = urljoin(BASE_URL, '/qr_codes/')

def patch_qr_codes(qr_codes_id, head, payload):
    response = requests.patch(QR_CODES_URL + qr_codes_id, payload, headers=head)
    if response.ok:
        return response
    else:
        return None