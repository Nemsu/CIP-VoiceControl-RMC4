import logging
import time
import cipclient
from gtts import gTTS
import playsound

def CIPControl(ControllerIP, XpanelIP, pressnum):
    cip = cipclient.CIPSocketClient(ControllerIP, XpanelIP)
    cip.start()
    cip.update_request()
    cip.press(pressnum)
    time.sleep(1.5)
    cip.stop()
    
def TVFB(text):
    print(text)
    output = gTTS(text,lang="vi", slow=False)
    output.save("output.mp3")
    playsound.playsound('output.mp3', True)