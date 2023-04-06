let sonar = 0
RingbitCar.init_wheel(AnalogPin.P1, AnalogPin.P2)
RingbitCar.forward()
basic.forever(function on_forever() {
    
    sonar = RingbitCar.ringbitcar_sonarbit(RingbitCar.Distance_Unit.Distance_Unit_cm)
    basic.showNumber(sonar)
    RingbitCar.forward()
})
