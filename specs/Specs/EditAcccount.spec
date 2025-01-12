Edit Account Scenarios
=====================

* "duygu.seyis@testinium.com" mail adresi ve "Df.080119" şifresiyle login olunur
* Open Money Transfer Butonuna Tıklanır
* Elementi bekle "HomePageTransferMoneyButon"

Edit Account Hesap İsmimi Değiştiğimde Home Pagede Hesap İsminin Değiştiğinin Kontrolü
---------------------------------
tags:editAccountHesapIsmimiDegistigimdeHomePagedeHesapIsmininDegistigininKontrolu,reg
* Edit Account Butonuna Tıklanır
* Edit Account Modülünde Account Name Textbox'ı temizlenir ve "test test" texti girilir
* Edit Account Modülünde Update Butonuna Tıklanır
* "HomePageAccountNameText" elementi "test test" değerini içeriyor mu kontrol et
* Edit Account Butonuna Tıklanır
* Edit Account Modülünde Account Name Textbox'ı temizlenir ve "Duygu Seyis" texti girilir
* Edit Account Modülünde Update Butonuna Tıklanır
* "HomePageAccountNameText" elementi "Duygu Seyis" değerini içeriyor mu kontrol et

Edit Account Tek Karakter Girilememe KOntrolü
----------------------
tags:editAccountTekKarakterGirilememeKontrolu
* Edit Account Butonuna Tıklanır
* Edit Account Modülünde Account Name Textbox'ı temizlenir ve "t" texti girilir
* Edit Account Modülünde Update Butonuna Tıklanır
* "HomePageAccountNameText" elementi "Duygu Seyis" değerini içeriyor mu kontrol et

