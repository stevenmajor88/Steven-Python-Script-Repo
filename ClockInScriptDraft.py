import pyautogui
# pip installpyautogui
# pyautogui.size()


def clicky():
    pyautogui.moveRel(-28, 27, duration=0.5)  # startbutton
    pyautogui.click()
    pyautogui.moveRel(83, 103, duration=0.5)  # 8AM
    pyautogui.click()
    pyautogui.moveRel(12, -103, duration=0.5)  # End Button
    pyautogui.click()
    pyautogui.moveRel(154, 132, duration=0.5)  # 4PM
    pyautogui.click()
    pyautogui.moveRel(144, -32, duration=0.5)  # 4:30PM
    pyautogui.click()
    pyautogui.moveRel(-270, 12, duration=0.5)  # Add
    pyautogui.click()


# pyautogui.click(1700, 100, duration=1.5)  # tool
# pyautogui.click(1700, 370, duration=1.5)  # eRecruit
# pyautogui.click(533, 453, duration=3.0)  # Job Title


pyautogui.click(345, 517, duration=3.0)  # add time Monday
clicky()
pyautogui.click(475, 517, duration=1.5)  # add time Tuesday
clicky()
pyautogui.click(600, 517, duration=1.5)  # add time Wednesday
clicky()
pyautogui.click(750, 517, duration=1.5)  # add time Thursday
clicky()
pyautogui.click(860, 517, duration=1.5)  # add time Friday
clicky()
