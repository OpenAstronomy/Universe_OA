.. title: RGB tile drawing in hips package
.. slug:
.. date: 2017-07-23 07:46:00 
.. tags: Astropy
.. author: Adeel Ahmad
.. link: https://adl1995.github.io/rgb-tile-drawing-in-hips-package.html
.. description:
.. category: gsoc2017

The hips package now supports RGB tile drawing. To make this possible, the output image dimensions had to be altered according to the following configuration:
The output image shape is two dimensional for grayscale, and three dimensional for color images:

shape = (height, width) for FITS images wit `...READ MORE... <https://adl1995.github.io/rgb-tile-drawing-in-hips-package.html>`__

