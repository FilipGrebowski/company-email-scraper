# company-email-scraper

A scraper fetching all company emails from Seedtable and Clutch websites.

🚀 Install the dependancies: `pip3 install -r requirements.txt`

In order to use sendgrid, you will need to go register with them and optain the SENDGRID_API_KEY that they provide you with.
You will have to store that SENDGRID_API_KEY in a sendgrid.env file.

[SendGrid API Getting Started](https://sendgrid.com/docs/for-developers/sending-email/api-getting-started/#prerequisites-for-sending-your-first-email-with-the-sendgrid-api)

Before running the program, remember to export your SENDGRID_API_KEY in terminal.\
`export SENDGRID_API_KEY='YOUR_SENDGRID_API_KEY'`

Once everything is set up, go into the `scrapers` folder and run either `python clutchco_scraper.py` or `python seedtable_scraper.py`. This will create your csv file with all thr emails.

Once that is done, go into the main directory, make sure you alter the message ur sending with your sender email, the subject line and the message content. After, just run `python send_emails.py` and you should be good!

💛 Happy Sending!

![Alt Text](https://media.giphy.com/media/kDaE01OtFSyobqta2C/giphy.gif)
