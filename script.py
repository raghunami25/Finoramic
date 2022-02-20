import sys
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor

successful_packages = []
failed_package = []

def package_installation(package):
    try:
        cmd = [sys.executable, '-m', 'pip', 'install',package]
        res = subprocess.call(cmd,stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        if res:
            successful_packages.append(package)
        else:
            failed_package.append(package)
    except Exception as e:
        print(e)

def main():
    try:
        f = open('package.json','r')
        data = json.load(f)
        with ThreadPoolExecutor(max_workers=700) as executor:
            for package in data['Dependencies']:
                executor.submit(package_installation, (package))
        f.close()
        print(successful_packages)
        print(failed_package)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
