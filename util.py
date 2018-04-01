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

import curses
import sys
import re

def die_curses(stdscr, message, e=None):
    """
    Print an error message and exit from a curses window.

    Args:
        stdscr:
        message (str): Error message to print to stderr.
        e (Exception): An Exception which was caught, if any.
    """
    stdscr.erase()
    stdscr.refresh()
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
    die(message, e)

def die(message, e=None):
    """
    Print an error message and exit.

    Args:
        message (str): Error message to print to stderr.
        e (Exception): An Exception which was caught, if any.
    """
    sys.stderr.write(message)
    sys.stderr.write("\n[%s]\n" % e)
    sys.exit(1)

def guess_format(alignment_file):
    """Guess the format of a multiple sequence alignment file
    
    Makes a rough guess at the format of an MSA file.

    Returns:
        a str from ['fasta', 'clustal', 'phylip' 'nexus', 'stockholm']
        None if no guess could be made
    
    """
    with open(alignment_file, 'rU') as infile:
        line1 = next(infile)
        while line1.strip() == "":
            line1 = next(infile)
        line2 = next(infile)
        if line1[0:11] == '# STOCKHOLM':
            return 'stockholm'
        if line1[0:7] == 'CLUSTAL':
            return 'clustal'
        if line1[0:5] == '#NEXUS':
            return 'nexus'
        if line1[0] == '>':
            return 'fasta'
        # Check for phylip format by looking for two integers on the first line
        # and a sequence in 10-character blocks on the next line
        words = line1.split()
        try:
            int(words[0])
            int(words[1])
            words2 = line2.split()
            if int(words[1]) >= 50:
                expected_words = 6
            else:
                expected_words = 2 + (int(words[1]) // 10)
            if expected_words == len(words2):
                return 'phylip'
        except (ValueError, IndexError):
            pass
        return None


def guess_nucleotide(alignment):
    """Guess if a multiple sequence alignment is a nucleotide alignment
    or an amino acid alignment
    
    Args:
        alignment
    Returns:
        True if alignment seems to contain DNA or RNA sequences
        False otherwise
    """
    pattern = re.compile("^[actgunACTGUN\-\.]+$") 
    if pattern.match(str(alignment[0].seq)) is not None:
        return True
    else:
        return False
