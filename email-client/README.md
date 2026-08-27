# Email implementation

built at freeCodeCamp

Three classes: an `Email` is a message, an `Inbox` is an
ordered collection of Emails, and a `User` owns an inbox and can send mail to
another user.



```bash
python email_client.py
```

## Sample output


Sent 2 emails from Tory to Ramy.

Ramy's inbox:
1. [Unread] From: Tory | Subject: Hello | Time: 2026-08-27 11:42
2. [Unread] From: Tory | Subject: Lunch | Time: 2026-08-27 11:42

--- Email ---
From: Tory
To: Ramy
Subject: Hello
Received: 2026-08-27 11:42
Body: Hi Ramy, just saying hello!
------------

Ramy's inbox after deleting email 1:
1. [Unread] From: Tory | Subject: Lunch | Time: 2026-08-27 11:42


## Tests

```bash
pytest test_email_client.py
```
