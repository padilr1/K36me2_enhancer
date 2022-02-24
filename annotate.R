using <- function(...) {
  libs <- unlist(list(...))
  need <- libs[!unlist(lapply(libs, require, character.only = T))]
  if(length(need) > 0){ 
    install.packages(need, repos = "https://cloud.r-project.org")
    need <- need[!unlist(lapply(need, require, character.only = T))]
    if (length(need) > 0) {
      if (!requireNamespace("BiocManager", quietly = T))
        install.packages("BiocManager")
      BiocManager::install(need)
    }
  }
}
using("ChIPseeker", "AnnotationDbi", "TxDb.Mmusculus.UCSC.mm10.knownGene", "org.Mm.eg.db",
      "dplyr", "data.table")
txdb <- TxDb.Mmusculus.UCSC.mm10.knownGene
options(ChIPseeker.ignore_1st_exon = TRUE)
options(ChIPseeker.ignore_1st_intron = TRUE)
options(ChIPseeker.ignore_downstream = TRUE)
options(ChIPseeker.ignore_promoter_subcategory = TRUE)

samplefiles <- list.files("~/Documents/K36me2_enhancer/ATACseq", pattern= ".bed", full.names=T)
samplefiles <- as.list(samplefiles)
names(samplefiles) <- c("K36M_ATAC","NSD12DKO_ATAC","PA_ATAC","SETD2KO_ATAC")
peakAnnolist <- lapply(samplefiles,annotatePeak,TxDb = txdb,tssRegion = c(-1000, 1000))

do_something <- function(data_path) {
  samplefiles <- list.files(data_path, pattern= ".bed", full.names=T)
  samplefiles <- as.list(samplefiles)
  peakAnnolist <- lapply(samplefiles,annotatePeak,TxDb = txdb,tssRegion = c(-1000, 1000))
  invisible(lapply(names(peakAnnolist),function(x) assign(x,peakAnnolist[[x]] %>% as.data.frame() %>% write.csv(paste0(x,".csv")),.GlobalEnv)))
}

do_something(snakemake@input[[1]])