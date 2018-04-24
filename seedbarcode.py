#!/usr/bin/env python

#from __future__ import print_function
#from __future__ import division
import sys
import argparse
import textwrap
#import timeit
import os
#import re
#import pandas as pd

def version():
    v0 = """
    ##########################################################################################
    seedbarcode version beta-0.1
    Jinliang Yang
    updated: 04-24-2018, generate barcoded Avery labels for seed planting and storage
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation.
    --------------------------------
    
    ##########################################################################################
    """
    return v0

def topscript(infile_name, outfile_name, ptype, fs):
    
    ## clean up the print dir
    os.system('cp ps/readbars.ps readbars.ps')
    ## file
    if(ptype == "avery5160" or ptype =="avery-5160" or ptype =="5160"):
        avery5160(infile_name, outfile_name, fs)
    if(ptype == "avery5167" or ptype =="avery-5167" or ptype == "5167"):
        avery5167(infile_name, outfile_name, fs)
    
    
# postscriptbarcode: https://github.com/bwipp/postscriptbarcode
# The meaning of each component of the invocation is as follows:

#150 750 moveto             % The position of the symbol on the canvas
#(0123456789)               % The data field: Data content represented by the symbol
#(includetext height=0.75)  % The options field: Properties of the symbol
#/interleaved2of5           % The type of barcode, often called the "symbology"
#/uk.co.terryburton.bwipp findresource exec  % A call to plot the symbol on the canvas
def avery5160(infile_name, outfile_name, fs):
    with open(infile_name, 'r') as infile, open('readbars.ps','a') as fout:
        
        line1 = infile.readline()
        #line1array = line1.split()
        
        for line in infile:
            tokens = line.split(",")
            fout.write('20 40 moveto (' +
            str(tokens[0]) +
            # donot support text for 2D barcode
            #') (version=10 eclevel=Q width=0.5 height=0.5 includetext textxalign=left textyalign=center textfont=Times-Roman textsize=5 )'+
            #' /qrcode /uk.co.terryburton.bwipp findresource exec\n')
            ') (includetext textxalign=left textsize=' + fs +
            ' ) /code128 /uk.co.terryburton.bwipp findresource exec\n')
            fout.write('XXXDELIM\n')
    print("###>>> printed Avery 5160 labels")
    os.system('labelnation -t avery-5160 -i readbars.ps -c -d "XXXDELIM" -o ' + outfile_name)
#os.system('ps2pdf fsbarcodes.ps final.pdf')


### Planting Envelope:
def avery5167(infile_name, outfile_name, fs):
    print("printed Avery 5167 planting labels")
    os.system('labelnation -t avery-5167 -i ' + infile_name + ' --csv --font-size ' + fs + ' -o ' + outfile_name)
#os.system('ps2pdf fsbarcodes.ps final.pdf')    

##########################################################################################
#get_loci_info(y[4:31])
    
def get_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(version())
        )

    # positional arguments:
    #parser.add_argument('query', metavar='QUERY', type=str, nargs='*', \
    #                    help='the question to answer')

    # optional arguments:
    parser.add_argument('-p', '--path', help='the path of the input files', \
                        nargs='?', default=os.getcwd())
    parser.add_argument('-i','--input', help='input file, must be csv', type=str)
    parser.add_argument('-t','--ptype', help='Avery label type (options: 5167 (planting labels), 5160 (regular seed envelope))', type=str)
    parser.add_argument('-f','--fontsize', help='Font size of the text', type=str)
    
    parser.add_argument('-o', '--output', help='output files, like chr1_merged', type=str)
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['input'] is not None:
        print(version())
    if args['path'] is not None:
        os.chdir(args['path'])
        
    topscript(infile_name=args['input'], outfile_name=args['output'], ptype=args['ptype'], fs=args['fontsize'])


    print("Job finished!")
