import curses
from db.users import check_username

def main(stdscr):
    curses.curs_set(1)
    stdscr.clear()
    
    stdscr.addstr(0, 0, "Welcome to the Animal Town. Please input your username to create a new game or load existing save:")
    stdscr.refresh()
    curses.echo()
    username = stdscr.getstr(2, 16).decode('utf-8')

    if check_username(username):
        stdscr.addstr(4, 0, "You have a game saved. Continue?")
    else:
        stdscr.addstr(4, 0, "No save detected. Do you want to start a new game?")
    
    stdscr.refresh()
    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
