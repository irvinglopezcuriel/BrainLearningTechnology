rrfrom neurosdk.scanner import Scanner
from neurosdk.sensor import Sensor
from neurosdk.brainbit_sensor import BrainBitSensor
from neurosdk.cmn_types import *

from tools.logging import logger
from distutils.util import strtobool
import os

#doing all this a the "module level" in "Demo" server mode it will work fine :)
gl_sensor = None
gl_scanner = None

def on_sensor_state_changed(sensor, state):
    logger.debug('Sensor {0} is {1}'.format(sensor.Name, state))

def on_brain_bit_signal_data_received(data):
    logger.debug(data)

def sensorFound(sensors):
    for i in range(len(sensors)):
        logger.debug('Sensor %s' % sensors[i])
        logger.debug('Connecting to sensor')
        gl_sensor = gl_scanner.create_sensor(sensors[i])
        gl_sensor.sensorStateChanged = on_sensor_state_changed
        gl_sensor.connect()
        gl_sensor.signalDataReceived = on_brain_bit_signal_data_received
        gl_scanner.stop()
        del gl_scanner

def init_headband():
    logger.debug("Create Headband Scanner")
    gl_scanner = Scanner([SensorFamily.SensorLEBrainBit])
    logger.debug("Sensor Found Callback")
    gl_scanner.sensorsChanged = sensorFound

    logger.debug("Start scan")
    gl_scanner.start()

def get_head_band_sensor_object():
    if not bool(strtobool(os.getenv('NO_HEADSET'))):
        return gl_sensor