gunpowder
=========

Tools to make plotting easier in Python

`gunpowder' is a set of Python scripts to read
data from files and plot it in a variety of ways.

Examples include reading CSV files (or similar)
and converting the contents into lists of (lists of)
numbers, and using the ROOT data analysis framework
(http://root.cern.ch/) to produce histograms or graphs.

Support for gnuplot may be added later.

`gunpowder' is released under the BSD license (see
the LICENSE file for details).

You can download `gunpowder' to your current working
directory using the command below.

```sh
for file in dataio.py dynamic_binning.py graphs.py histograms.py statistics.py LICENSE README.md ; do
    curl -O https://raw.github.com/ajbennieston/gunpowder/master/$file
done
```