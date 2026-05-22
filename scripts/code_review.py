import subprocess

def getdiff():
    diff = subprocess.check_output(['git','show'], text=True, )
    return diff



print(getdiff())