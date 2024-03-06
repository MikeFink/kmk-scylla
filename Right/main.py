from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

split = Split(
    split_type=SplitType.UART,
    split_side=SplitSide.RIGHT,
    data_pin=keyboard.data_pin,
    data_pin2=keyboard.data_pin2,
    use_pio=True,
    uart_flip = True
)
keyboard.modules.append(split)

# Layer Keys
FN_LAYER = KC.TG(1)
CODE_LAYER = KC.MO(2)
AUX_LAYER = KC.TG(3)

keyboard.keymap = [
    [   #DEFAULT
        KC.ESC,    KC.N1,  KC.N2,   KC.N3,   KC.N4,  KC.N5,                                            KC.N6, KC.N7,  KC.N8,   KC.N9,   KC.N0,   KC.MINS,
        KC.TAB,    KC.Q,   KC.W,    KC.F,    KC.P,   KC.B,                                             KC.J,  KC.L,   KC.U,    KC.Y,    KC.LBRC, KC.RBRC,
        KC.LCTL,   KC.A,   KC.R,    KC.S,    KC.T,   KC.G,                                             KC.M,  KC.N,   KC.E,    KC.I,    KC.O,    KC.QUOT,
        FN_LAYER,  KC.Z,   KC.X,    KC.C,    KC.D,   KC.V,                                             KC.K,  KC.H,   KC.COMM, KC.DOT,  KC.SLSH, KC.SCLN,
                                                    KC.BSPC, KC.SPACE, KC.TO(0),   CODE_LAYER, KC.ENT, KC.DEL,
                                                             KC.LALT,  KC.LWIN,    AUX_LAYER,  KC.LSFT
    ],
    [   #FN
        KC.ESC,    KC.F1,  KC.F2,   KC.F3,   KC.F4,  KC.F5,                                            KC.F6, KC.F7,  KC.F8,   KC.F9,   KC.F10,  KC.MINS,
        KC.TAB,    KC.Q,   KC.W,    KC.F,    KC.P,   KC.B,                                             KC.J,  KC.L,   KC.U,    KC.Y,    KC.LBRC, KC.RBRC,
        KC.LCTL,   KC.A,   KC.R,    KC.S,    KC.T,   KC.G,                                             KC.M,  KC.N,   KC.E,    KC.I,    KC.O,    KC.QUOT,
        FN_LAYER,  KC.Z,   KC.X,    KC.C,    KC.D,   KC.V,                                             KC.K,  KC.H,   KC.COMM, KC.DOT,  KC.SLSH, KC.SCLN,
                                                    KC.BSPC, KC.SPACE, KC.TO(0),   CODE_LAYER, KC.ENT, KC.DEL,
                                                             KC.LALT,  KC.LWIN,    AUX_LAYER,  KC.LSFT 
    ],
    [   #CODE
        KC.ESC,    KC.N1,  KC.N2,   KC.N3,   KC.N4,  KC.N5,                                            KC.N6, KC.N7,  KC.PGUP, KC.N9,   KC.N0,   KC.EQUAL,
        KC.TAB,    KC.Q,   KC.W,    KC.F,    KC.P,   KC.B,                                             KC.J,  KC.HOME,KC.UP,   KC.END,  KC.LBRC, KC.RBRC,
        KC.LCTL,   KC.A,   KC.R,    KC.S,    KC.T,   KC.G,                                             KC.M,  KC.LEFT,KC.DOWN, KC.RIGHT,KC.O, KC.QUOT,
        FN_LAYER,  KC.Z,   KC.X,    KC.C,    KC.D,   KC.V,                                             KC.K,  KC.H,   KC.PGDN, KC.DOT,  KC.BSLS, KC.GRAVE,
                                                    KC.BSPC, KC.SPACE, KC.TO(0),   CODE_LAYER, KC.ENT, KC.DEL,
                                                             KC.LALT,  KC.LWIN,    AUX_LAYER,  KC.LSFT
    ],
    [   #AUX
        KC.ESC,    KC.F1,  KC.F2,   KC.F3,   KC.F4,  KC.F5,                                            KC.KP_SLASH, KC.KP_PLUS, KC.KP_ASTERISK, KC.KP_MINUS, KC.F10, KC.MINS,
        KC.TAB,    KC.Q,   KC.W,    KC.F,    KC.P,   KC.B,                                             KC.J,        KC.N1,   KC.N2,   KC.N3,    KC.LBRC, KC.RBRC,
        KC.LCTL,   KC.A,   KC.R,    KC.S,    KC.T,   KC.G,                                             KC.KP_DOT,   KC.N4,   KC.N5,   KC.N6,    KC.O, KC.QUOT,
        FN_LAYER,  KC.Z,   KC.X,    KC.C,    KC.D,   KC.V,                                             KC.N0,       KC.N7,   KC.N8,   KC.N9,    KC.SLSH, KC.SCLN,
                                                    KC.BSPC, KC.SPACE, KC.TO(0),   CODE_LAYER, KC.ENT, KC.DEL,
                                                             KC.LALT,  KC.LWIN,    AUX_LAYER,  KC.LSFT
    ],
]

if __name__ == '__main__':
    keyboard.go()
