### [ENGLISH](https://github.com/erdincyz/defter/blob/main/README_EN.md)

![GIF](https://raw.githubusercontent.com/erdincyz/gorseller/master/_defter/defter.gif)


### Hoşgeldiniz
İnşallah, **Defter** vakit buldukça ve ihtiyaç duyuldukça halen geliştirilmekte olan açık kaynak bir yazılımdır. 

* Sayfanın her hangi bir yerine çift tıklayıp, hızlıca not almak için,
* Şekiller diyagramlar çizmek için,
* İnternetlerden sürükle bırak veri toplamak için,
* Belli konulardaki toplanmış verileri bir araya toparlamak için kullanılabilir.
* Görsellik ön plandadır. Belgeye fotoğraf, video, (herhangi)dosya ekleyebilme ve browserdan (ve diğer yazılımlardan) kopyala yapıştır, sürükle bırak yazı(HMTL destekler),ekleyebilme desteği vardır.
* HTML içeren yazi nesnelerini, nesneye sağ tıklayınca açılan menüdeki **Web Sayfası Olarak** göster özelliğini kullanarak tekrar içerdiği linklere tıklanabilir hale getirebilirsiniz.
* Mesela sahneye taşıyacağınız, **veya** izlemekte olduğunuz bir videodan ekran görüntüsü alıp, sahneye yapıştıracağınız o resmin üzerine çift tıklayınca, resmin tıkladığınız noktasında bir metin kutusu oluşur. Böylece resmin üzerine de dilediğiniz kadar not alabilirsiniz. 
* Sahneyi veya tüm belgeyi PDF veya HTML dosyası olarak kaydedebilirsiniz.

**GPLv3** lisanslıdır.

**Birçok Bug (Hata)** ve **tam olarak eklenmemiş özellikler** içerir. İyice kurcalayıp denemeden **önemli işler** için kullanma**MA**nız tavsiye edilir.

**Bilinen hataları ve eklenmek niyetinde olunan özellikleri (şu an güncel olmamakla beraber)** bu sayfadaki **[Issues](https://github.com/erdincyz/defter/issues)** kısmından takip edebilirsiniz.

### KURULUM
Sisteminizde Python 3 ve PySide6 (>= 6.4) yüklü olması gerekiyor.

Python 3' ü [https://www.python.org/downloads/](https://www.python.org/downloads/) adresinden indirebilirsiniz.

Python 3 yüklü ise PySide6' yi komut satirindan
```
pip install -U PySide6

```
komutu ile kurabilirsiniz.

Daha sonra bu sayfadan indirdiginiz defter klasorune girip
```
cd defter
python3 defter.py
```
komutu ile programı çalıştırabilirsiniz.

### [YARDIM SAYFALARI](https://github.com/erdincyz/defter/wiki)

### Dosya Yapısı:
Uzantısı "def" olarak değiştirilmiş sıkıştırma oranı 1 olan zip dosyalarıdır. 
Zip dosyaları konteynır gibi kullanılmaktadır.
Dosyaları bir zip dosyası gibi açıp içindeki gömülü diger dosyalara erişebilirsiniz.
Ayrıca her dosya kaydedildiğinde, belgedeki her sayfa icin bir html dosyası da def icine kaydedilir.
def dosyasını bir klasore açıp içindeki html dosyalarını web gezgininide açarak da belgenize erişebilirsiniz.


### İpuçları
Kağıt kalemin yerini hiç bir şey tutmuyor.

Sisteminizde 7z veya zip yuklu ise ve komut satırından direkt erişilebilir ise, Defter dosyaları daha hızlı kaydedebiliyor.
Çünkü, 7z veya zip in desteklediği arşiv güncelleme özelliğini, python ile gelen zipfile modulu desteklememekte. 
(Arşiv güncelleme özelliği: Sadece eklenen veya değişen dosyaları tekrar diske yazıyor. Tüm dosyaları tekrar diske yazmaktan kurtarıyor. )


Defter ile ekran goruntusu alabilirsiniz, ama sisteminize bu iş içi yazılmış başka bir program varsa
onu kullanmanız önerilir. Mesela linuxta aşagıdaki komutu sistem çapında bir kısayola atayıp kullanabilirsiniz.
Aşağıdaki komut ekran goruntusunu panoya kopyalar. 
(Scrot yazılımı yüklü değilse öncelikle paket yöneticiniz ile kurmanız gerekiyor.)
scrot -s -q 100 '/tmp/foo.jpg' -e 'xclip -selection clipboard -t image/jpg -i $f'

Windows için: Win + Shift + S
OS X için: Command + Shift + 4

Defter panodan yapıştırmayı destekler. Yukardaki yöntemler veya tercih edeceğiniz başka yöntemler ile ekran görüntüsünü panoya kopyalayıp deftere yapıştırabilirsiniz.


### Teşekkürler.
