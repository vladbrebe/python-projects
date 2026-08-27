
import datetime


class Email:

    # sender: The user sending the message
    # receiver: The user receiving it
    # subject: Subject line
    # body: Message body
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False

    # mark message as read
    def mark_as_read(self) -> None:
        self.read = True

    # Return the full message as text and mark it read
    def display_full_email(self) -> str:
        self.mark_as_read()
        
        return (
            "\n--- Email ---\n"
            f"From: {self.sender.name}\n"
            f"To: {self.receiver.name}\n"
            f"Subject: {self.subject}\n"
            f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}\n"
            f"Body: {self.body}\n"
            "------------\n"
        )

    def __str__(self) -> str:
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"



class Inbox:

    def __init__(self) -> None:
        self.emails = []

    # add email to 'emails'
    def receive_email(self, email) -> None:
        self.emails.append(email)

    # summarises each item in 'emails' on its own line
    def list_emails(self):
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')


        
    # reads the item in 'emails' at true index 'position'
    def read_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        self.emails[actual_index].display_full_email()

        
    # delete the item in 'emails' at true position 'index'
    def delete_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        del self.emails[actual_index]
        print('Email deleted.\n')


class User:

    # name
    def __init__(self, name: str) -> None:
        self.name = name
        self.inbox = Inbox()

    # sends an Email to 'receiver'
    def send_email(self, receive, subject: str, body: str):

        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    # displays all Emails in inbox
    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    # reads Email at index 'index'
    def read_email(self, index):
        self.inbox.read_email(index)

    # deletes Email at index 'index'
    def delete_email(self, index):
        self.inbox.delete_email(index)


def main():
    tory = User('Tory')
    ramy = User('Ramy')        
    
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')

    ramy.check_inbox()  
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox()  

if __name__ == "__main__":
    main()
