import sendgrid
import config
import sys

# configure sendgrid

sg = sendgrid.SendGridClient(config.SENDGRID_API_KEY)

def send(subject):
    message = sendgrid.Mail(
        to=config.TO,
        subject=subject,
        text=' ',
        from_email=config.FROM
    )
    status, msg = sg.send(message)
    if status != 200:
        print "SENDING SMS FAILED: " + str(msg)
    return status, msg

if __name__ == "__main__":
    send(" ".join(sys.argv[1:]))
