import re
import os
import fnmatch


pattern = re.compile(">(?s)(.*)</Text>")
exclude = set(['node_modules'])

for root, dirs, files in os.walk("./"):
        dirs[:] = [d for d in dirs if d not in exclude]
	for file in files:
		if(file.endswith(".js")):
                    path = str(os.path.join(root,file))
                    for i, line in enumerate(open(path)):
                       # for match in re.finditer(pattern, line):
                        for match in re.finditer(pattern, line):
                            print "Line %s: str ----> '%s' fichier ----> '%s'" % (i+1, match.group(1), path)
