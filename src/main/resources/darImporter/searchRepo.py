#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from darImporter import XLRequest
import simplejson as json
import sys


XLRESPONSE_RESULT = 200
result = []

if 'repoId' not in request.query:
        raise Exception("repoId not present in request")

repo = repositoryService.read(request.query['repoId'])
term = request.query['term']

serverUrl = repo.getProperty("serverUrl")
username = repo.getProperty("username")
password = repo.getProperty("password")
kind = repo.getProperty("kind")


query = "%s/lucene/search?a=%s&p=dar" % (serverUrl, term)

xlResponse = XLRequest.XLRequest(query, 'GET', None, username, password, 'application/json', 'application/json').send()

logger.info('xlResponse result is %s' % xlResponse.status)

if xlResponse.status == XLRESPONSE_RESULT:
    data = json.load(xlResponse)
    entries = data["data"]
    for entry in entries:
        result.append("%s - %s - %s - %s" % (entry["groupId"],entry["artifactId"],entry["version"],entry["artifactHits"][0]["repositoryId"]))
else:
    print "Failed to search records in repo: %s" % repo
    xlResponse.errorDump()
    sys.exit(1)

response.entity = result