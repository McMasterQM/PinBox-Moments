from ..x4_mocked import *
import numpy as np
from numpy.testing import assert_equal, assert_allclose
from scipy.integrate import quad
from functools import partial



def test_check_moments():
    """
    testing check_moments function
    :return:
    """
    n = np.random.randint(100,  size=10)
    a = abs(np.random.rand(10)*10)
    for n_, a_ in zip (n, a):
        n_ = int(abs(n_)) + 1
        res = calc_average(n_, a_, 2)
        true_answer = a_**2*(1/3 - 1./(2*n_**2*np.pi**2))
        assert_allclose(res, true_answer)
    
    answers = [1.4030543394148483,
               89.67763103318262,
               33.90126855204982,
               15.552063960203625,
               0.07257374517946559,
               0.07298247449868618,
               0.001408072622626313,
               69.80582880658015,
               16.218872442280706]
               
    power = 4
    np.random.seed(42)
    for n, a, t_answer in zip(range(1, 10), 5*abs(np.random.rand(10)), answers):
        answer = calc_average(int(n), a, power)
        assert_allclose(answer, t_answer)
