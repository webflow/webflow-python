# If we can I'd like to move this to the webhooks client wrapper, 
# but I can't find the Fern generation.yml to extend the client 
# according to documentation included here:
# https://buildwithfern.com/learn/sdks/capabilities/custom-code
import hmac
import hashlib
from collections.abc import Mapping

def verify(headers: Mapping, body:str , secret: str):
    """
    Verify that the signature on the webhook message is from Webflow

    Documentation:
    https://developers.webflow.com/data/docs/working-with-webhooks#validating-request-signatures

    Parameters:
        - headers : Mapping. The request headers in a Mapping-like object

        - body : str. The request body as a UTF-8 encoded string

        - secret : str. The secret key generated when creating the webhook or the OAuth client secret
    ---
    ```
    from fastapi import FastAPI, Request
    # ...

    @app.post('/webhookEndpoint')
    async def webhook_endpoint_handler(
        request: Request,
    ):
        # Read the request body as a utf-8 encoded string
        body = (await request.body()).decode("utf-8")  
    
        # Extract the headers as Mapping-like object
        headers = request.headers

        secret = get_secret()
        
        verified = verify(
            headers=request.headers, 
            body=(await request.body()).decode("utf-8"), 
            secret=new_webhook.secretKey)

        if verified:
            # ...process the request normally
        else:
            # ...handle unathenticated request
    ```
    """
    
    # Normalize header format to account for different python server implementations 
    # that may or may not normalize headers already
    normalized_headers = {k.lower(): v for k, v in headers.items()}

    message = f"{normalized_headers.get('x-webflow-timestamp', '')}:{body}".encode('utf-8')

    generated_signature = hmac.new(
        key=secret.encode('utf-8'),
        msg=message,
        digestmod=hashlib.sha256
    ).hexdigest()

    return normalized_headers.get("x-webflow-signature", "") == generated_signature