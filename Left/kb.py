import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.D7,
        board.D6,
        board.D2,
        board.D5,
        board.D3,
        board.D4
    )
    row_pins = (
        board.A3,
        board.A2,
        board.A1,
        board.A0,
        board.CLK
    )
    diode_orientation = DiodeOrientation.COLUMNS
    data_pin = board.D0
    data_pin2 = board.D1

    coord_mapping = [
        0,  1,  2,  3,  4,  5,                      30, 31, 32, 33, 34, 35, 
        6,  7,  8,  9,  10, 11,                     36, 37, 38, 39, 40, 41,
        12, 13, 14, 15, 16, 17,                     42, 43, 44, 45, 46, 47,
        18, 19, 20, 21, 22, 23,                     48, 49, 50, 51, 52, 53,
                            24, 25, 26,     54, 55, 56,
                                27, 28,     57, 58
    ]
