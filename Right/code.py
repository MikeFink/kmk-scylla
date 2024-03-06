import board


from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.layers import Layers



keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

split = Split(split_type=SplitType.UART, split_side=SplitSide.RIGHT, data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip = True)
keyboard.modules.append(split)

keyboard.col_pins = (board.D2, board.D3, board.D4, board.D5, board.D6, board.D7)
keyboard.row_pins = (board.A3, board.A2, board.A1, board.A0, board.CLK)
keyboard.diode_orientation = DiodeOrientation.COL2ROW



# Layer Keys

keyboard.keymap = [
    [
        KC.N6,   KC.N7,    KC.N8, KC.N9, KC.N0, KC.MINS,
        KC.Y,    KC.U,     KC.I,  KC.O,  KC.P,  KC.QUOT,
        KC.H,    KC.J,     KC.K,  KC.L,  KC.LBRC,  KC.RBRC,
        KC.N,    KC.M,     KC.COMMA,  KC.DOT,  KC.SLASH,  KC.SCLN,
        KC.DOWN, KC.SPACE, KC.NO, KC.NO, KC.NO,
    ],
]


if __name__ == '__main__':
    keyboard.go()