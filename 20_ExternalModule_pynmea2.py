# pip install pynmea2

import pynmea2

nmea_obj = pynmea2.parse("$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,100.00,M,-33.9,M,,0000*6D")
print(type(nmea_obj), nmea_obj)
print(nmea_obj.talker)
print(nmea_obj.data)
print(nmea_obj.latitude, nmea_obj.longitude, nmea_obj.altitude)

nmea_obj = pynmea2.GGA("GP", "GGA", ('184353.07', '1929.045', 'S', '02410.506', 'E', '1', '04', '2.6', '100.00', 'M', '-33.9', 'M', '', '0000'))
print(str(nmea_obj))