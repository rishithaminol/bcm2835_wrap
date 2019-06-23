cdef extern from "pwm.h":
    void motor_tune(int pw)
    void init_pwm_on_pin()
    void stop()

def py_motor_tune(pw: int):
    motor_tune(pw)

def py_init_pwm_on_pin():
    init_pwm_on_pin()

def py_stop():
    stop()
