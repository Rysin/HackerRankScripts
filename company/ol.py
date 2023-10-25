def star_pattern_recursion(i):
    if i == 0:
        return None
    else:
        print(i * "X")
        return star_pattern_recursion(i - 1)


if __name__ == "__main__":
    star_pattern_recursion(5)
