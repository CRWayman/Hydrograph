# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:16:31 2019

@author: Callum Wayman

Example of a hydrograph showing nearby precipitation and discharge for a given stream

Datasets: USGS mean daily discharge for Juniata River in Huntington PA, converted from cubic feet per second to 
cubic meters per second. Precipitation from the National Atmospheric Deposition Program (NADP) Leading Ridge 
site in Huntington County PA. Precipitation is converted from inches to mm of precip collected per day.

"""

#%%
#Package Import

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.dates as mdates

#%%
#File Input and Data Frame/Array Creation

'''Selecting the file from the correct path and creating a pandas dataframe from the excel file'''

user = 'Callum Wayman'

precip_filename = 'LeadingRidgePrecip.xlsx'
q_filename = 'Juniata_Discharge.xlsx'

precip_file = pd.ExcelFile(os.getcwd() + '\\' + precip_filename, sheetname = 'Data')
q_file = pd.ExcelFile(os.getcwd() + '\\' + q_filename, sheetname = 'Data')

precip = pd.DataFrame(pd.read_excel(precip_file))
q = pd.DataFrame(pd.read_excel(q_file))

'''Creating date and data arrays for precipitation and discharge'''
precip_arr = np.array(precip.loc[:,'Precipitation (mm)'])
precip_dates = np.array(precip.loc[:,'Date'])

q_arr = np.array(q.loc[:,'Discharge (cms)'])
q_dates = np.array(q.loc[:,'Date'])

months = mdates.MonthLocator()
years = mdates.YearLocator()

#%% Plots
'''Create a hydrograph plot of precipitation and discharge'''


plt.close('all')

fst = 20
fsa = 20
fsT = 25

datemin = pd.to_datetime('01/01/2017')
datemax = pd.to_datetime('12/31/2017')

plt.figure(figsize=[12,6])
host = host_subplot(111, axes_class=AA.Axes)
par1 = host.twinx()

p1 = host.plot(q_dates, q_arr,color='b')
p2 = par1.bar(precip_dates,precip_arr,color='k',width=1.5)
par1.invert_yaxis()

host.set_xlim(datemin,datemax)
host.set_ylim(0, 250)
par1.set_ylim(100, 0)

host.set_ylabel("Discharge (cms)",fontsize = fsa)
par1.set_ylabel("Precipitation (cm)",fontsize = fsa)
host.set_xlabel('Date', fontsize = fsa)
plt.title('Hydrograph for Juniata River (2017)',fontsize = fsT)

monthsFmt = mdates.DateFormatter('%b-%Y')
yearsFmt = mdates.DateFormatter('\n%Y')

#host.xaxis.set_minor_locator(years)
host.xaxis.set_major_locator(months)
host.xaxis.set_major_formatter(monthsFmt)
#host.xaxis.set_minor_formatter(yearsFmt)
host.set_xlim(datemin, datemax)
host.tick_params(axis='both',direction = 'in',labelsize = fst)

plt.tight_layout()

