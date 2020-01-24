from threading import Thread

import time

import smtplib

from secrets import HOST

class SenderThread(Thread):
    '''need a description'''

    def __init__(self, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)
        self.name = name

    def run(self):
        server = smtplib.SMTP(self.host)
        server.sendmail(self.FROM, self.TO, self.BODY)
