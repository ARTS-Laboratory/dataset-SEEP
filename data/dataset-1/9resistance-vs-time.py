#%% import modules and set default fonts and colors
"""
Default plot formatting code for Austin Downey's series of open source notes/
books. This common header is used to set the fonts and format.
Header file last updated May 16, 2024
"""

from IPython import get_ipython
get_ipython().run_line_magic('reset', '-f') 

import numpy as np
import matplotlib.pyplot as plt

# set default fonts and plot colors
plt.rcParams.update({'text.usetex': False})
plt.rcParams.update({'image.cmap': 'viridis'})
plt.rcParams.update({'font.serif':['Times New Roman', 'Times', 'DejaVu Serif',
'Bitstream Vera Serif', 'Computer Modern Roman', 'New Century Schoolbook',
'Century Schoolbook L', 'Utopia', 'ITC Bookman', 'Bookman',
'Nimbus Roman No9 L', 'Palatino', 'Charter', 'serif']})
plt.rcParams.update({'font.family':'serif'})
plt.rcParams.update({'font.size': 10})
plt.rcParams.update({'mathtext.rm': 'serif'})
# I don't think I need this next line as its set to 'stixsans' above.
plt.rcParams.update({'mathtext.fontset': 'custom'})
cc = plt.rcParams['axes.prop_cycle'].by_key()['color']
## End of plot formatting code
plt.close('all')

#%%

D = np.loadtxt('tds-data.csv',skiprows=2,delimiter=',')

'''
plt.figure()
plt.plot(D[:,1])
plt.plot(D[:,2])
plt.plot(D[:,3])
plt.plot(D[:,4])
plt.plot(D[:,5])
plt.plot(D[:,6])
plt.plot(D[:,7])
plt.plot(D[:,8])
plt.plot(D[:,9])
'''

import numpy as np

def voltage_to_resistance(V):
    tdsValue = (133.42 * V**3 - 255.86 * V**2 + 857.39 * V) * 0.5
    # Avoid divide-by-zero errors
    tdsValue = np.where(tdsValue == 0, np.nan, tdsValue)
    R = 134000 / tdsValue # k_cell = 0.268 cm^-1
    return R

x = ((D[:,0]*1000000)/60) - 18.24155

fig, ax = plt.subplots(figsize=(5.5,3.5))
ax.plot(x,voltage_to_resistance(D[:,1]),label='node 1', linewidth=1, color='#d62728')
ax.plot(x,voltage_to_resistance(D[:,2]),label='node 2', linewidth=1, color='#ff7f0e')
ax.plot(x,voltage_to_resistance(D[:,3]),label='node 3', linewidth=1, color='#bcbd22')
ax.plot(x,voltage_to_resistance(D[:,4]),label='node 4', linewidth=1, color='#2ca02c')
ax.plot(x,voltage_to_resistance(D[:,5]),label='node 5', linewidth=1, color='#17becf')
ax.plot(x,voltage_to_resistance(D[:,6]),label='node 6', linewidth=1, color='#1f77b4')
ax.plot(x,voltage_to_resistance(D[:,7]),label='node 7', linewidth=1, color='#9467bd')
ax.plot(x,voltage_to_resistance(D[:,8]),label='node 8', linewidth=1, color='#7f7f7f')
ax.plot(x,voltage_to_resistance(D[:,9]),label='node 9', linewidth=1, color='#8c564b')

# timestamp lines and labels
ax.axvline(x=19,linestyle='--',color='black',linewidth=1, zorder=0)
ax.text(19, 2500, '19 min',
        va='center', ha='center', bbox=dict(
            facecolor='white',
            edgecolor='none',
            boxstyle='round,pad=0.3',
            alpha=0.9))
ax.axvline(x=34,linestyle='--',color='black',linewidth=1, zorder=0)
ax.text(34, 7667, '34 min',
        va='center', ha='center', bbox=dict(
            facecolor='white',
            edgecolor='none',
            boxstyle='round,pad=0.3',
            alpha=0.9))
ax.axvline(x=44,linestyle='--',color='black',linewidth=1, zorder=0)
ax.text(44, 7667, '44 min',
        va='center', ha='center', bbox=dict(
            facecolor='white',
            edgecolor='none',
            boxstyle='round,pad=0.3',
            alpha=0.9))
ax.axvline(x=62,linestyle='--',color='black',linewidth=1, zorder=0)
ax.text(62, 7667, '62 min',
        va='center', ha='center', bbox=dict(
            facecolor='white',
            edgecolor='none',
            boxstyle='round,pad=0.3',
            alpha=0.9))
ax.axvline(x=72,linestyle='--',color='black',linewidth=1, zorder=0)
ax.text(72, 7667, '72 min',
        va='center', ha='center', bbox=dict(
            facecolor='white',
            edgecolor='none',
            boxstyle='round,pad=0.3',
            alpha=0.9))

ax.set_xlim(0,105)
ax.set_ylim(1500, 20000)
ax.autoscale(enable=False)
ax.set_xticks(np.linspace(0,105,7))
ax.set_yticks(np.linspace(1500,20000,10))
ax.tick_params(axis='both',direction='out')

ax.set_ylabel(r'resistance ($\Omega$)')
ax.set_xlabel('time (min)')
ax.legend(ncol=2, facecolor='white', framealpha=1)
plt.tight_layout(pad=0)
plt.grid(visible=True)
plt.savefig('9resistance-vs-time.jpg',dpi=275)