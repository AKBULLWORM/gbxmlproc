import eplustools


energyplus_install_dir= r'C:\EnergyPlusV9-5-0'
output_full_path = r'C:\EnergyPlusV9-5-0\sim'
idf_full_path = r'C:\EnergyPlusV9-5-0\ExampleFiles\1ZoneEvapCooler.idf'
weather_full_path = r'C:\EnergyPlusV9-5-0\WeatherData\USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw'
output_name = 'testname'






print(eplustools.runeplus(energyplus_install_dir,idf_full_path,weather_full_path,output_full_path,output_name))