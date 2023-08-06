import time

from ahk import AHK

ahk = AHK()

# time.sleep(3)
# ahk.key_down('control')
# ahk.key_down('a')
# ahk.key_up('control')
# ahk.key_up('a')
# time.sleep(3)
#
# ahk.key_down('control')
# ahk.key_down('b')
# ahk.key_up('control')
# ahk.key_up('b')


# time.sleep(3)
# ahk.send("^a")
# time.sleep(3)
# ahk.send("^b")

wins = ahk.windows()

for win in wins:
    print(win.title)

obs_window = ahk.find_window(title=b'OBS 27.2.3 (64-bit, windows) - Profile: Untitled - Scenes: Untitled')
obs_window.activate()
obs_window.send('^A', blocking=False)
obs_window.minimize()
time.sleep(5)
obs_window.activate()
obs_window.send('^B', blocking=False)
obs_window.minimize()