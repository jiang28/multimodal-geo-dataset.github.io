import pygrib as pg
import pandas as pd
import numpy as np
import csv
import datetime as dt
import matplotlib.pyplot as plt
from statistics import mean
import seaborn as sns
import matplotlib


#grbs = pg.open('MRMS_RadarOnly_QPE_01H_00.00_20220903-020000.grib2')


grbs = pg.open('test1.grib2')
#grb = grbs.read(1)[0]

#grbs.seek(0)
#for grb in grbs:
    #print('grb: ', grb)

#select specific feature
#grb = grbs.select(name='Total precipitation')[0]
#maxt = grb.values
#print(maxt.shape, maxt.min(), maxt.max())



#var_name = "PrecipRate_P0_L102_GLL0"
#var = grbs.variables[var_name][:]

#grb = grbs.select(name='PrecipRate_P0_L102_GLL0')[0]
#data=grb.values
#lat,lon = grb.latlons()


#grbs.seek(0)
#grb = grbs.select(name = 'PrecipRate')[0]
#value = grb.values

#data = pd.DataFrame(value)
#data.to_csv('test.csv', index = False, header = False)
#lats, lons = grb.latlons()
output_list = []
lat_list = []
lon_list = []
latlon_list = []
#for i in range(lats.shape[0]):
    #zip1 = zip(lats[i], lons[i])
    #output_list.append(list(zip1))

#output = pd.DataFrame(output_list)

keys = []
values = []
for grb in grbs:
    print(grb)
    #print(grb.values)
    lat,lon = grb.latlons()
    lon_list.append(lon)

    latlon = [lat,lon]
    latlon_list.append(latlon)
    #print(grb.keys())
    #keys.append(grb.keys())
    values.append(grb.values)
    #keys.append(grb)
    #print(grb.values)
#grb = grbs.data()[0]
temp_max = max(values)

#print("max: ", max(values[0][500]))
#print("mean: ", mean(values[0][0]))
#print("shape: ", values[0].shape)

#print(lat_list)

latlon_arr = np.array(lon_list)
latlon_arr_2d = np.squeeze(latlon_arr)

latlon_arr_2d_crop = latlon_arr_2d[2400:3000, 4600:5000]

#print(latlon_arr_2d_crop.shape)
#print(latlon_arr_2d_crop)

###########################################################

num_arr = np.array(values)
num_arr_2d = np.squeeze(num_arr)

num_arr_2d_crop = num_arr_2d = num_arr_2d[2400:3000, 4600:5000]

#print(num_arr_2d_crop.shape)
#print(num_arr_2d_crop)

print("max: ", np.amax(num_arr_2d_crop))

np.save('PrecipRate_00.00_20220923-000000', num_arr_2d_crop)
####################################
lat_arr = np.array(lat_list)
lat_arr_2d = np.squeeze(lat_arr)
#print(lat_arr_2d.shape)
#print(lat_arr_2d)
df = pd.DataFrame(lat_arr_2d)

#array to df
arr = np.array(values)
arr_2d = np.squeeze(arr)
#print("shape: ", arr.shape)
#print("shape_2d: ", arr_2d.shape)
#arr.reshape((3500,7000))
df = pd.DataFrame(num_arr_2d_crop)
#print(df)
##################heatmap plot##############################################
#sns.heatmap(df, cmap ='RdYlGn', linewidths = 0.30, annot = True)

#set figure size
#fig = matplotlib.pyplot.gcf()
#fig.set_size_inches(13.5, 10.5)

#fig.savefig("heatmap.png",bbox_inches='tight')
#plt.show()


#################################################################
#df.to_csv('mrms_prep_values.csv', index = False, header = False)


#arr_2d.tofile('mrms_prep_values.csv', sep = ',')

#with open('mrms_variables_header.txt', 'w') as f:
    #f.write('\n'.join([', '.join(line) for line in keys]))
#print(keys)
#fig, ax = plt.subplots()
#ax.contourf(lons, lats, data)
#plt.show()