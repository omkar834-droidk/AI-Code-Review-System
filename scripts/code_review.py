import subprocess
import os
from google import genai


def getdiff():
    diff = subprocess.check_output(['git','show'], text=True, )
    return diff


clinet = genai.Client()



def main():
    diff = getdiff()
    promt = f"Review the following code changes and provide feedback:\n\n mandatory : provide a output in html format that can used to send as an email :\n\n{diff}"
    response = clinet.models.generate_content(
        model="gemini-3-flash-preview",
        contents=promt
    )
    print("code review feedback:")
    print(response.text)

main()
