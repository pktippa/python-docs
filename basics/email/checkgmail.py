import imaplib, struct, time, os

class Mail():
    def __init__(self, username, password):
        self.user= username
        self.password= password
        self.M = imaplib.IMAP4_SSL('imap.gmail.com', '993')
        self.M.login(self.user, self.password)
        
    def checkMail(self):
        self.M.select()
        self.unRead = self.M.search(None, 'UnSeen')
        return len(self.unRead[1][0].split())
    
    def sendData(self):
        self.numMessages= self.checkMail()
        print('No of messages: ', self.numMessages)

if __name__ == "__main__":
    # Retrieving Environment variables.
    user = os.environ.get('GMAIL_USER')
    passw = os.environ.get('GMAIL_PASS')
    if user and passw:
        email = Mail(user, passw)
        # check for new mail every minute
        while 1:
            print('Sending')
            email.sendData()
            print('Sleeping for 1 minute and then trigger again.')
            time.sleep(60)
    else:
        print('Please set required Environment Variables')
