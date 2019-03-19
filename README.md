# Marquis Slideshow 2019

## Update

Just use `feh -Y -x -q -D 4 -B black -F -Z -r /media/pi/`

### Code for Raspberry Pi 3 Model B

In `~/.config/lxsession/LXDE-pi/autostart` add this line:
`@/home/pi/Marquis-Slideshow-2019/slideshow.py`

Adjust the global variable `flash_drive` to match the name of your flash drive.
