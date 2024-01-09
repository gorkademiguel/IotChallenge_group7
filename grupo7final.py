#!/usr/bin/env python3


import time
import RPi.GPIO as GPIO

from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.grove_relay import GroveRelay

def main():

    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(24, GPIO.OUT)

    # Ultrasonic Ranger conectado al puerto D16
    ultrasonic_sensor = GroveUltrasonicRanger(16)

    # Light Sensor conectado al puerto A2
    light_sensor = GroveLightSensor(2)
    
    # Grove - Relay conectado al puerto D18
    relay = GroveRelay(18)

    while True:
        
        distance = ultrasonic_sensor.get_distance()
        light = light_sensor.light

        print('////////////////////////////////////////////////////')
        print('Distancia  {} cm'.format(distance))       
        print('////////////////////////////////////////////////////')
        if 0 < distance < 100:
            print('--------------------------------------------------------------------------')
            print('El valor de la luz es {}'.format(light))
         
            if 0 <= light < 200:
                print('Presencia de un barco detectada, luces activadas. ')
                relay.on()
                time.sleep(5)
                relay.off()
            
        else:
            print('No hay ningun barco cerca.')
        time.sleep(1)
        
        print('##################################################################')
            
            
            

if __name__ == '__main__':
    main()
