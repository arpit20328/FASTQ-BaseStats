import matplotlib.pyplot as plt

def count_bases(fastq_file):
    counts = {
        'A': 0, 'T': 0, 'C': 0, 'G': 0, 'N': 0,
        'R': 0, 'Y': 0, 'S': 0, 'W': 0, 'K': 0, 'M': 0,
        'B': 0, 'D': 0, 'H': 0, 'V': 0,
        '.': 0, '-': 0
    }

    with open(fastq_file, 'r') as file:
        for line in file:
            if line.startswith('@') or line.startswith('+') or line.startswith('!'):
                continue
            for base in line.strip():
                if base in counts:
                    counts[base] += 1

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
    args = parser.parse_args()

    counts = count_bases(args.fastq_file)
    for base, count in counts.items():
        print(f"{base}: {count}")

    plot_counts(counts)


if __name__ == "__main__":
    main()
