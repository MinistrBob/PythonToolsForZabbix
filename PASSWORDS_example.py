DEBUG = True
# PROFILE = DEV, PROD
PROFILE = 'DEV'

default_settings = dict(
    max_counter=10,  # When memory utilization gets more 90% program try MAX_COUNTER times send email.
    try_pause=60,  # Pause between attempts TRY_PAUSE sec
    checks_pause=10,  # Every PROBE_PAUSE program checks memory utilization until the utilization is more than 90%
    sender_email='sender@domen.org',  # you can filter mail by it
    ymail_login='sender@domen.org',  # Yandex login for smtp
    ymail_password='wertiu4857jfk',
    recipient_emails=['admin@gmail.com'], # email TO list
)

if PROFILE == 'PROD':
    profile_settings = dict(
        recipient_emails=['admin@gmail.com'],
    )

if PROFILE == 'DEV':
    profile_settings = dict(
        recipient_emails=['admin@gmail.com'],
    )

# print(settings)
# merge dictionary Python 3.5 or greater (https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-in-python)
settings = {**default_settings, **profile_settings}

if __name__ == '__main__':
    import pprint

    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(profile_settings)
    pp.pprint(settings)
