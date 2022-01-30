import requests
from bs4 import BeautifulSoup


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
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        tanggal_waktu = soup.find('span', {'class': 'waktu'})
        waktu = tanggal_waktu.text.split(', ')[1]
        tanggal = tanggal_waktu.text.split(', ')[0]

        hasil = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        inilah = hasil.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        LS = None
        BT = None
        pusat = None
        dirasakan = None
        for res in inilah:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                LS = koordinat[0]
                BT = koordinat[1]
            elif i == 4:
                pusat = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1


        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['lokasi'] = {'LS': LS, 'BT': BT}
        hasil['pusat gempa'] = pusat
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('tidak bisa menemukan data gempa terkini')
        return
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['LS']}, BT={result['lokasi']['BT']}")
    print(f"{result['pusat gempa']}")
    print(f"{result['dirasakan']}")
