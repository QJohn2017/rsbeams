# sbend
execution_mode = 'serial'

lattice_file = """
% 0.5 sto arc_length
% pi 2 / sto bend_angle
% arc_length bend_angle / sto bend_radius

"S1": SBEN,angle="bend_angle",l="arc_length"
!"S1": CSBEND, angle="bend_angle",l="arc_length", N_KICKS=100
"W0": WATCH,filename="W0.filename.sdds"
"W1": WATCH,filename="W1.filename.sdds"
"BL1": LINE=(W0,S1,W1)

"""

elegant_file = """

&global_settings
  mpi_io_write_buffer_size = 1048576,
&end

&run_setup
  lattice = "elegant.lte",
  expand_for = "bunch_elegant.sdds",
  print_statistics = 1,
  use_beamline = "BL1",
  default_order = 1
&end

&run_control
&end

&twiss_output
  filename = "twiss_output.filename.sdds",
&end

&sdds_beam
    input = "bunch_elegant.sdds"
&end

&track
&end

"""

with open('elegant.lte', 'w') as f:
    f.write(lattice_file)

with open('elegant.ele', 'w') as f:
    f.write(elegant_file)

import os
os.system('elegant elegant.ele')
