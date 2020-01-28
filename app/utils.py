from threading import Thread

import os

import time
import datetime

import smtplib
import ssl


if os.path.isfile('app/secrets.py'):
    from .secrets import HOST, PORT, FROM, PASSWORD, LOGIN
else:
    HOST = os.environ.get('HOST')
    PORT = os.environ.get('MAILSERVERPORT')
    FROM = os.environ.get('FROM')
    PASSWORD = os.environ.get('PASSWORD')
    LOGIN = os.environ.get('LOGIN')

print(f'HOST = {HOST}')
print(f'PORT = {PORT}')
print(f'FROM = {FROM}')
print(f'PASSWORD = {PASSWORD}')
print(f'LOGIN = {LOGIN}')


class SenderThread(Thread):
# class SenderThread:
    '''need a description'''
    host = HOST
    time_to_send = None

    def __init__(self, *args, **kwargs):
        Thread.__init__(self)
        self.__host = kwargs.get('__host', HOST)
        self.__port = kwargs.get('__port', PORT)
        self.__from = kwargs.get('__from', FROM)
        self.__pass = kwargs.get('__pass', PASSWORD)
        self.__login = kwargs.get('__login', LOGIN)
        self.__from = kwargs.get('__from', FROM)
        self.rec_email = kwargs.get('rec_email')
        self.mailtext = kwargs.get('mailtext')
        self.sending_delay = kwargs.get('sending_delay', 0)
        
        if isinstance(self.sending_delay, str):
            self.sending_delay = int(self.sending_delay)

    def run(self):
        print('Thread run')
        time.sleep(self.sending_delay)
        self.send_email(self)
        print('Mail sended')

    # def send_email(self, *args, **kwargs):
    #     server = smtplib.SMTP_SSL(self.__host, self.__port)
    #     server.login(self.__login, self.__pass)
    #     server.sendmail(
    #         self.__from,
    #         self.rec_email,
    #         self.mailtext,
    #     )
    #     server.quit()

    def send_email(self, *args, **kwargs):
        server = smtplib.SMTP(self.__host, self.__port)
        server.login(self.__login, self.__pass)
        server.sendmail(
            self.__from,
            self.rec_email,
            self.mailtext,
        )
        server.quit()
    
    # def send_email(self, *args, **kwargs):
    #     context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    #     server = smtplib.SMTP(self.__host, self.__port)

    #     server.ehlo()
    #     server.starttls(context=context)
    #     server.ehlo()

    #     server.login(self.__login, self.__pass)

    #     server.sendmail(
    #         self.__from,
    #         self.rec_email,
    #         self.mailtext,
    #     )

    #     server.quit()


def main():
    sender = SenderThread(rec_email = '2100992@gmail.com', mailtext = 'testing mailtext', sending_delay = 10)
    sender.start()
    sender.is_alive


if __name__ == "__main__":
    main()