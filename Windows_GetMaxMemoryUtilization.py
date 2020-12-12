import psutil
import os
import PASSWORDS
import pprint
import time
from alert_to_mail import send_email
from custom_logger import get_logger
# psutil.Process(pid=4196, name='chrome.exe', status='running', started='2020-12-09 09:55:34')


def get_process_list():
    """Return last 10 items sorted dict processes by process.memory_percent()"""
    process = {p.memory_percent(): p.info for p in psutil.process_iter(['name', 'username'])}
    if PASSWORDS.DEBUG:
        logger.debug(f"process:\n{pprint.pformat(process)}")
    process = dict((sorted(process.items(), reverse=True))[:10])
    # print(process)
    return process


if __name__ == "__main__":
    program_file = os.path.realpath(__file__)
    logger = get_logger(program_file=program_file)
    print(f"Log file: {logger.handlers[0].baseFilename}")
    counter = 1
    logger.info(">>>> BEGIN PROBE >>>>")
    while True:
        work_done = False
        memory_utilization = psutil.virtual_memory().percent  # float
        logger.info(memory_utilization)
        if memory_utilization > 90:
            logger.info(f">>>> probe #{counter}")
            process_list = pprint.pformat(get_process_list())
            receiver_emails = PASSWORDS.settings['recipient_emails']
            subject = "MaxMemoryUtilization"
            message = f"List processes:\n{process_list}"
            logger.info(message)
            # attached_file = None
            attached_file = logger.handlers[0].baseFilename
            send_email(receiver_emails, subject, message, logger, attached_file)
            if PASSWORDS.settings['max_counter'] is not None:  # probe max_counter times
                counter += 1
                if counter > PASSWORDS.settings['max_counter']:
                    break  # exit
                else:
                    time.sleep(PASSWORDS.settings['try_pause'])
            else:  # infinity probe
                time.sleep(PASSWORDS.settings['try_pause'])
        else:
            time.sleep(PASSWORDS.settings['checks_pause'])
