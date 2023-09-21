gens = "TGTGTGTATAT"

parts = gens.split("ATG")

if len(parts) == 1:
    print("No start codon found")
    exit()

for i in range(1, len(parts)):
    end1 = parts[i].find("TAG")
    if end1 == -1:
        end1 = 999999999
    end2 = parts[i].find("TAA")
    if end2 == -1:
        end2 = 999999999
    end3 = parts[i].find("TGA")
    if end3 == -1:
        end3 = 999999999

    if end1 < end2 and end1 < end3 and end1 != -1:
        print(parts[i][:end1])
    elif end2 < end1 and end2 < end3 and end2 != -1:
        print(parts[i][:end2])
    elif end3 < end1 and end3 < end2 and end3 != -1:
        print(parts[i][:end3])
    else:
        print("No end codon found")
