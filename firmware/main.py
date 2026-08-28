import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

rgb = RGB(pixel_pin=board.D10, num_pixels=1, val_limit=100, hue_default=0, sat_default=255, val_default=100)
keyboard.extensions.append(rgb)

PINS = [
    board.D0,
    board.D1,
    board.D2,
    board.D3,
    board.D4,
    board.D5,
    board.D6,
    board.D7,
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.A, 
        KC.B, 
        KC.C,
        KC.LWIN(KC.D),
        KC.MACRO("Hello!"),
        KC.MUTE,
        KC.VOLU,
        KC.VOLD,
    ]
]

if __name__ == '__main__':
    keyboard.go()
