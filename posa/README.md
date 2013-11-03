# The Performance of Open Source Applications

This repository contains the source code for The Performance of Open Source Application, a book about open source applications that are fast, slow, big, and small.

### Copyediting

Please see the [style guide][style_guide] for copyediting instructions. There is a checklist there -- use it, especially if you have a dumb memory like me!

[style_guide]: https://github.com/tarmstrong/posa/wiki/Style-Guide

## Building

**Note: these are out of date and probably don't work**

Building the book isn't necessary for copyediting, but it does help if you want to help fix formatting glitches.

To build all chapters in PDF and ePUB format:

    python build.py --pdf --epub

To build only a PDF with only the "khmer" and "warp" chapters included (useful for a faster build when you're working on a single chapter):

    python build.py --pdf khmer warp

To view the HTML version:

    python build.py --html
    cd html/
    ./develop_server.sh start

.. and then visit [http://localhost:8000](http://localhost:8000) to view the site.

### Requirements

* Python, for the `build.py` script
  * The build script might not work on other platforms -- feel free to fix those issues or just let me know about them.
* [Pandoc](http://johnmacfarlane.net/pandoc/installing.html). If you dont have a recent enough version (I'm using 1.11.1) then the book won't build.
* PDFLaTeX (`sudo apt-get install texlive`) for PDF output
  * If you're not on linux, the Pandoc installations recommend a package for
    this. (e.g. MixTex on Windows)

On Ubuntu:

    sudo apt-get install texlive-full
    sudo apt-get install haskell-platform
    cabal update
    cabal install pandoc
