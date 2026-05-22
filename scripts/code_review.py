import subprocess
import os
from google import genai
import smtplib
from email.message import EmailMessage


def getdiff():
    diff = subprocess.check_output(['git','show'], text=True, )
    return diff


clinet = genai.Client()


def send_email(html_content):
    msg = EmailMessage()
    msg.set_content("please find the code review feedback in html format below:")
    msg['Subject'] = 'Code Review Feedback: ' 
    msg['From'] = 'salunkeomkar834@gmail.com'  # Replace with your email
    msg['To'] = 'salunkeomkar834@gmail.com'  # Replace with recipient's email
    msg.add_alternative(html_content, subtype='html')

    # Use Gmail's SMTP server with proper TLS setup
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Port 587 for TLS
    server.starttls()  # Enable TLS encryption BEFORE login
    server.login('salunkeomkar834@gmail.com', os.getenv('MAIL_PASSWORD'))
    server.send_message(msg)
    server.quit()
    
    return "Email sent successfully!"



 

def main():
    diff = getdiff()
    promt = f"Review the following code changes and provide feedback:\n\n mandatory : provide a output in html format that can used to send as an email :\n\n{diff}"
    response = clinet.models.generate_content(
        model="gemini-3-flash-preview",
        contents=promt
    )
    html = response.text
    send_email(html)
    

main()
