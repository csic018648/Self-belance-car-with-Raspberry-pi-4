import json
i=1
with open("/home/pi/config.json","w") as f:
    data = {"Kp":(4),"Ki":(0.55),"Kd":(18),"offset":(3.0),"Lmin":(4),"Rmin":(4),"LminR":(4),"RminR":(4),"flag":(0)}
    json.dump(data, f)