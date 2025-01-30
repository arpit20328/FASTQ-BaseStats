import subprocess
import matplotlib.pyplot as plt

def count_bases(fastq_file, threads):
    counts = {
        'A': 0, 'T': 0, 'C': 0, 'G': 0, 'N': 0,
        'R': 0, 'Y': 0, 'S': 0, 'W': 0, 'K': 0, 'M': 0,
        'B': 0, 'D': 0, 'H': 0, 'V': 0,
        '.': 0, '-': 0
    }

    seqkit_command = ["seqkit", "fx2tab", "--threads", str(threads), fastq_file]
    process = subprocess.Popen(seqkit_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    for line in process.stdout:
        for base in line.strip():
            if base in counts:
                counts[base] += 1

    process.wait()
    return counts


def plot_counts(counts):
    bases = list(counts.keys())
    values = list(counts.values())

    plt.figure(figsize=(12, 6))
    plt.bar(bases, values, color='blue')
    plt.xlabel('Base')
    plt.ylabel('Count')
    plt.title('Counts of Different Bases in FASTQ File')
    plt.show()


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Count bases in FASTQ file and plot the counts")
    parser.add_argument("fastq_file", help="Input FASTQ file")
    parser.add_argument("--threads", type=int, default=4, help="Number of threads to use for reading the FASTQ file")
    args = parser.parse_args()

    counts = count_bases(args.fastq_file, args.threads)
    for base, count in counts.items():
        print(f"{base}: {count}")

    plot_counts(counts)


if __name__ == "__main__":
    main()
