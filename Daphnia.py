import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from geojson import MultiPoint, Feature, FeatureCollection

df = pd.read_csv("../Data/Daphnia.csv")

# TODO: Create some geoJSON with the decial coordinates and any other important data like depth. use this to graph on arcGIS.
coordinates = df.filter(["adjCountPerBottle", "decimalLatitude", "decimalLongitude", "zooDepth1", "zooDepth2"])
multipoint = MultiPoint([(lon, lat) for lon, lat in zip(coordinates['decimalLongitude'], coordinates['decimalLatitude'])])

# Create properties for features
properties = []
for index, row in coordinates.iterrows():
    properties.append({
        'adjCountPerBottle': row['adjCountPerBottle'],
        'zooDepth1': row['zooDepth1']
    })

# Create GeoJSON features
features = []
for i in range(len(coordinates)):
    feature = Feature(geometry=multipoint, properties=properties[i])
    features.append(feature)

# Create FeatureCollection
feature_collection = FeatureCollection(features)

# Output GeoJSON
print(feature_collection)
