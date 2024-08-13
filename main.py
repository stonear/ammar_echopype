import echopype as ep

# ed = open_raw('aa-D20231124-T005648.raw', sonar_model='EK60')
ed = ep.open_raw('aa-D20231123-T234359.raw', sonar_model='EK60')
ed.to_netcdf(save_path='./unpacked_files')
