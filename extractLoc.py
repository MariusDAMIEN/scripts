import re
import os
import fnmatch


pattern = re.compile("Util.loc\(\"(.*)\"\)", flags=re.DOTALL)
exclude = set(['node_modules'])

for root, dirs, files in os.walk("./"):
        dirs[:] = [d for d in dirs if d not in exclude]
	for file in files:
		if(file.endswith(".js")):
                    path = str(os.path.join(root,file))
                    fd = open(path)
                    fd = fd.read()
                    for match in re.finditer(pattern, fd):
                        print "str ----> '%s' fichier ----> '%s'" % (match.group(1), path)
