import curses

def main(stdscr):
    curses.curs_get(0)
    stdscr.nodelay(True)
    stdscr.timeout(16)

    y, x = 5, 10

    while True:
        stdscr.clear()
        stdscr.addstr(y, x, "#")
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            y += 1
        elif key == curses.KEY_DOWN:
            y -= 1
        elif key == curses.KEY_RIGHT:
            x += 1
        elif key == curses.KEY_LEFT:
            x -= 1
        elif key == ord("q"):
            break
curses.wrapper(main)