# The Performance of Open Source Applications

This repository contains the source code for The Performance of Open Source Application, a book about open source applications that are fast, slow, big, and small.

### Copyediting

Please see the [style guide][style_guide] for copyediting instructions. There is a checklist there -- use it, especially if you have a dumb memory like me!

[style_guide]: https://github.com/tarmstrong/posa/wiki/Style-Guide

## Building

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

### TODO

* <del>References (only really a problem for khmer and DaNCE... and maybe mobile-perf)</del> Latex refs work; get them working for html/epub. The pandoc ref format wasn't working for me, so try adding something to `preprocessor.py`.
* <del>Epub - Mobi conversion</del>
* Web design for the HTML version
* <del>Set up a pelican env for posa</del>
* Proof the HTML version (typesetting edge cases)
  * Figure numbering in the HTML/epub version
  * mdashes (should have worked automatically...)
  * Ajax Math or whatever for the latex equations in chapters like khmer.
    * Particularly for the epub/mobi versions -- can't really rely on ajaxmath, can we? 
* Hard copy
  * Cover art / cover design
    * Add back cover copy (which is done, I just haven't added it yet)
    * Add ISBN barcode (blocked on uploading contents to Lulu)
    * Finalize spine width (blocked on uploading contents to Lulu)
  * Finalize front matter (copyright page, intro etc)
  * Finalize back matter (colophon)
  * create images files for title page, half-title page, etc

## Contributing

You can

* Copyedit (proofread). See the Copyediting section.
* Translate (into other languages). This should wait until after the English version is done, though.
* Test-read on your ebook device.

## Who's doing what?

Put your name here if you start on a chapter. When you're done, scratch it out so I know you're done <del>like this</del>.

I'd like to have at least two copyeditors per chapter. For `pugixml` we probably can't go overboard.

* <del>Alexandra: copyediting mobile-perf</del>
* <del>Amy: copyediting pugixml</del>
* <del>Natalie: copyediting ninja</del>
* <del>Peter Rood: copyediting memshrink</del>
* <del>Jessica McKellar: copyediting Talos</del>
* <del>Erik Habbinga: copyediting Warp</del>
* <del>Jeff Schwab: copyediting Infinispan</del>
* <del>Michael Baker: copyediting khmer</del>
* Adam Fletcher: copyediting mobile-perf
* Ben Trevor: copyediting chrome
* <del>Danielle Pham: copyediting chrome</del>
