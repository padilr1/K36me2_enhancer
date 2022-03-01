import pandas as pd
import sys
import argparse
def annotate(x):
    with open(x,'r') as file:
        df = pd.read_csv(file)
        df_promoter = df.loc[df['annotation']=='Promoter']
        df_intergenic = df.loc[df['annotation']=='Distal Intergenic']
        df_intron = df.loc[df['annotation'].str.contains('Intron')]
        df_promoter = df_promoter.iloc[:, 1:4]
        df_intergenic = df_intergenic.iloc[: , 1:4]
        df_intron = df_intron.iloc[:, 1:4]
        return([df_promoter,df_intergenic,df_intron])
# set up argument parser
#parser = argparse.ArgumentParser(description="Annotate peaks from ChIPseeker output")
#parser.add_argument('inputfile',nargs='?',type=argparse.FileType('r'),default=sys.stdin,help='A csv file containing output from ChIPseeker',required=True)
#get list of dfs
df = annotate(sys.argv[1])
#split into several bed files
df_promoter = df[0]
df_intergenic = df[1]
df_intron = df[2]
# 1st argument is promoter
df_promoter.to_csv(sys.argv[2],sep="\t",index=False,header=False)
# 2nd argument is intron
df_intron.to_csv(sys.argv[3],sep="\t",index=False,header=False)
# 3rd argument is intergenic
df_intergenic.to_csv(sys.argv[4],sep="\t",index=False,header=False)
#
#def main(argv):
 #  inputfile = ''
 ##  outputfile = ''
 #  try:
  #    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
 #  except getopt.GetoptError:
  #    print('get_annotated_bed.py -i <inputfile> -o <outputfile>')
  #    sys.exit(2)
  # for opt, arg in opts:
   #   if opt == '-h':
    #     print('get_annotated_bed.py -i <inputfile> -o <outputfile>')
     #    sys.exit()
     # elif opt in ("-i", "--ifile"):
     #    df = annotate(inputfile)
      #   print("Annotated inputfile")
         #df.to_csv(outputfile,sep="\t",index=False,header=False)
         #inputfile = arg
         #outputfile = arg

#df = annotate(inputfile)

#df.to_csv(outputfile,sep="\t",index=False,header=False)

#if __name__ == "__main__":
  # main(sys.argv[1:])

#do_something(snakemake.input[0], snakemake.output[0], snakemake.threads, snakemake.config["myparam"])