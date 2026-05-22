import subprocess

def getdiff():
    diff = subprocess.run(['git','diff'], text=True, )
    return diff



print(getdiff())