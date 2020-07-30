import subprocess

cows = subprocess.check_output(
    ["cowsay", '-l']).decode('utf-8').split()[4:]
cow_list = list(zip(cows, cows))
