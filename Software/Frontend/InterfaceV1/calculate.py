import math
import numpy as np
from numpy import sin, cos


class Calculator():

    def __init__(self, num_points):
        self.num_points = num_points
        self.t = np.linspace(0, 2 * np.pi, self.num_points)
        self.S0 = 0.0
        self.S1 = 0.0
        self.S2 = 0.0
        self.S3 = 0.0
        self.generate_random_polarisation()

    def generate_random_polarisation(self):
        S1 = np.random.random() * 2 - 1  # random number in range [-1, 1)
        S2 = np.random.random() * 2 - 1
        S3 = np.random.random() * 2 - 1
        self.S1 = S1 / 1.73205080757  # divide by sqrt(3) to have maximum sum of square be at max 1.0
        self.S2 = S2 / 1.73205080757
        self.S3 = S3 / 1.73205080757
        square_sum = np.sqrt(self.S1 ** 2 + self.S2 ** 2 + self.S3 ** 2)
        self.S0 = np.random.random() * (1 - square_sum) + square_sum  # force S0^2 >= S1^2 + S2^2 + S3^2

    def get_stokes_params(self):
        return [self.S0, self.S1, self.S2, self.S3]

    def get_dop(self):
        return np.sqrt(self.S1 ** 2 + self.S2 ** 2 + self.S3 ** 2) / self.S0

    def get_polarisation_ellipse_params(self):
        psi = math.atan(self.S2 / self.S1) / 2
        chi = math.asin(self.S3 / self.S0) / 2
        return (psi, chi)

    def get_poincare_sphere_params(self):
        phi = math.atan(self.S2 / self.S1)
        theta = math.acos(self.S3 / self.S0)
        return (phi, theta)

    def get_polarisation_ellipse_xy_data(self):

        psi, chi = self.get_polarisation_ellipse_params()

        sin_t = sin(self.t)
        cos_t = cos(self.t)

        x_t = np.sqrt(self.S0) * (cos(chi) * cos(psi) * sin_t - sin(chi) * sin(psi) * cos_t)
        y_t = np.sqrt(self.S0) * (cos(chi) * sin(psi) * sin_t + sin(chi) * cos(psi) * cos_t)

        return (x_t, y_t)


