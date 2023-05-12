# Multimodal Geo Dataset
This dataset contains multimodal geospatial data from NOAA MRMS, HRRR, and GOES sources.

Please visit [our website](https://jiang28.github.io/multimodal-geo-dataset.github.io/) for more dataset information.

## Accessing the dataset

### Dataset preview

Please visit [our website](https://jiang28.github.io/multimodal-geo-dataset.github.io/) for interactive viewing of our dataset.

We also provide decompressed sample data (mesh files in `obj` format) under `example_data/`.

### Access the entire dataset
We provide a compressed version of our dataset, together with a Python decompressor script that you can run to locally decompress it. Proceed as follows (this assumes you have conda installed):

### Download the Multimodal Geo Dataset from Dataverse and unzip files.
To reproduce the main results in the paper, you only need to download the NOAA_MRMS, HRRR, and GOES subsets as well as the data_split.tar.gz.
Refer to here for how to unzip splitted zip files.
Make sure the unzipped dataset looks like the following:


```
$DATA_ROOT/
├──── data_split/
│     ├──── everyday.train.txt
│     ├──── everyday.val.txt
│     ├──── artifact.train.txt
│     ├──── artifact.val.txt
│     ├──── other.train.txt
│     ├──── other.val.txt
├──── everyday_compressed/
│     ├──── BeerBottle/
│     |     |──── 3f91158956ad7db0322747720d7d37e8/
|     |     |     |──── compressed_data.npz
|     |     |     |──── compressed_mesh.obj
|     │     |     |──── mode_0/
|     |     |     |     |──── compressed_fracture.npy
•     •     •     •
•     •     •     •
|     |     |     |──── mode_19/
|     |     |     |──── fractured_0/
•     •     •     •
•     •     •     •
|     |     |     |──── fractured_79/
│     |     |──── 6da7fa9722b2a12d195232a03d04563a/
│     |     |──── 2927d6c8438f6e24fe6460d8d9bd16c6/
•     •     •
•     •     •
│     ├──── Bottle/
│     |     |──── 1/
│     |     |──── 1b64b36bf7ddae3d7ad11050da24bb12/
│     |     |──── 1c79735033726294724d5ee7f09ab66b/
•     •     •
•     •     •
│     ├──── Bowl/
•     •
•     •
├──── artifact_compressed/
│     ├──── 39084_sf/
│     ├──── 39085_sf/
│     ├──── 39086_sf/
•     •
•     •
├──── other_compressed/
│     ├──── 32770_sf/
│     ├──── 34783_sf/
│     ├──── 34784_sf/
•     •
•     •
```

## Dataset description

Our multimodal geo dataset contains data from three sources: NOAA MRMS, HRRR, and GOES.

### NOAA MRMS

NOAA MRMS (Multi-Radar Multi-Sensor) is a weather radar and satellite-based precipitation estimation system that integrates data from multiple radars and multiple sensors. Our dataset contains MRMS precipitation rate data at a resolution of 1 km x 1 km.

### HRRR

The High-Resolution Rapid Refresh (HRRR) model is a weather forecast model that provides hourly forecasts out to 18 hours. Our dataset contains HRRR temperature, humidity, and wind data at a resolution of 3 km x 3 km.

### GOES

The Geostationary Operational Environmental Satellite (GOES) series provides continuous monitoring of the weather for the Western Hemisphere. Our dataset contains GOES visible and infrared imagery at a resolution of 2 km x 2 km.

## Citation
1. MRMS. Multi-radar/multi-sensor system (mrms). https://www.nssl.noaa.gov/projects/mrms/
2. GOES. Noaa geostationary satellite (goes). https://www.goes.noaa.gov/index.html, (2021).
3. HRRR. Hrrr state variables. https://home.chpc.utah.edu/~u0553130/BrianBlaylock/HRRRarchive/hrrrprstablef00-f01.html, (2021).


