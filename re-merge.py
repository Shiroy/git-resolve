import os
import pygit2

repo = pygit2.Repository(os.getcwd())
ind = repo.index
ind.read()

print("Index contains: " + str(len(ind)) + " elements")

confs = ind.conflicts

ind2 = pygit2.Index()
paths = []
ids = []
for c in confs:
  ind2.add(c[1])
  paths.append(c[1].path)
  ids.append(c[1].id)
	
ind.clear()
for e in ind2:
  ind.add(e)

for c in confs:
  ind.add(c[1])

print("Index contains: " + str(len(ind)) + " elements")

ind.write()

commit = repo.revparse_single('HEAD')
merge_commit = repo.revparse_single('MERGE_HEAD')
aut = pygit2.Signature('name here','email here')
t = ind.write_tree()
repo.create_commit('HEAD', aut, aut, 'some comment', t, [commit.id, merge_commit.id])

for i in range(len(paths)):
  with open(paths[i], 'wb') as fd:
    fd.write(repo[ids[i]].data)


os.remove(repo.path + '/MERGE_HEAD')
os.remove(repo.path + 'MERGE_MODE')
os.remove(repo.path + 'MERGE_MSG')





