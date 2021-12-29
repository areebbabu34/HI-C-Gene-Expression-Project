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


plt.switch_backend("TkAgg")

HICcooler = cooler.Cooler('./4DNFIMDQ6WYX.mcool::resolutions/10000000')


print(HICcooler)
print(cooler.fileops.list_coolers('./4DNFIMDQ6WYX.mcool'))
print(f'chromosomes: {HICcooler.chromnames}, binsize: {HICcooler.binsize}, chromsizes: {HICcooler.chromsizes}')

chromosomes = []
for x in HICcooler.chromnames:
    print(f'{x} : {HICcooler.extent(x)}')
    chromosomes.append(HICcooler.extent(x)[0])

for y in chromosomes:
    print(y)

HICmatrix = HICcooler.matrix(balance = True)

# f, ax = plt.subplots(
#     figsize=(7,6))
# im = ax.matshow((HICcooler.matrix(balance=False)[:]),vmax=2500);
# plt.colorbar(im ,fraction=0.046, pad=0.04, label='raw counts')
# ax.set(xticks=chromosomes, xticklabels=HICcooler.chromnames,
#        xlabel='position, chrom#', ylabel='position, bin#')
# ax.xaxis.set_label_position('top')
#plt.plot()
#plt.show()
# plt.savefig("output.jpg")

bp_formatter = EngFormatter('b')

def format_ticks(ax, x=True, y=True, rotate=True):
    if y:
        ax.yaxis.set_major_formatter(bp_formatter)
    if x:
        ax.xaxis.set_major_formatter(bp_formatter)
        ax.xaxis.tick_bottom()
    if rotate:
        ax.tick_params(axis='x',rotation=45)

# f, axs = plt.subplots(
#     figsize=(14,4),
#     ncols=3)

# ax = axs[0]
# im = ax.matshow(HICcooler.matrix(balance=False)[:], vmax=2500);
# plt.colorbar(im, ax=ax ,fraction=0.046, pad=0.04, label='raw counts');
# ax.set_xticks(chromosomes)
# ax.set_xticklabels(HICcooler.chromnames)
# ax.set_yticks(chromosomes)
# ax.set_yticklabels(HICcooler.chromnames)
# ax.xaxis.tick_bottom()
# ax.set_title('All data')

# ax = axs[1]
# im = ax.matshow(
#     HICcooler.matrix(balance=False).fetch('chrY'),
#     vmax=2500,
#     extent=(0,HICcooler.chromsizes['chrY'], HICcooler.chromsizes['chrY'], 0)
# );
# plt.colorbar(im, ax=ax ,fraction=0.046, pad=0.04, label='raw counts');
# ax.set_title('chrY', y=1.08)
# ax.set_ylabel('position, Mb')
# format_ticks(ax)


# ax = axs[2]
# start, end = 30_000, 60_000
# region = ('chrY', start, end)
# im = ax.matshow(
#     HICcooler.matrix(balance=False).fetch(region),
#     vmax=2500,
#     extent=(start, end, end, start)
# );
# ax.set_title(f'chrY:{start:,}-{end:,}', y=1.08)
# plt.colorbar(im, ax=ax ,fraction=0.046, pad=0.04, label='raw counts');
# format_ticks(ax)
# plt.tight_layout()

# plot heatmaps at megabase resolution with 3 levels of zoom in log-scale with a consistent colormap#
from matplotlib.colors import LogNorm

f, axs = plt.subplots(
    figsize=(14,4),
    ncols=3)
bp_formatter = EngFormatter('b')
norm = LogNorm(vmax=50_000)

ax = axs[0]
im = ax.matshow(
    HICcooler.matrix(balance=False)[:],
    norm=norm,
)
plt.colorbar(im, ax=ax ,fraction=0.046, pad=0.04, label='raw counts');
ax.set_xticks(chromosomes)
ax.set_xticklabels(HICcooler.chromnames)
ax.set_yticks(chromosomes)
ax.set_yticklabels(HICcooler.chromnames)
ax.xaxis.tick_bottom()
ax.set_title('All data')

ax = axs[1]
im = ax.matshow(
    HICcooler.matrix(balance=False).fetch('chrY'),
    norm=norm,
    extent=(0,HICcooler.chromsizes['chrY'], HICcooler.chromsizes['chrY'], 0)
);
plt.colorbar(im, ax=ax ,fraction=0.046, pad=0.04, label='raw counts');
ax.set_title('chrY', y=1.08)
ax.set(ylabel='position, Mb', xlabel='position, Mb')
format_ticks(ax)

ax = axs[2]
start, end = 30_000, 60_000
region = ('chrY', start, end)
im = ax.matshow(
    HICcooler.matrix(balance=False).fetch(region),
    norm=norm,
    extent=(start, end, end, start)
);
ax.set_title(f'chrY:{start:,}-{end:,}', y=1.08)
plt.colorbar(im, ax=ax ,fraction=0.046, pad=0.04, label='raw counts');
ax.set(xlabel='position, Mb')
format_ticks(ax)
plt.tight_layout()


plt.savefig("chrYlog.jpg") 