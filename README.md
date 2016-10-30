# SMS Mailer

## About

This is an absurdly simple script, it allows you to text yourself from the
command line.

I wrote it last spring while I was working on a machine learning assignment with
REALLY long run times, so I could go out and do other things (AFK) while my code
ran, while still getting updates. 

## Usage

First configure the `./config.py` file by adding your email, the email you want
to send messages from, and your sendgrid api key (http://sendgrip.com).

By calling sms mailer from the command line, it will send the arguments as a
email (or text if you use an email to text gateway,
http://www.digitaltrends.com/mobile/how-to-send-e-mail-to-sms-text/).

This is useful for when running really long commands:

```
$ some-really-long-command; sms "Done running really long command!"
```

You can also import the python file to other scripts and call the `send(msg)`
function yourself (for example in a for loop during some machine learning
training procedure, to keep you updated on progress)

## Author

Tomas Reimers, 2016
