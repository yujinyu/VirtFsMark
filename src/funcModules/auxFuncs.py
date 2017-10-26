# -*- coding: UTF-8 -*-
import paramiko
import re
from time import sleep
from random import Random


def random_str(randomlength=6):
    string = ""
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    length = len(chars) - 1
    random = Random()
    for l in range(randomlength):
        string += chars[random.randint(0, length)]
    return string


class Rhost(object):
    def __init__(self, ip, username, password, timeout=30):
        self.ip = ip
        self.username = username
        self.password = password
        self.timeout = timeout
        # transport and chanel
        self.transport = ''
        self.channel = ''
        self.try_times = 3

    def connect(self):
        while True:
            try:
                self.transport = paramiko.Transport(sock=(self.ip, 22))
                self.transport.connect(username=self.username, password=self.password)
                self.channel = self.transport.open_session()
                self.channel.settimeout(self.timeout)
                self.channel.get_pty()
                self.channel.invoke_shell()
                return
            except Exception as e1:
                if self.try_times != 0:
                    print('%s\nFailed to connect to %s' % (str(e1),self.ip))
                    self.try_times -= 1
                else:
                    print('Exit')
                    exit(1)


    def exec_cmd(self, cmd):
        cmd += '\r'
        p = re.compile(r':~#')

        result = ''
        self.channel.send(cmd)
        while True:
            ret = self.channel.recv(65535)
            ret = ret.decode('utf-8')
            result += ret
            if p.search(ret):
                # print(result)
                return result
            sleep(0.5)

    def close(self):
        self.channel.close()
        self.transport.close()