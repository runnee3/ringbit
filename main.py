sonar = 0
RingbitCar.init_wheel(AnalogPin.P1, AnalogPin.P2)
RingbitCar.forward()

def on_forever():
    global sonar
    sonar = RingbitCar.ringbitcar_sonarbit(RingbitCar.Distance_Unit.DISTANCE_UNIT_CM)
    basic.show_number(sonar)
    RingbitCar.forward()
basic.forever(on_forever)
