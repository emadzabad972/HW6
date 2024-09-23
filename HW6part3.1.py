# start
max_stars: int = int(input("type a number: "))
stars: int = 1
while stars <= max_stars:
    print(f"{'*' * stars:^{max_stars}}")
    stars += 2

# end
print()
# start

max_stars: int = int(input("whats your max stars? "))
stars: int = 1
spaces: int = max_stars // 2

for stars in range(1, max_stars + 2, 2):
    for _ in range(1, spaces + 1):
        print(" ", end="")
    for _ in range(1, stars + 1):
        print("*", end="")
    print()
    spaces -= 1
# end