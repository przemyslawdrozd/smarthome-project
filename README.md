# Soil Moisture Monitoring System

## Overview

This project involves using a Raspberry Pi 4 (RPI4) with a soil moisture sensor to monitor soil moisture levels. The RPI4 sends this data to a local computer server via UDP.

## Components

- **Raspberry Pi 4**: Main controller interfacing with the soil moisture sensor.
- **Soil Moisture Sensor**: Used to detect the moisture level of the soil.
- **Local Computer**: Acts as a server to receive and process data.
- **Network Connection**: Ensures communication between the RPI4 and the local computer.

## Setup

### Raspberry Pi 4 Setup
1. **Connect the Soil Moisture Sensor**:
    - Connect the sensor to GPIO 23 on the RPI4.
2. **Install Required Libraries**:
    - Run `pip install RPi.GPIO` to install the GPIO library.
3. **Script Execution**:
    - Run the RPI4 Python script to start monitoring.

### Local Computer Server Setup
1. **Python Installation**:
    - Ensure Python is installed on your local computer.
2. **Configure Server Script**:
    - Set the `server_ip` variable in the script to the local computer's IP.
3. **Run the Server Script**:
    - Execute the server script to begin receiving data from the RPI4.

