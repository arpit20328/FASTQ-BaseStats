import argparse
import gzip
import time
from collections import defaultdict
import matplotlib.pyplot as plt
import os

def count_base_frequencies(fastq_file):
    base_counts = defaultdict(int)  # Dictionary to store base counts
    total_lines = sum(1 for line in open(fastq_file))  # Total number of lines in the file

    # Open the file (supports both .fastq and .fastq.gz)
    open_func = gzip.open if fastq_file.endswith(".gz") else open
    with open_func(fastq_file, "rt") as fq:
        line_count = 0
        start_time = time.time()  # Start time for remaining time calculation
        for line in fq:
            line_count += 1
            if line_count % 4 == 2:  # 2nd line of each read (sequence)
                for base in line.strip():
                    base_counts[base] += 1  # Count each letter

            # Update remaining time estimate after every 1000 lines
            if line_count % 1000 == 0:
                elapsed_time = time.time() - start_time
                lines_processed = line_count // 4
                lines_remaining = (total_lines // 4) - lines_processed
                if lines_processed > 0:
                    time_per_line = elapsed_time / lines_processed
                    remaining_time = time_per_line * lines_remaining
                    remaining_minutes = remaining_time / 60
                    print(f"\rProcessed {lines_processed}/{total_lines//4} reads - Estimated time remaining: {remaining_minutes:.2f} minutes", end="")

        print("\nProcessing complete!")
    
    return base_counts

def plot_base_frequencies(base_counts, fastq_file):
    # Plot the frequency of each base
    bases = list(base_counts.keys())
    counts = list(base_counts.values())

    plt.figure(figsize=(8, 6))
    plt.bar(bases, counts, color='skyblue')
    plt.xlabel('Base')
    plt.ylabel('Frequency')
    plt.title(f'Base Frequencies in {os.path.basename(fastq_file)}')

    # Save the plot as PNG file
    output_file = f"Basetasts_{os.path.basename(fastq_file)}.png"
    plt.savefig(output_file)
    plt.close()
    print(f"Plot saved as {output_file}")

def save_base_frequencies(base_counts, fastq_file):
    # Save the base frequencies to a text file
    output_file = f"Basetasts_{os.path.basename(fastq_file)}.txt"
    with open(output_file, "w") as f:
        f.write("Base\tCount\n")  # Write header
        for base, count in sorted(base_counts.items()):
            f.write(f"{base}\t{count}\n")  # Write each base and its count
        
        # Calculate total ATCG count (A + T + C + G)
        total_ATCG = sum(base_counts[base] for base in ['A', 'T', 'C', 'G'])
        f.write(f"\nTotal_ATCG: {total_ATCG}\n")
        
    print(f"Data saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Count letter frequencies in FASTQ sequences (2nd line of each read)")
    parser.add_argument("fastq_file", help="Input FASTQ file")
    args = parser.parse_args()

    counts = count_base_frequencies(args.fastq_file)

    # Print results
    print("\nBase Frequency Counts:")
    for base, count in sorted(counts.items()):
        print(f"{base}: {count}")

    # Calculate and print total ATCG
    total_ATCG = sum(counts[base] for base in ['A', 'T', 'C', 'G'])
    print(f"\nTotal_ATCG: {total_ATCG}")

    # Plot the base frequencies
    plot_base_frequencies(counts, args.fastq_file)

    # Save the base frequencies to a text file
    save_base_frequencies(counts, args.fastq_file)

if __name__ == "__main__":
    main()
