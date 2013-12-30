from sys import argv
import *


#### MAIN ####
# Validate arguments
# 1: Node01
# 2: Env01
# 3: Node02
# 4: Env02
# 5: puppet master URI (optional)
# 6: destination file (optional)
script, node01, env01, node02, env02, puppeturi, dest_file = argv

catalog1 = Catalog()
catalog2 = Catalog()

# Get contents from puppet master
catalog1.read(node01,env01)
catalog2.read(node02,env02)

# Do a diff and see how many changes are
changes = catalog1.diff(catalog2)

# Apply changes into first catalog
catalog1.applyPatches(changes)

# Write on a file or print into stdout
if dest_file != None:
  target = open(dest_file, 'w')
  target.truncate()
  target.write(catalog1.getPuppetCode())
  target.close()
  print "Puppet resources written into %s" % (dest_file)
else:
  print catalog1.getPuppetCode()