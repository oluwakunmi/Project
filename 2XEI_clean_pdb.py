
input_pdb_file = '2XEI_CLEAN.pdb'
output_pdb_file = '2XEI_clean.pdb'
residue_to_correct = 'GLU'
atom_to_correct = 'N'

with open(input_pdb_file, 'r') as infile, open(output_pdb_file, 'w') as outfile:
    for line in infile:
        if line.startswith('ATOM') or line.startswith('HETATM'):
            residue_name = line[17:20].strip()
            atom_name = line[12:16].strip()
            if residue_name == residue_to_correct and atom_name == atom_to_correct:
                
                corrected_line = line[:12] + ' ' * (16 - len(atom_to_correct)) + atom_to_correct + line[16:]
                outfile.write(corrected_line)
            else:
                outfile.write(line)
        else:
            outfile.write(line)

