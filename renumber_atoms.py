import numpy as np

def renumber_atoms(coord_file, topology_file, output_file):
    # Read coordinate file
    with open(coord_file, 'r') as f:
        coord_lines = f.readlines()

    # Read topology file to get atom order
    with open(topology_file, 'r') as f:
        topology_lines = f.readlines()

    # Extract atom order from topology file
    atom_order = [line.split()[3] for line in topology_lines if line.startswith("ATOM")]

    # Check if the number of atoms matches
    if len(coord_lines) != len(atom_order) + 3:  # Assumes standard GROMACS coordinate file format
        print("Error: Number of atoms in coordinate file does not match topology file.")
        return

    # Renumber atoms in the coordinate file
    for i in range(3, len(coord_lines)):
        atom_info = coord_lines[i].split()
        atom_info[2] = atom_order[i - 3]
        coord_lines[i] = "{:<5}{:<5}{:<5}{:<5}{:<8}{:<8}{:<8}\n".format(*atom_info)

    # Write the modified coordinate file
    with open(output_file, 'w') as f:
        f.writelines(coord_lines)

    print(f"Coordinate file renumbered and saved to {output_file}")

# Usage
renumber_atoms("solv.gro", "topol.top", "renumbered_solv.gro")

