#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import urllib
import jarray
from urlparse import urlparse
from java.net import URL
import java
from org.apache.commons.codec.binary import Base64
from com.xebialabs.deployit.engine.api.dto import FileUpload



if 'repoId' not in request.query:
    raise Exception("repoId not present in request")
if 'packageId' not in request.query:
	raise Exception("packageId not present in request")

repo = repositoryService.read(request.query['repoId'])
serverUrl = repo.getProperty("serverUrl")
parsedServerUrl = urlparse(serverUrl)
username = repo.getProperty("username")
password = repo.getProperty("password")
kind = repo.getProperty("kind")

packageId = request.query['packageId']
packageIdSplit = packageId.split(' - ')
repository = packageIdSplit[3]
groupId = packageIdSplit[0]
artifactId = packageIdSplit[1]
version = packageIdSplit[2]

urlString = "%s://%s%s/repositories/%s/content/%s/%s/%s/%s-%s.dar" % (parsedServerUrl.scheme, parsedServerUrl.netloc, parsedServerUrl.path, repository, groupId.replace('.','/'), artifactId, version, artifactId, version)


url = URL(urlString);
uc = url.openConnection();
userpass = "%s:%s" % (username,password);
basicAuth = java.lang.String("Basic %s" % java.lang.String(Base64().encodeBase64(java.lang.String(userpass).getBytes())));
logger.info("Using basic auth with %s" % basicAuth)
uc.setRequestProperty ("Authorization", basicAuth);
inputStream = uc.getInputStream();

fileUpload = FileUpload()
fileUpload.setFileData(inputStream)
packageService.upload("%s-%s.dar" % (artifactId,version),fileUpload)