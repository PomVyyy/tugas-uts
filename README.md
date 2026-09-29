# Program Persamaan Kuadrat dan Analisis Path Testing

## A. Source Code

```python
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
```

## B. Deskripsi Program

Program menerima koefisien `a`, `b`, dan `c` untuk persamaan `ax^2 + bx + c = 0`.
Program menolak input ketika `a = 0`, menghitung diskriminan `D = b^2 - 4ac`,
kemudian mengklasifikasikan dan menghitung akar sesuai nilai diskriminan.

## C. Node Program

| Node | Pernyataan |
|---|---|
| 1 | Mulai `main()` |
| 2 | Tampilkan judul dan baca `a`, `b`, `c` |
| 3 | Keputusan `a == 0` |
| 4 | Tampilkan pesan bukan persamaan kuadrat |
| 5 | Hitung dan tampilkan diskriminan |
| 6 | Keputusan `D > 0` |
| 7 | Hitung dua akar real |
| 8 | Tampilkan klasifikasi `D > 0` dan kedua akar |
| 9 | Keputusan `D == 0` |
| 10 | Hitung akar kembar |
| 11 | Tampilkan klasifikasi `D == 0` dan akar |
| 12 | Tampilkan klasifikasi `D < 0` |
| 13 | Selesai |

Node 2 mencakup tiga operasi input berurutan. Node 7 dan 8, serta node 10 dan
11, dipisahkan agar perhitungan dan keluaran pada source code terlihat jelas.

## D. Decision dan Kondisi

| Decision | Kondisi True | Kondisi False |
|---|---|---|
| D1 | `a == 0` menuju node 4 | `a != 0` menuju node 5 |
| D2 | `D > 0` menuju node 7 | `D <= 0` menuju node 9 |
| D3 | `D == 0` menuju node 10 | `D < 0` menuju node 12 |

D2 dan D3 hanya dijalankan jika D1 bernilai false. Pada source code, `D2`
menggunakan `if`, sedangkan D3 menggunakan `elif`.

## E. Control Flow Graph (CFG)

```mermaid
flowchart TD
    N1([1 Mulai]) --> N2[2 Input a, b, c]
    N2 --> N3{3 a == 0?}
    N3 -- Ya --> N4[4 Tampilkan bukan kuadrat]
    N4 --> N13([13 Selesai])
    N3 -- Tidak --> N5[5 Hitung dan tampilkan D]
    N5 --> N6{6 D > 0?}
    N6 -- Ya --> N7[7 Hitung dua akar real]
    N7 --> N8[8 Tampilkan dua akar]
    N8 --> N13
    N6 -- Tidak --> N9{9 D == 0?}
    N9 -- Ya --> N10[10 Hitung akar kembar]
    N10 --> N11[11 Tampilkan akar kembar]
    N11 --> N13
    N9 -- Tidak --> N12[12 Tampilkan tidak ada akar real]
    N12 --> N13
```

CFG memiliki satu node awal (1), satu node akhir (13), dan tiga node
keputusan (3, 6, 9). Semua edge pada diagram mengikuti urutan eksekusi source
code.

## F. Cyclomatic Complexity

Cyclomatic complexity dihitung dengan dua cara berikut:

1. Berdasarkan jumlah decision: `V(G) = jumlah decision + 1 = 3 + 1 = 4`.
2. Berdasarkan edge dan node: `V(G) = E - N + 2 = 15 - 13 + 2 = 4` bila
   semua node pada tabel dihitung satu per satu.

Agar perhitungan konsisten dengan CFG, node output yang selalu berurutan
digabung sebagai satu blok dasar: node 7-8 menjadi satu blok dan node 10-11
menjadi satu blok. Dengan demikian CFG dasar memiliki `N = 11`, `E = 13`,
dan `V(G) = 13 - 11 + 2 = 4`. Nilai cyclomatic complexity program adalah
**4**, sesuai dengan tiga decision pada source code.

## G. Independent Path

Empat independent path yang mencakup setiap outcome decision adalah:

| Path | Urutan node | Kondisi |
|---|---|---|
| P1 | 1-2-3-4-13 | `a == 0` |
| P2 | 1-2-3-5-6-7-8-13 | `a != 0` dan `D > 0` |
| P3 | 1-2-3-5-6-9-10-11-13 | `a != 0` dan `D == 0` |
| P4 | 1-2-3-5-6-9-12-13 | `a != 0` dan `D < 0` |

P1 adalah jalur validasi, sedangkan P2-P4 adalah tiga klasifikasi
diskriminan. Keempat jalur membentuk basis path untuk `V(G) = 4`.

## H. Test Case Path Testing

| Test case | Input `a, b, c` | Diharapkan | Path |
|---|---|---|---|
| TC1 | `0, 2, 1` | Pesan bukan persamaan kuadrat | P1 |
| TC2 | `1, -5, 6` | `D = 1`, akar `3` dan `2` | P2 |
| TC3 | `1, 2, 1` | `D = 0`, akar kembar `-1` | P3 |
| TC4 | `1, 2, 5` | `D = -16`, tidak ada akar real | P4 |

## I. Expected Output

### TC1

```text
Bukan persamaan kuadrat karena a harus bukan 0.
```

### TC2

```text
Diskriminan (D) = 1
D > 0: memiliki dua akar real berbeda.
x1 = 3
x2 = 2
```

### TC3

```text
Diskriminan (D) = 0
D = 0: memiliki satu akar real kembar.
x1 = x2 = -1
```

### TC4

```text
Diskriminan (D) = -16
D < 0: tidak memiliki akar real.
```

Baris judul dan tiga baris prompt input tidak ditampilkan pada cuplikan agar
fokus pada keluaran program setelah input diberikan.

## J. Kesimpulan Path Testing

Empat jalur independen berhasil menguji validasi `a`, kasus dua akar real,
akar real kembar, dan tidak adanya akar real. Setiap decision serta seluruh
klasifikasi diskriminan pada source code tercakup, sehingga path testing
memberikan cakupan cabang yang lengkap untuk program ini.
