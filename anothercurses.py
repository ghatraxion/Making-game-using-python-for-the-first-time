import curses

def main(stdscr):
    curses.curs_get(0)
    stdscr.nodelay(True)
    stdscr.timeout(16)

    y, x = 5, 10

    while True:
        stdscr