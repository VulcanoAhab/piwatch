#directly from piccamera tutorial

import socket
import subprocess
import argparse



def server_forever(HOST, PORT)
    #start server
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen(0)

    # Accept a single connection and make a file-like object out of it
    connection = server_socket.accept()[0].makefile('rb')
    print('Starting server...')

    try:
        # Run a viewer with an appropriate command line. Uncomment the mplayer
        # version if you would prefer to use mplayer instead of VLC
        cmdline = ['vlc', '--demux', 'h264', '-']
        #cmdline = ['mplayer', '-fps', '25', '-cache', '1024', '-']
        player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
        while True:
            data = connection.read(1024)
            if not data:break
            player.stdin.write(data)
    except KeyboardInterrupt:
        connection.close()
        server_socket.close()
        player.terminate()
    finally:
        connection.close()
        server_socket.close()
        player.terminate()

if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Debug server for camera stream')
    parser.add_argument('--host', '-h')
    parser.add_argument('--port', '-p')
    args = parser.parse_args()

    server_forever(args.port, args.port)
