import signal


def catch_ctrl_c(signum, frame):
    print ("cat Ctrl+C, Go to exit...")
    exit (0)


if __name__ == "__main__":
    try:
        print ("test A!")
    finally:
        signal.signal (signal.SIGINT, catch_ctrl_c)
