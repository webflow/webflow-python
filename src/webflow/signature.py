# If we can I'd like to move this to the webhooks client wrapper, 
# but I can't find the Fern generation.yml to extend the client 
# according to documentation included here:
# https://buildwithfern.com/learn/sdks/capabilities/custom-code
import hmac
import hashlib
from collections.abc import Mapping

def verify(headers: Mapping, body:str , secret: str):
    # Normalize header format to account for different server implementations
    normalized_headers = {k.lower(): v for k, v in headers.items()}

    message = f"{normalized_headers.get('x-webflow-timestamp', '')}:{body}".encode('utf-8')

    generated_signature = hmac.new(
        key=secret.encode('utf-8'),
        msg=message,
        digestmod=hashlib.sha256
    ).hexdigest()

    return normalized_headers.get("x-webflow-signature", "") == generated_signature