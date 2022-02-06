# Standard library imports...
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.parse import urljoin

# Local imports...
from services import patch_qr_codes
from constants import BASE_URL

@patch('services.requests.patch')
def test_qr_codes_patch_description(mock_patch):
    print('\n Be able to return an response code 200 when description body parameter is patched successfully')

    # Configure the mock to return a response with an OK status code.
    mock_patch.return_value.ok = True
    mock_patch.return_value.status_code = 200
    mock_patch.return_value.json = {
        'description': 'description test'
    }

    # Call the service to update description
    qr_code_id = '123456'
    header = { 'Authentication': 'fake-auth' }
    payload = { 'description': 'description test' }

    # call patch service with request created
    response = patch_qr_codes(qr_code_id, header, payload)

    assert response.ok == True
    assert response.status_code == 200
    assert response.json['description'] == 'description test'

@patch('services.requests.patch')
def test_qr_codes_patch_callback_url(mock_patch):
    print('\n Be able to return an response code 200 when callback_url body parameter is patched successfully')

    # Configure mock to return updated callback_url
    mock_patch.return_value.ok = True
    mock_patch.return_value.status_code = 200
    mock_patch.return_value.json = {
        'callback_url': 'https://update-mock.url/'
    }

    # Call the service to update callback_url
    qr_code_id = '123456'
    header = { 'Authentication': 'fake-auth' }
    payload = { 'callback_url': 'https://update-mock.url/' }

    # call patch service with request created
    response = patch_qr_codes(qr_code_id, header, payload)

    assert response.ok == True
    assert response.status_code == 200
    assert response.json['callback_url'] == 'https://update-mock.url/' 

@patch('services.requests.patch')
def test_qr_codes_patch_amount(mock_patch):
    print('\n Be able to return an response code 200 when amount body parameter is patched successfully')

    # Configure mock to return updated amount
    mock_patch.return_value.ok = True
    mock_patch.return_value.status_code = 200
    mock_patch.return_value.json = {
        'amount': 100000
    }

    # Call the service to update amount
    qr_code_id = '123456'
    header = { 'Authentication': 'fake-auth' }
    payload = { 'amount': 100000 }

    # call patch service with request created
    response = patch_qr_codes(qr_code_id, header, payload)

    assert response.ok == True
    assert response.status_code == 200
    assert response.json['amount'] == 100000

@patch('services.requests.patch')
def test_qr_codes_patch_invalid_description(mock_patch):
    print('\n Should able to validate when description value is invalid')

    # Configure the mock to return a response with an ERROR
    mock_patch.side_effect = HTTPError(
        urljoin(BASE_URL, '/qr_codes/fake-qr-code-id'), # url to access
        "API_VALIDATION_ERROR", # error code
        'Please enter a valid description value. Description field only accepts text.', # error reason/message
        {},
        None
    )

    # Call the service, which will send a request to the server.
    qr_code_id = '123456'
    header = { 'Authentication': 'fake-auth' }
    payload = { 'description': 1234 } # invalid description value

    try:
        response = patch_qr_codes(qr_code_id, header, payload)
        return response
    except HTTPError as error:
        print(error)
        assert error.code == "API_VALIDATION_ERROR"
        assert error.reason == 'Please enter a valid description value. Description field only accepts text.'

@patch('services.requests.patch')
def test_qr_codes_patch_invalid_amount(mock_patch):
    print('\n Should able to validate when QR code id does not exist')

    # Configure the mock to return a response with an ERROR
    mock_patch.side_effect = HTTPError(
        urljoin(BASE_URL, '/qr_codes/fake-qr-code-id'), # url to access
        "QR_CODE_NOT_FOUND_ERROR", # error code
        'QR code does not exist. Please try again with a valid QR code Id.', # error reason/message
        {},
        None
    )

    # Call the service, which will send a request to the server.
    qr_code_id = 'does-not-exist-qr-code-id'
    header = { 'Authentication': 'fake-auth' }
    payload = { 'amount': 1234 } 

    try:
        response = patch_qr_codes(qr_code_id, header, payload)
        return response
    except HTTPError as error:
        print(error)
        assert error.code == "QR_CODE_NOT_FOUND_ERROR"
        assert error.reason == 'QR code does not exist. Please try again with a valid QR code Id.'

# @patch('services.requests.patch')
# def test_qr_codes_patch_invalid_jsonformat(mock_patch):
#     print('\n Should able to validate when json format has missing (" ") on the description value')

#     # Configure the mock to return a response with an ERROR
#     mock_patch.side_effect = HTTPError(urljoin(BASE_URL, '/qr_codes/fake-qr-code-id'), "400", 'INVALID_JSON_FORMAT', {}, None)

#     # Call the service, which will send a request to the server.
#     qr_code_id = '123456'
#     header = { 'Authentication': 'fake-auth' }
#     payload = { "description": "1234" } 

#     try:
#         response = patch_qr_codes(qr_code_id, header, payload)
#         return response
#     except HTTPError as error:
#         print(error)
#         assert error.code == "400"
#         assert error.reason == 'INVALID_JSON_FORMAT'

