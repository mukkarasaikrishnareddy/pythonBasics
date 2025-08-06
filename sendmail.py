import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

if weekday <= 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quotes = random.choice(all_quotes)

        print(quotes)

        MY_EMAIL = "rockstarkid2006@gmail.com"
        MY_PASSWORD = "nvlz kzta oirj imrx"

        while True:
            for quotes in range(0, 1000):
                with smtplib.SMTP("smtp.gmail.com", 587) as s:
                    s.starttls()
                    s.login(MY_EMAIL, MY_PASSWORD)
                    s.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs="sairockstar2006@gmail.com",
                        msg=f"Subject: its for you\n\n{quotes}"
                    )

