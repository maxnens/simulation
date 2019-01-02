g = 9.8 #m/s2
height = 5000.0 #meters
velocity = 0.0 #m/s
seconds = 0.0
interval = 0.01

def meters_per_second_to_miles_per_hour(mps):
    meters_per_hour = mps * 3600.0
    miles_per_hour = meters_per_hour / 1600
    return miles_per_hour

print("sec, v, v_mph, h")
while height > 0:
    seconds += interval
    velocity = velocity + (g * interval)
    height = height - (velocity * interval)
    print("{:0.3f}, {:0.3f}, {:0.3f}, {:0.3f}".format(
        seconds, velocity, meters_per_second_to_miles_per_hour(velocity), height))
