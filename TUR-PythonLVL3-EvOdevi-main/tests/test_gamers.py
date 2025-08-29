import pytest
from gamers import Gamer


def test_Gorev_1_ad_ve_yas_kontrol():
    gamer = Gamer("Asil", 16, "SatiricKarma63", "asilturkekole@gmail.com")
    assert hasattr(gamer, 'name'), "Görev 1 tamamlanmadı. 'Gamer' sınıfı 'name' niteliğini içermiyor"
    assert hasattr(gamer, 'age'), "Görev 1 tamamlanmadı. 'Gamer' sınıfı 'age' niteliğini içermiyor"


def test_Gorev_2_ekle_takmaad():
    gamer = Gamer("Asil", 16, "SatiricKarma63", "asilturkekole@gmail.com")
    assert hasattr(gamer, 'nickname'), "Görev 2 tamamlanmadı. 'Gamer' sınıfı 'nickname' niteliğini içermiyor"


def test_Gorev_3_ekle_eposta():
    gamer = Gamer("Asil", 16, "SatiricKarma63", "asilturkekole@gmail.com")
    assert hasattr(gamer, 'email'), "Görev 3 tamamlanmadı. 'Gamer' sınıfı 'email' niteliğini içermiyor"


def test_Task_4_degistir_mesaj(capsys):
    gamer = Gamer("Asil", 16, "SatiricKarma63", "asilturkekole@gmail.com")
    gamer.introduce()
    captured = capsys.readouterr()
    expected_output = "Merhaba, bana Asil, ve ben 16 yaşındayım. Bana SatiricKarma63 diye hitap edebilirsin ve eğer bana ulaşmak istersen, e-posta adresim: asilturkekole@gmail.com."
    assert expected_output in captured.out, f"Görev 4 tamamlanmadı. Beklenen mesaj: {expected_output}, Alınan çıktı: {captured.out}"


if __name__ == "__main__":
    pytest.main(["-v"])
