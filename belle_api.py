#possible api
#/<zone>/   returns current vals and state
# /<zone>/mode/<"heat"|"cool"|"off">
# /<zone>/temp/<target_temp>
# /<zone>/fan/<"on"|"off">
#a more general api
# /<zone>/<function>/<option>



from flask import Blueprint, redirect, render_template
from belle_thermostat import Zone
import json
from pprint import pprint

api = Blueprint("api", __name__)

zones = []
zones.append(Zone("Upstairs", targetTemperature=73))
zones.append(Zone("Downstairs", targetTemperature=76))



@api.route("//")
def zoneIndex():
    out = []
    for zone in zones:
        out.append(vars(zone))
    return json.dumps(out)


@api.route("/<zone>")
def zone(zone):
    for z in zones:
        if z.name.upper() == zone.upper():
            return  json.dumps(vars(z))
    return "invalid zone"

@api.route("/<zone>/mode/<option>") #"heat", "cool", or "off"
def zoneMode(zone, option):
    for z in zones:
        if z.name.upper() == zone.upper():
            if z.validMode(option):
                z.setMode(option.upper())
                return "%s is set to %s" %(zone, option)
            else:
                return "invalid mode"


@api.route("/<zone>/temp/<target_temp>") #an integer
def zoneTemp(zone, target_temp):
    for z in zones:
        if z.name.upper() == zone.upper():
            if z.validTemp(int(target_temp)):
                z.setTemp(target_temp)
                return "%s temperature is set to %s" % (zone, target_temp)
            else:
                return "invalid temperature"


@api.route("/<zone>/fan/<option>") # "on" or "off"
def zoneFan(zone, option):
    return "%s fan is set to  %s" % (zone, option)


@api.route('/')
def index():
    return "Belle Index"
