#!/usr/local/bin/bash
python3 anno_reg.py NSD12DKO_ATAC.csv NSD12DKO_ATAC.promoter.bed NSD12DKO_ATAC.intergenic.bed NSD12DKO_ATAC.intron.bed
python3 anno_reg.py PA_ATAC.csv PA_ATAC.promoter.bed PA_ATAC.intergenic.bed PA_ATAC.intron.bed
python3 anno_reg.py K36M_ATAC.csv K36M_ATAC.promoter.bed K36M_ATAC.intergenic.bed K36M_ATAC.intron.bed

