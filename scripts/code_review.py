import subprocess

def getdiff():
    diff = subprocess.check_output(['git','diff'], text=True, )
    return diff



print(getdiff())