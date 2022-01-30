def ekstraksi_data():
    """
    Tanggal : 30 Januari 2022
    Waktu : 04:17:13 WIB
    Magnitudo : 4.2
    Kedalaman : 14 km
    Lokasi : 2.42 LS - 140.15 BT
    Pusat gempa :  berada di darat 33 km Barat Laut Kab. Jayapura
    Dirasakan :  (Skala MMI): II Genyem
    """
    hasil = dict()
    hasil['tanggal'] = '30 Januari 2022'
    hasil['waktu'] = '04:17:13 WIB'
    hasil['magnitudo'] = 4.2
    hasil['kedalaman'] = '14 km'
    hasil['lokasi'] = {'LS': 2.42, 'BT': 140.15}
    hasil['pusat gempa'] = 'berada di darat 33 km Barat Laut Kab. Jayapura'
    hasil['dirasakan'] = '(Skala MMI): II Genyem'

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['LS']}, BT={result['lokasi']['BT']}")
    print(f"Pusat Gempa {result['pusat gempa']}")
    print(f"Dirasakan {result['dirasakan']}")
