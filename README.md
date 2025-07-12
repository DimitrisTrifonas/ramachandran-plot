# Ramachandran Plot Generator
This Python script generates a Ramachandran plot from a given PDB file.
It uses BioPython to extract φ (phi) and ψ (psi) backbone dihedral angles and matplotlib to visualize them.
Shaded regions highlight typical α-helix and β-sheet conformations.

# Files
ramachandran_plot.py – Main script to generate the plot.
Input: any .pdb file (e.g., 1QLX.pdb).

# Requirements
Python 3.x
Biopython
Matplotlib

-> Install the dependencies using:
pip install biopython matplotlib

# Usage
-> From the terminal, run:
python ramachandran_plot.py 1QLX.pdb
This will generate: ramachandran.png – A high-quality PNG of the plot
