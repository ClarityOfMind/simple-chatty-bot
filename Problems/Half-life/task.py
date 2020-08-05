initial_atom_count = int(input())
final_atom_count = int(input())
half_life_count = 0

while initial_atom_count > final_atom_count:
    initial_atom_count /= 2
    half_life_count += 1
print(half_life_count * 12)
