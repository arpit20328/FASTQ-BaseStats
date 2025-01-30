from collections import defaultdict
import argparse
import gzip

def count_base_frequencies(fastq_file):
    base_counts = defaultdict(int)  # Dictionary to store base counts

    # Open the file (supports both .fastq and .fastq.gz)
    open_func = gzip.open if fastq_file.endswith(".gz") else open
    with open_func(fastq_file, "rt") as fq:
        line_count = 0
        for line in fq:
            line_count += 1
            if line_count % 4 == 2:  # 2nd line of each read (sequence)
                for base in line.strip():
                    base_counts[base] += 1  # Count each letter
    
    return base_counts


def main():
    parser = argparse.ArgumentParser(description="Count letter frequencies in FASTQ sequences (2nd line of each read)")
    parser.add_argument("fastq_file", help="Input FASTQ file")
    args = parser.parse_args()

    counts = count_base_frequencies(args.fastq_file)

    # Print results
    print("\nBase Frequency Counts:")
    for base, count in sorted(counts.items()):
        print(f"{base}: {count}")


if __name__ == "__main__":
    main()



import matplotlib.pyplot as plt

def plot_counts(counts):
    bases = list(counts.keys())
    values = list(counts.values())

    plt.figure(figsize=(10, 5))
    plt.bar(bases, values, color='blue')
    plt.xlabel('Base')
    plt.ylabel('Count')
    plt.title('Base Frequency in FASTQ Sequences')
    plt.show()
