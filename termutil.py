import sys
import os

def term_size(fd):
    """
    Returns the size of the terminal, connected to file_descriptor fd.

    If [fd] is not terminal returns null.

    Uses one of several metods [ioctl, stty size], to determine terminal size.
    """
    #if not isterminal(fd):
    #    print("File descriptor not a terminal!")
    #    sys.exit(1)
    try:
        rows, cols = fcntl_term_size()
    except:
        rows, cols = stty_term_size()
    return rows, cols

# Use ioctl's to get current terminal size
def fcntl_term_size():
    import fcntl, termios, struct
    h, w, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return h, w

def stty_term_size():
    import os
    rows, columns = os.popen('stty size', 'r').read().split()
    return rows, columns

def isterminal(fd):
    return os.isatty(fd) 
