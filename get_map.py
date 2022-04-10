import argparse

def get_map(cds_file):
    gene_ids = []
    with open(cds_file,"r") as f1:
        for line in f1:
            if ">" in line :
                gene_id = line.strip().strip(">")
                gene_ids.append(gene_id)
    return gene_ids
def write_map(gene_ids,out_file):
    with open(out_file,"w") as f1:
        for id in gene_ids:
            f1.write(id+"\t"+id+"\n")
                    
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("-infile", type=str)#cds_file
parser.add_argument("-outfile", type=str)#out_file
args = parser.parse_args()  

cds_file = args.infile
out_file = args.out
gene_ids = get_map(cds_file)
write_map(gene_ids,out_file)
