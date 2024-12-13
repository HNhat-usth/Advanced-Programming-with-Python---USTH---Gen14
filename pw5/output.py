import curses


class UI:
    def __init__(self):
        self.stdscr = None

    def start(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.stdscr.keypad(True)

        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    def close(self):
        if self.stdscr:
            curses.nocbreak()
            curses.echo()
            curses.curs_set(2)
            self.stdscr.keypad(False)
            curses.endwin()

    def display(self, message, title, color_pair=1, emphasis=curses.A_BOLD):
        while True:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, title, curses.color_pair(2) | curses.A_ITALIC)
            self.stdscr.addstr(
                1, 1, "(Press q to quit)", curses.color_pair(1) | curses.A_ITALIC
            )
            self.stdscr.addstr(2, 0, message, curses.color_pair(color_pair) | emphasis)
            key = self.stdscr.getch()
            if key == ord("q"):
                break
