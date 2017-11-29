# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def convert_to_roman(value):
    old_value = value
    mapping = (
        (1000, 'M'),
        (900, 'DM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'LC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    )
    output = ''
    for dec, rom in mapping:
        count = value / dec
        output += count * rom
        value -= count * dec
    print old_value, "->", output
    return output

#
# Tests
#
assert convert_to_roman(1) == 'I'
assert convert_to_roman(2) == 'II'
assert convert_to_roman(4) == 'IV'
assert convert_to_roman(5) == 'V'
assert convert_to_roman(6) == 'VI'
assert convert_to_roman(8) == 'VIII'
assert convert_to_roman(9) == 'IX'
assert convert_to_roman(10) == 'X'
assert convert_to_roman(12) == 'XII'
assert convert_to_roman(14) == 'XIV'
assert convert_to_roman(15) == 'XV'
assert convert_to_roman(20) == 'XX'
assert convert_to_roman(40) == 'XL'
assert convert_to_roman(44) == 'XLIV'
assert convert_to_roman(123) == 'CXXIII'
assert convert_to_roman(449) == 'CDXLIX'
assert convert_to_roman(564) == 'DLXIV'
assert convert_to_roman(9767) == 'MMMMMMMMMDCCLXVII'
