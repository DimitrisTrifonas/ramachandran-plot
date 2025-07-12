# Ramachandran Plot Generator 

This Python script generates a **Ramachandran plot** from a given PDB file.  
It uses BioPython to extract φ (phi) and ψ (psi) dihedral angles and plots them with matplotlib, including shaded regions for α-helices and β-sheets.

---

##  Files

- `ramachandran_plot.py` – The main script to generate the plot.
- Example input: a `.pdb` file such as `1QLX.pdb`.

---

##  Requirements

- Python 3.x
- [Biopython](https://biopython.org/)
- Matplotlib

Install dependencies:

```bash
pip install biopython matplotlib

##  Usage

From the terminal:

```bash
python ramachandran_plot.py 1QLX.pdb
