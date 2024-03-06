import board


from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

split = Split(data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip = True)
keyboard.modules.append(split)

keyboard.col_pins = (board.D7, board.D6, board.D2, board.D5, board.D3, board.D4)
keyboard.row_pins = (board.A3, board.A2, board.A1, board.A0, board.CLK)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Layer Keys
MOD_LAYER = KC.TG(1)

keyboard.keymap = [
    [
        KC.ESCAPE, KC.N1,    KC.N2, KC.N3, KC.N4, KC.N5,
        KC.TAB,    KC.Q,     KC.W,  KC.E,  KC.R,  KC.T,
        KC.LCTRL,  KC.A,     KC.S,  KC.D,  KC.F,  KC.G,
        KC.LSHIFT, KC.Z,     KC.X,  KC.C,  KC.V,  KC.B,
        KC.LALT,   KC.SPACE, KC.UP, MOD_LAYER, KC.LWIN,
    ],
    [
        KC.ESCAPE, KC.F1,    KC.F2, KC.F3, KC.F4, KC.F5,
        KC.TAB,    KC.Q,     KC.W,  KC.E,  KC.R,  KC.T,
        KC.LALT,   KC.A,     KC.S,  KC.D,  KC.F,  KC.G,
        KC.LSHIFT, KC.Z,     KC.X,  KC.C,  KC.V,  KC.B,
        KC.SPACE,  KC.LCTRL, KC.UP, MOD_LAYER, KC.LWIN,
    ]
]


if __name__ == '__main__':
    keyboard.go()