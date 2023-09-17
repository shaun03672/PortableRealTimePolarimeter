import math
import numpy as np


class Calculator:

    S0 = 1.00
    S1 = 0.25
    S2 = 0.32
    S3 = 0.55

    polarisation_ellipse_x_data = np.linspace(0, 358, 180) * np.pi / 180


    def get_stokes_params(self):
        return [self.S0, self.S1, self.S2, self.S3]

    def get_polarisation_ellipse_params(self):
        psi = math.atan(self.S2 / self.S1) / 2
        chi = math.asin(self.S3 / self.S0) / 2
        return (psi, chi)

    def get_poincare_sphere_params(self):
        phi = math.atan(self.S2 / self.S1)
        theta = math.acos(self.S3 / self.S0)
        return (phi, theta)

    def get_polarisation_ellipse_x_data(self):
        return np.random.rand(1,180)[0] * 2 - 1

    def get_polarisation_ellipse_y_data(self):
        return np.random.rand(1,180)[0] * 2 - 1


