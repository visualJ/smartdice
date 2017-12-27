# smartdice
This is a webapp that allows to interact with the 'smartdice' devices. This is part of a project in the module **IoT** (HSRM WS17/18).
Documentation can be found in the [wiki](https://github.com/visualJ/smartdice/wiki). The smartdice firmware can be found [here](https://github.com/jonask1337/esp8266-smartdice).

## Key features
The key features of the webapp are:
- creating and managing sessions
- adding and managing participants in sessions
- adding and managing smartdice in sessions
- displaying dice roll results

## Installation
You can install the webapp with
```bash
git clone https://github.com/visualJ/smartdice.git
cd smartdice
pip install -r requirements.txt
python manage.py migrate
```
and use
```
python manage.py runserver
```
to run it locally. On windows, you need to run `pip install pypiwin32` first. The webapp will run on port 8000 by default.
