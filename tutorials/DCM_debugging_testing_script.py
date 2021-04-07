from cana.datasets.bio import BREAST_CANCER
from cana.datasets.regan_networks import load_all_regan_pi3k_models
from cana.drawing.canalizing_map import draw_canalizing_map_graphviz
from IPython.display import display
import re

def make_DCM (N, filename='output.png', FLAG_VIEW=True):
    # Request the DCM to the Network
    dcm = N.dynamics_canalization_map(simplify=True)
    # Draws using the graphviz interface.
    # gdcm = draw_canalizing_map_graphviz(dcm)
    # gdcm.render(filename, view=FLAG_VIEW)
    # Display
    # display(gdcm)

breast_cancer_N = BREAST_CANCER()

# Request the CM for one node (note that the node doesn't know the name of its inputs)
CM = breast_cancer_N.nodes[3].canalizing_map()
# Draw using the graphviz interface.
# gCM = draw_canalizing_map_graphviz(CM)
# Display
# display(gCM)

make_DCM(breast_cancer_N, 'Albert_breast_cancer_model_DCM', True)
DCM = breast_cancer_N.dynamics_canalization_map(simplify=True)

reg = re.compile("Ful+")

string = "Fulvestrant-1"
match = bool(re.match(reg, string))
print(match)

for node in DCM.nodes:
    match = bool(re.match(reg, node))
    if match == True:
        print(node)
        print(match)