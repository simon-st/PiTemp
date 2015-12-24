'''
Created on Dec 22, 2015

@author: simonsays
'''

import sys
import Adafruit_DHT
from datetime import datetime
from time import sleep

DHT11_DATA_PIN = 4
FILENAME_FORMAT = 'output_%Y%m%d_%H%M%S.dat'
FILE_HEADER = 'Datetime\tTemperature (C)\tHumidity (%)\n'
LINE_FORMAT = '{0}\t{1:0.1f}\t{2:0.1f}\n'
LINE_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
INTERRUPT_SECONDS = 60

if __name__ == '__main__':
    dt = datetime.now()
    filename = dt.strftime(FILENAME_FORMAT)
    
    with open(filename, 'w') as outfile:
        outfile.write(FILE_HEADER)
        
        try:
            while True:
                humidity, temperature = Adafruit_DHT.read_retry(11, DHT11_DATA_PIN)
                
                if humidity is not None and temperature is not None:
                    print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
                    outfile.write(LINE_FORMAT.format(datetime.now().strftime(LINE_DATE_FORMAT), temperature, humidity))
                else:
                    print 'Failed to get reading. Try again!'
                
                sleep(INTERRUPT_SECONDS)
        except KeyboardInterrupt:
            print 'Stopping...'
            pass
