# The curses library lets you create programs with a terminal or text-based user interface (TUI).
# In this program, we want to create and learn small projects using curses.

# First, let's import the library
import curses

# All the code should go into the main function, with a variable passed to it called stdscr.
# 'stdscr' stands for "standard screen" and is passed automatically by curses.wrapper().
def main(stdscr):
    # This function clears the standard screen
    stdscr.clear()
    
    # One important thing in curses is the use of x and y coordinates (rows and columns).
    # When displaying something or getting input, we need to set the position using y and x.

    # The addstr() function displays text to the screen
    stdscr.addstr(0, 0, "Hello, World!")

    # The refresh() function is very important because it updates the screen and allows changes to appear.
    # Without calling refresh(), nothing will be visible. Remember that.

    stdscr.refresh()

    # The getch() function waits for a key press.
    # We're not handling specific keys here because this isn't an input program.
    stdscr.getch()

# Now it's time to call our function and start the program
curses.wrapper(main)
