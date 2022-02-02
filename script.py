from struct import pack
import sys
import json
import subprocess

f = open('package.json','r')
data = json.load(f)
for i in data['Dependencies']:
    subprocess.call([sys.executable, '-m', 'pip', 'install',i],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
f.close()

reqs = subprocess.check_output([sys.executable, '-m', 'pip','freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

if(set(data['Dependencies']).issubset(set(installed_packages))):
    print("Success")
else:
    print("Failed Packages")
    for package in data['Dependencies']:
        if package not in installed_packages:
            if package == "pip":
                continue
            print(i)

