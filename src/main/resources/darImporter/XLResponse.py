#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import httplib, base64, sys, string
from java.net import URI

class XLResponse:

    def __init__(self, response):
        self.response = response
        self.status = response.status
        self.location = response.getheader("location")

    def isSuccessful(self):
        return self.response.status >= 200 and self.response.status < 400

    def errorDump(self):
        print "Status: %s" % self.response.status
        print "Reason: %s" % self.response.reason
        print "Raw error:"
        print self.response.read()

    def read(self):
        return self.response.read()
