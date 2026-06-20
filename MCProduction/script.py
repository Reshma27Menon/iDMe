input_file = 'premix_files.txt'
output_file = 'premix_files_prefixed.txt'

prefix = 'root://cmsxrootd.fnal.gov/'

with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
    for line in fin:
        line = line.strip()
        if not line.startswith(prefix):
            line = prefix + line
        fout.write(line + '\n')

