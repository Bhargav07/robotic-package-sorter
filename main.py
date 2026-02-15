from sorter import sort

if __name__ == "__main__":
    examples = [
        (10, 10, 10, 5),
        (200, 50, 50, 10),
        (100, 100, 100, 25),
    ]

    for w, h, l, m in examples:
        result = sort(w, h, l, m)
        print(f"{(w, h, l, m)} -> {result}")