import pytest

import numpy as np

from D3HRE import Task, MaritimeRobot
from D3HRE.core.mission_utility import Mission
from PyResis import propulsion_power

test_route =  np.array([[ 10.69358 , -178.94713892], [ 11.06430687, +176.90022735]])
# -------------------------------------------------------------------------------------
#  The route is the most basic concept in D3HRE. The route of a vehicle is defined as
#  an array (numpy.ndarray) of coordinates. It can either from route planning software
#  (e.g. OpenCPN), or hand picked coordinates, or even from shortest path planning.
#
#  np.array([[lat1, lon1], [lat2,lon2], ...])
# -------------------------------------------------------------------------------------


test_mission = Mission('2014-01-01', test_route, 2)
# -------------------------------------------------------------------------------------
#  When there is a route there is a mission. Mission is about how to go through certain
#  route. Basic information on when an how to go through the route is required to form
#  a mission. Start time, route and speed can define this.
#
#
# -------------------------------------------------------------------------------------




test_ship = propulsion_power.Ship()
test_ship.dimension(5.72, 0.248, 0.76, 1.2, 5.72/(0.549)**(1/3),0.613)
# -------------------------------------------------------------------------------------
#  To accomplish
#
#
#
#
# -------------------------------------------------------------------------------------



power_consumption_list = {'single_board_computer': {'power': [2, 10], 'duty_cycle': 0.5},
                              'webcam': {'power': [0.6], 'duty_cycle': 1},
                              'gps': {'power': [0.04, 0.4], 'duty_cycle': 0.9},
                              'imu': {'power': [0.67, 1.1], 'duty_cycle': 0.9},
                              'sonar': {'power': [0.5, 50], 'duty_cycle': 0.5},
                              'ph_sensor': {'power': [0.08, 0.1], 'duty_cycle': 0.95},
                              'temp_sensor': {'power': [0.04], 'duty_cycle': 1},
                              'wind_sensor': {'power': [0.67, 1.1], 'duty_cycle': 0.5},
                              'servo_motors': {'power': [0.4, 1.35], 'duty_cycle': 0.5},
                              'radio_transmitter': {'power': [0.5, 20], 'duty_cycle': 0.2}}


config = {'load': {'prop_load': {'prop_eff': 0.7,
   'sea_margin': 0.2,
   'temperature': 25}},
 'optimization': {'constraints': {'turbine_diameter_ratio': 1.2,
   'volume_factor': 0.1,
   'water_plane_coff': 0.88},
  'cost': {'battery': 1, 'lpsp': 10000, 'solar': 210, 'wind': 320},
  'method': {'nsga': {'cr': 0.95, 'eta_c': 10, 'eta_m': 50, 'm': 0.01},
   'pso': {'eta1': 2.05,
    'eta2': 2.05,
    'generation': 100,
    'max_vel': 0.5,
    'neighb_param': 4,
    'neighb_type': 2,
    'omega': 0.7298,
    'population': 100,
    'variant': 5}},
  'safe_factor': 0.2},
 'simulation': {'battery': {'B0': 1,
   'DOD': 0.9,
   'SED': 500,
   'eta_in': 0.9,
   'eta_out': 0.8,
   'sigma': 0.005},
  'coupling': {'eff': 0.05}},
 'source': {'solar': {'brl_parameters': {'a0': -5.32,
    'a1': 7.28,
    'b1': -0.03,
    'b2': -0.0047,
    'b3': 1.72,
    'b4': 1.08}}},
 'transducer': {'solar': {'azim': 0,
   'pitch': 0.1,
   'roll': 0.1,
   'stationary': False,
   'loss': 0.1,
   'power_density': 140,
   'tacking': 0,
   'tech': 'csi',
   'tilt': 0},
  'wind': {'power_coef': 0.3,
   'thurse_coef': 0.6,
   'v_in': 2,
   'v_off': 45,
   'v_rate': 15}}}

test_robot = MaritimeRobot(power_consumption_list, from_pyresis=test_ship, use_ocean_current=False)

test_task = Task(test_mission, test_robot)
