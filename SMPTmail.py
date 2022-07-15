from __future__ import print_function

import base64
from email.message import EmailMessage
from operator import index
import google.auth
from googleapiclient.discovery import build
from googleapiclient.discovery import HttpError
import senWind, os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./token.json"

SCOPES = "https://www.googleapis.com/auth/gmail.modify","https://www.googleapis.com//auth/userinfo.email"


def gmail_send_message():

    creds, _ = google.auth.default()
    try:
        service = build('gmail', 'v1', credentials=creds)
        message = EmailMessage()

        message.set_content(senWind.contentMail.get("1.0",'end-1c'))

        message['To'] = senWind.receiverMail.get()

        message['Subject'] = senWind.subjectMail.get()

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            .decode()

        create_message = {
            'raw': encoded_message
        }
        # pylint: disable=E1101
        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        print(F'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message


if __name__ == '__main__':
    gmail_send_message()
