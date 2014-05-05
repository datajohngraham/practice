from subprocess import Popen, PIPE
import re
import sys
invocation = ['ps', 'fax']
#r = subprocess.call(invocation)
process = Popen(invocation, stdin = PIPE, stdout = PIPE)
print(process)
output = process.communicate()[0]
for line in list(str(output)):
        print(line)
#print(str(output))
#p = re.compile(str(sys.argv[1]))
#m = p.findall(str(output))
#print(len(m))
#print
#for line in output:
#       if re.findall

