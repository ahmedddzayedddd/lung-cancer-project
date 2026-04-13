id="bio_script"
import os

# Example SRA IDs
sra_ids = [
    "SRR25403874",
    "SRR25403875"
]

for sra in sra_ids:
    print(f"Downloading {sra}...")
    
    # download
    os.system(f"prefetch {sra}")
    
    # convert to FASTQ
    os.system(f"fastq-dump --split-files {sra}")

print("Done!")