#modules
import imaplib
import email
import webbrowser
import re
import requests

def initializeServer(username, app_password, email_search) :
    # https://www.systoolsgroup.com/imap/
    gmail_host= 'imap.gmail.com'

    #set connection
    mail = imaplib.IMAP4_SSL(gmail_host)

    #login
    mail.login(username, app_password)

    #select inbox
    mail.select("INBOX")

    #select specific mails
    _, selected_mails = mail.search(None, email_search)

    return mail, selected_mails


def getLinks(username, password, emails) :
    links = []
    mail, selected_mails = initializeServer(username, password, emails)

    #total number of mails from specific user
    print("Total Messages:" , len(selected_mails[0].split()))

    for num in selected_mails[0].split():
        _, data = mail.fetch(num , '(RFC822)')
        _, bytes_data = data[0]

        #convert the byte data to message
        email_message = email.message_from_bytes(bytes_data)
        print("\n===========================================")

        #access data
        print("Subject: ",email_message["subject"])
        print("To:", email_message["to"])
        print("From: ",email_message["from"])
        print("Date: ",email_message["date"])
        for part in email_message.walk():
            if part.get_content_type()=="image" or part.get_content_type()=="text/html":
                message = part.get_payload(decode=True)
                decodedMessage = message.decode()
                inMessageLinks = re.findall(r'(https?://[^\s]+)', decodedMessage)
                links.append(inMessageLinks)
                print("==========================================\n")

    return links
    

def start(username, password, email_list) :
    for email in email_list :
        email_search = '(FROM ' + email + ')'
        emailLinks = getLinks(username, password, email_search)
        for links in emailLinks :
            for link in links :
                requests.get(link) 

start("cjuang23@sjs.org", "3874NmEb", ["elliot.savoie@communications.ttu.edu"])