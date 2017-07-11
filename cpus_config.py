import os
import glob


def is_int(s):
    if s.isdigit():
        return int(s)
    return s


#
# processor Range syntax
#

def parse_range(r):
    """
        Parse an integer sequence such as '0-3,8-11'.
        '' is the empty sequence.
    """
    if not r.strip():
        return []

    res = []
    for piece in r.strip().split(","):
        lr = piece.split("-")
        if len(lr) == 1 and lr[0].isdigit():
            res.append(int(lr[0]))
        elif len(lr) == 2 and lr[0].isdigit() and lr[1].isdigit():
            res.extend(range(int(lr[0]), int(lr[1]) + 1))
        else:
            raise ValueError("Invalid range syntax: %r" % r)
    return res


def get_cpu_info_from_sys(name):
    return parse_range(file("/sys/devices/system/cpu/%s" % name).read())


def get_cpu_info_from_proc(path):
    """
        Read a cpuinfo file and return [{field : value}].
    """

    res = []
    for block in file(path, "r").read().split("\n\n"):
        if len(block.strip()):
            res.append({})
            for line in block.splitlines():
                k, v = map(str.strip, line.split(":", 1))
                res[-1][k] = is_int(v)
            # Try to get additional info
            processor = res[-1]["processor"]
            node_files = glob.glob("/sys/devices/system/cpu/cpu%d/node*" % processor)
            if len(node_files):
                print node_files
                print os.path.basename(node_files[0])[4:]
                res[-1]["node"] = int(os.path.basename(node_files[0])[4:])
    return res

if __name__ == "__main__":
    print(get_cpu_info_from_sys("online"))
    result = get_cpu_info_from_proc("/proc/cpuinfo")
    a = 0
    for sp in result:
        print a
        print sp
        print ("")
        a += 1
