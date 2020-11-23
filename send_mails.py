import os
import smtplib

EMAIL_ADDRESS = os.environ.get("GMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("GMAIL_PASS")

TO_SEND_SEO = 1
TO_SEND_FB = 1

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Test Email'

    # Send from "site"
    for m in range(TO_SEND_SEO):
        # Edit according to the required format
        body = '''name: yonatan
phone: 0524798290
email: jonatangurevich4@gmail.com
product: DevOps
branch: tel-aviv'''

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, 'qa.lidimrtg@gmail.com', msg)

    # # Send from "facebook"
    # for m in range(TO_SEND_FB):
    #     # Edit according to the required format
    #     body = '[evgeny\'s mail format]'
    #
    #     msg = f'Subject: {subject}\n\n{body}'
    #
    #     smtp.sendmail(EMAIL_ADDRESS, 'qa.job.mai.rtg@gmail.com', msg)
