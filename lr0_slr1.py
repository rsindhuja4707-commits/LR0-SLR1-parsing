# LR(0) Items and SLR(1) Parsing Table

grammar = {
    "S": [["C", "C"]],
    "C": [["c", "C"], ["d"]]
}

print("Grammar:")
for lhs, rules in grammar.items():
    for rhs in rules:
        print(lhs, "->", " ".join(rhs))

print("\nLR(0) Items:")
print("I0:")
print("S' -> . S")
print("S  -> . C C")
print("C  -> . c C")
print("C  -> . d")

print("\nI1:")
print("S' -> S .")

print("\nI2:")
print("S -> C . C")
print("C -> . c C")
print("C -> . d")

print("\nSLR(1) Parsing Table:")
print("State | c  | d  | $      | S | C")
print("----------------------------------")
print("0     | s3 | s4 |        | 1 | 2")
print("1     |    |    | accept |   |")
print("2     | s3 | s4 |        |   | 5")
print("3     | s3 | s4 |        |   | 6")
print("4     |    |    | r3     |   |")
print("5     |    |    | r1     |   |")
print("6     |    |    | r2     |   |")