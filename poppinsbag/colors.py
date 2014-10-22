#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Set of tools to deals with colors in python
"""
import hashlib


class Color(object):
    """ Object to create, convert and manipulate color in python
        >>> c = Color()
        >>> c.set_rgb_from_string(b'network')
        >>> c.get_rgb()
        (210, 12, 100)
        >>> c = Color()
        >>> c.set_hex_from_string(b'network')
        >>> c.get_rgb()
        (210, 12, 100)
        >>> c.get_hex()
        '#d20c64'
    """

    def __init__(self, rgb=(0, 0, 0), hex_rgb="#000000"):
        """ Color object constuctor
            :param: rgb: The RGB int tuple of this color
            :type rgb: :py:class `tuple`
            :param: hex_rgb: The hexadecimale rgb of this color
            :type hex_rgb: :py:class `str`
        """
        self._rgb = rgb
        self._hex_rgb = hex_rgb

    def __repr__(self):
        return "<Color r:%s, g:%s, b:%s>" % self.get_rgb()

    def get_hex(self):
        """ Get the hexadecimal representation of the color. """
        return self._hex_rgb

    def get_rgb(self):
        """ Get the rgb representation of the color. """
        return self._rgb

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
        """ Set the hex color representation of
            a given string.
            :param: string: The string to colorize_string
            :type string: :py:class `bytes`
       """
        # Set the RGB of the object
        self.set_rgb_from_string(string)
        # unpack rgb
        (int_r, int_g, int_b) = self.get_rgb()
        # Then we get the hex value, keep only the interesting part
        # since hex(int) return 0x??.
        # At the end, fill result with 0 to get a two characters string
        hex_r = hex(int_r)[2:].zfill(2)
        # do this for the rest of color parts
        hex_g = hex(int_g)[2:].zfill(2)
        hex_b = hex(int_b)[2:].zfill(2)
        # return the concatenation or hex_{r,g,b}, prefixed by `#`
        self._hex_rgb = "#%s" % "".join((hex_r, hex_g, hex_b))
