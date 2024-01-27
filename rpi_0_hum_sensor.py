import socket
import time
import RPi.GPIO as GPIO

# Constants
SENSOR_PIN = 23
SERVER_IP = '192.168.0.102'  # Replace with your server's IP
SERVER_PORT = 12345
SLEEP_TIME = 1  # Time interval between readings

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

def read_sensor():
    """Reads the sensor and returns the status."""
    if GPIO.input(SENSOR_PIN):
        return "Gleba sucha"  # Dry Soil
    else:
        return "Gleba wilgotna"  # Moist Soil

def send_data(data, sock):
    """Sends data to the server."""
    try:
        sock.sendto(data.encode(), (SERVER_IP, SERVER_PORT))
    except Exception as e:
        print("Error sending data:", str(e))

def create_udp_socket():
    """Creates and returns a UDP socket."""
    try:
        return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except Exception as e:
        print("Error creating socket:", str(e))
        return None

def main():
    print("Sensor monitoring started")
    sock = create_udp_socket()
    if not sock:
        return

    try:
        while True:
            sensor_data = read_sensor()
            print("sensor_data:", sensor_data)
            send_data(sensor_data, sock)
            time.sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        print("UDP Client stopped")
    except Exception as e:
        print("Error:", str(e))
    finally:
        if sock:
            sock.close()
        GPIO.cleanup()

if __name__ == "__main__":
    main()
