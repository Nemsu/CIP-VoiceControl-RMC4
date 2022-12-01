import speech_recognition as sr
from TVControl import CIPControl, TVFB

Processor = "172.16.13.120"

r = sr.Recognizer()
m = sr.Microphone()

cmd_on = "bật"
cmd_off = "Tắt"
botname = "ơi"

try:
    print("Vui lòng giữ yên lặng...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Cài đặt âm thanh thành công {}".format(r.energy_threshold))
    while True:
        print("Đang nghe")
        with m as source: audio = r.listen(source)
        print("Đã nghe, đang thực hiện...")
        try:
            value = r.recognize_google(audio, language="vi-VI")
            print("Bạn nói: {}".format(value))
            if botname in value:
                TVFB("Ơi mình đây")
            if cmd_on in value:
                TVFB("Đang bật TV")
                CIPControl(Processor, 0x03, 1)
            elif cmd_off in value:
                TVFB("Đang tắt TV")
                CIPControl(Processor, 0x03, 2)
        except sr.UnknownValueError:
            TVFB("Vui lòng nói chậm lại")
        except sr.RequestError as e:
            print("Lỗi Google Speech Recognition; {0}".format(e))
except KeyboardInterrupt:
    pass