# Neofetch_ImageConverter

This is a small application for creating custom image files for Neofetch.
It takes the HTML of an ascii image and outputs a text file with all the color
tags in place. You can get the HTML file by feeding an image into a number of
online ascii image creators then choosing HTML as the output.

I'll do a full set of instructions when it's more complete.

TODOs:

1. Right now, the input file is static, so I need add a prompt allowing the user to choose.
    Also, it only outputs to the terminal and must be manually copy/pasted into a text file.
    I'll change this so you can choose an output file.

2. It tags the different colors, but doesn't convert the RGB values to 256-color, which is
    what Neofetch recongises. This means the user must choose colors by hand after conversion.
    I'm looking into ways of sorting this out.

3. It will currently accept any number of different colors and tag them all, even though Neofetch
    will only display 6 at once. Any additional ones will not appear, but the tags will, ruining
    the image. There are three possible solution to this that I can think of:

        - Keep images limited to 6 colors, although this can be tough when using an image converter,
            as they often add shading or pick up on colors that aren't in the original.

        - I'm thinking of adding an initial pass that counts all the colors and, if more than 6 are
            found, the user will be prompted to merge similar colors until they are down to 6. As a
            reminder to myself, I'll do this with a list of offsets, the first 6 of which will always 
            be 0.

        - There is also the option to recompile Neofetch to accept more than 6 colors. This isn't 
            difficult, and I'll probably leave instructions soon, but as a quick reminder to myself,
            it's just adding extra variables to the main neofetch file then running 'make install'
            from within the folder. The lines to add to all mention color, text, or ascii, and can be 
            found by looking for these line numbers or strings:

            4086 / # Colors.
            4675 / set_colors()
            5315 / # Text Colors
            5387 / "--ascii_colors"