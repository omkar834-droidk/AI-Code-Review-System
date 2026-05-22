# import subprocess
# import os
# from google import genai
# import smtplib
# from email.message import EmailMessage




# def getdiff():
#     diff = subprocess.check_output(['git','show'], text=True, )
#     return diff


# client = genai.Client()
# client = genai.Client(
#     api_key=os.getenv("GEMINI_API_KEY")
# )




# def get_commit_info():

#  diff = subprocess.check_output(
#     ['git', 'diff', 'HEAD~1', 'HEAD'],
#     text=True
# )   
#  commit_id, author, message = commit_id.split("\n")


#  return {
#         "commit_id": commit_id,
#         "author": author,
#         "message": message
#     }


# def send_email(html_content):
#     msg = EmailMessage()
#     msg.set_content("please find the code review feedback in html format below:")
#     msg['Subject'] = 'Code Review Feedback: ' 
#     msg['From'] = 'salunkeomkar834@gmail.com'  # Replace with your email
#     msg['To'] = 'salunkeomkar834@gmail.com'  # Replace with recipient's email
#     msg.add_alternative(html_content, subtype='html')

#     # Use Gmail's SMTP server with proper TLS setup
#     server = smtplib.SMTP('smtp.gmail.com', 587)  # Port 587 for TLS
#     server.starttls()  # Enable TLS encryption BEFORE login
#     server.login('salunkeomkar834@gmail.com', os.getenv('MAIL_PASSWORD'))
#     server.send_message(msg)
#     server.quit()
    
#     return "Email sent successfully!"


# def main():

#     diff = getdiff()

#     commit_info = get_commit_info()

#     prompt = f"""
# You are a senior AI code reviewer.

# Commit Details:
# Author: {commit_info['author']}
# Commit Message: {commit_info['message']}
# Commit ID: {commit_info['commit_id']}

# Analyze the following git code changes.

# Check for:
# 1. Bugs and logical issues
# 2. Security vulnerabilities
# 3. Performance optimization
# 4. Code readability
# 5. Best practices

# Provide:
# - Summary
# - Issues found
# - Severity level
# - Suggested fixes
# - Final score out of 10


# IMPORTANT:

# Return ONLY clean and modern HTML email format.

# Use:
# - colorful UI
# - modern cards
# - proper headings
# - tables
# - sections
# - severity colors
# - padding and spacing

# Color Rules:
# - Critical = Red
# - Medium = Orange
# - Low = Green
# - Headers = Blue

# Add:
# 1. Project title
# 2. Commit details section
# 3. AI review summary
# 4. Issues found section
# 5. Suggested fixes section
# 6. Final score card

# Use inline CSS styling.

# Make the email visually beautiful and professional.

# Git Diff:
# {diff}
# """

#     response = client.models.generate_content(
#         model="gemini-3-flash-preview",
#         contents=prompt
#     )

#     html = response.text

#     send_email(html)







import subprocess
import os
from google import genai
import smtplib
from email.message import EmailMessage


# Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# Get Latest Git Diff
def getdiff():

    diff = subprocess.check_output(
        ['git', 'diff', 'HEAD~1', 'HEAD'],
        text=True
    )

    return diff[:15000]


# Get Commit Information
def get_commit_info():

    commit = subprocess.check_output(
        ["git", "log", "-1", "--pretty=format:%H%n%an%n%s"],
        text=True
    )

    commit_id, author, message = commit.split("\n")

    return {
        "commit_id": commit_id,
        "author": author,
        "message": message
    }


# Send Email
def send_email(html_content, commit_info):

    msg = EmailMessage()

    msg['Subject'] = f"AI Code Review - {commit_info['message']}"

    msg['From'] = "salunkeomkar834@gmail.com"

    msg['To'] = "salunkeomkar834@gmail.com"

    msg.set_content(
        "Please open this email in HTML format."
    )

    msg.add_alternative(html_content, subtype='html')

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(
        "salunkeomkar834@gmail.com",
        os.getenv("MAIL_PASSWORD")
    )

    server.send_message(msg)

    server.quit()

    print("Email sent successfully!")


# Main Function
def main():

    print("Getting latest git diff...")

    diff = getdiff()

    print("Getting commit details...")

    commit_info = get_commit_info()

    print("Generating AI review...")

    prompt = f"""
You are a senior AI code reviewer.

Commit Details:
Author: {commit_info['author']}
Commit Message: {commit_info['message']}
Commit ID: {commit_info['commit_id']}

Analyze the following git code changes carefully.

Check for:
1. Bugs and logical issues
2. Security vulnerabilities
3. Performance optimization
4. Code readability
5. Best practices violations

Provide:
- Summary
- Issues found
- Severity level
- Suggested fixes
- Final score out of 10

IMPORTANT:

Return ONLY clean and modern HTML email format.

Use:
- colorful UI
- modern cards
- proper headings
- tables
- sections
- severity colors
- padding and spacing

Color Rules:
- Critical = Red
- Medium = Orange
- Low = Green
- Headers = Blue

Add:
1. Project title
2. Commit details section
3. AI review summary
4. Issues found section
5. Suggested fixes section
6. Final score card

Use inline CSS styling.

Make the email visually beautiful and professional.

Git Diff:
{diff}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("AI review generated successfully!")

    html = response.text

    print("Sending review email...")

    send_email(html, commit_info)

    print("Workflow completed successfully!")


# Run App
if __name__ == "__main__":
    main()