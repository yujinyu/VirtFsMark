import multiprocessing
import sys
import time
import os
from random import Random


def random_str(randomlength=6):
    string = ""
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    length = len(chars) - 1
    random = Random()
    for l in range(randomlength):
        string += chars[random.randint(0, length)]
    return string


class Write2file(multiprocessing.Process):
    def __init__(self, filename, line):
        multiprocessing.Process.__init__(self)
        self.filename = filename
        self.line = line

    def run(self):
        fp = open(self.filename, 'w')
        for i in range(1, self.line + 1):
            fp.write("%d line %s\n" % (i, random_str(8)))
        fp.close()


if __name__ == "__main__":
    filenum = int(sys.argv[2])
    degree_of_parallelism = int(sys.argv[1])
    type = ["T","B"]
    jobs = []
    fp = open("/mnt/multifile%s-%s" % (str(degree_of_parallelism), time.strftime('%y%m%d%H%M', time.localtime(time.time()))), 'w')
    for tp in type:
        # print("-"*128)
        # print("type: %s\n\n" % tp)
        if tp == "T":
            os.system("mkdir -p /testT && cd /testT && touch file{1..%s}" % filenum)
        tmp = 1 + degree_of_parallelism
        start = time.time()
        while tmp <= filenum:
            for i in range(tmp - degree_of_parallelism, tmp):
                filepath = "/test%s/file%s" % (tp, str(i))
                p = Write2file(filepath, 32)
                jobs.append(p)
                p.start()
            for p in jobs:
                p.join()
            tmp += degree_of_parallelism
        for i in range(tmp - degree_of_parallelism, filenum):
            filepath = "/test%s/file%s" % (tp, str(i))
            p = Write2file(filepath, 80)
            jobs.append(p)
            p.start()
        for p in jobs:
            p.join()
        end = time.time()
        fp.write("%s runtime: %s s\n" % (tp, str(round(end - start, 3))))
    fp.close()
