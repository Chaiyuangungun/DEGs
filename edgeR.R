library( "edgeR" )
# 读取数据
counts <- read.table("input.counts", sep = "\t", header = T, row.names = 1)
# 创建分组
group <- c(rep(1,3),rep(2,3))#edgeR要求重复，这里设置为分组1为前三个，分组2为后三个，可以自己设置分组
#去除批次效应
#batch <- c(rep("1",3),rep("2",3))
#counts <- removeBatchEffect(counts, batch)
# 创建DGEList类型变量
y <- DGEList(counts=counts, group=group)
# 数据过滤
keep <- filterByExpr(y)
y <- y[keep, , keep.lib.sizes=FALSE]
# 计算标准化因子
y <- calcNormFactors(y,method="TMM")
# 计算离散度
y <- estimateDisp(y)
# 显著性检验
et <- exactTest(y)
# 获取排名靠前的基因，这里设置n=100000是为了输出所以基因
et <- topTags(et, n=100000)
# 转换为数据框类型
et <- as.data.frame(et)
# 将行名粘贴为数据框的第一列
et <- cbind(rownames(et),et)
# 指定列名
colnames(et) <- c("gene_id", "log2FoldChange", "log2CPM", "PValue", "FDR")
# 差异基因筛选
etSig <- et[which(et$PValue < 0.05 & abs(et$log2FoldChange) > 1),]
# 加入一列，up_down 体现上下调信息
etSig[which(etSig$log2FoldChange > 0), "up_down"] <- "Up"
etSig[which(etSig$log2FoldChange < 0), "up_down"] <- "Down"
# 保存文件
write.table(etSig, "out.gene.xls", sep = "\t",col.names = TRUE, row.names = FALSE, quote = FALSE, na = "")
