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

from __future__ import division
import curses
from curses import error
import vcolours 

class MSAVis:
    """
    Overall curses display for viewing MSAs
    """
    class StatusBar:
        """ A one line horizontal bar displaying status information."""
        def __init__(self, y0, x0, y1, x1, filename, alignment):
            """
            Args:
                y0 (int): top boundary
                x0 (int): left boundary
                y1 (int): bottom boundary
                x1 (int): right boundary
                filename (str): name of alignment file displayed
                alignment (Bio.Align.MultipleSeqAlignment): MSA

            Returns: None
            """
            self.filename = filename
            self.num_seq = len(alignment)
            self.align_width = len(alignment[0])
            if curses.has_colors():
                attr2 = curses.color_pair(2)
                if not curses.can_change_color():
                    attr2 |= curses.A_BOLD
            else:
                attr2 = curses.A_NORMAL

            self.pad_width = x1 - x0 + 1
            self.pad = curses.newpad(1, self.pad_width + 1)
            self.pad.addstr(0,0, " " * (self.pad_width), attr2)
           
            status = "Loading {}...".format(filename)
            self.pad.addstr(0, 0, status[0:self.pad_width],
                    attr2)
            self.pad.noutrefresh(0, 0, y0, x0, y1, x1)
        
        def update(self, y0, x0, y1, x1, offset_y, disp_height):
            """
            Update how the status bar is drawn.
            Args:
                y0 (int): top boundary
                x0 (int): left boundary
                y1 (int): bottom boundary
                x1 (int): right boundary
                offset_y (int): index of the top sequence displayed in the
                    sequence area.
                disp_height (int): number of lines displayed in the sequence
                    area.

            Returns: None
            """
            if curses.has_colors():
                attr2 = curses.color_pair(2)
                if not curses.can_change_color():
                    attr2 |= curses.A_BOLD
            else:
                attr2 = curses.A_NORMAL
            if self.pad_width < x1 - x0 + 1:
                self.pad_width = x1 - x0 + 1
                self.pad = curses.newpad(1, self.pad_width + 1)

            self.pad.addstr(0,0, " " * (x1 - x0 + 1), attr2)
            if self.num_seq > disp_height:
                viewmax = offset_y + disp_height
            else:
                viewmax = self.num_seq
            status = "Viewing sequences: {}-{}/{}, Alignment length: {} [{}]"
            status = status.format(
                    offset_y + 1, viewmax, self.num_seq, self.align_width,
                        self.filename)
            self.pad.addstr(0, 0, status[0:self.pad_width], attr2)
            self.pad.noutrefresh(0, 0, y0, x0, y1, x1)

    class IDPanel:
        """ Panel displaying IDs of sequences in the alignment"""
        def __init__(self, y0, x0, y1, x1, alignment):
            """
            Args:
                y0 (int): top boundary
                x0 (int): left boundary
                y1 (int): bottom boundary
                x1 (int): right boundary
                alignment (Bio.Align.MultipleSeqAlignment): MSA

            Returns: None
            """
            self.max_len = 0
            for seq in alignment:
                j = len(seq.id)
                if j  > self.max_len:
                    self.max_len = j
            if self.max_len < 13:
                self.max_len = 13
            if self.max_len > 13:
                 self.width = 13
            else:
                 self.width = self.max_len - 1
            if curses.has_colors():
                attr4 = curses.color_pair(4)
            else:
                attr4 = curses.A_REVERSE
            self.pad = curses.newpad(len(alignment)+1, self.max_len + 1)
            j = 0
            for seq in alignment:
                self.pad.addstr(j, 0, (self.max_len + 1) * " ", attr4)
                self.pad.addstr(j, 0, seq.id, attr4)
                j += 1
            self.pad.noutrefresh(0, 0, y0, x0, y1, x1)

        def update(self, y0, x0, y1, x1, offset):
            """
            Update how the sequence id panel is drawn.
            Args:
                y0 (int): top boundary
                x0 (int): left boundary
                y1 (int): bottom boundary
                x1 (int): right boundary
                offset (int): index of the top sequence displayed in the
                    sequence area.

            Returns: None
            """
            self.pad.noutrefresh(offset, 0, y0, x0, y1, x1)

    

    class SeqPanel:
        """Main panel displaying sequences of MSA"""
        def __init__(self, y0, x0, y1, x1, alignment, preserve_gaps=False):
            """
            Args:
                y0 (int): top boundary
                x0 (int): left boundary
                y1 (int): bottom boundary
                x1 (int): right boundary
                alignment (Bio.Align.MultipleSeqAlignment): MSA
                preserve_gaps (bool): display the original gap characters from
                MSA file, instead of displaying all gaps as '.' characters.

            Returns: None
            """
            if curses.has_colors():
                attr11 = curses.color_pair(11)
            else:
                attr11 = curses.A_NORMAL
            self.pad = curses.newpad(len(alignment)+1, len(alignment[0])+0)
            y = 0
            for seq in alignment: 
                seq = str(seq.seq) 
                x = 0  # counter for columns
                hgap_count = 0; # count a run of '-' type gap symbols
                pgap_count = 0; # count a run of '.' type gap symbols
                for char in seq:
                    if char == '-' and pgap_count == 0: # continue a run of '-'
                        x += 1
                        hgap_count += 1
                        continue
                    elif char == '.' and hgap_count == 0: # continue a run of '.'
                        x += 1
                        pgap_count += 1
                        continue
                    elif char not in ['.', '-'] and hgap_count != 0:
                        # end of '-' gap
                        if preserve_gaps:
                            self.pad.addstr(y, x - hgap_count, '-' * hgap_count,
                                    attr11 )
                        else:
                            self.pad.addstr(y, x - hgap_count, '.' * hgap_count,
                                    attr11 )
                        hgap_count = 0
                    elif char not in ['.', '-'] and pgap_count != 0:
                        # end of '.' gap
                        self.pad.addstr(y, x - pgap_count, '.' * pgap_count,
                                attr11 )
                        pgap_count = 0
                    elif char == '-' and pgap_count != 0:
                        # run of '.'s changes to run of '-'s
                        self.pad.addstr(y, x - pgap_count, '.' * pgap_count,
                                attr11 )
                        pgap_count = 0
                        x += 1
                        hgap_count += 1
                        continue
                    elif char == '.' and hgap_count != 0:
                        # run of '-'s changes to run of '.'s
                        if preserve_gaps:
                            self.pad.addstr(y, x - hgap_count, '-' * hgap_count,
                                    attr11 )
                        else:
                            self.pad.addstr(y, x - hgap_count, '.' * hgap_count,
                                    attr11 )
                        hgap_count = 0
                        x += 1
                        pgap_count += 1
                        continue
                    if char in vcolours.aa_dict: # recognised non-gap
                        attr = curses.A_BOLD
                        attr = curses.A_NORMAL
                        if curses.has_colors():
                            attr |= curses.color_pair(vcolours.aa_dict[char])
                        self.pad.addstr(y, x, char, attr)
                    else: # unrecognised non-gap
                        self.pad.addstr(y, x, char, attr11)
                    x += 1
                # Trailing gaps:
                if hgap_count and pgap_count:
                    raise Exception
                elif hgap_count:
                    if preserve_gaps:
                        self.pad.addstr(y, x - hgap_count, "-" * hgap_count,
                                attr11)
                    else:
                        self.pad.addstr(y, x - hgap_count, "." * hgap_count,
                                attr11)
                elif pgap_count:
                    self.pad.addstr(y, x - pgap_count, "." * pgap_count,
                            attr11)
                y += 1
            self.height = y + 1
            self.pad.noutrefresh(0, 0, y0, x0, y1, x1)

        def update(self, y0, x0, y1, x1, offset_y, offset_x):
            """
            Update how the sequence display panel is drawn.
            Args:
                y0 (int): top boundary
                x0 (int): left boundary
                y1 (int): bottom boundary
                x1 (int): right boundary
                offset_y (int): index of the top sequence displayed in the
                    sequence area.
                offset_x (int): index of leftmost column of MSA currently
                        displayed.

            Returns: None
            """
            self.pad.noutrefresh(offset_y, offset_x, y0, x0, y1, x1)


    
    class GapsTrack:
        """
        Track showing the percentage of non-gap characters in each column of the 
        MSA
        """
        def __init__(self, y0, x0, y1, x1, alignment):
            """
            Args:
                y0 (int): top boundary
                x0 (int): left boundary
                y1 (int): bottom boundary
                x1 (int): right boundary
                alignment (Bio.Align.MultipleSeqAlignment): MSA

            Returns: None
            """
            align_width = len(alignment[0])
            num_seq = len(alignment)
            self.pad = curses.newpad(2, align_width)
            gap_count = {}
            for seq in alignment:
                seq = str(seq.seq)
                for i in range(align_width):
                    if i not in gap_count:
                        gap_count[i] = 0
                    if seq[i] in ['-', '.']:
                        gap_count[i] += 1
            if curses.has_colors():
                attr3 = curses.color_pair(3)
            else:
                attr3 = curses.A_NORMAL
            for i in range(align_width):
                pc = gap_count[i] / num_seq
                if pc > .89:
                    self.pad.addstr(0, i, " ", attr3)
                elif pc > .77:
                    self.pad.addstr(0, i, "\u2581", attr3)
                elif pc > .66:
                    self.pad.addstr(0, i, "\u2582", attr3)
                elif pc > .55:
                    self.pad.addstr(0, i, "\u2583", attr3)
                elif pc > .44:
                    self.pad.addstr(0, i, "\u2584", attr3)
                elif pc > .33:
                    self.pad.addstr(0, i, "\u2585", attr3)
                elif pc > .22:
                    self.pad.addstr(0, i, "\u2586", attr3)
                elif pc > .11:
                    self.pad.addstr(0, i, "\u2587", attr3)
                else:
                    self.pad.addstr(0, i, "\u2588", attr3)
            self.pad.noutrefresh(0, 0, y0, x0, y1, x1)
        
        def update(self, y0, x0, y1, x1, offset_x):
            """Redraw gaps track.
            Args:
                y0 (int): top boundary
                x0 (int): left boundary
                y1 (int): bottom boundary
                x1 (int): right boundary
                offset_x (int): index of leftmost column of MSA currently
                        displayed.
            Returns: None
            """
            self.pad.noutrefresh(0, offset_x, y0, x0, y1, x1)

    class PositionTrack:
        """A one line track to mark column numbers in the alignment"""
        def __init__(self, y0, x0, y1, x1, align_width):
            """
            Args:
                y0 (int): upper boundary for drawing
                x0 (int): left boundary for drawing
                y1 (int): bottom boundary for drawing
                x1 (int): right bottom for drawing
                align_width (int): number of columns in alignment 
            Returns: None
            """
            self.pad = curses.newpad(2, align_width)
            if align_width <= 10:
                position_string = "1" + (" " * (align_width - 1))
            else:
                position_string = "1" + (" " * 8)
                topnum = int(align_width - (align_width % 10))
                for i in range(1, topnum//10):
                    position_string += str(i*10) + (" " * (9 - len(str(i))))
                if align_width - topnum > len(str(topnum)):
                   position_string += str(topnum)
                padding =  align_width - len(position_string) + 1
                if padding > 1:
                    position_string += " " * padding
            if curses.has_colors():
                attr1 = curses.color_pair(1)
            else:
                attr1 = curses.A_NORMAL
            self.pad.addstr(0, 0, position_string, attr1)
            self.pad.noutrefresh(0, 0, y0, x0, y1, x1)

        def update(self, y0, x0, y1, x1, offset_x):
            """Redraw position track 
            Args:
                y0 (int): top boundary
                x0 (int): left boundary
                y1 (int): bottom boundary
                x1 (int): right boundary
                offset_x (int): index of leftmost column of MSA currently
                        displayed.
            Returns: None
            """
            self.pad.noutrefresh(0, offset_x, y0, x0, y1, x1)
 
    def __init__(self, y0, x0, y1, x1, filename, alignment,
            preserve_gaps=False, nucleotide=False):
        """
        Args:
            y0 (int): top boundary
            x0 (int): left boundary
            y1 (int): bottom boundary
            x1 (int): right boundary
            filename (str): name of alignment file displayed
            alignment (Bio.Align.MultipleSeqAlignment): MSA
            preserve_gaps (bool): display the original gap characters from the
                MSA file, instead of displaying all gaps as '.' characters.

        Returns: None
        """
        self.y0 = y0
        self.x0 = x0
        self.y1 = y1
        self.x1 = x1
        self.id_width = 13
        self.offset_y = 0
        self.offset_x = 0
        self.nucleotide = nucleotide
        self.total_seqs = len(alignment)
        self.align_width = len(alignment[0])
        
        try: # Not every terminal can make the cursor invisible:
            curses.curs_set(0)
        except Exception:
            pass

        if curses.has_colors():
            if nucleotide and curses.can_change_color():
                vcolours.init_colours_nt_256_light()
            elif curses.can_change_color():
                vcolours.init_colours_aa_256_light()
            elif nucleotide:
                vcolours.init_colours_nt_xterm_light()
            else:
                vcolours.init_colours_aa_xterm_light()
            attr1 = curses.color_pair(1)
            attr3 = curses.color_pair(3)
        else:
            attr1 = curses.A_NORMAL
            attr3 = curses.A_NORMAL
        
        # Draw fixed background panel: 
        self.bg = curses.newpad(y1-y0+1, x1-x0+1)
        line = " " * (x1 - x0 + 1)
        for j in range(y1 - y0):
            self.bg.addstr(j, 0, line, attr1)
        self.bg.noutrefresh(0, 0, y0, x0, y1, x1)

        self.bgcorner = curses.newpad(3, 13)
        self.bgcorner.addstr(0, 0, " " * 13, attr3)
        self.bgcorner.addstr(1, 0, "Non-gap %    ", attr3)
        self.bgcorner.noutrefresh(0, 0, y0, x0, 2, self.id_width) 

        position_y0 = position_y1 = y0
        gaps_y0 = gaps_y1 = position_y1 + 1

        seq_y0 = id_y0 = gaps_y1 + 1
        status_y0 = status_y1 = y1

        if self.total_seqs < status_y0 - seq_y0:
            seq_y1 = id_y1 = seq_y0 + self.total_seqs - 1
        else:
            seq_y1 = id_y1 = status_y0 - 1
        self.view_height = seq_y1 - seq_y0 + 1

        # Quick to draw:
        self.statusBar = MSAVis.StatusBar(status_y0, x0, status_y1, x1,
                filename, alignment)
        self.positionTrack = MSAVis.PositionTrack(position_y0,
                x0 + self.id_width, position_y1, x1, self.align_width)
        self.idPanel = MSAVis.IDPanel(id_y0, x0, id_y1, x0 + self.id_width-1,
                alignment)
        curses.doupdate()

        # Slow to draw:
        self.gapTrack = MSAVis.GapsTrack(gaps_y0, x0 + self.id_width,
                gaps_y1, x1, alignment)
        self.seqPanel = MSAVis.SeqPanel(seq_y0, x0 + self.id_width, seq_y1,
                x1, alignment, preserve_gaps=preserve_gaps)
        self.statusBar.update(status_y0, x0, status_y1, x1, self.offset_y,
                self.view_height)
        curses.doupdate()

    def update(self, y0, x0, y1, x1):
        """
        Update drawing.
        Args:
            y0 (int): top boundary
            x0 (int): left boundary
            y1 (int): bottom boundary
            x1 (int): right boundary

        Returns: None
        """
        if self.offset_x < 0:
            self.offset_x = 0
        if self.offset_y < 0:
            self.offset_y = 0
        if self.nucleotide:
            position_y0 = position_y1 = y0
            gaps_y0 = gaps_y1 = position_y1 + 1
        else:
            position_y0 = position_y1 = y0
            gaps_y0 = gaps_y1 = position_y1 + 1
        seq_y0 = id_y0 = gaps_y1 + 1
        status_y0 = status_y1 = y1

        if self.total_seqs < status_y0 - seq_y0:
            seq_y1 = id_y1 = seq_y0 + self.total_seqs - 1
        else:
            seq_y1 = id_y1 = status_y0 - 1
        self.view_height = seq_y1 - seq_y0 + 1

        if curses.has_colors():
            attr1 = curses.color_pair(1)
        else:
            attr1 = curses.A_NORMAL

        self.bg = curses.newpad(y1-y0+1, x1-x0+1)
        line = " " * (x1 - x0 +1)
        for j in range(y1 - y0 ):
            self.bg.addstr(j, 0, line, attr1)
        self.bg.noutrefresh(0, 0, y0, x0, y1, x1)
        self.bgcorner.noutrefresh(0, 0, y0, x0, 3, self.id_width) 

        self.positionTrack.update(position_y0, x0 + self.id_width, position_y1,
                x1, self.offset_x)
        self.gapTrack.update(gaps_y0, x0 + self.id_width, gaps_y1, x1,
                self.offset_x)
        self.idPanel.update(id_y0, x0, id_y1, x0 + self.id_width, self.offset_y)
        self.seqPanel.update(seq_y0, x0 + self.id_width, seq_y1, x1,
                self.offset_y, self.offset_x)
        self.statusBar.update(status_y0, x0, status_y1, x1, self.offset_y,
                self.view_height)
        curses.doupdate()

    def move_view_left(self):
        """
        Move the view to the left by ten positions.
        """
        self.offset_x -= 10
        if self.offset_x < 0: 
            self.offset_y = 0

    def move_view_right(self):
        """
        Move the view to the right by ten positions.
        """
        view_width = self.x1 - self.id_width + 1
        self.offset_x += 10
        if self.offset_x > self.align_width - view_width:
            self.offset_x = self.align_width - view_width

    def move_view_up(self):
        """
        Move the view up by one page.
        """
        self.offset_y -= self.view_height
        if self.offset_y < 0:
            self.offset_y = 0

    def move_view_down(self):
        """
        Move the view down by one page.
        """
        self.offset_y += self.view_height
        if self.offset_y > self.total_seqs - self.view_height:
            self.offset_y = self.total_seqs - self.view_height

    def move_view_bottom(self):
        """
        Move the view to the last sequence in the MSA.
        """
        self.offset_y = self.total_seqs - self.view_height

    def move_view_top(self):
        """
        Move the view to the first sequence in the MSA.
        """
        self.offset_y = 0

    def move_view_end_right(self):
        """
        Move the view to the last column of the MSA.
        """
        view_width = self.x1 - self.id_width + 1
        self.offset_x = self.align_width - view_width

    def move_view_begin_left(self):
        """
        Move the view to the first column of the MSA.
        """
        self.offset_x = 0

    def increase_id_width(self):
        """
        Increase the display width of sequence id pane by 1.
        """
        self.id_width += 1
        if self.id_width > self.idPanel.max_len:
            self.id_width = self.idPanel.max_len

    def decrease_id_width(self):
        """
        Decrease the display width of sequence id pane by 1.
        """
        self.id_width -= 1
        if self.id_width < 0:
            self.id_width = 0

    def maximise_id_width(self):
        """
        Increase the display width of sequences ids to accomodate the longest
        sequence id.
        """
        self.id_width = self.idPanel.max_len
    
    def minimise_id_width(self):
        """
        Set width of display of sequence ids to zero.
        """
        self.id_width = 0
