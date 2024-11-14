import pyautogui as pa
import subprocess as sb
import time
import webbrowser as wb


main_id = '225 787 8086'
urdu_id = '371 391 0283'
passw = '98765'

# sb.call(['C:\\Users\\Ali\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'])
wb.open('C:\\Users\\Ali\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')

time.sleep(4)


joinbtnm = pa.locateCenterOnScreen('joinbtnmt.png')

pa.moveTo(joinbtnm)
pa.click()

time.sleep(2)

idfield = pa.locateCenterOnScreen('idfield.png', confidence=0.5)

pa.moveTo(idfield)
pa.click()
pa.write(main_id)
pa.press('tab')
pa.press('tab')
pa.hotkey('ctrl','a')
pa.press('backspace')
pa.write('Abdullah 353 9B')


joinbtn = pa.locateCenterOnScreen('joinbtn.png')

pa.moveTo(joinbtn)
pa.click()



time.sleep(3)


pa.write(passw)
pa.press('enter')

