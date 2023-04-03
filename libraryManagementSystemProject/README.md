Github Readme dosyanıza eklemek için sınıf şemasını bir görsel olarak hazırlayabilirsiniz. Bunun için pyreverse adlı bir Python aracını kullanabilirsiniz.

Öncelikle, projenizin Python dosyalarının bulunduğu klasöre geçin ve aşağıdaki komutu çalıştırın:

pyreverse -o png -p kütüphane_yönetim_sistemi kütüphane.py kitap.py kullanıcı.py odunc_kitap.py

Bu komut, kütüphane.py, kitap.py, kullanıcı.py ve odunc_kitap.py dosyalarını içeren bir paket olan kütüphane_yönetim_sistemi isimli bir sınıf şeması oluşturacaktır. -o png seçeneği, çıktının PNG formatında olacağını belirtir. -p seçeneği, oluşturulacak sınıf şemasının ismini belirtir.

Bu komutu çalıştırdıktan sonra, kütüphane_yönetim_sistemi.png adlı bir görsel dosyası oluşacaktır. Bu dosyayı Readme dosyanıza eklemek için, Github hesabınıza dosyayı yükleyip Markdown formatında ![](kütüphane_yönetim_sistemi.png) şeklinde görseli çağırabilirsiniz.

Böylece, Github Readme dosyanızda projenizin sınıf şemasını gösteren bir görsel yer alacaktır.
