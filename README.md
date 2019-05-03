# Spotify RFID Jukebox

This library is built using Python to run on a dedicated Raspberry Pi. It uses an MFRC522 RFID Reader, attached to the GPIO pins of the Raspberry Pi to read RFID cards which can be linked to Spotify URL's to play music when scanned.

## Getting Started

These instructions will get you a copy of the project up and running on a dedicated Raspberry Pi

### Prerequisites

Before installing this library you'll want to update your Raspberry Pi

```
> sudo apt-get update
> sudo apt-get upgrade
```

Next you'll need to enable SPI on your Raspberry Pi
```
> sudo raspi-config
```
Find "Interfacing Options" and change "SPI" to "enable"

Run the following command and verify that you see "spi_bcm2835" running
```
> lsmod | grep spi
```

Make sure git is installed
```
> sudo apt-get install git
```

For the purposes of this project make a new directory for the libraries and controller named "Projects"
```
> sudo mkdir ~/Projects
```

Clone the SPI-Py library into the Projects directory. This library is for using Python to interface with the GPIO pins
```
> cd ~/Projects
> git clone https://github.com/lthiery/SPI-Py.git
> cd SPI-Py
> git checkout 8cce26b9ee6e69eb041e9d5665944b88688fca68
> sudo python setup.py install
> cd ../
```
We checkout this specific commit to avoid errors with reading from the RFID reader

## Installing the Spotify Controller

Now we'll install the controller

First we'll clone the project
```
> git clone https://github.com/walker76/spotify-controller.git
> cd spotify-controller
```

### Configuring the Spotify Controller

Now you'll have to create an "auth_values.py" to hold your specific Spotify data

```
> sudo vim auth_values.py
```

In the "auth_values.py" file add the following, filling in your information as needed. The recommended redirect-url is "https://localhost/". You can find the other information, and setup your redirect-url at https://developer.spotify.com/

```
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
REDIRECT_URL = "your-redirect-url"
USERNAME = "your-username"
```

### Configuring autostart

```
> mkdir -p ~/.config/autostart
> sudo vim ~/.config/autostart/spotify.desktop
```

In the "spotify.desktop" file add the following
```
[Desktop Entry]
Encoding=UTF-8
Name=Spotify Controller
Comment=Autostart the Spotify Controller in a terminal window
Exec=lxterminal --command="/home/pi/Projects/spotify-controller/startup.sh"
```

Now reboot the Raspberry Pi for changes to take effect
```
> sudo reboot
```


## Built With

* [SPI-Py](https://github.com/lthiery/SPI-Py) - Library used for controlling the GPIO pins on the Raspberry Pi
* [Spotipy](https://spotipy.readthedocs.io/) - Python library for interfacing with the Spotify API
* [MFRC522-Python](https://github.com/mxgxw/MFRC522-python) - Example code for reading from the RFID reader
* [Spotify API](https://developer.spotify.com/) - API to control Spotify

## Authors

* **Andrew Walker** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Special thanks to Franscisco Sahli Costabal for the [inspiration](https://fsahli.wordpress.com/2015/11/02/music-cards-rfid-cards-spotify-raspberry-pi/)
