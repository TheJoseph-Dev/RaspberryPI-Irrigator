# RaspberryPI Irrigator

Irrigator integrated with RaspberryPI and Python  

This project was made during the SENAI course


## Features

- Detect Light
- Detect Ambient Temperature and Humidity
- Detect Soil Humidity
- Turn on LEDs
- Photosynthesiser
- Real-Time WebPage Data Display


## To Run

Clone the project

```bash
git clone https://github.com/TheJoseph-Dev/RaspberryPI-Irrigator.git
```

Go to the project directory

```bash
cd RaspberryPI-Irrigator
```

Create Virtual Env

```bash
python -m venv env
```

Activate Virtual Env

Windows:
```cmd
.\env\Scripts\activate
```

Mac or Linux:
```bash
source .\env\bin\activate
```

Install dependencies

```bash
pip install -r requirements.py
```

Connect the pins to the RaspberryPI

Run it:

```bash
python Main.py
```