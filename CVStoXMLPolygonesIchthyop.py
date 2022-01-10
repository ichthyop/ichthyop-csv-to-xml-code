#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 15:41:22 2022

@author: Celine Barrier
"""
import numpy as np 
import pandas as pd

data=pd.read_csv("yourfilename.csv",sep=";").to_numpy()

nbPoly=len(np.unique(data[:,0]))

f=open("polygonsFile.xml","w")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<zones>\n")

for i in range(nbPoly):

    poly=data[np.where(data[:,0]==(i+1))]
    f.write("\t<zone>\n\t\t<key>zone"+str(i+1)+"</key>\n\t\t<type>release</type>\n\t\t<enabled>true</enabled>\n\t\t<color>[r=255,g=0,b=255]</color>\n\t\t<polygon>\n")
    for j in range(poly.shape[0]):
        f.write("\t\t\t<point>\n\t\t\t\t<index>"+str(j)+"</index>\n\t\t\t\t<lon>"+str(poly[j,1])+"</lon>\n\t\t\t\t<lat>"+str(poly[j,2])+"</lat>\n\t\t\t</point>\n")
    f.write("\t\t</polygon>\n\t\t<bathy_mask>\n\t\t\t<enabled>false</enabled>\n\t\t\t<line_inshore>0.0</line_inshore>\n\t\t\t<line_offshore>12000.0</line_offshore>\n\t\t</bathy_mask>\n\t\t<thickness>\n\t\t\t<enabled>true</enabled>\n\t\t\t<lower_depth>20.0</lower_depth>\n\t\t\t<upper_depth>0.0</upper_depth>\n\t\t</thickness>\n\t</zone>\n")

f.write("</zones>")

f.close()