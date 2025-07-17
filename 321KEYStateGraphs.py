###############################################################################
###############################################################################
#                                KEY Graphs 321
###############################################################################
###############################################################################

###############################################################################
#                   Load Libraries - Import & Subset Data
###############################################################################
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.close('all')

directory = "G:/SYNC/School/VT/RESEARCH/Dissertation/Working Research/Forestry (both papers)/Paper 2/Old Files (2021)/321 & 322/Data/Modeling/"
df = pd.read_excel (directory+"ForecastData321.xlsx")
#print(df.head(1))

AL = df.loc[df['state'] == "AL"]
AR = df.loc[df['state'] == "AR"]
ME = df.loc[df['state'] == "ME"]
MS = df.loc[df['state'] == "MS"]
OR = df.loc[df['state'] == "OR"]
WI = df.loc[df['state'] == "WI"]

x = AL['time']



################################ Employment ###################################

eAL = AL['employ']
eAR = AR['employ']
eME = ME['employ']
eMS = MS['employ']
eOR = OR['employ']
eWI = WI['employ']
feAL = AL['f_employ']
feAR = AR['f_employ']
feME = ME['f_employ']
feMS = MS['f_employ']
feOR = OR['f_employ']
feWI = WI['f_employ']
rcfeAL = AL['rcf_employ']
rcfeAR = AR['rcf_employ']
rcfeME = ME['rcf_employ']
rcfeMS = MS['rcf_employ']
rcfeOR = OR['rcf_employ']
rcfeWI = WI['rcf_employ']

###############################
# Data Graph
###############################

import seaborn as sns

sns.set_style('whitegrid')
fig, ax1 = plt.subplots()
#fig.suptitle('Employment',x=.55,y=1.02)
#plt.ylim(top=12)

ax1.set_title('Employment')
ax1.plot(x, eAL, 'b', label='Alabama',linewidth=1)
ax1.plot(x, eAR, 'y', label='Arkansas',linewidth=1)
ax1.plot(x, eME, 'g', label='Maine',linewidth=1)
ax1.plot(x, eMS, 'c', label='Mississippi',linewidth=1)
ax1.plot(x, eOR, 'm', label='Oregon',linewidth=1)
ax1.plot(x, eWI, 'k', label='Wisconsin',linewidth=1)

ax1.set(ylabel='N')
ax1.set(xlabel='Time')
ax1.set_xticks(x[::8])
ax1.set_xticklabels(x[::8],rotation=60,ha="center",fontsize=11)

fig.legend(frameon=True, shadow=True,facecolor="white")
fig.tight_layout()
fig.savefig(directory+'321employData.png', dpi=1200)

###############################
# Forecast Graph
###############################
sns.set_style('whitegrid')
fig, ax1 = plt.subplots()
#fig.suptitle('Employment',x=.55,y=1.02)
#plt.ylim(top=12)

ax1.set_title('Employment')
ax1.plot(x, eAL, 'b', label='Alabama',linewidth=1)
ax1.plot(x, feAL, '--b', linewidth=1)
ax1.plot(x, eAR, 'y', label='Arkansas',linewidth=1)
ax1.plot(x, feAR, '--y', linewidth=1)
ax1.plot(x, eME, 'g', label='Maine',linewidth=1)
ax1.plot(x, feME, '--g', linewidth=1)
ax1.plot(x, eMS, 'c', label='Mississippi',linewidth=1)
ax1.plot(x, feMS, '--c', linewidth=1)
ax1.plot(x, eOR, 'm', label='Oregon',linewidth=1)
ax1.plot(x, feOR, '--m', linewidth=1)
ax1.plot(x, eWI, 'k', label='Wisconsin',linewidth=1)
ax1.plot(x, feWI, '--k', label='Wisconsin',linewidth=1)

ax1.set(ylabel='N')
ax1.set(xlabel='Time')
ax1.set_xticks(x[::8])
ax1.set_xticklabels(x[::8],rotation=60,ha="center",fontsize=11)

fig.legend(frameon=True, shadow=True,facecolor="white")
fig.tight_layout()
fig.savefig(directory+'321employForecast.png', dpi=1200)

##################################
# Forecast Robustness Check Graph
##################################
sns.set_style('whitegrid')
fig, ax1 = plt.subplots()
#fig.suptitle('Employment',x=.55,y=1.02)
#plt.ylim(top=12)

ax1.set_title('Employment Forecast Check')
ax1.plot(x, eAL, 'b', label='Alabama',linewidth=1)
ax1.plot(x, rcfeAL, '--b', linewidth=1)
ax1.plot(x, eAR, 'y', label='Arkansas',linewidth=1)
ax1.plot(x, rcfeAR, '--y', linewidth=1)
ax1.plot(x, eME, 'g', label='Maine',linewidth=1)
ax1.plot(x, rcfeME, '--g', linewidth=1)
ax1.plot(x, eMS, 'c', label='Mississippi',linewidth=1)
ax1.plot(x, rcfeMS, '--c', linewidth=1)
ax1.plot(x, eOR, 'm', label='Oregon',linewidth=1)
ax1.plot(x, rcfeOR, '--m', linewidth=1)
ax1.plot(x, eWI, 'k', label='Wisconsin',linewidth=1)
ax1.plot(x, rcfeWI, '--k', label='Forecast',linewidth=1)

ax1.set(ylabel='N')
ax1.set(xlabel='Time')
ax1.set_xticks(x[::8])
ax1.set_xticklabels(x[::8],rotation=60,ha="center",fontsize=11)

fig.legend(frameon=True, shadow=True,facecolor="white")
fig.tight_layout()
fig.savefig(directory+'321employRC.png', dpi=1200)



################################ Output ###################################

oAL = AL['output']
oAR = AR['output']
oME = ME['output']
oMS = MS['output']
oOR = OR['output']
oWI = WI['output']
foAL = AL['f_output']
foAR = AR['f_output']
foME = ME['f_output']
foMS = MS['f_output']
foOR = OR['f_output']
foWI = WI['f_output']
rcfoAL = AL['rcf_output']
rcfoAR = AR['rcf_output']
rcfoME = ME['rcf_output']
rcfoMS = MS['rcf_output']
rcfoOR = OR['rcf_output']
rcfoWI = WI['rcf_output']

###############################
# Data Graph
###############################

sns.set_style('whitegrid')
fig, ax1 = plt.subplots()
#fig.suptitle('Output',x=.55,y=1.02)
#plt.ylim(top=12)

ax1.set_title('Output')
ax1.plot(x, oAL, 'b', label='Alabama',linewidth=1)
ax1.plot(x, oAR, 'y', label='Arkansas',linewidth=1)
ax1.plot(x, oME, 'g', label='Maine',linewidth=1)
ax1.plot(x, oMS, 'c', label='Mississippi',linewidth=1)
ax1.plot(x, oOR, 'm', label='Oregon',linewidth=1)
ax1.plot(x, oWI, 'k', label='Wisconsin',linewidth=1)

ax1.set(ylabel='Millions')
ax1.set(xlabel='Time')
ax1.set_xticks(x[::8])
ax1.set_xticklabels(x[::8],rotation=60,ha="center",fontsize=11)

fig.legend(frameon=True, shadow=True,facecolor="white")
fig.tight_layout()
plt.savefig(directory+'321outputData.png', dpi=1200)

###############################
# Forecast Graph
###############################
sns.set_style('whitegrid')
fig, ax1 = plt.subplots()
#fig.suptitle('Output',x=.55,y=1.02)
#plt.ylim(top=12)

ax1.set_title('Output')
ax1.plot(x, oAL, 'b', label='Alabama',linewidth=1)
ax1.plot(x, foAL, '--b', linewidth=1)
ax1.plot(x, oAR, 'y', label='Arkansas',linewidth=1)
ax1.plot(x, foAR, '--y', linewidth=1)
ax1.plot(x, oME, 'g', label='Maine',linewidth=1)
ax1.plot(x, foME, '--g', linewidth=1)
ax1.plot(x, oMS, 'c', label='Mississippi',linewidth=1)
ax1.plot(x, foMS, '--c', linewidth=1)
ax1.plot(x, oOR, 'm', label='Oregon',linewidth=1)
ax1.plot(x, foOR, '--m', linewidth=1)
ax1.plot(x, oWI, 'k', label='Wisconsin',linewidth=1)
ax1.plot(x, foWI, '--k', label='Forecast',linewidth=1)

ax1.set(ylabel='Millions')
ax1.set(xlabel='Time')
ax1.set_xticks(x[::8])
ax1.set_xticklabels(x[::8],rotation=60,ha="center",fontsize=11)

fig.legend(frameon=True, shadow=True,facecolor="white")
fig.tight_layout()
plt.savefig(directory+'321outputForecast.png', dpi=1200)

##################################
# Forecast Robustness Check Graph
##################################
sns.set_style('whitegrid')
fig, ax1 = plt.subplots()
#fig.suptitle('Output',x=.55,y=1.02)
#plt.ylim(top=12)

ax1.set_title('Output Forecast Check')
ax1.plot(x, oAL, 'b', label='Alabama',linewidth=1)
ax1.plot(x, rcfoAL, '--b', linewidth=1)
ax1.plot(x, oAR, 'y', label='Arkansas',linewidth=1)
ax1.plot(x, rcfoAR, '--y', linewidth=1)
ax1.plot(x, oME, 'g', label='Maine',linewidth=1)
ax1.plot(x, rcfoME, '--g', linewidth=1)
ax1.plot(x, oMS, 'c', label='Mississippi',linewidth=1)
ax1.plot(x, rcfoMS, '--c', linewidth=1)
ax1.plot(x, oOR, 'm', label='Oregon',linewidth=1)
ax1.plot(x, rcfoOR, '--m', linewidth=1)
ax1.plot(x, oWI, 'k', label='Wisconsin',linewidth=1)
ax1.plot(x, rcfoWI, '--k', label='Forecast',linewidth=1)

ax1.set(ylabel='Millions')
ax1.set(xlabel='Time')
ax1.set_xticks(x[::8])
ax1.set_xticklabels(x[::8],rotation=60,ha="center",fontsize=11)

fig.legend(frameon=True, shadow=True,facecolor="white")
fig.tight_layout()
plt.savefig(directory+'321outputRC.png', dpi=1200)



################################ Wage ###################################

wAL = AL['wage']/1000
wAR = AR['wage']/1000
wME = ME['wage']/1000
wMS = MS['wage']/1000
wOR = OR['wage']/1000
wWI = WI['wage']/1000
fwAL = AL['f_wage']/1000
fwAR = AR['f_wage']/1000
fwME = ME['f_wage']/1000
fwMS = MS['f_wage']/1000
fwOR = OR['f_wage']/1000
fwWI = WI['f_wage']/1000
rcfwAL = AL['rcf_wage']/1000
rcfwAR = AR['rcf_wage']/1000
rcfwME = ME['rcf_wage']/1000
rcfwMS = MS['rcf_wage']/1000
rcfwOR = OR['rcf_wage']/1000
rcfwWI = WI['rcf_wage']/1000

###############################
# Data Graph
###############################

sns.set_style('whitegrid')
fig, ax1 = plt.subplots()
#fig.suptitle('Wage',x=.55,y=1.02)
#plt.ylim(top=12)

ax1.set_title('Total Wage')
ax1.plot(x, wAL, 'b', label='Alabama',linewidth=1)
ax1.plot(x, wAR, 'y', label='Arkansas',linewidth=1)
ax1.plot(x, wME, 'g', label='Maine',linewidth=1)
ax1.plot(x, wMS, 'c', label='Mississippi',linewidth=1)
ax1.plot(x, wOR, 'm', label='Oregon',linewidth=1)
ax1.plot(x, wWI, 'k', label='Wisconsin',linewidth=1)

ax1.set(ylabel='Millions')
ax1.set(xlabel='Time')
ax1.set_xticks(x[::8])
ax1.set_xticklabels(x[::8],rotation=60,ha="center",fontsize=11)

fig.legend(frameon=True, shadow=True,facecolor="white")
fig.tight_layout()
plt.savefig(directory+'321wageData.png', dpi=1200)

###############################
# Forecast Graph
###############################
sns.set_style('whitegrid')
fig, ax1 = plt.subplots()
#fig.suptitle('Wage',x=.55,y=1.02)
#plt.ylim(top=12)

ax1.set_title('Total Wage')
ax1.plot(x, wAL, 'b', label='Alabama',linewidth=1)
ax1.plot(x, fwAL, '--b', linewidth=1)
ax1.plot(x, wAR, 'y', label='Arkansas',linewidth=1)
ax1.plot(x, fwAR, '--y', linewidth=1)
ax1.plot(x, wME, 'g', label='Maine',linewidth=1)
ax1.plot(x, fwME, '--g', linewidth=1)
ax1.plot(x, wMS, 'c', label='Mississippi',linewidth=1)
ax1.plot(x, fwMS, '--c', linewidth=1)
ax1.plot(x, wOR, 'm', label='Oregon',linewidth=1)
ax1.plot(x, fwOR, '--m', linewidth=1)
ax1.plot(x, wWI, 'k', label='Wisconsin',linewidth=1)
ax1.plot(x, fwWI, '--k', label='Forecast',linewidth=1)

ax1.set(ylabel='Millions')
ax1.set(xlabel='Time')
ax1.set_xticks(x[::8])
ax1.set_xticklabels(x[::8],rotation=60,ha="center",fontsize=11)

fig.legend(frameon=True, shadow=True,facecolor="white")
fig.tight_layout()
plt.savefig(directory+'321wageForecast.png', dpi=1200)

##################################
# Forecast Robustness Check Graph
##################################
sns.set_style('whitegrid')
fig, ax1 = plt.subplots()
#fig.suptitle('Wage',x=.55,y=1.02)
#plt.ylim(top=12)

ax1.set_title('Wage Forecast Check')
ax1.plot(x, wAL, 'b', label='Alabama',linewidth=1)
ax1.plot(x, rcfwAL, '--b', linewidth=1)
ax1.plot(x, wAR, 'y', label='Arkansas',linewidth=1)
ax1.plot(x, rcfwAR, '--y', linewidth=1)
ax1.plot(x, wME, 'g', label='Maine',linewidth=1)
ax1.plot(x, rcfwME, '--g', linewidth=1)
ax1.plot(x, wMS, 'c', label='Mississippi',linewidth=1)
ax1.plot(x, rcfwMS, '--c', linewidth=1)
ax1.plot(x, wOR, 'm', label='Oregon',linewidth=1)
ax1.plot(x, rcfwOR, '--m', linewidth=1)
ax1.plot(x, wWI, 'k', label='Wisconsin',linewidth=1)
ax1.plot(x, rcfwWI, '--k', label='Forecast',linewidth=1)

ax1.set(ylabel='Millions')
ax1.set(xlabel='Time')
ax1.set_xticks(x[::8])
ax1.set_xticklabels(x[::8],rotation=60,ha="center",fontsize=11)

fig.legend(frameon=True, shadow=True,facecolor="white")
fig.tight_layout()
plt.savefig(directory+'321wageRC.png', dpi=1200)



################################ # of Firms ###################################

nAL = AL['numfirm']
nAR = AR['numfirm']
nME = ME['numfirm']
nMS = MS['numfirm']
nOR = OR['numfirm']
nWI = WI['numfirm']
fnAL = AL['f_numfirm']
fnAR = AR['f_numfirm']
fnME = ME['f_numfirm']
fnMS = MS['f_numfirm']
fnOR = OR['f_numfirm']
fnWI = WI['f_numfirm']
rcfnAL = AL['rcf_numfirm']
rcfnAR = AR['rcf_numfirm']
rcfnME = ME['rcf_numfirm']
rcfnMS = MS['rcf_numfirm']
rcfnOR = OR['rcf_numfirm']
rcfnWI = WI['rcf_numfirm']

###############################
# Data Graph
###############################

sns.set_style('whitegrid')
fig, ax1 = plt.subplots()
#fig.suptitle('Number of Firms',x=.55,y=1.02)
#plt.ylim(top=12)

ax1.set_title('Number of Firms')
ax1.plot(x, nAL, 'b', label='Alabama',linewidth=1)
ax1.plot(x, nAR, 'y', label='Arkansas',linewidth=1)
ax1.plot(x, nME, 'g', label='Maine',linewidth=1)
ax1.plot(x, nMS, 'c', label='Mississippi',linewidth=1)
ax1.plot(x, nOR, 'm', label='Oregon',linewidth=1)
ax1.plot(x, nWI, 'k', label='Wisconsin',linewidth=1)

ax1.set(ylabel='N')
ax1.set(xlabel='Time')
ax1.set_xticks(x[::8])
ax1.set_xticklabels(x[::8],rotation=60,ha="center",fontsize=11)

fig.legend(frameon=True, shadow=True,facecolor="white")
fig.tight_layout()
plt.savefig(directory+'321numfirmData.png', dpi=1200)

###############################
# Forecast Graph
###############################
sns.set_style('whitegrid')
fig, ax1 = plt.subplots()
#fig.suptitle('Number of Firms',x=.55,y=1.02)
#plt.ylim(top=12)

ax1.set_title('Number of Firms')
ax1.plot(x, nAL, 'b', label='Alabama',linewidth=1)
ax1.plot(x, fnAL, '--b', linewidth=1)
ax1.plot(x, nAR, 'y', label='Arkansas',linewidth=1)
ax1.plot(x, fnAR, '--y', linewidth=1)
ax1.plot(x, nME, 'g', label='Maine',linewidth=1)
ax1.plot(x, fnME, '--g', linewidth=1)
ax1.plot(x, nMS, 'c', label='Mississippi',linewidth=1)
ax1.plot(x, fnMS, '--c', linewidth=1)
ax1.plot(x, nOR, 'm', label='Oregon',linewidth=1)
ax1.plot(x, fnOR, '--m', linewidth=1)
ax1.plot(x, nWI, 'k', label='Wisconsin',linewidth=1)
ax1.plot(x, fnWI, '--k', label='Forecast',linewidth=1)

ax1.set(ylabel='N')
ax1.set(xlabel='Time')
ax1.set_xticks(x[::8])
ax1.set_xticklabels(x[::8],rotation=60,ha="center",fontsize=11)

fig.legend(frameon=True, shadow=True,facecolor="white")
fig.tight_layout()
plt.savefig(directory+'321numfirmForecast.png', dpi=1200)

##################################
# Forecast Robustness Check Graph
##################################
sns.set_style('whitegrid')
fig, ax1 = plt.subplots()
#fig.suptitle('Number of Firms',x=.55,y=1.02)
#plt.ylim(top=12)

ax1.set_title('Number of Firms Forecast Check')
ax1.plot(x, nAL, 'b', label='Alabama',linewidth=1)
ax1.plot(x, rcfnAL, '--b', linewidth=1)
ax1.plot(x, nAR, 'y', label='Arkansas',linewidth=1)
ax1.plot(x, rcfnAR, '--y', linewidth=1)
ax1.plot(x, nME, 'g', label='Maine',linewidth=1)
ax1.plot(x, rcfnME, '--g', linewidth=1)
ax1.plot(x, nMS, 'c', label='Mississippi',linewidth=1)
ax1.plot(x, rcfnMS, '--c', linewidth=1)
ax1.plot(x, nOR, 'm', label='Oregon',linewidth=1)
ax1.plot(x, rcfnOR, '--m', linewidth=1)
ax1.plot(x, nWI, 'k', label='Wisconsin',linewidth=1)
ax1.plot(x, rcfnWI, '--k', label='Forecast',linewidth=1)

ax1.set(ylabel='N')
ax1.set(xlabel='Time')
ax1.set_xticks(x[::8])
ax1.set_xticklabels(x[::8],rotation=60,ha="center",fontsize=11)

fig.legend(frameon=True, shadow=True,facecolor="white")
fig.tight_layout()
plt.savefig(directory+'321numfirmRC.png', dpi=1200)
