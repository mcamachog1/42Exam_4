#!/usr/bin/env python3

def rotate_right(arr: list, k: int) -> list:
    temp:list = arr[:]
    print(f"arr={arr}-temp={temp}")
    return temp


def main() -> None:
    print("hola!")
    rotate_right([1, 2, 3], 1)
  

if __name__ == "__main__":
    main()