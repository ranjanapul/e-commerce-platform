import re
import base64
import json
def getToken(request):
    regex = re.compile('^HTTP_')
    http_headers = dict((regex.sub('', header), value) for (header, value)
                        in request.META.items() if header.startswith('HTTP_'))
    token = http_headers['AUTHORIZATION'].split()[1]


    codedString = token.split(".")[1] # get the payload
    pad = len(codedString)%4
    codedString = codedString + "="*pad
    data = json.loads(base64.b64decode(codedString).decode("utf-8"))
    # used base64decode bec jwt token is base64 encoded
    email = data['firebase']['identities']['email'][0]



    return email
# Get userid from IDToken. Also print on webpage.