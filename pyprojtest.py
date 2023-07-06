import pyproj
#import folium

#m = folium.Map(location=[41,29])

# Define the source and target CRS
src_crs = pyproj.CRS("EPSG:5972")
dst_crs = pyproj.CRS("EPSG:5950")

# Define the source and target coordinates
src_coords_FM1 = (592345.817,6737250.730)
src_coords_FM2 = (592535.245 ,6737243.461)
src_coords_FM3 =  (592512.154,6737346.941 )

# Create a Transformer object to perform the transformation
transformer = pyproj.Transformer.from_crs(src_crs, dst_crs)

# Perform the transformation
dst_coords_FM1 = transformer.transform(src_coords_FM1[0], src_coords_FM1[1])
dst_coords_FM2 = transformer.transform(src_coords_FM2[0], src_coords_FM2[1])
dst_coords_FM3 = transformer.transform(src_coords_FM3[0], src_coords_FM3[1])


#m.save("mymap.html")



print('FM1',dst_coords_FM1 ,'\n','FM2', dst_coords_FM2 , '\n','FM3',dst_coords_FM3)


#1 grunnlaget. Nei du taper ikke nøyaktighet når du konverterer koordinater.
