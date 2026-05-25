from machine import Pin, PWM
import time

# PWM設定
red = PWM(Pin(10))
green = PWM(Pin(11))
blue = PWM(Pin(12))

# PWM周波数
red.freq(1000)
green.freq(1000)
blue.freq(1000)

# 色設定
def set_color(r, g, b):
    red.duty_u16(r)
    green.duty_u16(g)
    blue.duty_u16(b)

# なめらかに色変更
def fade(r1, g1, b1, r2, g2, b2, duration=1.0):
    steps = 100

    for i in range(steps + 1):
        t = i / steps

        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)

        set_color(r, g, b)

        time.sleep(duration / steps)

# 色定義
RED     = (65535, 0, 0)
GREEN   = (0, 65535, 0)
BLUE    = (0, 0, 65535)
YELLOW  = (65535, 65535, 0)
CYAN    = (0, 65535, 65535)
MAGENTA = (65535, 0, 65535)
WHITE   = (65535, 65535, 65535)
OFF     = (0, 0, 0)

colors = [
    RED,
    GREEN,
    BLUE,
    YELLOW,
    CYAN,
    MAGENTA,
    WHITE,
    OFF
]

while True:
    for i in range(len(colors)):
        c1 = colors[i]
        c2 = colors[(i + 1) % len(colors)]

        fade(
            c1[0], c1[1], c1[2],
            c2[0], c2[1], c2[2],
            1.0   # 1秒かけて変化
        )
