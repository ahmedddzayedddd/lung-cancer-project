from Bio import SeqIO
import os

# Example SRA IDs
sra_ids = [
    "SRR25403874",
    "SRR25403875"
]

for sra in sra_ids:
    print(f"Downloading {sra}...")
    os.system(f"prefetch {sra}")
    os.system(f"fastq-dump --split-files {sra}")

# Example Biopython usage
example_file = "SRR25403874_1.fastq"

if os.path.exists(example_file):
    count = 0
    for record in SeqIO.parse(example_file, "fastq"):
        count += 1
    print("Total reads in example file:", count)
else:
    print(f"{example_file} not found. Download first to parse it with Biopython.")