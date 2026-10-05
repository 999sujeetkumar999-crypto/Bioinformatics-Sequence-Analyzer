
print("===== MUTATION ANALYSIS =====")

original = input("Enter original DNA sequence: ").upper().strip()
mutated = input("Enter mutated DNA sequence: ").upper().strip()

valid_bases = set("ATGC")

# Validate original sequence
if not set(original).issubset(valid_bases):
    print("Invalid original DNA sequence!")
    exit()

# Validate mutated sequence
if not set(mutated).issubset(valid_bases):
    print("Invalid mutated DNA sequence!")
    exit()

print("\nOriginal DNA :", original)
print("Mutated DNA  :", mutated)

mutations = []


common_length = min(len(original), len(mutated))

for i in range(common_length):

    if original[i] != mutated[i]:
        mutations.append(
            (i, original[i], mutated[i])
        )


print("\n===== MUTATIONS =====")

if mutations:
    for position, old_base, new_base in mutations:
        print(
            f"Position {position}: "
            f"{old_base} -> {new_base}"
        )
else:
    print("No substitution mutation found.")


if len(mutated) > len(original):
    print(
        "\nInsertion detected:",
        len(mutated) - len(original),
        "base(s)"
    )


elif len(original) > len(mutated):
    print(
        "\nDeletion detected:",
        len(original) - len(mutated),
        "base(s)"
    )

print("\nTotal substitutions:", len(mutations))
print("Original length:", len(original))
print("Mutated length:", len(mutated))