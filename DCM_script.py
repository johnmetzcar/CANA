import os
from cana.datasets.bio import THALIANA
from cana.drawing.canalizing_map import draw_canalizing_map_graphviz
from IPython.display import display

import cana

def make_DCM (N, filename=output.png, FLAG_VIEW=True)
    # Request the DCM to the Network
    dcm = N.dynamics_canalization_map(simplify=True)
    # Draws using the graphviz interface.
    gdcm = draw_canalizing_map_graphviz(dcm)
    gdcm.render(filename, view=FLAG_VIEW)
    # Display
    display(gdcm)

def load_network (path, name):

    return cana.boolean_network.from_file(path + name + '.txt', name=name, keep_constants=True)

load_network(.)

This isn't working ... '


# if __name__ == '__main__':
#     globals()[sys.argv[1]]()
#
#     What is my goal? running all of the networks or creating something that does just what I need? How about I do something that I just need ...