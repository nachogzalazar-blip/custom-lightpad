import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys

KEY_PINS = [
    board.GP2,     # Key 1
    board.GP27,    # Key 2
    board.GP7,     # Key 3

    board.GP1,     # Key 4
    board.GP3,     # Key 5
    board.GP4,     # Key 6

    board.GP29,    # Key 7
    board.GP6,     # Key 8
    board.GP28,    # Key 9
]


keyboard = KMKKeyboard()

keyboard.matrix = KeysScanner(
    pins=KEY_PINS,
    value_when_pressed=False,
    pull=True,
)

keyboard.extensions.append(MediaKeys())

keyboard.keymap = [
    [
        KC.A,            # 1
        KC.B,            # 2
        KC.C,            # 3

        KC.LWIN(KC.D),   # 4 - Mostrar escritorio
        KC.M,            # 5
        KC.MUTE,         # 6

        KC.VOLD,         # 7 - Volumen -
        KC.VOLU,         # 8 - Volumen +
        KC.ENTER,        # 9
    ]
]

if __name__ == '__main__':
    keyboard.go()
