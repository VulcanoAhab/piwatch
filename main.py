import io
import random
import picamera
import socket
import time
import traceback
import argparse

def motion_detected():
    return True

#connect to video server
def call_server(HOST, PORT):
    socket = socket.socket()
    socket.connect((HOST, PORT))
    connection = socket.makefile('wb')
    return connection, socket

#little work
def work_forever(recsize=10):
    '''
    '''
    while True:
        try:
            if motion_detected():
               camera.wait_recording(recsize)
               stream.copy_to(connection)
            time.sleep(2)
        except KeyboardInterrupt:
            break
        except:
            traceback.print_exc()
    return




if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Camera Cycle Stream program')
    parser.add_argument('--host', '-h')
    parser.add_argument('--port', '-p')
    args = parser.parse_args()

    connection, socket=call_server(args.host, args.port)
    print('Starting camera.')
    stream = picamera.PiCameraCircularIO(camera, seconds=20)
    # Start a preview and let the camera warm up forseconds
    camera.start_preview()
    time.sleep(2)
    camera.start_recording(stream, format='h264')

    print('Monitoring.')
    work_forever()
    camera.stop_recording()
    socket.close()
