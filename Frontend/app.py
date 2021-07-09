from sklearn.cluster import KMeans
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
import pandas as pd

st.header("""Clustering App for Kmeans """)

X = pd.read_csv('/content/DataKmeans.csv')

cluster_slider = st.slider(
    min_value=1, max_value=6, value=2, label="Number of clusters: "
)
kmeans = KMeans(n_clusters=cluster_slider, random_state=0).fit(X)
labels = kmeans.labels_


clrs = ["red", "seagreen", "orange", "blue", "yellow", "purple"]

n_labels = len(set(labels))

individual = st.selectbox("Individual subplots?", [False, True])

FirstColumn = st.sidebar.slider(
    min_value=0, max_value=25, value=0, label="Choose first column : ")
SecondColumn = st.sidebar.slider(
    min_value=0, max_value=25, value=1, label="Choose second column : ")

if individual:
    fig, ax = plt.subplots(ncols=n_labels)
else:
    fig, ax = plt.subplots()

for i, yi in enumerate(set(labels)):
    if not individual:
        a = ax
    else:
        a = ax[i]

    xi = X[labels == yi]
    x_pts = xi.iloc[:, FirstColumn]
    y_pts = xi.iloc[:, SecondColumn]
    a.scatter(x_pts, y_pts, c=clrs[yi])

    
plt.tight_layout()
st.write(fig)

st.write("""Show clustering Kmeans """)
st.sidebar.header('Columns')
st.sidebar.subheader('Number of each product')

st.sidebar.write('Outlay=0')
st.sidebar.write('WHITE HANGING HEART T-LIGHT HOLDER=1')
st.sidebar.write('REGENCY CAKESTAND 3 TIER=2')
st.sidebar.write('JUMBO BAG RED RETROSPOT=3')
st.sidebar.write('ASSORTED COLOUR BIRD ORNAMENT=4')
st.sidebar.write('PARTY BUNTING=5')
st.sidebar.write('LUNCH BAG RED RETROSPOT=6')
st.sidebar.write('SET OF 3 CAKE TINS PANTRY DESIGN=7')
st.sidebar.write('LUNCH BAG  BLACK SKULL.=8')
st.sidebar.write('JAM MAKING SET PRINTED=9')
st.sidebar.write('PACK OF 72 RETROSPOT CAKE CASES=10')
st.sidebar.write("PAPER CHAIN KIT 50'S CHRISTMAS=11")
st.sidebar.write('SPOTTY BUNTING=12')
st.sidebar.write('LUNCH BAG SPACEBOY DESIGN=13')
st.sidebar.write('LUNCH BAG CARS BLUE=14')
st.sidebar.write('HEART OF WICKER SMALL=15')
st.sidebar.write('NATURAL SLATE HEART CHALKBOARD=16')
st.sidebar.write('LUNCH BAG PINK POLKADOT=17')
st.sidebar.write('REX CASH+CARRY JUMBO SHOPPER=18')
st.sidebar.write('LUNCH BAG SUKI DESIGN=19')
st.sidebar.write('ALARM CLOCK BAKELIKE RED=20')
st.sidebar.write('LUNCH BAG APPLE DESIGN=21')
st.sidebar.write('SET OF 4 PANTRY JELLY MOULDS=22')
st.sidebar.write('JUMBO BAG PINK POLKADOT=23')
st.sidebar.write('JAM MAKING SET WITH JARS=24')
st.sidebar.write('WOODEN PICTURE FRAME WHITE FINISH=25')

