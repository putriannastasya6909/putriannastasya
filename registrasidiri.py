class RegistrasiData:

    def __init__(self):
        self.nik = ""
        self.nama = ""
        self.ttl = ""
        self.jenis_kelamin = ""
        self.alamat = ""
        self.rtrw = ""
        self.desa = ""
        self.kecamatan = ""
        self.kabupaten = ""
        self.agama = ""
        self.status = ""
        self.pekerjaan = ""
        self.kewarganegaraan = ""

    def input_data(self):
        print("\n=== INPUT DATA DIRI ===")

        self.nik = input("NIK                  : ")
        self.nama = input("Nama Lengkap         : ")
        self.ttl = input("Tempat/Tanggal Lahir : ")
        self.jenis_kelamin = input("Jenis Kelamin        : ")
        self.alamat = input("Alamat               : ")
        self.rtrw = input("RT/RW                : ")
        self.desa = input("Kelurahan/Desa       : ")
        self.kecamatan = input("Kecamatan            : ")
        self.kabupaten = input("Kabupaten            : ")
        self.agama = input("Agama                : ")
        self.status = input("Status Perkawinan    : ")
        self.pekerjaan = input("Pekerjaan            : ")
        self.kewarganegaraan = input("Kewarganegaraan      : ")

        print("\n data berhasil ditambahkan.")

    def tampil_data(self):
        if self.nama == "":
            print("\n data belum diinput.")
        else:
            print("\n" + "=" * 45)
            print("           PROFIL DATA DIRI")
            print("=" * 45)
            print("NIK                  :", self.nik)
            print("Nama Lengkap         :", self.nama)
            print("Tempat/Tanggal Lahir :", self.ttl)
            print("Jenis Kelamin        :", self.jenis_kelamin)
            print("Alamat               :", self.alamat)
            print("RT/RW                :", self.rtrw)
            print("Kelurahan/Desa       :", self.desa)
            print("Kecamatan            :", self.kecamatan)
            print("Kabupaten/Kota       :", self.kabupaten)
            print("Agama                :", self.agama)
            print("Status Perkawinan    :", self.status)
            print("Pekerjaan            :", self.pekerjaan)
            print("Kewarganegaraan      :", self.kewarganegaraan)
            print("=" * 45)

    def ubah_data(self):
        if self.nama == "":
            print("\nSilakan input  data terlebih dahulu.")
            return

        print("\n=== MENU UBAH DATA ===")
        print("1. NIK")
        print("2. Nama Lengkap")
        print("3. Tempat/Tanggal Lahir")
        print("4. Jenis Kelamin")
        print("5. Alamat")
        print("6. RT/RW")
        print("7. Kelurahan/Desa")
        print("8. Kecamatan")
        print("9. Kabupaten/Kota")
        print("10. Agama")
        print("11. Status Perkawinan")
        print("12. Pekerjaan")
        print("13. Kewarganegaraan")

        pilihan = input("Pilih data yang diubah: ")

        if pilihan == "1":
            self.nik = input("NIK : ")
        elif pilihan == "2":
            self.nama = input("Nama : ")
        elif pilihan == "3":
            self.ttl = input("Tempat/Tanggal Lahir : ")
        elif pilihan == "4":
            self.jenis_kelamin = input("Jenis Kelamin : ")
        elif pilihan == "5":
            self.alamat = input("Alamat : ")
        elif pilihan == "6":
            self.rtrw = input("RT/RW : ")
        elif pilihan == "7":
            self.kelurahan = input("Kelurahan/Desa : ")
        elif pilihan == "8":
            self.kecamatan = input("Kecamatan : ")
        elif pilihan == "9":
            self.kabupaten = input("Kabupaten/Kota : ")
        elif pilihan == "10":
            self.agama = input("Agama : ")
        elif pilihan == "11":
            self.status = input("Status Perkawinan : ")
        elif pilihan == "12":
            self.pekerjaan = input("Pekerjaan : ")
        elif pilihan == "13":
            self.kewarganegaraan = input("Kewarganegaraan : ")
        else:
            print("Pilihan tidak valid.")
            return

        print(" data berhasil diubah.")


    def menu(self):
        while True:
            print("\n=== MENU REGISTRASI DATA ===")
            print("1. Input Data")
            print("2. Tampilkan Data")
            print("3. Ubah Data")
            print("4. Keluar")

            pilihan = input("Pilih menu (1-4): ")

            if pilihan == "1":
                self.input_data()
            elif pilihan == "2":
                self.tampil_data()
            elif pilihan == "3":
                self.ubah_data()
            elif pilihan == "4":
                print("Program selesai.")
                break
            else:
                print("Pilihan salah, silakan coba lagi.")


data = RegistrasiData()
data.menu()
