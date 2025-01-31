# FASTQ-BaseStats
Tool to Count Every type of Bases Present in the FASTQ file with txt and Frequency Barplot 
This is applicable to both Short and Long Read FASTQ file. If your FASTQ file is gzipped, make sure its unzipped. Use pigz -d -p <no of threads> <your fastq file path>

## Sample Output 
Base    Count
A       40160918  \n

C       46209207
G       46098045
T       40245144

![Basetasts_CK29976-EP1_S304_R1_001](https://github.com/user-attachments/assets/d26f5e45-67bf-4346-903b-ba25155a0817)


## Usage
```sh
python BaseStats.py <Enter your FASTQ file Path>


### New Heading
