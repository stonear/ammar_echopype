import echopype as ep
from echopype import open_raw
# from pathlib import Path

# ed = open_raw('aa-D20231124-T005648.raw', sonar_model='EK60')
ed = open_raw('aa-D20231123-T234359.raw', sonar_model='EK60')
ed.to_netcdf(save_path='./unpacked_files')