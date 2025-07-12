import sys
import math
import matplotlib.pyplot as plt
from Bio.PDB import PDBParser, PPBuilder

def calculate_phi_psi(structure):
    phi_psi = []
    for model in structure:
        for chain in model:
            polypeptides = PPBuilder().build_peptides(chain)
            for poly in polypeptides:
                angles = poly.get_phi_psi_list()
                for phi, psi in angles:
                    if phi is not None and psi is not None:
                        phi_psi.append((math.degrees(phi), math.degrees(psi)))
    return phi_psi

def plot_ramachandran(phi_psi, output_file='ramachandran.png'):
    plt.figure(figsize=(8, 8))

    # Define approximate allowed regions (manually defined polygons for clarity)
    # Alpha helix region
    plt.fill_betweenx(
        [-60, 0], -90, -30,
        color='lightgreen', alpha=0.3, label='α-helix region'
    )
    # Beta sheet region
    plt.fill_betweenx(
        [90, 180], -180, -45,
        color='lightblue', alpha=0.3, label='β-sheet region'
    )

    # Plot data points
    phi_angles = [phi for phi, _ in phi_psi]
    psi_angles = [psi for _, psi in phi_psi]
    plt.scatter(phi_angles, psi_angles, s=30, color='darkblue', edgecolors='k', alpha=0.7, label='Residues')

    # Plot styling
    plt.title('Ramachandran Plot', fontsize=16)
    plt.xlabel('Phi (ϕ) angles', fontsize=12)
    plt.ylabel('Psi (ψ) angles', fontsize=12)
    plt.xlim(-180, 180)
    plt.ylim(-180, 180)
    plt.xticks(range(-180, 181, 60))
    plt.yticks(range(-180, 181, 60))
    plt.axhline(0, color='gray', lw=0.5)
    plt.axvline(0, color='gray', lw=0.5)
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.legend(loc='upper right', fontsize=10)

    # Save high-quality images
    plt.savefig(output_file, dpi=300)
    plt.savefig(output_file.replace('.png', '.pdf'))  # optional PDF version
    plt.show()
    print(f"Ramachandran plot saved as {output_file} and {output_file.replace('.png', '.pdf')}")

def main(pdb_file):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure('protein', pdb_file)
    phi_psi = calculate_phi_psi(structure)
    if not phi_psi:
        print("No phi/psi angles found. Check your PDB file.")
        return
    plot_ramachandran(phi_psi)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python ramachandran_plot.py 1QLX.pdb")
        sys.exit(1)
    main(sys.argv[1])
