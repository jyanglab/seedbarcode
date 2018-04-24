[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

# Project Guideline

- To guide group members having a better sense about the project layout, here we briefly introduce the specific purposes of the [dir system](https://jyanglab.github.io/2017-01-07-project/). The layout of dirs is based on the idea borrowed from [ProjectTemplate](http://projecttemplate.net/architecture.html).

- The guideline for the collaborative [workflow](https://jyanglab.github.io/2017-01-10-project-using-github/).

- Check out progress and things [to-do](TODO.md) and throw ideas via the wiki page.

## Dependency

- [postscriptbarcode](https://github.com/bwipp/postscriptbarcode)
- [labelnation](https://www.red-bean.com/labelnation/)

## INSTALL

```
git clone git@github.com:jyanglab/seedbarcode.git
```
Make sure to get the above dependencies installed first and export them in your $PATH.
And then cd to the directory that you just cloned.

```
chmod +x seedbarcode.py
seedbarcode.py -h
```

## USAGE

### Print Avery-5167 Planting Envelope Labels

Note: will print all the columns in the csv file:
```
seedbarcode.py -i input_test.csv -t avery-5167 -f 12 -o output.ps
```

### Print Avery-5160 Seed Labels

Note: will only print the first column of the csv file:
```
seedbarcode.py -i input_test.csv -t avery-5167 -f 12 -o output.ps
```


## License
This is an ongoing research project. It was intended for internal lab usage. It has not been extensively tested. Use at your own risk.
It is a free and open source software, licensed under [GPLv3](LICENSE).
