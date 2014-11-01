#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Set of tools to deals with colors in python
"""
import hashlib


class Color(object):
    """ Object to create, convert and manipulate color in python
        >>> c = Color(string=b'network')
        >>> c.get_rgb()
        (210, 12, 100)
        >>> c.get_hex()
        '#d20c64'
    """
    def __init__(self, rgb=(0, 0, 0), hex_rgb="#000000", string=None):
        """ Color object constuctor
            :param: rgb: The RGB int tuple of this color
            :type rgb: :py:class `tuple`
            :param: hex_rgb: The hexadecimale rgb of this color
            :type hex_rgb: :py:class `str`
            :param: string: A string to convert into a color
            :type string: :py:class `str`
        """
        if not hex_rgb == "#000000":
            self._hex_rgb = hex_rgb
            self._rgb = self.convert_hex_to_rgb()
        elif string:
            self.set_hex_from_string(string)
        else:
            self._rgb = rgb
            self._hex = self.convert_rgb_to_hex()

    def __repr__(self):
        return "<Color r:%s, g:%s, b:%s>" % self.get_rgb()

    def get_hex(self):
        """ Get the hexadecimal representation of the color. """
        return self._hex_rgb

    def get_rgb(self):
        """ Get the rgb representation of the color. """
        return self._rgb

    def set_hex_from_rgb(self):
        """ set the HEX color value """
        self._hex_rgb = self.convert_rgb_to_hex()

    def set_rgb_from_hex(self):
        """ set the RGB from the HEX value """
        self._rgb = self.convert_hex_to_rgb()

    def convert_rgb_to_hex(self):
        """ Convert RGB color to HEX color """
        # unpack rgb
        (red, green, blue) = self.get_rgb()
        # Then we get the hex value, keep only the interesting part
        # since hex(int) return 0x??.
        # At the end, fill result with 0 to get a two characters string
        hexred = hex(int(red))[2:].zfill(2)
        # do this for the rest of color parts
        hexgreen = hex(int(green))[2:].zfill(2)
        hexblue = hex(int(blue))[2:].zfill(2)
        # return the concatenation or hex_{r,g,b}, prefixed by `#`
        return "#%s" % "".join((hexred, hexgreen, hexblue))

    def convert_hex_to_rgb(self):
        """ Convert HEX color to RGB color """
        # split hex
        _ = self.get_hex()[1:]
        return (int(_[:2], 16),
                int(_[2:4], 16),
                int(_[4:], 16))

    def set_rgb_from_string(self, string):
        """ Set the rgb color representation of
            a given string.
            :param: string: The string to colorize_string
            :type string: :py:class `bytes`
        """
        # get the md5 hexdigest of the string
        # its length is always 32
        hash_str = hashlib.md5(string).hexdigest()
        # take 3 slices of 8 bytes in this hash to create
        # red, green and blue values
        red, green, blue = (hash_str[8*i:8*(i+1)] for i in range(0, 3))
        # compute the int representation for red, green and blue
        # We first get the int value of color part with int(red, 16)
        # The color part (red,green or blue) is ranged between 0 and 256
        int_r = int(red, 16) % 256
        # do this for the rest of color parts
        int_g = int(green, 16) % 256
        int_b = int(blue, 16) % 256
        # return the r, g, b tuple
        self._rgb = (int_r, int_g, int_b)

    def set_hex_from_string(self, string):
        """ Set the HEX color representation of
            a given string.
            :param: string: The string to colorize_string
            :type string: :py:class `bytes`
        """
        # convert string to RGB then RGB to HEX and HEX TO HSL
        self.set_rgb_from_string(string)
        self.set_hex_from_rgb()
