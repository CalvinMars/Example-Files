# The recipe gives simple implementation of a Discrete Proportional-Integral-Derivative (PID) controller. PID controller gives output value for error between desired reference input and measurement feedback to minimize error value.
# More information: http://en.wikipedia.org/wiki/PID_controller
#
# cnr437@gmail.com
#
#######	Example	#########
#
# p=PID(3.0,0.4,1.2)
# p.setPoint(5.0)
# while True:
#     pid = p.update(measurement_value)
#
#


class PID:
    """  Discrete PID control  """

    def __init__(self, P=2.0, I=0.0, D=1.0, Derivator=0, Integrator=0, Integrator_max=500, Integrator_min=-500):

        self.Kp = P
        self.Ki = I
        self.Kd = D
        self.Derivator = Derivator
        self.Integrator = Integrator
        self.Integrator_max = Integrator_max
        self.Integrator_min = Integrator_min

        self.set_point = 0.0
        self.error = 0.0

    def update(self, current_value):
        """ Calculate PID output value for given reference input and feedback """

        self.error = self.set_point - current_value
        p_value = self.Kp * self.error
        d_value = self.Kd * (self.error - self.Derivator)
        self.Derivator = self.error
        self.Integrator = self.Integrator + self.error

        if self.Integrator > self.Integrator_max:
            self.Integrator = self.Integrator_max
        elif self.Integrator < self.Integrator_min:
            self.Integrator = self.Integrator_min
        i_value = self.Integrator * self.Ki

        return p_value + i_value + d_value

    def set_point(self, set_point):
        """ Initialize the set point of PID """
        self.set_point = set_point
        self.Integrator = 0
        self.Derivator = 0

    def set_integrator(self, Integrator):
        self.Integrator = Integrator

    def set_derivator(self, Derivator):
        self.Derivator = Derivator

    def set_Kp(self, P):
        self.Kp = P

    def set_Ki(self, I):
        self.Ki = I

    def set_Kd(self, D):
        self.Kd = D

    def get_point(self):
        return self.set_point

    def get_error(self):
        return self.error

    def get_integrator(self):
        return self.Integrator

    def get_derivator(self):
        return self.Derivator
