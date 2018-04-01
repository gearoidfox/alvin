# Alvin (ALignment VIsualisatioN)

Alvin is a tool for viewing protein and nucleotide multiple sequence alignments (MSAs) in a terminal.

### Usage

    alvin.py alignment_file
    alvin.py -h

### Dependencies

 - [Biopython](biopython.org)


### Interface

 - Quit with q or CTRL-C.
 - Move around with WASD or the arrow keys or hjkl.
 - Jump to the top/bottom/left/right with PageUp/PageDown/Home/End or gg/G/^/$
 - Adjust the width of sequence labels with +/-. Maximise with = and minimise with 0.
 - Change colour schemes with 1/2/3/4/5.

### Screenshots

![A screenshot of Alvin](images/screenshot1.png?raw=true)


### Supported file formats

Alvin uses BioPython to read alignment files, so every format supported by BioPython is supported by Alvin, including FASTA, Stockholm, CLUSTAL, Phylip, etc. It will try to guess both the file format and whether the alignment is of nucleotide or amino acid sequences. You can override these guesses with command line flags.

### Terminal compatibility

Alvin will display colours if your terminal supports that. It will try define custom colours if your terminal supports that, too. If you want the custom colours, set your TERM environment variable to xterm-256color. If you really *don't* want them, you can set TERM to xterm-color and alvin will use the default 8 colours, which you can probably redefine in your terminal emulator. If you don't want colour at all, pressing 5 always switches to a black and white colour scheme. If necessary, you can also force alvin not to use colours by setting TERM to, e.g., vt220.
