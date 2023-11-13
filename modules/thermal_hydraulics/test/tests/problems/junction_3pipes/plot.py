#* This file is part of the MOOSE framework
#* https://www.mooseframework.org
#*
#* All rights reserved, see COPYRIGHT for full restrictions
#* https://github.com/idaholab/moose/blob/master/COPYRIGHT
#*
#* Licensed under LGPL 2.1, please see LICENSE for details
#* https://www.gnu.org/licenses/lgpl-2.1.html

import matplotlib.pyplot as plt
import pandas as pd

p_low = 100

sol_data = pd.read_csv('junction_3pipes_out.csv')

def makePlot(pipe_loc_str):
  exp_file_name = 'experimental_data/3pipe_open_' + pipe_loc_str + '.csv'
  exp_data = pd.read_csv(exp_file_name)
  exp_data = exp_data.sort_values(by=['time'])

  pp_name = 'p_' + pipe_loc_str
  plot_name = pipe_loc_str + '.png'

  plt.figure(figsize=(8, 6))
  plt.rc('text', usetex=True)
  plt.rc('font', family='sans-serif')
  ax = plt.subplot(1, 1, 1)
  ax.get_yaxis().get_major_formatter().set_useOffset(False)
  plt.xlabel("Time, $t$ [s]")
  plt.ylabel("Pressure Difference, $\\Delta p$ [kPa]")
  plt.plot(exp_data['time'], exp_data['dp'], linestyle='-', marker='', color='black', label='Experiment')
  plt.plot(sol_data['time'], sol_data[pp_name] / 1e3 - p_low, linestyle='--', marker='', color='cornflowerblue', label='THM')
  ax.legend(frameon=False, prop={'size':12})
  plt.tight_layout()
  plt.savefig(plot_name, dpi=300)

makePlot('pipe1_048')
makePlot('pipe1_313')
makePlot('pipe2_052')
makePlot('pipe3_048')
