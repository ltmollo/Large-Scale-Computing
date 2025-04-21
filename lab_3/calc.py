import re

def parse_time_to_hours(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h + m / 60 + s / 3600

file_path = "hpc-jobs-history.txt"

total_cpu_hours = 0
total_efficiency = 0
job_count = 0

with open(file_path, "r") as file:
    for line in file:
        # ID   Name   Partition   Nodes   Cores   Decl._mem   Mem._%_usage   Eff. CPU._used   Wall._Used   Wall._Req.   End_Time
        match = re.search(r"(\d+)\s+\S+\s+\S+\s+\d+\s+(\d+)\s+\S+\s+\S+\s+(\S+)%\s+(\d+:\d+:\d+)\s+(\d+:\d+:\d+)", line)
        if match:
            cores = int(match.group(2))
            efficiency = float(match.group(3))
            cpu_time = parse_time_to_hours(match.group(4))
            print(match.group(1), match.group(2), match.group(3), match.group(4))
            total_cpu_hours += cpu_time
            total_efficiency += efficiency
            job_count += 1

average_efficiency = (total_efficiency / job_count) if job_count else 0


print(f"Total CPU-Hours Used: {total_cpu_hours:.2f} hours")
print(f"Average Efficiency: {average_efficiency:.2f}%")
