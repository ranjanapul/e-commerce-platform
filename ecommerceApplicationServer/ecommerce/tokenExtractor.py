import re


def getToken(request):
    regex = re.compile('^HTTP_')
    http_headers = dict((regex.sub('', header), value) for (header, value)
                        in request.META.items() if header.startswith('HTTP_'))
    return int(http_headers['AUTHORIZATION'].split()[1])
