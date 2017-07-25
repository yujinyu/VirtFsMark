import signal
from env_config import *
from variables_defined import pkg_list

def catch_ctrl_c(signum, frame):
    print ("cat Ctrl+C, Go to exit...")
    exit (0)


if __name__ == "__main__":
    try:
        ls = " "
        for pkg in pkg_list:
            if not is_installed(pkg):
                ls.join(" " + pkg)
        if ls is " ":
            print(" All Packages have been installed!")
        elif pkg_install(ls):
            print("Successfully!")
    finally:
        signal.signal (signal.SIGINT, catch_ctrl_c)
