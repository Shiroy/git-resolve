import os
import pygit2

repo = pygit2.Repository(os.getcwd())
ind = repo.index
ind.read()

confs = ind.conflicts

ind2 = pygit2.Index()
for c in confs:
	ind2.add(c[1]) 
ind.clear()
for e in ind2:
	ind.add(e)

commit = repo.revparse_single('HEAD')
aut = pygit2.Signature('name here','email here')
t = ind.write_tree()
repo.create_commit('HEAD', aut, aut, 'some comment', t, [commit.id])
with open(ind[0].path, 'wb') as fd:
	fd.write(repo[ind[0].id].data)

