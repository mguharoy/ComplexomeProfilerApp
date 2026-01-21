import sys
from pathlib import Path

import Complexome
    

if __name__ == "__main__":
    cpx = Complexome.setup({"": Path(sys.argv[1]).read_bytes()})
    subunits = Complexome.identify_perturbed_complexes(cpx.complexes, cpx.complex_names, cpx.proteomics_data, 1.0, 0.05)
    Complexome.perturbation_scores(cpx, subunits)
