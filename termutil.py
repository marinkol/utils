import sys
import os
from subprocess import check_output, CalledProcessError

def term_size(fd):
    """
    Returns the size of the terminal, connected to file_descriptor fd.

    If [fd] is not terminal returns null.

    Uses one of several metods [ioctl, stty size], to determine terminal size.
    """
    if not isterminal(fd):
        print("File descriptor not a terminal!")
        sys.exit(1)
    try:
        rows, cols = fcntl_term_size(fd)
    except:
        try:
            rows, cols = stty_term_size()
        except CalledProcessError as e:
            print("Could not execute stty_term_size!")
            sys.exit(1)
    return rows, cols

# Use ioctl's to get current terminal size
def fcntl_term_size(fd):
    import fcntl, termios, struct
    h, w, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(fd, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return h, w

def stty_term_size():
    rows, columns = check_output(["stty", "size"]).split()
    return int(rows), int(columns)

def isterminal(fd):
    return os.isatty(fd) 
