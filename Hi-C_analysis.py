import matplotlib
#matplotlib.rcParams['backend'] = 'TkAgg' 
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
#plt.rcParams['backend'] = 'TkAgg' 
#plt.switch_backend('TKAgg')
import numpy as np
import seaborn as sns
import pandas as pd
import os
import cooltools
import cooler
from matplotlib.ticker import EngFormatter
import bioframe
import math

def selfRegionCompare(chromosome, chromStart, chromEnd):
    print("Unfinished")


def intraChromosomalCompare(chromosome, chromStart, chromEnd):
    print("Unfinished")


def interChromosomalCompare(chromosome, chromStart, chromEnd, chromComp):
    print("Unfinished")


HICcooler = cooler.Cooler('./4DNFIMDQ6WYX.mcool::resolutions/10000000')



#print(HICcooler)
#print(cooler.fileops.list_coolers('./4DNFIMDQ6WYX.mcool'))
#print(f'chromosomes: {HICcooler.chromnames}, binsize: {HICcooler.binsize}, chromsizes: {HICcooler.chromsizes}')

#chromosomes = []
#for x in HICcooler.chromnames:
#    print(f'{x} : {HICcooler.extent(x)}')
#    chromosomes.append(HICcooler.extent(x)[0])

#for y in chromosomes:
#    print(y)


HICmatrix = HICcooler.matrix(balance = True) 

geneLocationFile = open("chromosomalAnnotations0-10.txt", 'r')
tempFile = open("temp.txt", 'w')

geneLocationFile.readline()  #reads first line which is just a description

count = 0 #Running count of matrix entries
sum = 0 #Sum of all matrix entries

for line in geneLocationFile:

    chromosome = line.split()[0]

    if "_" in chromosome:
        continue

    if "chr" not in chromosome:
        continue

    chromStart = line.split()[1]
    chromEnd = line.split()[2]

    UCSCstring = chromosome + ":" + chromStart + "-" + chromEnd
    binPair = HICcooler.extent(UCSCstring)
    binLeft = binPair[0]
    binRight = binPair[1]
    #comparisonMatrix = HICmatrix[binLeft:binRight, binLeft:binRight] #Can change this to different comparisons depending on what is required
    #tempFile.write(str(comparisonMatrix))
    #tempFile.write("\n")
    #comparisonMatrix = HICmatrix[binLeft:binRight, chromosome] #intraChromosomal
    comparisonMatrix = HICmatrix[binLeft:binRight, :] #allChromosomes

    for x in comparisonMatrix:
        for y in x:
            if math.isnan(y):
                continue
            count = count + 1
            sum = sum + y
            #print(sum / count)
            tempFile.write(str(y))
            tempFile.write("\n")

   

average = sum / count

tempFile.write("Sum: ")
tempFile.write(str(sum))
tempFile.write("\n")
tempFile.write("Count: ")
tempFile.write(str(count))
tempFile.write("\n")
tempFile.write("Average: ")
tempFile.write(str(average))

#print(average)

geneLocationFile.close()
tempFile.close()



#print(HICmatrix[12:49265082-49274600])
#print(HICmatrix[:])
#print(HICcooler.extent('chr12:49,265,082-49,274,600'))
#print(HICcooler.extent('chr12:9,065,177-9,068,060'))
#print(HICmatrix['chr12:49,265,082-49,274,600' : 'chr1'])

#print(HICmatrix[200:201, :])
#print(HICmatrix[204:205, 204:205])
#print(HICmatrix.fetch('chr12:49265082-49274600','chr12:49265082-49274600'))