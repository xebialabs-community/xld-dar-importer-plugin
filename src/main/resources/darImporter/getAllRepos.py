print request

result = []
repos = repositoryService.query(Type.valueOf("repository.Importer"),None,None,None,None,None,1,-1)
for repo in repos:
	result.append(repo.id)

response.entity = result