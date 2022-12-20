import subprocess
import os


energyplus_install_dir= r'C:\EnergyPlusV22-2-0'

output_full_path = r'C:\Users\brmarquardt\OneDrive - kfi-eng.com\Documents'


os.chdir(energyplus_install_dir)
idf_relative_filepath=r'ExampleFiles\1ZoneEvapCooler.idf'
epw_relative_filepath=r"WeatherData\USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw"
output_relative_directory=r'C:\Users\brmarquardt\OneDrive - kfi-eng.com\Documents'
cl_st=(f'"{energyplus_install_dir}\\EnergyPlus" '
       + '--readvars '  # included to create a .csv file of the results
       + f'--output-directory "{output_relative_directory}" '
       + f'--weather "{epw_relative_filepath}" '
       + f'"{idf_relative_filepath}"'
      )
print(cl_st)

result=subprocess.run(cl_st,
                      capture_output=True
                     )