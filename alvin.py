#!/usr/bin/env python3
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

"""
Alvin: A simple, terminal-based viewer for multiple sequence alignments (MSAs)
using curses.

Usage: python3 alvin.py -h
"""

import argparse
import curses
import signal
import sys

try:
    from Bio import AlignIO
except ImportError as e:
    die("FATAL: BioPython is required.\n", e)

import vcolours
from msavis import MSAVis
from util import guess_format, guess_nucleotide, die, die_curses



class KilledException(Exception):
    """ 
    Throw this exception when the user kills the program with SIGINT,
    then we can catch it and clean up the curses environment before exiting
    """
    pass



def interrupt_handler(signal, frame):
    """
    We'll use this to handle getting interrupted by SIGINT
    """
    raise KilledException("Caught %s" % signal)



def curses_main(stdscr, args):
    """
    Handle file input, initialise the curses display and wait for user input.

    Args:
        stdscr :
        args : arguments passed along from argparse
        
    Attempts to read an alignment, initialises an MSAVis object to display the
    alignment, then enters a loop and waits for keyboard input.
    """
    signal.signal(signal.SIGINT, interrupt_handler)
    try:
        alignment = AlignIO.read(args.aln_file, args.format)
    except IOError as e:
        die_curses(stdscr, " FATAL: Can't read from file [%s]" % args.aln_file, e)
    except ValueError as e:
        die_curses(stdscr, " FATAL: Can't read sequences in %s "
                "format from file [%s]" % (args.format, args.aln_file), e)
    if args.nucleotide is False:
        args.nucleotide = guess_nucleotide(alignment)

    stdscr.refresh()
    ymax, xmax = curses.LINES-1, curses.COLS-1

    msaVis = MSAVis(0, 0, ymax, xmax, args.aln_file, alignment,
            preserve_gaps=args.gapsym, nucleotide=args.nucleotide)


    while True:
        inkey = stdscr.getkey()
        # quitting:
        if inkey in ['q', 'Q', 'KEY_EXIT', 'KEY_CLOSE']:
            break
        # moving around the alignment:
        elif inkey in ['s', 'S', 'j', 'KEY_DOWN']:
            msaVis.move_view_down()
        elif inkey in ["KEY_UP", 'w', 'W', 'k']:
            msaVis.move_view_up()
        elif inkey in [ "KEY_RIGHT","d", "D", 'l']:
            msaVis.move_view_right()
        elif inkey in ["KEY_LEFT", "a", "A", 'h']:
            msaVis.move_view_left()
        elif inkey in ['g']:
            inkey = stdscr.getkey()
            if inkey == 'g':
                msaVis.move_view_top()
            else:
                continue
        elif inkey in ['KEY_PPAGE']:
            msaVis.move_view_top()
        elif inkey in ['G', 'KEY_NPAGE']:
            msaVis.move_view_bottom()
        elif inkey in ['^', 'KEY_HOME']:
            msaVis.move_view_begin_left()
        elif inkey in ["$", 'KEY_END']:
            msaVis.move_view_end_right()
        # adjusting the width of the sequence id panel:
        elif inkey in ["-"]:
            msaVis.decrease_id_width()
        elif inkey in ["+"]:
            msaVis.increase_id_width()
        elif inkey in ['0']:
            msaVis.minimise_id_width()
        elif inkey in ['=']:
            msaVis.maximise_id_width()
        # changing colour scheme:
        # Numeric keys have different effects based on terminal capabilities,
        # and whether we're viewing protein or nucleotide sequences.
        # 1: Dark background scheme suitable for the terminal and data
        elif inkey == "1" and curses.has_colors():
            if curses.can_change_color() and args.nucleotide:
                vcolours.init_colours_nt_256_dark()
            elif curses.can_change_color(): 
                vcolours.init_colours_aa_256_dark()
            elif args.nucleotide:
                vcolours.init_colours_nt_xterm_dark()
            else:
                vcolours.init_colours_aa_xterm_dark()
        # 2: Dark coloured scheme suitable for the terminal and data
        elif inkey == "2" and curses.has_colors():
            if curses.can_change_color() and args.nucleotide:
                vcolours.init_colours_nt_256_dark_reverse()
            elif curses.can_change_color(): 
                vcolours.init_colours_aa_256_dark_reverse()
            elif args.nucleotide:
                vcolours.init_colours_nt_xterm_dark_reverse()
            else:
                vcolours.init_colours_aa_xterm_dark_reverse()
        # 3: Light background scheme suitable for the terminal and data
        elif inkey == "3" and curses.has_colors():
            if curses.can_change_color() and args.nucleotide:
                vcolours.init_colours_nt_256_light()
            elif curses.can_change_color(): 
                vcolours.init_colours_aa_256_light()
            elif args.nucleotide:
                vcolours.init_colours_nt_xterm_light()
            else:
                vcolours.init_colours_aa_xterm_light()
        # 4: Light coloured scheme suitable for the terminal and data
        elif inkey == "4" and curses.has_colors():
            if curses.can_change_color() and args.nucleotide:
                vcolours.init_colours_nt_256_light_reverse()
            elif curses.can_change_color(): 
                vcolours.init_colours_aa_256_light_reverse()
            elif args.nucleotide:
                vcolours.init_colours_nt_xterm_light_reverse()
            else:
                vcolours.init_colours_aa_xterm_light_reverse()
        # 5: Black and white
        elif inkey == "5" and curses.has_colors():
            vcolours.init_alignment_colours_white()
       
        # Know when the terminal has been resized:
        if curses.is_term_resized(ymax+1, xmax+1):
            stdscr.clear()
            ymax, xmax = stdscr.getmaxyx()
            curses.resizeterm(ymax, xmax)
            ymax -= 1
            xmax -= 1
        msaVis.update(0, 0, ymax, xmax)



def main():
    """
    Handle command line arguments and launch curses display, then enter
    curses_main()
    """

    epilog = """
    Reads MSAs in any format supported by BioPython. Autodetects alignments in
    FASTA, Stockholm, Phylip and Nexus formats.

    Current does not autodetect PIR format correctly.

    By default, all gaps are displayed as '.'

    To preserve the original gap symbols from the alignment file, use the
    --gapsym option.
    """

    description = """
    Terminal-based multiple sequence alignment viewer.
    """

    parser = argparse.ArgumentParser(epilog=epilog, description=description)
    parser.add_argument('aln_file', help="Path to alignment file.")
    parser.add_argument('--format', '-f', help="MSA format (skip autodetection)")
    parser.add_argument('--gapsym', help="Preserve gap symbols from file.",
            action='store_true', default=False)
    parser.add_argument('--nucleotide', '-n', action='store_true',
            default=False, help="Nucleotide alignment.")
    args = parser.parse_args()

    if args.format is None:
        args.format = guess_format(args.aln_file)
        if args.format is None:
            die( "FATAL: can't determine format of %s. Try specifying the "
                    "alignment format manually.\n" % args.aln_file, None)
    try:
        stdscr=curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(1)
        if curses.has_colors():
            curses.start_color()
        curses_main(stdscr, args)
    # don't print a stack trace if killed by, e.g, SIGINT
    # we just want to clean up the environment and quit
    except KilledException: 
        pass 
    finally:
        stdscr.erase()
        stdscr.refresh()
        stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
    return 0



if __name__=='__main__':
    sys.exit(main())

