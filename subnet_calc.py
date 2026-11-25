import ipaddress


def hitung_subnet():
    print("=" * 45)
    print("   IP & SUBNET CALCULATOR CLI - TKJ PROJECT")
    print("=" * 45)

    while True:
        input_ip = input(
            "\nMasukkan IP & CIDR (contoh: 192.168.10.5/24) atau 'q' untuk keluar: "
        ).strip()

        if input_ip.lower() == "q":
            print("Program selesai. Terima kasih!")
            break

        try:
            # strict=False memungkinkan input berupa IP host (bukan hanya Network ID)
            jaringan = ipaddress.IPv4Network(input_ip, strict=False)
            interface = ipaddress.IPv4Interface(input_ip)

            # Menghitung jumlah host yang bisa dipakai (total IP dikurangi Network & Broadcast)
            total_ip = jaringan.num_addresses
            host_valid = total_ip - 2 if total_ip > 2 else 0

            # Menentukan rentang IP Host pertama dan terakhir
            daftar_host = list(jaringan.hosts())
            host_pertama = daftar_host[0] if host_valid > 0 else "Tidak ada"
            host_terakhir = daftar_host[-1] if host_valid > 0 else "Tidak ada"

            print("\n--- HASIL ANALISIS JARINGAN ---")
            print(f"IP Address Input : {interface.ip}")
            print(f"Network ID       : {jaringan.network_address}")
            print(f"Broadcast ID     : {jaringan.broadcast_address}")
            print(f"Subnet Mask      : {jaringan.netmask}")
            print(f"Wildcard Mask    : {jaringan.hostmask}")
            print(f"Rentang Host     : {host_pertama} - {host_terakhir}")
            print(f"Total Host Valid : {host_valid} perangkat")
            print(
                f"Jenis IP         : {'Private (Lokal)' if jaringan.is_private else 'Public'}"
            )
            print("-" * 31)

        except ValueError:
            print(
                "[Error] Format IP atau CIDR tidak valid! Pastikan formatnya seperti 192.168.1.1/24"
            )


if __name__ == "__main__":
    hitung_subnet()
