# op  =1 12 123 1234 12345
def seq_gen(n):
    sequence = ""
    for i in range(1, n + 1):
        sequence += str(sequence) + str(i) + " "
    return sequence.strip()

output = seq_gen(5)
print(output)