# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 07:57:32 2016

@author: areed145
"""

import pandas as pd
import matplotlib.pyplot as plt
import glob
import time

directory = '/Users/areed145/Dropbox/Apps/OBDLink/CsvLogs/'
car = '1C4RJFBG7EC482134'
sleeptime = 30

rpm_x = ' Engine RPM (RPM)'
rpm_y1 = ' Vehicle speed (MPH)'
rpm_y2 = ' Mass air flow rate (lb/min)'
rpm_y3 = ' Intake manifold absolute pressure (inHg)'
rpm_y4 = ' Instant fuel economy (MPG)'

spd_x = ' Vehicle speed (MPH)'
spd_y1 = ' Absolute load value (%)'
spd_y2 = ' Mass air flow rate (lb/min)'
spd_y3 = ' Intake manifold absolute pressure (inHg)'
spd_y4 = ' Instant fuel economy (MPG)'

props = {}
props['01mov'] = [' Vehicle speed (MPH)', ' Acceleration (ft/s²)']
props['02eng'] = [' Engine RPM (RPM)', ' Ignition timing advance for #1 cylinder (deg)']
props['03rate'] = [' Fuel rate (gal/hr)', ' Mass air flow rate (lb/min)']
props['04rate'] = [' Instant fuel economy (MPG)',' Fuel level input (%)']
props['05pres'] = [' Intake manifold absolute pressure (inHg)', ' Barometric pressure (inHg)']
props['06pres'] = [' Evap system vapor pressure (inH2O)', ' Boost (psi)']
props['07temp'] = [' Engine coolant temperature (F)', ' Intake air temperature (F)']
props['08temp'] = [' Ambient air temperature (F)', ' Engine oil temperature (F)']
props['09ratio'] = [' Relative throttle position (%)', ' Absolute throttle position (%)']
props['10ratio'] = [' Calculated load value (%)', ' Absolute load value (%)']
props['11volt'] = [' O2 voltage (Bank 1  Sensor 1) (V)', ' O2 voltage (Bank 1  Sensor 2) (V)']
props['12volt'] = [' O2 voltage (Bank 2  Sensor 1) (V)', ' O2 voltage (Bank 2  Sensor 2) (V)']

gps = {}
gps['01gps'] = [' Altitude (m)', ' Bearing (deg)']
gps['02gps'] = [' GPS Speed (m/s)', ' GPS Accuracy (m)']
gps['03loc'] = [' Latitude', ' Longitude']

lims = {}
lims[' Vehicle speed (MPH)'] = {'min':0, 'max':100, 'color':'orangered'}
lims[' Acceleration (ft/s²)']= {'min':-20, 'max':20, 'color':'gold'}
lims[' Engine RPM (RPM)']= {'min':0, 'max':5000, 'color':'deeppink'}
lims[' Ignition timing advance for #1 cylinder (deg)']= {'min':-20, 'max':60, 'color':'forestgreen'}
lims[' Fuel rate (gal/hr)']= {'min':0, 'max':10, 'color':'orange'}
lims[' Mass air flow rate (lb/min)']= {'min':0, 'max':10, 'color':'deepskyblue'}
lims[' Instant fuel economy (MPG)']= {'min':0, 'max':100, 'color':'dodgerblue'}
lims[' Fuel level input (%)']= {'min':0, 'max':100, 'color':'red'}
lims[' Intake manifold absolute pressure (inHg)']= {'min':0, 'max':40, 'color':'yellowgreen'}
lims[' Barometric pressure (inHg)']= {'min':0, 'max':40, 'color':'seagreen'}
lims[' Evap system vapor pressure (inH2O)']= {'min':0, 'max':3, 'color':'pink'}
lims[' Boost (psi)']= {'min':-15, 'max':0, 'color':'yellow'}
lims[' Engine coolant temperature (F)']= {'min':None, 'max':None, 'color':'tomato'}
lims[' Intake air temperature (F)']= {'min':None, 'max':None, 'color':'mediumorchid'}
lims[' Ambient air temperature (F)']= {'min':None, 'max':None, 'color':'lawngreen'}
lims[' Engine oil temperature (F)']= {'min':None, 'max':None, 'color':'slateblue'}
lims[' Relative throttle position (%)']= {'min':0, 'max':100, 'color':'coral'}
lims[' Absolute throttle position (%)']= {'min':0, 'max':100, 'color':'goldenrod'}
lims[' Calculated load value (%)']= {'min':0, 'max':100, 'color':'steelblue'}
lims[' Absolute load value (%)']= {'min':0, 'max':100, 'color':'mediumseagreen'}
lims[' O2 voltage (Bank 1  Sensor 1) (V)']= {'min':0, 'max':1, 'color':'darkorange'}
lims[' O2 voltage (Bank 1  Sensor 2) (V)']= {'min':0, 'max':1, 'color':'mediumvioletred'}
lims[' O2 voltage (Bank 2  Sensor 1) (V)']= {'min':0, 'max':1, 'color':'blueviolet'}
lims[' O2 voltage (Bank 2  Sensor 2) (V)']= {'min':0, 'max':1, 'color':'khaki'}
lims[' Altitude (m)']= {'min':None, 'max':None, 'color':'crimson'}
lims[' Bearing (deg)']= {'min':0, 'max':360, 'color':'greenyellow'}
lims[' GPS Speed (m/s)']= {'min':None, 'max':None, 'color':'chartreuse'}
lims[' GPS Accuracy (m)']= {'min':None, 'max':None, 'color':'darkmagenta'}
lims[' Latitude']= {'min':None, 'max':None, 'color':'fuchsia'}
lims[' Longitude']= {'min':None, 'max':None, 'color':'magenta'}

while 1<2:
    filenames = glob.glob(directory+car+'/*.csv')
    for filepath in filenames:
        try:
            file = filepath[len(directory+car)+1:][:22]
            log = pd.read_csv(filepath, skiprows=1)
            log.index = pd.to_datetime(log.Time)
            
            cats = props.keys()
            cat_len = len(cats)
            
            plt.close("all")
            fig = plt.figure()
            fig.set_size_inches(15, 20)
            fig.suptitle(car+' - '+file+' combo')
            for idx_cat, cat in enumerate(sorted(cats)):
                ax = plt.subplot(cat_len, 1, idx_cat+1)
                ax.set_axisbelow(True)
                ax.spines['top'].set_visible(True)
                try:
                    ax.plot_date(log.index,
                                  log[props[cat][0]],
                                  marker='',
                                  color=lims[props[cat][0]]['color'],
                                  linestyle='-',
                                  linewidth=1)
                except:
                    pass        
                ax.set_ylim([lims[props[cat][0]]['min'],lims[props[cat][0]]['max']])          
                ax.set_ylabel(props[cat][0])
                ax.yaxis.label.set_color(lims[props[cat][0]]['color'])
                ax.grid(b=True, which='major', color='k', linestyle='-')
                if len(props[cat]) > 1:
                    for idx_prop in range(1,len(props[cat])):
                        ax_sub = ax.twinx()
                        try:
                            ax_sub.plot_date(log.index,
                                           log[props[cat][idx_prop]],
                                           marker='',
                                           color=lims[props[cat][idx_prop]]['color'],
                                           linestyle='-',
                                           linewidth=1)
                        except:
                            pass
                        ax_sub.set_ylim([lims[props[cat][idx_prop]]['min'],lims[props[cat][idx_prop]]['max']])
                        ax_sub.set_ylabel(props[cat][idx_prop])
                        ax_sub.yaxis.label.set_color(lims[props[cat][idx_prop]]['color'])
                        
            fig.savefig(directory+car+'/'+file+'_combo.png')
            
            cats = gps.keys()
            
            plt.close("all")
            fig = plt.figure()
            fig.set_size_inches(10, 10)
            fig.suptitle(car+' - '+file+' gps')
            ax_map = plt.subplot2grid((4,1), (0,0), rowspan=2)
            ax_alt = plt.subplot2grid((4,1), (2,0))
            ax_gps = plt.subplot2grid((4,1), (3,0))
            
            ax_map.plot(log[gps['03loc'][1]],
                           log[gps['03loc'][0]],
                           marker='',
                           color='orangered',
                           linestyle='-',
                           linewidth=1)
                           
            ax_alt.plot_date(log.index,
                           log[gps['01gps'][0]],
                           marker='',
                           color=lims[gps['01gps'][0]]['color'],
                           linestyle='-',
                           linewidth=1)
            ax_altsub = ax_alt.twinx()
            ax_altsub.plot_date(log.index,
                           log[gps['01gps'][1]],
                           marker='',
                           color=lims[gps['01gps'][1]]['color'],
                           linestyle='-',
                           linewidth=1)
                           
            ax_gps.plot_date(log.index,
                           log[gps['02gps'][0]],
                           marker='',
                           color=lims[gps['02gps'][0]]['color'],
                           linestyle='-',
                           linewidth=1)
            ax_gpssub = ax_gps.twinx()
            ax_gpssub.plot_date(log.index,
                           log[gps['02gps'][1]],
                           marker='',
                           color=lims[gps['02gps'][1]]['color'],
                           linestyle='-',
                           linewidth=1)
            
            fig.savefig(directory+car+'/'+file+'_gps.png')
            
            plt.close("all")
            fig = plt.figure()
            fig.set_size_inches(10, 10)
            fig.suptitle(car+' - '+file+' rpm')
            ax1 = plt.subplot(2,2,1)
            ax1.scatter(log[rpm_x],
                           log[rpm_y1],
                           marker='+',
                           color=lims[rpm_y1]['color'])
            ax1.set_xlim([lims[rpm_x]['min'],lims[rpm_x]['max']])
            ax1.set_ylim([lims[rpm_y1]['min'],lims[rpm_y1]['max']])
            ax1.set_ylabel(rpm_y1)
            ax1.yaxis.label.set_color(lims[rpm_y1]['color'])               
            
            ax2 = plt.subplot(2,2,2)
            ax2.scatter(log[rpm_x],
                           log[rpm_y2],
                           marker='+',
                           color=lims[rpm_y2]['color'])
            ax2.set_xlim([lims[rpm_x]['min'],lims[rpm_x]['max']])
            ax2.set_ylim([lims[rpm_y2]['min'],lims[rpm_y2]['max']])
            ax2.set_ylabel(rpm_y2)
            ax2.yaxis.label.set_color(lims[rpm_y2]['color'])               
            
            ax3 = plt.subplot(2,2,3)
            ax3.scatter(log[rpm_x],
                           log[rpm_y3],
                           marker='+',
                           color=lims[rpm_y3]['color'])
            ax3.set_xlim([lims[rpm_x]['min'],lims[rpm_x]['max']])
            ax3.set_ylim([lims[rpm_y3]['min'],lims[rpm_y3]['max']])
            ax3.set_ylabel(rpm_y3)
            ax3.yaxis.label.set_color(lims[rpm_y3]['color'])               
                           
            ax4 = plt.subplot(2,2,4)
            ax4.scatter(log[rpm_x],
                           log[rpm_y4],
                           marker='+',
                           color=lims[rpm_y4]['color'])
            ax4.set_xlim([lims[rpm_x]['min'],lims[rpm_x]['max']])
            ax4.set_ylim([lims[rpm_y4]['min'],lims[rpm_y4]['max']])
            ax4.set_ylabel(rpm_y4)
            ax4.yaxis.label.set_color(lims[rpm_y4]['color'])               
            
            ax1.grid(b=True, which='major', color='k', linestyle='-')
            ax2.grid(b=True, which='major', color='k', linestyle='-')
            ax3.grid(b=True, which='major', color='k', linestyle='-')
            ax4.grid(b=True, which='major', color='k', linestyle='-')                          
            
            fig.savefig(directory+car+'/'+file+'_rpm.png')
            
            plt.close("all")
            fig = plt.figure()
            fig.set_size_inches(10, 10)
            fig.suptitle(car+' - '+file+' spd')
            ax1 = plt.subplot(2,2,1)
            ax1.scatter(log[spd_x],
                           log[spd_y1],
                           marker='+',
                           color=lims[spd_y1]['color'])
            ax1.set_xlim([lims[spd_x]['min'],lims[spd_x]['max']])
            ax1.set_ylim([lims[spd_y1]['min'],lims[spd_y1]['max']])
            ax1.set_ylabel(spd_y1)
            ax1.yaxis.label.set_color(lims[spd_y1]['color'])               
            
            ax2 = plt.subplot(2,2,2)
            ax2.scatter(log[spd_x],
                           log[spd_y2],
                           marker='+',
                           color=lims[spd_y2]['color'])
            ax2.set_xlim([lims[spd_x]['min'],lims[spd_x]['max']])
            ax2.set_ylim([lims[spd_y2]['min'],lims[spd_y2]['max']])
            ax2.set_ylabel(spd_y2)
            ax2.yaxis.label.set_color(lims[spd_y2]['color'])               
            
            ax3 = plt.subplot(2,2,3)
            ax3.scatter(log[spd_x],
                           log[spd_y3],
                           marker='+',
                           color=lims[spd_y3]['color'])
            ax3.set_xlim([lims[spd_x]['min'],lims[spd_x]['max']])
            ax3.set_ylim([lims[spd_y3]['min'],lims[spd_y3]['max']])
            ax3.set_ylabel(spd_y3)
            ax3.yaxis.label.set_color(lims[spd_y3]['color'])               
                           
            ax4 = plt.subplot(2,2,4)
            ax4.scatter(log[spd_x],
                           log[spd_y4],
                           marker='+',
                           color=lims[spd_y4]['color'])
            ax4.set_xlim([lims[spd_x]['min'],lims[spd_x]['max']])
            ax4.set_ylim([lims[spd_y4]['min'],lims[spd_y4]['max']])
            ax4.set_ylabel(spd_y4)
            ax4.yaxis.label.set_color(lims[spd_y4]['color'])               
            
            ax1.grid(b=True, which='major', color='k', linestyle='-')
            ax2.grid(b=True, which='major', color='k', linestyle='-')
            ax3.grid(b=True, which='major', color='k', linestyle='-')
            ax4.grid(b=True, which='major', color='k', linestyle='-')                          
            
            fig.savefig(directory+car+'/'+file+'_spd.png')
        except:
            pass
        
    time.sleep(60*sleeptime)
                       