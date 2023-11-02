from herbie.archive import Herbie
# Create Herbie object to discover ECMWF operational forecast product
H = Herbie("2022-05-26", model="ecmwf", product="oper", fxx=12)

# Download the full grib2 file
H.download()

# Download just the 10-m u and v winds
H.download(searchString=":10(u|v):")

# Retrieve the 500 hPa temperature as an xarray.Dataset
#ds = H.xarray(searchString=":t:500:")