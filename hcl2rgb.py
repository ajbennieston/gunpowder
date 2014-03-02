#!/usr/bin/env python

from math import fabs, fmod

# The functions listed below are imported when using:
#   from hcl2rgb import *
__all__ = ['hcl_to_rgb', 'rgb_to_hex', 'generate_colors']

def range_limit(value, low=0, high=255):
    return max(low, min(value, high))

def hcl_to_rgb(hcl):
    '''
    Hue, Chroma, Luminance --> RGB Colour Space

    Algorithm taken from the ImageMagick codebase:
    http://www.imagemagick.org/api/MagickCore/gem_8c_source.html#l00086

    Range adapted from 0-65535 to 0-255 to fit 24-bit colour
    RGB values, and allow easy conversion to hex colours.
    '''
    (hue, chroma, luma) = hcl
    h = 6.0 * hue
    c = chroma
    x = c * (1.0 - fabs(fmod(h, 2.0) - 1.0))

    val = None
    if h < 0.0:
        val = (0.0, 0.0, 0.0)
    elif h < 1.0:
        val = (c, x, 0.0)
    elif h < 2.0:
        val = (x, c, 0.0)
    elif h < 3.0:
        val = (0.0, c, x)
    elif h < 4.0:
        val = (0.0, x, c)
    elif h < 5.0:
        val = (x, 0.0, c)
    elif h < 6.0:
        val = (c, 0.0, x)
    else:
        val = (0.0, 0.0, 0.0)
    
    m = luma - (0.298839*val[0] + 0.586811*val[1] + 0.114350*val[2])
    rgbcolor = map(lambda v: range_limit(int(255*(v + m))), val)
    return tuple(rgbcolor)

def rgb_to_hex(rgb):
    '''
    Convert a tuple of (r, g, b) with values between
    0 and 255 into a string of the form '#rrggbb', where
    rr, gg and bb are the 2-digit hex values of r, g and b.
    '''
    return '#%02x%02x%02x' % tuple(rgb)

def generate_rgb_colors(N, chroma=0.7, luma=0.5):
    incr = 1.0 / (N + 0.5)
    colors = [hcl_to_rgb((incr * i, chroma, luma))
              for i in xrange(N)]
    return colors

def generate_hex_colors(N, chroma=0.7, luma=0.5):
    '''
    Generate N colours with hues equally distributed around
    a circle. Returns a list of hex strings corresponding to
    the colours generated.
    '''
    colors = [rgb_to_hex(color) for color in
              generate_rgb_colors(N, chroma, luma)]
    return colors

def main():
    '''
    Demonstration of this module, if executed with
        python hcl2rgb.py

    Produces a list of Gnuplot line style strings for the
    number of colours requested.
    '''
    import sys
    if len(sys.argv) != 4:
        print 'Usage: %s num_colors chroma luminance'
        print '  chroma and luminance between 0 and 1.'
        print '  Sensible defaults are 0.7 and 0.5, respectively.'
        sys.exit(1)

    num = int(sys.argv[1])
    chroma = float(sys.argv[2])
    luminance = float(sys.argv[3])

    colors = enumerate(generate_hex_colors(num, chroma, luminance),
                       start=1)
    for entry in colors:
        print "set style line %d lc rgbcolor '%s'" % entry

if __name__ == '__main__':
    main()
