import os
import smtplib
import csv
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# List of folder paths
folders = ["N:\\i1", "N:\\v2", "N:\\v3"]

# EmailSender class is used to send emails with attachments
class EmailSender:
    # Initialize the object with the recipient's email address, the subject and body of the email, and the file path of the attachment
    def __init__(self, to, subject, body, filePath):
        self.to = to
        self.subject = subject
        self.body = body
        self.filePath = filePath
    
    # send email method
    def send_email(self):
        msg = MIMEMultipart()
        msg['From'] = 'backup@bandicoot.co.uk'
        msg['To'] = self.to
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.body, 'plain'))

        # open the file in bynary
        binary_csv = open(self.filePath, 'rb')

        # attach the file
        payload = MIMEBase('application', 'octate-stream', Name=self.filePath)
        payload.set_payload((binary_csv).read())

        # enconding the binary into base64
        encoders.encode_base64(payload)

        # add header with pdf name
        payload.add_header('Content-Decomposition', 'attachment', filename=self.filePath)
        msg.attach(payload)

        # create server
        s = smtplib.SMTP('localhost')
        # start TLS for security
        s.starttls()
        # send message via server.
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        # Terminating the session
        s.quit()

def main():
    # Function to check if a file was modified within the past 24 hours
    def modifiedWithin24hr(file):
        now = datetime.now()
        last_modified = datetime.fromtimestamp(os.stat(file).st_mtime)
        return now - last_modified < timedelta(hours=24)

    with open("output.csv", "w", newline="") as csvfile:
        fieldnames = ["Server", "file", "Last modified"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Iterate through the folders
        for folder in folders:
            # Get a list of all the files in the folder
            files = os.listdir(folder)
            
            for item in files:
                # Get the full path of the file
                filePath = os.path.join(folder, item)
                # Create a dictionary to store the folder name, the file name, and whether the file was modified within the past 24 hours
                itemProblemDict = {
                    "Server": folder,
                    "file": item,
                    "Last modified": modifiedWithin24hr
                }
            # Filter the list of files to only include files that were modified within the past 24 hours
            recentFiles = [f for f in files if modifiedWithin24hr(os.path.join(folder, f))]
            
            # If there are no recent files, skip to the next folder
            if not recentFiles:
                writer.writerow(itemProblemDict)
                emailSender = EmailSender('sean@bandicoot.co.uk', 'CSV File', 'Please find attached the CSV file with the list of modified files from the last 24 hours.', 'output.csv')
                emailSender.send_email()
            else:
                print(filePath)
            
main()