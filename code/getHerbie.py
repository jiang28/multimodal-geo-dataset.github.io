from herbie import Herbie
from datetime import datetime
from datetime import timedelta

# Herbie object for the HRRR model 6-hr surface forecast product
start = datetime(2022, 11, 2, 0, 0)
end = datetime(2022, 11, 4, 0, 0)
hour = timedelta(hours=1)
date = start

while date <= end:
    H = Herbie(
        '{:04d}-{:02d}-{:02d} {:02d}:00'.format(date.year, date.month, date.day, date.hour),
        model='hrrr',
        product='sfc',
        fxx=6
        )
    
# Look at file contents
    H.inventory()
# Download the full GRIB2 file
    H.download()
# hour plus one  
    date += hour