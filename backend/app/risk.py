import math
SEV_WEIGHT={'critical':10.0,'high':8.0,'medium':5.0,'low':2.5,'info':0.5}
def calculate_risk(severity,confidence):
    try:
        value=float(confidence)
        if not math.isfinite(value): value=0.0
    except (TypeError,ValueError):
        value=0.0
    value=max(0.0,min(1.0,value))
    key=getattr(severity,'value',str(severity))
    return round(min(10.0,SEV_WEIGHT.get(key,1.0)*value),2)
