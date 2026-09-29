import math


def main():
    print("Program Persamaan Kuadrat ax^2 + bx + c = 0")
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))
    c = float(input("Masukkan nilai c: "))

    if a == 0:
        print("Bukan persamaan kuadrat karena a harus bukan 0.")
    else:
        diskriminan = b**2 - 4 * a * c
        print(f"Diskriminan (D) = {diskriminan:g}")

        if diskriminan > 0:
            akar_1 = (-b + math.sqrt(diskriminan)) / (2 * a)
            akar_2 = (-b - math.sqrt(diskriminan)) / (2 * a)
            print("D > 0: memiliki dua akar real berbeda.")
            print(f"x1 = {akar_1:g}")
            print(f"x2 = {akar_2:g}")
        elif diskriminan == 0:
            akar = -b / (2 * a)
            print("D = 0: memiliki satu akar real kembar.")
            print(f"x1 = x2 = {akar:g}")
        else:
            print("D < 0: tidak memiliki akar real.")


if __name__ == "__main__":
    main()
