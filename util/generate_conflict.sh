# Script to generate a git repository and
# generate a merge conflict on four files
# marked with a '*'.
#
#           repo
#          /   \
#         x     y
#        / \   / \
#       x1 x2 y1  y2
#       *  *  *   *

# Create git repo in 'tmp'
mkdir ./tmp
cd tmp
git init
mkdir x
mkdir y
touch x/x1
touch x/x2
touch y/y1
touch y/y2
git status
git add x
git add y
git commit -m 'Initial commit on master branch' 

# Modify x1, x2, y1 and y2 on a feature branch
git checkout -b feature
echo x1foo > x/x1 
echo x2foo > x/x2 
echo y1foo > y/y1 
echo y2foo > y/y2
git commit -a -m 'Changes on feature branch'

# Modify x1, x2, y1 and y2 on the master branch
git checkout master 
echo x1bar > x/x1 
echo x2bar > x/x2 
echo y1bar > y/y1 
echo y2bar > y/y2
git status
git commit -a -m 'Changes on master branch'

# Create the merge conflict
git merge feature
