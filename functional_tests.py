from selenium import webdriver

browser = webdriver.Firefox()

# Maximilian, an amateur 'brain hacker' would like to find a tool to improve his working memory.
# He decides to visit a site promising to do just that (memotune) through the vehicle of music...
browser.get('http://localhost:8000')

# He sees a brief few lines of (welcome) text followed by a 'next' button.  Underneath is a 'ready' button, in case he is already familiar with the app.
message = browser.find_elements_by_id("message")
ready_button = browser.find_elements_by_id("ready")
assert 'welcome' in message

# He clicks next and learns (explanation) that he will need to compare a musical note that he is hearing with one he heard before.
next_button = browser.find_elements_by_id("next")
next_button.click()

assert 'compare' in message

# A 'back' button becomes available that takes Max to the previous instruction when clicked.

back_button = browser.find_elements_by_id("back")

# He clicks 'next' and reads a few (tips) on how to use Memotune productively.
next_button.click()
assert 'productive' in message

# Since this is the last instruction, the 'next' button disappears.

assert next_button.is_displayed() == False 

# Max clicks 'ready'.  On the previously empty canvas appears a thin black outline of a square on white.

ready.click()
canvas = browser.find_element_by_id("canvas")

# The 'GO' button replaces the 'ready' button and instruction buttons underneath the canvas.

go_button = browser.find_elements_by_id("go")
assert ready_button.is_displayed() == False
assert back_button.is_displayed() == False
assert go_button.is_displayed()

# Beside the canvas is a table of information on Max's session.  This includes...

table = browser.find_element_by_id("session_table")

## level
assert 'level' in table
assert r'[0-9]+' in table
## score
assert 'score' in table
assert r'[0-9]+' in table

# Max clicks 'GO' and immediately hears a musical note, then another, then a third.  He's not sure whether the first and third were the same, so he guesses --
go_button.click()
square = browser.find_elements_by_id("square")
browser.implicit_wait(note_length * 2)
square.click()

## If he was right and this was indeed the same note, the box outline flashes green for the duration of one note.

## If he was wrong and this was a different note, the box outline flashes magenta/red for the duration of one note and increases its thickness, which symbolizes how close he is to losing.

# Max continues playing and goes through enough notes such that he can potentially lose or progress one level...

# If Max progresses to the next level, a brief message congratulates him.

## A new set of notes then begin to play, this time more rapidly than before.

# If Max loses, his current score is displayed on the screen along with a 'start over' button.

## If Max's score is sufficiently high, he will be congratulated and given the option to enter his name, which will be recorded in the 'high scores' list.

## The 'high scores' are then displayed along with Max's.

# Satisfied, he decides to come back another day.

browser.quit()