# Oyuncular hakkında bilgiler

Merhaba. Çevrimiçi oyun için bir platform oluşturuyoruz ve oyuncularımız hakkındaki bilgileri depolamak, işlemek, kullanmak için yardıma ihtiyacımız var. Bu yıl size uygulamanız için birkaç görev vereceğiz; bu, bunlardan ilki. README.md dosyasına her zaman bakmayı unutmayın - içinde ayrıntılı gereksinimleri ve ipuçlarını bulacaksınız!

## GÖREV 1. Gamer sınıfının iyileştirilmesi ve kullanıcı verilerinin eklenmesi aracı
Gamer sınıfını zaten oluşturduk. Bu sınıf, kullanıcılar hakkında adları, yaşları ve favori oyunları gibi bilgileri işlememizi sağlayacak. Bu bilgiler, oyuncunun yeni arkadaşlar edinmesine olanak tanıyan düzenli bir sunum olarak gösterilecek! Ancak, bir sorun var - kullanıcının takma adı ve e-posta için alanlar eklemeyi unuttuk... Bu görevde ekibimize yardımcı olabilir misiniz? Eğer öyleyse, işte görev kontrol listesi ve bazı ipuçları!


### GÖREV 1 Kontrol Listesi
 - [ ] Oyuncu sınıfını iyileştirin -  **nickname** ve **email** alanlarını ekleyin
 - [ ] Mini sunum mesajını, yeni verileri içerecek şekilde düzenleyin
 - [ ] Kodun isteğimizi karşıladığından emin olmak için hazırladığımız **Pytest testi** ile kodu test edin!

## Testler Hakkında

### Pytest testi
Kodun uyumluluğunu otomatik olarak kontrol eden testler yazdık:
-   `test_Gorev_1_ad_ve_yas_kontrol`: "Gamer" sınıfının hala "name" ve "age" niteliklerine sahip olduğunu kontrol ediyoruz.
-   `test_Gorev_2_ekle_takmaad`: "Gamer" sınıfına "nickname" niteliğinin eklendiğini kontrol ediyoruz.
-   `test_Gorev_3_ekle_eposta`: "Gamer" sınıfına "email" niteliğinin eklendiğini kontrol ediyoruz.
-   `test_Task_4_degistir_mesaj`: Oyuncunun mini sunumu için bilgi çıktısını test ediyoruz.

## Tavsiyeler

### Python sınıfları

#### 1. Bir sınıf tanımlamak:
```python
class SinifAdi:
    def __init__(self, parametreler):
        # Sınıf kurucusu
        self.alan1 = deger1
        self.alan2 = deger2
        # ...

    def metot(self, parametreler):
        # Metodun tanımlanması
        # ...

# Örnek:
class Hayvan:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def tanitim(self):
        print(f"Merhaba, benim adım {self.ad} ve ben {self.yas} yaşındayım.")
```
#### 2. Sınıf örneklerinin oluşturulması:
```python
# Sınıf örneği oluşturma
nesne = SinifAdi(argumanlar)

# Örnek:
kedi = Hayvan("Boncuk", 3)
```
#### 3. Bir sınıfa alan ekleme:
```python
# Bir sınıfa yeni alanlar ekleme
nesne.yeniAlan = deger

# Example:
kedi.renk = "turuncu"
```
#### 4. Bir projede bir sınıf kullanma:
```python
# Bir sınıfın metotlarını ve alanlarını kullanma
nesne.metot(argumanlar) 
deger = nesne.alan

# Örnek:
kedi.tanitim()
print(kedi.renk)
```
