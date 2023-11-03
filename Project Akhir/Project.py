import os
import random
import json
from datetime import datetime
import pwinput
from prettytable import PrettyTable
import sys
os.system("cls")

json_path = "D:/Punya Rizky/Progamming/Coding/Project Akhir/database.json"
with open(json_path, "r") as jsondatabase:
        data = json.loads(jsondatabase.read())

def data_pt():
    table = PrettyTable()
    table.field_names = ["No", "Nama Panjang", "Username", "PIN", "No HP", "Saldo E-Money"]

    username = data["Username"]
    name_panjang = data["Nama_Panjang"]
    pin = data["PIN"]
    no_hp = data["No_HP"]
    saldo_emoney = data["Saldo_EMoney"]

    for i in range(len(username)):
        table.add_row([i + 1, name_panjang[i][0], username[i], pin[i], no_hp[i], saldo_emoney[i]])
    print(table)

def menu():
    print("    ╔══════════════════════════╗")
    print("     Selamat Datang Di DompetKu")
    print("              (っ˘ڡ˘ς)         ")
    print("    ╚══════════════════════════╝")
    print("╭▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╮")
    print("    Silakan Pilih Login/Sign Up")
    print(" 1. Login (Jika Sudah Punya akun)")
    print(" 2. Sign Up (Jika Belum Punya akun)")
    print("╰▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╯")

    while True:
        try:
            mode = input("• • ━━❪ヾ Silakan Pilih masukan sesuai menu Login(1)/Sign Up(2) : ")
            if mode == "1" or mode.lower() == "login":
                login()
            elif mode == "2" or mode.lower() == "sign up":
                daftar()
            else:
                print("Menu Tidak ada silakan pastikan diantara Login(1)/Sign Up(2)!")
            continue
        except KeyboardInterrupt:
            print("\n▰▰▰▰▰▰▰▰▰▰▰▰ Anda telah menekan Ctrl+C, Program akan keluar. ▰▰▰▰▰▰▰▰▰▰▰▰")
            sys.exit()

def login():
    os.system("cls")
    print("Masukan Username dan PIN anda!")
    with open(json_path, "r") as jsondatabase:
        data = json.loads(jsondatabase.read())

    login_username = data.get("Username")
    login_admin = data.get("Admin")
    login_pin = data.get("PIN")
    percobaan_login = 3
    
    try:
        for i in range(percobaan_login):
            input_username = input("Username : ")
            if input_username == login_admin.get("Username"):
                input_pin = pwinput.pwinput(prompt="PIN : ")
                if input_pin == login_admin.get("PIN"):
                    admin()
                else:
                    print("PIN Admin salah!")
            elif input_username in login_username:
                index = login_username.index(input_username)
                data_pin = login_pin[index]
                input_pin = int(pwinput.pwinput(prompt="PIN : "))
                if input_pin == data_pin:
                    pembeli(input_username)
                    break
                else:
                    print("PIN salah!")
            else:
                print("Username tidak valid. Silakan coba lagi.")
            if i == percobaan_login - 1:
                print("Anda telah menggunakan semua kesempatan login, Silakan Ulang kembali Program ᕙ(⇀‸↼‶)ᕗ.")
                sys.exit()
    except ValueError:
        print("MASUKIN DATANYA HARUS SESUAI YA BRO( ˘▽˘)っ♨")


def admin():
    while True:
        os.system("cls")
        print("࣪࣪࣪࣪࣪◇─◇──◇─────◇──◇─◇ Selamat Datang Admin! ◇─◇──◇─────◇──◇─◇")
        print("╔══════════════════╗")
        print("    Fitur Admin     ")
        print("╚══════════════════╝")
        print("╔══════════════════╗")
        print(" 1. Tambah Akun")
        print(" 2. Lihat Akun")
        print(" 3. Perbarui Akun")
        print(" 4. Hapus Akun")
        print(" 5. Keluar")
        print("╚══════════════════╝")
        input_admin = input("Pilih fitur yang anda inginkan : ")
        if input_admin == "1":
            tambah_akun()
        elif input_admin == "2":
            lihat_akun()
        elif input_admin == "3":
            perbarui_akun()
        elif input_admin == "4":
            hapus_akun()
        elif input_admin == "5":
            print("Terimakasih Telah Menggunakan Program ini sir Admin (づ ￣ ³￣)づ")
            sys.exit()
        else:
            print("Fitur yang anda pilih tidak ada silakan pilih nomor yang sesuai 1/2/3/4/5")
            os.system("pause")
        continue

def tambah_akun():
    while True:
        input_nama = input("Masukan Nama Panjang : ")
        input_username = input("Masukan Username : ")
        input_pin = int(input("Masukan PIN : "))
        input_noHP = int(input("Masukan Nomor HP : "))
        input_saldo = input("Masukan Saldo E-Money : ")

        if input_username in data["Username"]:
            print("Username sudah digunakan. Silakan gunakan username yang lain.")
            return

        data["Nama_Panjang"].append([input_nama])
        data["Username"].append(input_username)
        data["PIN"].append(int(input_pin))
        data["No_HP"].append(input_noHP)
        data["Saldo_EMoney"].append(input_saldo)

        with open(json_path, "w") as jsondatabase:
            json.dump(data, jsondatabase, indent=4)

        print("Mantap cuy akun berhasil ditambahkan ٩(◕‿◕)۶")

        input_lagi = input("Apakah Anda ingin menambahkan akun lagi? (y/n) ")
        if input_lagi.lower() == "y":
            tambah_akun()
        else:
            admin()

def lihat_akun():
    os.system("cls")
    data_pt()
    while True:
        input_back = input("Apakah anda ingin kembali ke fitur admin? (y/n) : ")
        if input_back == "y":
            admin()
        elif input_back == "n":
            admin()
        else:
            print("Pemilihan yang anda masukan tidak sesuai opsi, Pilih y/n")
        continue


def perbarui_akun():
    data_pt()
    input_username = input("Masukan Username yang ingin diubah : ")
    if input_username in data["Username"]:
        index = data["Username"].index(input_username)
        print("Akun yang ingin diperbarui:")
        print("◤━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◥")
        print("Pilih Informasi yang ingin diperbarui")
        print("◣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◢")
        print("╔═════════▣◎▣═════════╗")
        print(" 1. Nama Panjang")
        print(" 2. PIN")
        print(" 3. Nomor HP")
        print(" 4. Saldo E-Money")
        print(" 5. Kembali ke menu admin")
        print("╚═════════▣◎▣═════════╝")
        try:
                pilihan = input("Masukan Opsi Nomor Menu : ")
                if pilihan == "1":
                    nama_baru = input("Masukan Nama Panjang yang baru : ")
                    data["Nama_Panjang"][index] = [nama_baru]
                elif pilihan == "2":
                    pin_baru = int(input("Masukan PIN yang baru : "))
                    data["PIN"][index] = pin_baru
                elif pilihan == "3":
                    nomorhp_baru = (input("Masukan Nomor HP yang baru : "))
                    if nomorhp_baru.isdigit() and len(nomorhp_baru) == 12:
                        data["No_HP"][index] = nomorhp_baru
                    else:
                        print("Nomor HP tidak valid. Harus memiliki 12 digit.")
                elif pilihan == "4":
                    saldo = int(input("Masukan Saldo E-Money yang baru : "))
                    data["Saldo_EMoney"][index] = saldo
                elif pilihan == "5":
                    admin()
                else:
                    print("Fitur tidak ada, Silakan Pilih Fitur yang valid sesuai opsi!")
        except ValueError:
            print("Masukinnya harus sesuai")
            os.system("pause")
        data_pt()
        with open(json_path, "w") as jsondatabase:
            json.dump(data, jsondatabase, indent=4)
        print("Informasi akun telah diperbarui ( ˘▽˘)っ♨")
        os.system("pause")

def hapus_akun():
    while True:
        data_pt()
        input_user = input("Masukan Username yang ingin dihapus : ")

        if input_user in data["Username"]:
            index = data["Username"].index(input_user)
            data["Username"].pop(index)
            data["Nama_Panjang"].pop(index)
            data["PIN"].pop(index)
            data["No_HP"].pop(index)
            data["Saldo_EMoney"].pop(index)

            with open(json_path, "w") as jsondatabase:
                json.dump(data, jsondatabase, indent=4)

                print("Akun dengan username '{}' telah dihapus.".format(input_user))
            while True:
                input_perulangan = input("Apakah Anda ingin menghapus akun lagi? (y/n) : ")
                if input_perulangan.lower() == "y":
                    hapus_akun()
                elif input_perulangan.lower() == "n":
                    admin()
                else:
                    print("Operasi yang anda pilih tidak ada!")
                    continue
        else:
            print("Username tidak ditemukan. Silakan coba lagi.")

def pembeli(username):
    os.system("cls")
    if username in data.get("Username"):
        index = data.get("Username").index(username)
        full_name = data.get("Nama_Panjang")[index][0]
        saldo_emoney = data.get("Saldo_EMoney")[index]
        format_saldo = f"{saldo_emoney:,}"
        print(" ╔════════════════════════════════════════════════════╗")
        print(f"          Selamat Datang {full_name} ")
        print(" ╚════════════════════════════════════════════════════╝")
        print(f"        ◤ Saldo E-Money Anda: Rp.{format_saldo.replace(',', '.')} ◥")
        print(f"   ■□■□■□■□■□■□■□■ Menu Fitur ■□■□■□■□■□■□■□■")
        print( "   1. Transfer Saldo ")
        print( "   2. Isi Saldo ")
        print( "   3. Cek Informasi Akun ")
        print( "   4. Log Out ")
        print(" ╚════════════════════════════════════════════════════╝")

        while True:
            try:
                menu_pembeli = input("• • ━━❪ヾPilih fitur (1/2/3/4): ")
                if menu_pembeli == "1":
                    transfer_saldo(username)
                elif menu_pembeli == "2":
                    isi_saldo(username)
                elif menu_pembeli == "3":
                    cek_informasi_akun(username)
                elif menu_pembeli == "4":
                    logout()
                else:
                    print("Pilihan tidak valid. Silakan pilih fitur yang sesuai.")
            except KeyboardInterrupt:
                print("\n▰▰▰▰▰▰▰▰▰▰▰▰ Anda telah menekan Ctrl+C, Program akan keluar. ▰▰▰▰▰▰▰▰▰▰▰▰")
                sys.exit()

def transfer_saldo(username):
    os.system("cls")
    while True:
        print("◇─◇──◇─────◇──◇─◇ Transfer Saldo ◇─◇──◇─────◇──◇─◇")
        username_penerima = input("Masukkan Username penerima: ")

        if username_penerima not in data["Username"]:
            print("Username penerima tidak valid.")
            os.system("pause")
            pembeli(username)

        if username_penerima == username:
            print("Anda tidak dapat mentransfer ke diri sendiri.")
            os.system("pause")
            pembeli(username)

        index_penerima = data["Username"].index(username_penerima)
        index_pengirim = data["Username"].index(username)
        uang_pengirim = data["Saldo_EMoney"][index_pengirim]

        try:
            amount = int(input("Masukkan jumlah saldo yang ingin Anda transfer: "))
            if amount <= 0:
                print("Jumlah saldo harus lebih dari 0.")
                os.system("pause")
                transfer_saldo(username)
            if amount > uang_pengirim:
                print("Saldo tidak mencukupi.")
                os.system("pause")
                transfer_saldo(username)

            confirm = input(f"Konfirmasi transfer Rp.{amount:,} saldo ke {username_penerima}? (y/n): ")
            if confirm.lower() == "y":
                data["Saldo_EMoney"][index_penerima] += amount
                data["Saldo_EMoney"][index_pengirim] -= amount
                with open(json_path, "w") as jsondatabase:
                    json.dump(data, jsondatabase, indent=4)

                current_time = datetime.now()
                formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                invoice_content = invoice_output(formatted_time, amount, username, username_penerima)

                invoice_path = "D:/Punya Rizky/Progamming/Coding/Project Akhir/Invoice/invoice_transfer.txt"
                with open(invoice_path, "a") as invoice_file:
                    invoice_file.write(invoice_content + "\n")
                    invoice_path = "D:/Punya Rizky/Progamming/Coding/Project Akhir/Invoice/invoice_transfer.txt"
                    with open(invoice_path, "a") as invoice_file:
                        invoice_file.write(invoice_content)
                    print(invoice_content)
                os.system("pause")
                pembeli(username)
            else:
                print("Transfer dibatalkan.")
                os.system("pause")
                pembeli(username)
        except ValueError:
            print("Masukan harus berupa angka.")
            os.system("pause")
            transfer_saldo(username)

def isi_saldo(username):
    os.system("cls")
    print("◇─◇──◇─────◇──◇─◇ Isi Saldo ◇─◇──◇─────◇──◇─◇")
    try:
        amount = int(input("Masukkan jumlah saldo yang ingin Anda isi: "))
        if amount <= 0:
            print("Jumlah saldo harus lebih dari 0.")
            os.system("pause")
            isi_saldo(username)

        confirm = input(f"Konfirmasi pengisian Rp.{amount:,} saldo? (y/n): ")
        if confirm.lower() == "y":
            index_penerima = data["Username"].index(username)
            data["Saldo_EMoney"][index_penerima] += amount
            with open(json_path, "w") as jsondatabase:
                json.dump(data, jsondatabase, indent=4)
            print(f"Isi saldo berhasil. Saldo Anda sekarang: Rp.{data['Saldo_EMoney'][index_penerima]:,}")

            current_time = datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            invoice_content = invoice_isisaldo(formatted_time, amount,username)

            invoice_path = "D:/Punya Rizky/Progamming/Coding/Project Akhir/Invoice/invoice_isi_saldo.txt"
            with open(invoice_path, "a") as invoice_file:
                invoice_file.write(invoice_content + "\n")
            print(invoice_content)
            
            os.system("pause")
            pembeli(username)
        else:
            print("Pengisian saldo dibatalkan.")
            os.system("pause")
            pembeli(username)
    except ValueError:
        print("Masukan harus berupa angka.")
        os.system("pause")
        isi_saldo(username)


def cek_informasi_akun(username):
    os.system("cls")
    if username in data.get("Username"):
        index = data.get("Username").index(username)
        full_name = data.get("Nama_Panjang")[index][0]
        saldo_emoney = data.get("Saldo_EMoney")[index]
        if index < len(data.get("No_HP")):
            no_hp = data.get("No_HP")[index]
        else:
            no_hp = "Nomor HP tidak tersedia"

        format_saldo = f"{saldo_emoney:,}"
        print("╔══════════════════════════════════════╗")
        print(f"           Informasi Akun ")          
        print("╚══════════════════════════════════════╝")
        print(f"  Nama Panjang: {full_name} ")
        print("=========================================")
        print(f"  Username: {username}")
        print("=========================================")
        print(f"  Saldo E-Money: Rp.{format_saldo.replace(',', '.')}")
        print("=========================================")
        print(f"  Nomor HP: 0{no_hp}")
        os.system("pause")
        os.system("cls")
        pembeli(username)


def logout():
    os.system("cls")
    menu()


def daftar():
        os.system("cls")
        while True:
            try:
                print("▂ ▃ ▄ ▅ ▆ ▇ █ Sign Up Account █ ▇ ▆ ▅ ▄ ▃ ▂")

                input_nama = str(input("Masukan nama panjang anda : "))
                input_username = input("Masukan Username anda : ")
                if input_username in data["Username"]:
                    print("Username sudah digunakan. Silakan gunakan username yang lain.")
                    continue
                input_nohp = int(input("Masukan No HP anda : "))
                random_pin = generate_random_pin()

                data["Nama_Panjang"].append([input_nama])
                data["Username"].append(input_username)
                data["Saldo_EMoney"].append(0)
                data["No_HP"].append(str(input_nohp))
                data["PIN"].append(random_pin)

                os.system("cls")
                print("◇─◇──◇─────◇──◇─◇─◇─◇──◇─────◇──◇─◇─◇─◇──◇─────◇──◇─◇─◇─◇──◇─────◇──◇─◇")
                print(f"Selamat Datang {input_nama}, Dengan username {input_username} dan Nomor HP 0{input_nohp}")
                print("╔═════════════════════════════════════════════════════╗")
                print(f"  Saldo E-Money Anda: Rp.{data['Saldo_EMoney'][-1]:,}, HARAP MELAKUKAN PENGISIAN!")
                print("╚═════════════════════════════════════════════════════╝")
                print("╔═════════════════════════════════════════════════════╗")
                print(f"     PIN Anda adalah: {random_pin}, Jangan sampai lupa ya")
                print("╚═════════════════════════════════════════════════════╝")

                with open(json_path, "w") as jsondatabase:
                    json.dump(data, jsondatabase, indent=4)

                while True:
                    login_input = str(input("Apakah anda ingin login? (y/n) : "))
                    if login_input.lower() == "y":
                        login()
                    elif login_input.lower() == "n":
                        print("Terimakasih Telah Menggunakan Program Kami (づ ◕‿◕ )づ")
                        sys.exit()
                    else:
                        print("Pilihan tidak ada silakan ulang!")
            except ValueError:
                print("Inputan Harus Berupa Angka!")
                os.system("pause")

def generate_random_pin():
    return random.randint(100000, 999999)

def invoice_output(formatted_time, amount, username_pengirim, username_penerima):
    invoice_content = f"===== Detail Invoice =====\n"
    invoice_content += f"Waktu Transfer: {formatted_time}\n"
    invoice_content += f"Jumlah: Rp.{amount:,}\n"
    invoice_content += f"dari: {username_pengirim}\n"
    invoice_content += f"ke: {username_penerima}\n"
    invoice_content += f"===========================\n"
    invoice_content += f"Terimakasih Telah menggunakan program kami!\n"
    return invoice_content

def invoice_isisaldo(formatted_time, amount, username_penerima):
    invoice_content = f"===== Detail Invoice =====\n"
    invoice_content += f"Waktu Transfer: {formatted_time}\n"
    invoice_content += f"Jumlah: Rp.{amount:,}\n"
    invoice_content += f"Dikirim ke: {username_penerima}\n"
    invoice_content += f"===========================\n"
    invoice_content += f"Terimakasih Telah menggunakan program kami!\n"
    return invoice_content

menu()