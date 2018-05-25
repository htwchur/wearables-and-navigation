# wearables-and-navigation

## Setup

The installation is based on Raspbian Stretch 2017-11-29.

Change keyboard layout:

```bash
sudo dpkg-reconfigure keyboard-configuration # reboot afterwards
```

Set timezone:

```bash
raspi-config # -> Localisation Options -> Change Timezone -> Europe -> Zurich
```

Connect to WiFi using GUI.

Install necessary software:

```bash
sudo apt install vim gpsbabel python-espeak libgeos-dev python-gps gpsd-clients colordiff
pip3 install gpsd-py3 tenacity openrouteservice Flask gpiozero shapely pyproj pyttsx3
```

Clone git repo:

```bash
cd ~; git clone https://github.com/htwchur/wearables-and-navigation.git
```

Setup autostart:

```bash
sudo cp ~/wearables-and-navigation/src/init/wan-router /etc/init.d/wan-router
sudo chmod +x /etc/init.d/wan-router
```

Start software for the first time (this will happen automatically with future boots):

```bash
sudo /etc/init.d/wan-router start
```




## src

### Start Flask

Call

    start-flask-dev.sh

which then starts

    flask-app.py

which will start/stop

    main.py

### Start `main.py` directly:

    cd src/; export GPIOZERO_PIN_FACTORY=mock; ./main.py --lat 46.85449 --lon 9.52864

Explanation:

- Setting `GPIOZERO_PIN_FACTORY` is necessary (only) on systems that are not a Raspberry Pi
- `--lat` and `--lon` are the destination coordinates (these are necessary)

### Class diagram

![Class diagram](https://raw.githubusercontent.com/htwchur/wearables-and-navigation/master/doc/klassendiagramm.png?token=AEgeBcwyK-BGEYOd-_7Hbdl9AD3iPqvnks5bENfjwA%3D%3D "Class diagram")

The class diagram was rendered using http://plantuml.com/ .

## test1

Read way from Chur Bahnhof to Medienhaus, display waypoints, instruction and angle in console.
Next step: Make simulation on a map for position, compare then simulated position with angle.

## test2

- Generate fake gps data and read it from python
- Calculate distance to linestring

## Links

- https://docs.google.com/document/d/***REMOVED***/edit
