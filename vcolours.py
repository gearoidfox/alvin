# -*- coding: utf-8 -*-
#
# Copyright 2017 Gearóid Fox
#
# This file is part of Alvin.
#
# Alvin is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Alvin is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Alvin.  If not, see <http://www.gnu.org/licenses/>.

""" Functions to initialise colour palettes for curses display """


import curses


# Map one letter amino acid codes to integers. Each character gets its
# own fg/bg color_pair so we can make arbitrary colour schemes.
aa_dict = {
        'G' : 21,
        'A' : 22,
        'L' : 23,
        'M' : 24,
        'F' : 25,
        'W' : 26,
        'K' : 27,
        'Q' : 28,
        'E' : 29,
        'S' : 30,
        'P' : 31,
        'V' : 32,
        'I' : 33,
        'C' : 34,
        'Y' : 35,
        'H' : 36,
        'R' : 37,
        'N' : 38,
        'D' : 39,
        'T' : 40,
        'g' : 41,
        'a' : 42,
        'l' : 43,
        'm' : 44,
        'f' : 45,
        'w' : 46,
        'k' : 47,
        'q' : 48,
        'e' : 49,
        's' : 50,
        'p' : 51,
        'v' : 52,
        'i' : 53,
        'c' : 54,
        'y' : 55,
        'h' : 56,
        'r' : 57,
        'n' : 58,
        'd' : 59,
        't' : 60,
        'u' : 61,
        'U' : 62
        }



def init_rgb255(colour, r, g, b):
    """
    Wrapper around curses.init_color taking values in range 0-255 instead
    of 0-999
    
    Args:
        colour (int): number of colour to assign
        r (int): red componenta (0-255)
        g (int): green componenta (0-255)
        b (int): blue component (0-255)

    """
    if r < 0 or r > 255:
        raise ValueError
    elif g < 0 or g > 255:
        raise ValueError
    elif b < 0 or b > 255:
        raise ValueError
    adj = 999 / 255. 
    curses.init_color(colour, int(r*adj), int(g*adj), int(b*adj))



def init_alignment_colours_white():
    """
    Initialise colour scheme: black and white
    """
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(11, curses.COLOR_WHITE, curses.COLOR_BLACK)
    for key in aa_dict.keys():
        curses.init_pair(aa_dict[key], curses.COLOR_WHITE, curses.COLOR_BLACK) 



def init_colours_nt_xterm_dark():
    """ 
    Initialise nucleotide colour scheme for xterm colour terminals without
    colour-changing capabilities.

    Coloured text on a black background.
    """
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(11, curses.COLOR_WHITE, curses.COLOR_BLACK)
    for key in aa_dict.keys():
        curses.init_pair(aa_dict[key], curses.COLOR_WHITE, curses.COLOR_BLACK) 
    for key in ['a', 'A']:
        curses.init_pair(aa_dict[key], curses.COLOR_GREEN, curses.COLOR_BLACK) 
    for key in ['c', 'C']:
        curses.init_pair(aa_dict[key], curses.COLOR_YELLOW, curses.COLOR_BLACK) 
    for key in ['t', 'T', 'u', 'U']:
        curses.init_pair(aa_dict[key], curses.COLOR_BLUE, curses.COLOR_BLACK) 
    for key in ['g', 'G']:
        curses.init_pair(aa_dict[key], curses.COLOR_RED, curses.COLOR_BLACK) 



def init_colours_nt_xterm_dark_reverse():
    """ 
    Initialise nucleotide colour scheme for xterm colour terminals without
    colour-changing capabilities.

    Black text with coloured backgrounds.
    """
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(11, curses.COLOR_WHITE, curses.COLOR_BLACK)
    for key in aa_dict.keys():
        curses.init_pair(aa_dict[key], curses.COLOR_WHITE, curses.COLOR_BLACK) 
    for key in ['a', 'A']:
        curses.init_pair(aa_dict[key], curses.COLOR_BLACK, curses.COLOR_GREEN) 
    for key in ['c', 'C']:
        curses.init_pair(aa_dict[key], curses.COLOR_BLACK, curses.COLOR_YELLOW) 
    for key in ['t', 'T', 'u', 'U']:
        curses.init_pair(aa_dict[key], curses.COLOR_BLACK, curses.COLOR_BLUE) 
    for key in ['g', 'G']:
        curses.init_pair(aa_dict[key], curses.COLOR_BLACK, curses.COLOR_RED) 



def init_colours_nt_xterm_light():
    """ 
    Initialise nucleotide colour scheme for xterm colour terminals without
    colour-changing capabilities.

    Coloured text on a light background.
    """
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(11, curses.COLOR_BLACK, curses.COLOR_WHITE)
    for key in aa_dict.keys():
        curses.init_pair(aa_dict[key], curses.COLOR_BLACK, curses.COLOR_WHITE) 
    for key in ['a', 'A']:
        curses.init_pair(aa_dict[key], curses.COLOR_GREEN, curses.COLOR_WHITE) 
    for key in ['c', 'C']:
        curses.init_pair(aa_dict[key], curses.COLOR_YELLOW, curses.COLOR_WHITE) 
    for key in ['t', 'T', 'u', 'U']:
        curses.init_pair(aa_dict[key], curses.COLOR_BLUE, curses.COLOR_WHITE) 
    for key in ['g', 'G']:
        curses.init_pair(aa_dict[key], curses.COLOR_RED, curses.COLOR_WHITE) 



def init_colours_nt_xterm_light_reverse():
    """ 
    Initialise nucleotide colour scheme for xterm colour terminals without
    colour-changing capabilities.

    White text on a coloured background.
    """
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(11, curses.COLOR_BLACK, curses.COLOR_WHITE)
    for key in aa_dict.keys():
        curses.init_pair(aa_dict[key], curses.COLOR_BLACK, curses.COLOR_WHITE) 
    for key in ['a', 'A']:
        curses.init_pair(aa_dict[key], curses.COLOR_WHITE, curses.COLOR_GREEN) 
    for key in ['c', 'C']:
        curses.init_pair(aa_dict[key], curses.COLOR_WHITE, curses.COLOR_YELLOW) 
    for key in ['t', 'T', 'u', 'U']:
        curses.init_pair(aa_dict[key], curses.COLOR_WHITE, curses.COLOR_BLUE) 
    for key in ['g', 'G']:
        curses.init_pair(aa_dict[key], curses.COLOR_WHITE, curses.COLOR_RED) 



def init_colours_aa_xterm_dark():
    """ 
    Initialise amino acid colour scheme for xterm colour terminals without
    colour-changing capabilities.

    Coloured text on a black background.
    """
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(11, curses.COLOR_WHITE, curses.COLOR_BLACK)
    for key in ['a', 'A', 'i', 'I', 'l', 'L', 'm', 'M', 'f', 'F', 'w', 'W', 'v', 'V', 'c', 'C']:
        curses.init_pair(aa_dict[key], curses.COLOR_BLUE, curses.COLOR_BLACK) 
    for key in ['k', 'K', 'r', 'R']:
        curses.init_pair(aa_dict[key], curses.COLOR_RED, curses.COLOR_BLACK) 
    for key in ['e', 'E', 'd', 'D']:
        curses.init_pair(aa_dict[key], curses.COLOR_MAGENTA, curses.COLOR_BLACK) 
    for key in ['n', 'N', 'q', 'Q', 's', 'S', 't', 'T']:
        curses.init_pair(aa_dict[key], curses.COLOR_GREEN, curses.COLOR_BLACK) 
    for key in ['h', 'H', 'y', 'Y']:
        curses.init_pair(aa_dict[key], curses.COLOR_CYAN, curses.COLOR_BLACK) 
    for key in ['p', 'P']:
        curses.init_pair(aa_dict[key], curses.COLOR_YELLOW, curses.COLOR_BLACK) 
    for key in ['g', 'G']:
        curses.init_pair(aa_dict[key], curses.COLOR_WHITE, curses.COLOR_BLACK) 



def init_colours_aa_xterm_dark_reverse():
    """ 
    Initialise amino acid colour scheme for xterm colour terminals without
    colour-changing capabilities.

    Black text on a coloured background.
    """
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(11, curses.COLOR_WHITE, curses.COLOR_BLACK)
    for key in ['a', 'A', 'i', 'I', 'l', 'L', 'm', 'M', 'f', 'F', 'w', 'W', 'v', 'V', 'c', 'C']:
        curses.init_pair(aa_dict[key], curses.COLOR_BLACK, curses.COLOR_BLUE) 
    for key in ['k', 'K', 'r', 'R']:
        curses.init_pair(aa_dict[key], curses.COLOR_BLACK, curses.COLOR_RED) 
    for key in ['e', 'E', 'd', 'D']:
        curses.init_pair(aa_dict[key], curses.COLOR_BLACK, curses.COLOR_MAGENTA) 
    for key in ['n', 'N', 'q', 'Q', 's', 'S', 't', 'T']:
        curses.init_pair(aa_dict[key], curses.COLOR_BLACK, curses.COLOR_GREEN) 
    for key in ['h', 'H', 'y', 'Y']:
        curses.init_pair(aa_dict[key], curses.COLOR_BLACK, curses.COLOR_CYAN) 
    for key in ['p', 'P']:
        curses.init_pair(aa_dict[key], curses.COLOR_BLACK, curses.COLOR_YELLOW) 
    for key in ['g', 'G']:
        curses.init_pair(aa_dict[key], curses.COLOR_BLACK, curses.COLOR_WHITE) 



def init_colours_aa_xterm_light():
    """ 
    Initialise amino acid colour scheme for xterm colour terminals without
    colour-changing capabilities.

    Coloured text on a white background.
    """
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(11, curses.COLOR_BLACK, curses.COLOR_WHITE)
    for key in ['a', 'A', 'i', 'I', 'l', 'L', 'm', 'M', 'f', 'F', 'w', 'W', 'v', 'V', 'c', 'C']:
        curses.init_pair(aa_dict[key], curses.COLOR_BLUE, curses.COLOR_WHITE) 
    for key in ['k', 'K', 'r', 'R']:
        curses.init_pair(aa_dict[key], curses.COLOR_RED, curses.COLOR_WHITE) 
    for key in ['e', 'E', 'd', 'D']:
        curses.init_pair(aa_dict[key], curses.COLOR_MAGENTA, curses.COLOR_WHITE) 
    for key in ['n', 'N', 'q', 'Q', 's', 'S', 't', 'T']:
        curses.init_pair(aa_dict[key], curses.COLOR_GREEN, curses.COLOR_WHITE) 
    for key in ['h', 'H', 'y', 'Y']:
        curses.init_pair(aa_dict[key], curses.COLOR_CYAN, curses.COLOR_WHITE) 
    for key in ['p', 'P']:
        curses.init_pair(aa_dict[key], curses.COLOR_YELLOW, curses.COLOR_WHITE) 
    for key in ['g', 'G']:
        curses.init_pair(aa_dict[key], curses.COLOR_BLACK, curses.COLOR_WHITE) 



def init_colours_aa_xterm_light_reverse():
    """ 
    Initialise amino acid colour scheme for xterm colour terminals without
    colour-changing capabilities.

    White text on a coloured background.
    """
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(11, curses.COLOR_BLACK, curses.COLOR_WHITE)
    for key in ['a', 'A', 'i', 'I', 'l', 'L', 'm', 'M', 'f', 'F', 'w', 'W', 'v', 'V', 'c', 'C']:
        curses.init_pair(aa_dict[key], curses.COLOR_WHITE, curses.COLOR_BLUE) 
    for key in ['k', 'K', 'r', 'R']:
        curses.init_pair(aa_dict[key], curses.COLOR_WHITE, curses.COLOR_RED) 
    for key in ['e', 'E', 'd', 'D']:
        curses.init_pair(aa_dict[key], curses.COLOR_WHITE, curses.COLOR_MAGENTA) 
    for key in ['n', 'N', 'q', 'Q', 's', 'S', 't', 'T']:
        curses.init_pair(aa_dict[key], curses.COLOR_WHITE, curses.COLOR_GREEN) 
    for key in ['h', 'H', 'y', 'Y']:
        curses.init_pair(aa_dict[key], curses.COLOR_WHITE, curses.COLOR_CYAN) 
    for key in ['p', 'P']:
        curses.init_pair(aa_dict[key], curses.COLOR_WHITE, curses.COLOR_YELLOW) 
    for key in ['g', 'G']:
        curses.init_pair(aa_dict[key], curses.COLOR_WHITE, curses.COLOR_BLACK) 



def init_colours_nt_256_dark():
    """ 
    Initialise nucleotide colour scheme for 256 colour terminals with
    colour-changing capabilities.

    Coloured text on a black background.
    """
    if not curses.can_change_color():
        return
    # nucleotide colours:
    brightred = 51
    orange = 54
    midblue = 55
    green = 58

    lightgrey = 57
    darkgrey = 59
    # ui colours:
    orange1 = 63
    bg = 64
    
    init_rgb255(curses.COLOR_BLACK, 0, 0, 0)
    init_rgb255(curses.COLOR_WHITE, 255, 255, 255)
    init_rgb255(bg, 0, 0, 0)
    init_rgb255(brightred, 230, 10, 10) 
    init_rgb255(orange, 250, 150, 0)
    init_rgb255(midblue, 90, 90, 210)
    init_rgb255(lightgrey, 235, 235, 235)
    init_rgb255(green, 30, 165, 30)
    init_rgb255(orange1, 218, 59, 1)
    
    curses.init_pair(1, curses.COLOR_WHITE, bg)
    curses.init_pair(2, curses.COLOR_WHITE, orange1)
    curses.init_pair(3, orange1, bg)
    curses.init_pair(4, curses.COLOR_BLACK, lightgrey)    
    curses.init_pair(11, darkgrey, bg)
    
    for key in aa_dict.keys():
        curses.init_pair(aa_dict[key], lightgrey, bg) 

    for key in ['a', 'A']:
        curses.init_pair(aa_dict[key], green, bg) 
    for key in ['c', 'C']:
        curses.init_pair(aa_dict[key], orange, bg) 
    for key in ['t', 'T', 'u', 'U']:
        curses.init_pair(aa_dict[key], midblue, bg) 
    for key in ['g', 'G']:
        curses.init_pair(aa_dict[key], brightred, bg) 



def init_colours_nt_256_dark_reverse():
    """ 
    Initialise nucleotide colour scheme for 256 colour terminals with
    colour-changing capabilities.

    Dark text on a coloured background.
    """
    if not curses.can_change_color():
        return
    # nucleotide colours:
    brightred = 51
    orange = 54
    midblue = 55
    green = 58

    lightgrey = 57
    darkgrey = 59
    # ui colours:
    orange1 = 63
    bg = 64
    
    init_rgb255(curses.COLOR_BLACK, 0, 0, 0)
    init_rgb255(curses.COLOR_WHITE, 255, 255, 255)
    init_rgb255(bg, 0, 0, 0)
    init_rgb255(brightred, 230, 10, 10) 
    init_rgb255(orange, 250, 150, 0)
    init_rgb255(midblue, 90, 90, 210)
    init_rgb255(lightgrey, 235, 235, 235)
    init_rgb255(green, 30, 165, 30)
    init_rgb255(orange1, 218, 59, 1)
    
    curses.init_pair(1, curses.COLOR_WHITE, bg)
    curses.init_pair(2, curses.COLOR_WHITE, darkgrey)
    curses.init_pair(3, curses.COLOR_WHITE, bg)
    curses.init_pair(4, curses.COLOR_WHITE, darkgrey)    
    curses.init_pair(11, curses.COLOR_WHITE, bg)
    
    for key in aa_dict.keys():
        curses.init_pair(aa_dict[key], lightgrey, bg) 

    for key in ['a', 'A']:
        curses.init_pair(aa_dict[key], bg, green) 
    for key in ['c', 'C']:
        curses.init_pair(aa_dict[key], bg, orange) 
    for key in ['t', 'T', 'u', 'U']:
        curses.init_pair(aa_dict[key], bg, midblue) 
    for key in ['g', 'G']:
        curses.init_pair(aa_dict[key], bg, brightred) 



def init_colours_nt_256_light():
    """ 
    Initialise nucleotide colour scheme for 256 colour terminals with
    colour-changing capabilities.

    Coloured text on a white background.
    """
    if not curses.can_change_color():
        return
    # nucleotide colours:
    brightred = 51
    yellow = 52
    blue = 53
    orange = 54
    midblue = 55
    cyan = 56
    lightgrey = 57
    green = 58
    darkgrey = 59
    pink = 60
    paleblue = 61
    flesh = 62
    # ui colours:
    orange1 = 63
    bg = 64
    
    init_rgb255(curses.COLOR_BLACK, 0, 0, 0)
    init_rgb255(curses.COLOR_WHITE, 255, 255, 255)
    init_rgb255(bg, 255, 255, 255)
    init_rgb255(brightred, 200, 0, 0) 
    init_rgb255(yellow, 210, 210, 0) 
    init_rgb255(blue, 10, 80, 245) 
    init_rgb255(orange, 180, 110, 0)
    init_rgb255(midblue, 10, 10, 160)
    init_rgb255(cyan, 0, 210, 210)
    init_rgb255(lightgrey, 195, 195, 195)
    init_rgb255(green, 0, 140, 0)
    init_rgb255(orange1, 208, 49, 1)

    curses.init_pair(1, curses.COLOR_BLACK, bg)
    # colour pair 2 for status bar
    curses.init_pair(2, curses.COLOR_WHITE, orange1)
    # colour pair 3 for gap % track
    curses.init_pair(3, orange1, bg)
    # colour pair 4 for sequence id labels
    curses.init_pair(4, curses.COLOR_WHITE, midblue)    
    # colour pair 11 for gaps and misc characters
    curses.init_pair(11, lightgrey, bg)
    
    for key in aa_dict.keys():
        curses.init_pair(aa_dict[key], lightgrey, bg) 

    for key in ['a', 'A']:
        curses.init_pair(aa_dict[key], green, bg) 
    for key in ['c', 'C']:
        curses.init_pair(aa_dict[key], orange, bg) 
    for key in ['t', 'T', 'u', 'U']:
        curses.init_pair(aa_dict[key], midblue, bg) 
    for key in ['g', 'G']:
        curses.init_pair(aa_dict[key], brightred, bg) 



def init_colours_nt_256_light_reverse():
    """ 
    Initialise nucleotide colour scheme for 256 colour terminals with
    colour-changing capabilities.

    White text on a coloured background.
    """
    if not curses.can_change_color():
        return
    # nucleotide colours:
    brightred = 51
    yellow = 52
    blue = 53
    orange = 54
    midblue = 55
    cyan = 56
    lightgrey = 57
    green = 58
    darkgrey = 59
    pink = 60
    paleblue = 61
    flesh = 62
    # ui colours:
    orange1 = 63
    bg = 64
    
    init_rgb255(curses.COLOR_BLACK, 0, 0, 0)
    init_rgb255(curses.COLOR_WHITE, 255, 255, 255)
    init_rgb255(bg, 255, 255, 255)
    init_rgb255(brightred, 200, 0, 0) 
    init_rgb255(yellow, 210, 210, 0) 
    init_rgb255(blue, 10, 80, 245) 
    init_rgb255(orange, 180, 110, 0)
    init_rgb255(midblue, 10, 10, 160)
    init_rgb255(cyan, 0, 210, 210)
    init_rgb255(lightgrey, 195, 195, 195)
    init_rgb255(green, 0, 140, 0)
    init_rgb255(orange1, 208, 49, 1)

    curses.init_pair(1, curses.COLOR_BLACK, bg)
    # colour pair 2 for status bar
    curses.init_pair(2, curses.COLOR_WHITE, orange1)
    # colour pair 3 for gap % track
    curses.init_pair(3, orange1, bg)
    # colour pair 4 for sequence id labels
    curses.init_pair(4, curses.COLOR_WHITE, darkgrey)    
    # colour pair 11 for gaps and misc characters
    curses.init_pair(11, lightgrey, bg)
    
    for key in aa_dict.keys():
        curses.init_pair(aa_dict[key], lightgrey, bg) 

    for key in ['a', 'A']:
        curses.init_pair(aa_dict[key], bg, green) 
    for key in ['c', 'C']:
        curses.init_pair(aa_dict[key], bg, orange) 
    for key in ['t', 'T', 'u', 'U']:
        curses.init_pair(aa_dict[key], bg, midblue) 
    for key in ['g', 'G']:
        curses.init_pair(aa_dict[key], bg, brightred) 



def init_colours_aa_256_dark():
    """
    Initialise amino acid colour scheme for 256 colour terminals with
    colour-changing capabilities.

    Coloured text on a black background.

    Colours modified from the RasMol amino acid colour scheme
    (http://life.nthu.edu.tw/~fmhsu/rasframe/COLORS.HTM)
    """
    if not curses.can_change_color():
        return
    # amino acid colours:
    brightred = 51
    yellow = 52
    blue = 53
    orange = 54
    midblue = 55
    cyan = 56
    lightgrey = 57
    green = 58
    darkgrey = 59
    pink = 60
    paleblue = 61
    flesh = 62
    # ui colours:
    orange1 = 63
    bg = 64
    
    init_rgb255(curses.COLOR_BLACK, 0, 0, 0)
    init_rgb255(curses.COLOR_WHITE, 255, 255, 255)
    init_rgb255(bg, 0, 0, 0)
    init_rgb255(brightred, 230, 10, 10) 
    init_rgb255(yellow, 230, 230, 0) 
    init_rgb255(blue, 20, 90, 255) 
    init_rgb255(orange, 250, 150, 0)
    init_rgb255(midblue, 75, 75, 200)
    init_rgb255(cyan, 0, 220, 220)
    init_rgb255(lightgrey, 235, 235, 235)
    init_rgb255(darkgrey, 135, 135, 135)
    init_rgb255(green, 35, 180, 35)
    init_rgb255(orange1, 218, 59, 1)
    init_rgb255(flesh, 220, 150, 130)
    init_rgb255(pink, 180, 90, 180)

    curses.init_pair(1, curses.COLOR_WHITE, bg)
    curses.init_pair(2, curses.COLOR_WHITE, orange1)
    curses.init_pair(3, orange1, bg)
    curses.init_pair(4, curses.COLOR_BLACK, lightgrey)    
    curses.init_pair(11, darkgrey, bg)

    for key in ['D', 'E']:
        curses.init_pair(aa_dict[key], brightred, bg) 
    for key in ['C', 'M']:
        curses.init_pair(aa_dict[key], yellow, bg) 
    for key in ['K', 'R']:
        curses.init_pair(aa_dict[key], blue, bg) 
    for key in ['S', 'T']:
        curses.init_pair(aa_dict[key], orange, bg) 
    for key in ['F', 'Y']:
        curses.init_pair(aa_dict[key], midblue, bg) 
    for key in ['Q', 'N']:
        curses.init_pair(aa_dict[key], cyan, bg) 
    for key in ['G']:
        curses.init_pair(aa_dict[key], lightgrey, bg) 
    for key in ['L', 'V', 'I']:
        curses.init_pair(aa_dict[key], green, bg) 
    for key in ['A']:
        curses.init_pair(aa_dict[key], darkgrey, bg) 
    for key in ['W']:
        curses.init_pair(aa_dict[key], pink, bg) 
    for key in ['H']:
        curses.init_pair(aa_dict[key], paleblue, bg) 
    for key in ['P']:
        curses.init_pair(aa_dict[key], flesh, bg) 
    
    for key in ['d', 'e']:
        curses.init_pair(aa_dict[key], brightred, bg) 
    for key in ['c', 'm']:
        curses.init_pair(aa_dict[key], yellow, bg) 
    for key in ['k', 'r']:
        curses.init_pair(aa_dict[key], blue, bg) 
    for key in ['s', 't']:
        curses.init_pair(aa_dict[key], orange, bg) 
    for key in ['f', 'y']:
        curses.init_pair(aa_dict[key], midblue, bg) 
    for key in ['q', 'n']:
        curses.init_pair(aa_dict[key], cyan, bg) 
    for key in ['g']:
        curses.init_pair(aa_dict[key], lightgrey, bg) 
    for key in ['l', 'v', 'i']:
        curses.init_pair(aa_dict[key], green, bg) 
    for key in ['a']:
        curses.init_pair(aa_dict[key], darkgrey, bg) 
    for key in ['w']:
        curses.init_pair(aa_dict[key], pink, bg) 
    for key in ['h']:
        curses.init_pair(aa_dict[key], paleblue, bg) 
    for key in ['p']:
        curses.init_pair(aa_dict[key], flesh, bg) 
    curses.init_pair(aa_dict['u'], darkgrey, bg) 
    curses.init_pair(aa_dict['U'], darkgrey, bg) 



def init_colours_aa_256_dark_reverse():
    """
    Initialise amino acid colour scheme for 256 colour terminals with
    colour-changing capabilities.

    Black text on a coloured background.

    Colours modified from the RasMol amino acid colour scheme
    (http://life.nthu.edu.tw/~fmhsu/rasframe/COLORS.HTM)
    """
    if not curses.can_change_color():
        return
    # amino acid colours:
    brightred = 51
    yellow = 52
    blue = 53
    orange = 54
    midblue = 55
    cyan = 56
    lightgrey = 57
    green = 58
    darkgrey = 59
    pink = 60
    paleblue = 61
    flesh = 62
    # ui colours:
    orange1 = 63
    bg = 64
    
    init_rgb255(curses.COLOR_BLACK, 0, 0, 0)
    init_rgb255(curses.COLOR_WHITE, 255, 255, 255)
    init_rgb255(bg, 0, 0, 0)
    init_rgb255(brightred, 230, 10, 10) 
    init_rgb255(yellow, 230, 230, 0) 
    init_rgb255(blue, 20, 90, 255) 
    init_rgb255(orange, 250, 150, 0)
    init_rgb255(midblue, 75, 75, 200)
    init_rgb255(cyan, 0, 220, 220)
    init_rgb255(lightgrey, 235, 235, 235)
    init_rgb255(darkgrey, 135, 135, 135)
    init_rgb255(green, 35, 180, 35)
    init_rgb255(orange1, 218, 59, 1)
    init_rgb255(flesh, 220, 150, 130)
    init_rgb255(pink, 180, 90, 180)

    curses.init_pair(1, curses.COLOR_WHITE, bg)
    curses.init_pair(2, curses.COLOR_WHITE, orange1)
    curses.init_pair(3, orange1, bg)
    curses.init_pair(4, curses.COLOR_BLACK, lightgrey)    
    curses.init_pair(11, darkgrey, bg)

    for key in ['D', 'E']:
        curses.init_pair(aa_dict[key], bg, brightred) 
    for key in ['C', 'M']:
        curses.init_pair(aa_dict[key], bg, yellow) 
    for key in ['K', 'R']:
        curses.init_pair(aa_dict[key], bg, blue) 
    for key in ['S', 'T']:
        curses.init_pair(aa_dict[key], bg, orange) 
    for key in ['F', 'Y']:
        curses.init_pair(aa_dict[key], bg, midblue) 
    for key in ['Q', 'N']:
        curses.init_pair(aa_dict[key], bg, cyan) 
    for key in ['G']:
        curses.init_pair(aa_dict[key], bg, lightgrey) 
    for key in ['L', 'V', 'I']:
        curses.init_pair(aa_dict[key], bg, green) 
    for key in ['A']:
        curses.init_pair(aa_dict[key], bg, darkgrey) 
    for key in ['W']:
        curses.init_pair(aa_dict[key], bg, pink) 
    for key in ['H']:
        curses.init_pair(aa_dict[key], bg, paleblue) 
    for key in ['P']:
        curses.init_pair(aa_dict[key], bg, flesh) 
    
    for key in ['d', 'e']:
        curses.init_pair(aa_dict[key], bg, brightred) 
    for key in ['c', 'm']:
        curses.init_pair(aa_dict[key], bg, yellow) 
    for key in ['k', 'r']:
        curses.init_pair(aa_dict[key], bg, blue) 
    for key in ['s', 't']:
        curses.init_pair(aa_dict[key], bg, orange) 
    for key in ['f', 'y']:
        curses.init_pair(aa_dict[key], bg, midblue) 
    for key in ['q', 'n']:
        curses.init_pair(aa_dict[key], bg, cyan) 
    for key in ['g']:
        curses.init_pair(aa_dict[key], bg, lightgrey) 
    for key in ['l', 'v', 'i']:
        curses.init_pair(aa_dict[key], bg, green) 
    for key in ['a']:
        curses.init_pair(aa_dict[key], bg, darkgrey) 
    for key in ['w']:
        curses.init_pair(aa_dict[key], bg, pink) 
    for key in ['h']:
        curses.init_pair(aa_dict[key], bg, paleblue) 
    for key in ['p']:
        curses.init_pair(aa_dict[key], bg, flesh) 
    curses.init_pair(aa_dict['u'], bg, darkgrey) 
    curses.init_pair(aa_dict['U'], bg, darkgrey) 



def init_colours_aa_256_light():
    """
    Initialise amino acid colour scheme for 256 colour terminals with
    colour-changing capabilities.

    Coloured text on a light background.

    Colours modified from the RasMol amino acid colour scheme
    (http://life.nthu.edu.tw/~fmhsu/rasframe/COLORS.HTM)
    """
    if not curses.can_change_color():
        return
    # amino acid colours:
    brightred = 51
    yellow = 52
    blue = 53
    orange = 54
    midblue = 55
    cyan = 56
    lightgrey = 57
    green = 58
    darkgrey = 59
    pink = 60
    paleblue = 61
    flesh = 62
    # ui colours:
    orange1 = 63
    bg = 64
    
    init_rgb255(curses.COLOR_BLACK, 0, 0, 0)
    init_rgb255(curses.COLOR_WHITE, 255, 255, 255)
    init_rgb255(bg, 255, 255, 255)
    init_rgb255(brightred, 220, 5, 5) 
    init_rgb255(yellow, 190, 190, 0) 
    init_rgb255(blue, 10, 80, 245) 
    init_rgb255(orange, 230, 130, 0)
    init_rgb255(midblue, 20, 20, 180)
    init_rgb255(cyan, 0, 210, 210)
    init_rgb255(lightgrey, 175, 175, 175)
    init_rgb255(darkgrey, 45, 45, 45)
    init_rgb255(green, 10, 140, 10)
    init_rgb255(orange1, 208, 49, 1)
    init_rgb255(flesh, 220, 150, 130)
    init_rgb255(pink, 180, 90, 180)

    curses.init_pair(1, curses.COLOR_BLACK, bg)
    # colour pair 2 for status bar
    curses.init_pair(2, curses.COLOR_WHITE, orange1)
    # colour pair 3 for gap % track
    curses.init_pair(3, orange1, bg)
    # colour pair 4 for sequence id labels
    curses.init_pair(4, curses.COLOR_WHITE, midblue)    
    # colour pair 11 for gaps and misc characters
    curses.init_pair(11, lightgrey, bg)

    for key in ['D', 'E']:
        curses.init_pair(aa_dict[key], brightred, bg) 
    for key in ['C', 'M']:
        curses.init_pair(aa_dict[key], yellow, bg) 
    for key in ['K', 'R']:
        curses.init_pair(aa_dict[key], blue, bg) 
    for key in ['S', 'T']:
        curses.init_pair(aa_dict[key], orange, bg) 
    for key in ['F', 'Y']:
        curses.init_pair(aa_dict[key], midblue, bg) 
    for key in ['Q', 'N']:
        curses.init_pair(aa_dict[key], cyan, bg) 
    for key in ['G']:
        curses.init_pair(aa_dict[key], lightgrey, bg) 
    for key in ['L', 'V', 'I']:
        curses.init_pair(aa_dict[key], green, bg) 
    for key in ['A']:
        curses.init_pair(aa_dict[key], darkgrey, bg) 
    for key in ['W']:
        curses.init_pair(aa_dict[key], pink, bg) 
    for key in ['H']:
        curses.init_pair(aa_dict[key], paleblue, bg) 
    for key in ['P']:
        curses.init_pair(aa_dict[key], flesh, bg) 
    
    for key in ['d', 'e']:
        curses.init_pair(aa_dict[key], brightred, bg) 
    for key in ['c', 'm']:
        curses.init_pair(aa_dict[key], yellow, bg) 
    for key in ['k', 'r']:
        curses.init_pair(aa_dict[key], blue, bg) 
    for key in ['s', 't']:
        curses.init_pair(aa_dict[key], orange, bg) 
    for key in ['f', 'y']:
        curses.init_pair(aa_dict[key], midblue, bg) 
    for key in ['q', 'n']:
        curses.init_pair(aa_dict[key], cyan, bg) 
    for key in ['g']:
        curses.init_pair(aa_dict[key], lightgrey, bg) 
    for key in ['l', 'v', 'i']:
        curses.init_pair(aa_dict[key], green, bg) 
    for key in ['a']:
        curses.init_pair(aa_dict[key], darkgrey, bg) 
    for key in ['w']:
        curses.init_pair(aa_dict[key], pink, bg) 
    for key in ['h']:
        curses.init_pair(aa_dict[key], paleblue, bg) 
    for key in ['p']:
        curses.init_pair(aa_dict[key], flesh, bg) 
    curses.init_pair(aa_dict['u'], darkgrey, bg) 
    curses.init_pair(aa_dict['U'], darkgrey, bg) 



def init_colours_aa_256_light_reverse():
    """
    Initialise amino acid colour scheme for 256 colour terminals with
    colour-changing capabilities.

    Light text on a coloured background.

    Colours modified from the RasMol amino acid colour scheme
    (http://life.nthu.edu.tw/~fmhsu/rasframe/COLORS.HTM)
    """
    if not curses.can_change_color():
        return
    # amino acid colours:
    brightred = 51
    yellow = 52
    blue = 53
    orange = 54
    midblue = 55
    cyan = 56
    lightgrey = 57
    green = 58
    darkgrey = 59
    pink = 60
    paleblue = 61
    flesh = 62
    # ui colours:
    orange1 = 63
    bg = 64
    
    init_rgb255(curses.COLOR_BLACK, 0, 0, 0)
    init_rgb255(curses.COLOR_WHITE, 255, 255, 255)
    init_rgb255(bg, 255, 255, 255)
    init_rgb255(brightred, 220, 5, 5) 
    init_rgb255(yellow, 190, 190, 0) 
    init_rgb255(blue, 10, 80, 245) 
    init_rgb255(orange, 230, 130, 0)
    init_rgb255(midblue, 20, 20, 180)
    init_rgb255(cyan, 0, 210, 210)
    init_rgb255(lightgrey, 175, 175, 175)
    init_rgb255(darkgrey, 45, 45, 45)
    init_rgb255(green, 10, 140, 10)
    init_rgb255(orange1, 208, 49, 1)
    init_rgb255(flesh, 220, 150, 130)
    init_rgb255(pink, 180, 90, 180)

    curses.init_pair(1, curses.COLOR_BLACK, bg)
    # colour pair 2 for status bar
    curses.init_pair(2, curses.COLOR_WHITE, orange1)
    # colour pair 3 for gap % track
    curses.init_pair(3, orange1, bg)
    # colour pair 4 for sequence id labels
    curses.init_pair(4, curses.COLOR_WHITE, midblue)    
    # colour pair 11 for gaps and misc characters
    curses.init_pair(11, lightgrey, bg)

    for key in ['D', 'E']:
        curses.init_pair(aa_dict[key], bg, brightred) 
    for key in ['C', 'M']:
        curses.init_pair(aa_dict[key], bg, yellow) 
    for key in ['K', 'R']:
        curses.init_pair(aa_dict[key], bg, blue) 
    for key in ['S', 'T']:
        curses.init_pair(aa_dict[key], bg, orange) 
    for key in ['F', 'Y']:
        curses.init_pair(aa_dict[key], bg, midblue) 
    for key in ['Q', 'N']:
        curses.init_pair(aa_dict[key], bg, cyan) 
    for key in ['G']:
        curses.init_pair(aa_dict[key], bg, lightgrey) 
    for key in ['L', 'V', 'I']:
        curses.init_pair(aa_dict[key], bg, green) 
    for key in ['A']:
        curses.init_pair(aa_dict[key], bg, darkgrey) 
    for key in ['W']:
        curses.init_pair(aa_dict[key], bg, pink) 
    for key in ['H']:
        curses.init_pair(aa_dict[key], bg, paleblue) 
    for key in ['P']:
        curses.init_pair(aa_dict[key], bg, flesh) 
    
    for key in ['d', 'e']:
        curses.init_pair(aa_dict[key], bg, brightred) 
    for key in ['c', 'm']:
        curses.init_pair(aa_dict[key], bg, yellow) 
    for key in ['k', 'r']:
        curses.init_pair(aa_dict[key], bg, blue) 
    for key in ['s', 't']:
        curses.init_pair(aa_dict[key], bg, orange) 
    for key in ['f', 'y']:
        curses.init_pair(aa_dict[key], bg, midblue) 
    for key in ['q', 'n']:
        curses.init_pair(aa_dict[key], bg, cyan) 
    for key in ['g']:
        curses.init_pair(aa_dict[key], bg, lightgrey) 
    for key in ['l', 'v', 'i']:
        curses.init_pair(aa_dict[key], bg, green) 
    for key in ['a']:
        curses.init_pair(aa_dict[key], bg, darkgrey) 
    for key in ['w']:
        curses.init_pair(aa_dict[key], bg, pink) 
    for key in ['h']:
        curses.init_pair(aa_dict[key], bg, paleblue) 
    for key in ['p']:
        curses.init_pair(aa_dict[key], bg, flesh) 
    curses.init_pair(aa_dict['u'], bg, darkgrey) 
    curses.init_pair(aa_dict['U'], bg, darkgrey) 
