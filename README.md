# DEGs
trinity + rsem +edgeR
###Trimmomatic 对双端测序的RNA数据进行过滤,trimmomatic可以conda安装
输入为双端测序文件
输出结果为paired和unpaired的结果，保留paired的结果进行后续实验
####trinity+rsem对表达量进行计算
首先用get_map.py脚本获得map文件。###python3 get_map.py -infile cds_file -outfile map_file
然后运行trinity+rsem
将上述得到的目录中的结果文件中RSEM.genes.results更改为样本的名字，后将样本名字按每行每个列到一个文件中
将所有文件放在一个目录
最后用get gene express profile 获得表达谱用于后续的差异表达分析#### -input 样本名字文件 -output 输出文件的前缀
共输出两个文件，一个为counts，一个为FPKMs
用counts进行后续的edgeR分析，计算差异表达基因，默认的PValue<0.05 logFC >1##edgeR默认需要重复，以及主要分组
导出文件后，自己根据最后一列，grep出down和up genes
