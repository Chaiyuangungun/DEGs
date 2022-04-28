import argparse

def get_genome_file(name_file):
    file_names = []
    with open(name_file,"r") as f1:
        for line in f1:
            file_names.append(line.strip())
    return file_names

def get_gene_counts_FPKMs(file_names):
    expression_file = {}
    expression_file["counts"] = {}
    expression_file["FPKMs"] = {}
    gene_ids = []
    for file in file_names:
        expression_file["counts"][file] = {}
        expression_file["FPKMs"][file] = {}
        with open(file,"r") as f1:
            for line in f1:
                lines = line.strip().split()
                if lines[0] == "gene_id":
                    continue
                gene_id = lines[0]
                counts = int(lines[-3])
                FPKMs = float(lines[-1])
                expression_file["counts"][file][gene_id] = counts
                expression_file["counts"][file][FPKMs] = FPKMs
                gene_ids.append(gene_id)
    gene_ids = list(set(gene_id))
    return gene_ids,expression_file

def write_out_file(gene_ids,expression_file,out_file):
    with open(out_file+".counts","w") as f1:
        f1.write("Gene_id"+"\t")
        for file in expression_file["counts"]:
            f1.write(file+"\t")
        f1.write("\n")
        for id in gene_ids:
            f1.write(id+"\t")
            for file in expression_file["counts"]:
                f1.write(str(expression_file["counts"][id])+"\t")
            f1.write("\n")
    with open(out_file+".FPKMs","w") as f2:
        f2.write("Gene_id"+"\t")
        for file in expression_file["FPKMs"]:
            f2.write(file+"\t")
        f2.write("\n")
        for id in gene_ids:
            f2.write(id+"\t")
            for file in expression_file["FPKMs"]:
                f2.write(str(expression_file["FPKMs"][id])+"\t")
            f2.write("\n")    

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("-input", type=str)#输入文件
parser.add_argument("-output", type=str)#输出文件
args = parser.parse_args()
name_file = args.input
out_file = args.output
file_names = get_genome_file(name_file)
gene_ids,expression_file = get_gene_counts_FPKMs(file_names)
write_out_file(gene_ids,expression_file,out_file)
