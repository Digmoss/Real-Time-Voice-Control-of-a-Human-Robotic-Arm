import board
import busio
from adafruit_servokit import ServoKit

class commands:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.kit = ServoKit(address=0X40, i2c=self.i2c, frequency=50, channels=16)
        self.thumb_flag = False
        self.thumb_close = 0
        self.thumb_open = 180
        self.index_flag = False
        self.index_close = 0
        self.index_open = 180
        self.middle_flag = False
        self.middle_close = 0
        self.middle_open = 180
        self.ring_flag = False
        self.ring_close = 180
        self.ring_open = 0
        self.pinky_flag = False
        self.pinky_close = 180
        self.pinky_open = 0

    def open_all(self):
        self.kit.servo[0].angle = self.thumb_open
        self.kit.servo[1].angle = self.index_open
        self.kit.servo[2].angle = self.middle_open
        self.kit.servo[3].angle = self.ring_open
        self.kit.servo[4].angle = self.pinky_open
        self.thumb_flag = True
        self.index_flag = True
        self.middle_flag = True
        self.ring_flag = True
        self.pinky_flag = True
        return "פתח"

    def close_all(self):
        self.kit.servo[0].angle = self.thumb_close
        self.kit.servo[1].angle = self.index_close
        self.kit.servo[2].angle = self.middle_close
        self.kit.servo[3].angle = self.ring_close
        self.kit.servo[4].angle = self.pinky_close
        self.thumb_flag = False
        self.index_flag = False
        self.middle_flag = False
        self.ring_flag = False
        self.pinky_flag = False
        return "אגרוף"

    def thumb(self):
        if self.thumb_flag:
            self.kit.servo[0].angle = self.thumb_close
            self.thumb_flag = False
        else:
            self.kit.servo[0].angle = self.thumb_open
            self.thumb_flag = True
        return "אגודל"

    def index(self):
        if self.index_flag:
            self.kit.servo[1].angle = self.index_close
            self.index_flag = False
        else:
            self.kit.servo[1].angle = self.index_open
            self.index_flag = True
        return "אצבע"

    def middle(self):
        if self.middle_flag:
            self.kit.servo[2].angle = self.middle_close
            self.middle_flag = False
        else:
            self.kit.servo[2].angle = self.middle_open
            self.middle_flag = True
        return "אמה"

    def ring(self):
        if self.ring_flag:
            self.kit.servo[3].angle = self.ring_close
            self.ring_flag = False
        else:
            self.kit.servo[3].angle = self.ring_open
            self.ring_flag = True
        return "קמיצה"

    def pinky(self):
        if self.pinky_flag:
            self.kit.servo[4].angle = self.pinky_close
            self.pinky_flag = False
        else:
            self.kit.servo[4].angle = self.pinky_open
            self.pinky_flag = True
        return "זרת"
