import httplib, base64, sys, string, urllib
from java.net import URI
from darImporter import XLResponse

class XLRequest:

    def __init__(self, url, method, body, username, password, content_type, accept):
        self.__buildCredentials(username, password)
        self.__buildHeaders(content_type, accept)
        self.__buildURI(url)
        self.__buildRequest()
        self.__buildConnection()
        self.method = method
        self.body = body

    def send(self):
        self.connection.request(self.method, self.request, self.body, self.headers)
        return XLResponse.XLResponse(self.connection.getresponse())

    def __buildCredentials(self, username, password):
        if username and password:
            self.credentials = base64.b64encode(username + ':' + password)
        else:
            self.credentials = None

    def __buildHeaders(self, content_type, accept):
        if self.credentials:
            self.headers = {'Authorization': 'Basic ' + self.credentials, 'Content-Type': content_type, 'User-Agent': 'XebiaLabs', 'Accept': accept}
        else:
            self.headers = {'Content-Type': content_type, 'User-Agent': 'XebiaLabs', 'Accept': accept}

    def __buildURI(self, url):
        self.uri = URI(urllib.quote(url, ':/?&=%'))

    def __buildRequest(self):
        self.request = self.uri.getPath()
        if self.uri.getQuery():
            self.request = '%s?%s' % (self.request, self.uri.getQuery())

    

    def __buildConnection(self):
        host = self.uri.getHost()
        if self.uri.getPort() != -1:
            host = '%s:%s' % (host, self.uri.getPort())

        if self.uri.getScheme() == 'https':
            self.connection = httplib.HTTPSConnection(host)
        else:
            self.connection = httplib.HTTPConnection(host)


