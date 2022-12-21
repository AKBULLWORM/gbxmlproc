import subprocess
import os


def runeplus(eplusversion,idfpath,weatherpath,outputpath,outputname):


    energyplus_install_dir = eplusversion
    output_full_path = outputname
    idf_full_path = idfpath
    weather_full_path = weatherpath
    output_name = outputpath

    cl_st = (f'"{energyplus_install_dir}\\EnergyPlus" '
             + f'--output-prefix "{output_name}" '
             + '--readvars '  # included to create a .csv file of the results
             + f'--output-directory "{output_full_path}" '
             + f'--weather "{weather_full_path}" '
             + f'"{idf_full_path}" '
             )
    result = subprocess.run(cl_st,
                            capture_output=True
                            )
    return f"{output_name}\{output_full_path}out.csv"


#energyplus_install_dir= r'C:\EnergyPlusV9-5-0'
#output_full_path = r'C:\EnergyPlusV9-5-0\sim'
#idf_full_path = r'C:\EnergyPlusV9-5-0\ExampleFiles\1ZoneEvapCooler.idf'
#weather_full_path = r'C:\EnergyPlusV9-5-0\WeatherData\USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw'
#output_name = 'testname'

#cl_st=(f'"{energyplus_install_dir}\\EnergyPlus" '
#       + f'--output-prefix "{output_name}" '
#       + '--readvars '  # included to create a .csv file of the results
#       + f'--output-directory "{output_full_path}" '
#       + f'--weather "{weather_full_path}" '
#       + f'"{idf_full_path}" '
#      )
#result=subprocess.run(cl_st,
#                      capture_output=True
#                     )
#print('---ARGS---\n',result.args)
#print('---RETURNCODE---\n',result.returncode, '(SUCCESS)' if result.returncode==0 else '(FAIL)')
#print('---STDOUT---\n',result.stdout.decode())
#print('---STDERR---\n',result.stderr.decode())