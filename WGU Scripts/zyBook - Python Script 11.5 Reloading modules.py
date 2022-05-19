# send_gmail.py: Sends a single email through gmail.
import smtplib
from email.mime.text import MIMEText

header = 'Hello. This is an automated email.\n\n'

def send(subject, to, frm, text):
    # The message to send
    msg = MIMEText(header + text)
    msg['Subject'] = subject
    msg['To'] = to
    msg['From'] = frm

    # Connect to gmail's email server and send
    s = smtplib.SMTP('smtp.gmail.com', port=587)
    s.ehlo()
    s.starttls()
    s.login(user=frm, password='password')
    s.sendmail(frm, [to], msg.as_string())
    s.quit()

if __name__ == "__main__":
    send(
        subject='A coupon for you!',
        to='billgates@microsoft.com',
        frm='JohnnysHotDogs1@gmail.com',
        text='Enjoy!')






# send_coupons.py: Automates emails to loyal customers.
import os
from imp import reload
import send_gmail

mod_time = os.path.getmtime(send_gmail.__file__)

emails = [  # Could be large list or stored in file
    'billgates@microsoft.com',
    'president@whitehouse.gov',
    'benedictxvi@vatican.va'
]

my_email = 'JohnnysHotDogs1@gmail.com'
subject = 'A coupon for you!'
text = ("As a loyal customer of Johnny's HotDogs, "
        "here is a coupon for 1 free bratwurst!")

for addr in emails:
    send_gmail.send(subject, addr, my_email, text)

    # Check if file has been modified
    last_mod = os.path.getmtime(send_gmail.__file__)
    if last_mod > mod_time:
        mod_time = last_mod
        reload(send_gmail)




# Modifying send_gmail.py while the program is running updates the email contents.
import smtplib
from email.mime.text import MIMEText

header = 'This is an important message from Johnny!'

def send(subject, to frm, txt):
    # ...




# Reloading modules doesn't affect attributes imported using 'from'.
from imp import reload
import send_gmail
from send_gmail import header

print('Original value of header:', header)

print('\n(---- send_gmail.py source code edited ----)')

print('\nReloading send_gmail\n')
reload(send_gmail)

print('header:', header)
print('send_gmail.header:', send_gmail.header)





