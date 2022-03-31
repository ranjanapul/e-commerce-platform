import re
import jwt
from jwt.algorithms import get_default_algorithms
import base64
import json
def getToken(request):
    regex = re.compile('^HTTP_')
    http_headers = dict((regex.sub('', header), value) for (header, value)
                        in request.META.items() if header.startswith('HTTP_'))
    token = http_headers['AUTHORIZATION'].split()[1]
    print(token)
    '''
    try:
        print(jwt.decode(token, key="your-256-bit-secret", algorithms='HS256'))
    except Exception as e:
        print(e)
    '''

    codedString = token.split(".")[1]
    pad = len(codedString)%4
    codedString = codedString + "="*pad

    print(codedString)
    data = json.loads(base64.b64decode(codedString).decode("utf-8"))
    email = data['firebase']['identities']['email'][0]



    return email
# Get userid from IDToken. Also print on webpage.