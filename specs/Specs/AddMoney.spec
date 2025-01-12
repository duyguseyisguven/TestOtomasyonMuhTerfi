Add Money Scenarios
=====================

* "duygu.seyis@testinium.com" mail adresi ve "Df.080119" şifresiyle login olunur
* Open Money Transfer Butonuna Tıklanır
* Elementi bekle "HomePageTransferMoneyButon"

Gecmis Expiry Date Tarihiyle Para İşleminde Hata Atma Kontrolü
------------------------------------------------------------
tags:gecmisExpiryDateTarihiyleParaIslemindeHataAtmaKontrolu
* "MyAccountAmount" elementinden alınan value değerini "amountValueString" değişkenine kaydet
* Add Money Butonuna Tıklanır
* Add Money Modülünde "1234123412341234" Kart Numarası,"test test" Kart Sahibi,"1020" Geçerlilik Tarihi,"110" Cvv Girilir
* Add Money Modülünde "100" Amount Girilir ve "addamount"'e Kaydedilir
* Add Money Modülünde Add Butonuna Tıklanır
* "5000" milisaniye bekle
* Kaydedilen "amountValueString" deger "MyAccountAmount" elementinde hala aynı mı

Dort Hane Cvv Verisiyle Para Isleminde Hata Atma Kontrolu
---------------------------------------------------------
tags:dortHaneCvvVerisiyleParaIslemindeHataAtmaKontrolu
* "MyAccountAmount" elementinden alınan value değerini "amountValueString" değişkenine kaydet
* Add Money Butonuna Tıklanır
* Add Money Modülünde "1234123412341234" Kart Numarası,"test test" Kart Sahibi,"1026" Geçerlilik Tarihi,"1110" Cvv Girilir
* Ekrana alert geldi mi?

17 Haneli Kart Numarası Girilince Gelen Hata Kontrolü
-----------------------------------------------------
tags:onYediHaneliKartNumarasiGirilinceGelenHataKontrolu
* "MyAccountAmount" elementinden alınan value değerini "amountValueString" değişkenine kaydet
* Add Money Butonuna Tıklanır
* Elementi bekle "AddMoneyCardNumberInput"
* "123412341234123412" textini "AddMoneyCardNumberInput" elemente yaz
* Element "TooLongText" var mı kontrol et yoksa hata mesajı ver "Too long hatası gelmedi"

Add Money Amount Sayi Harici Karakter Girilince Hata Kontrolü
-------------------------------------------------------------
tags:addMoneyAmountSayiHariciKarakterGirilinceHataKontrolü
* Add Money Butonuna Tıklanır
* Add Money Modülünde "1234123412341234" Kart Numarası,"test test" Kart Sahibi,"1027" Geçerlilik Tarihi,"110" Cvv Girilir
* "y2" textini "AddMoneyAmount" elemente yaz
* Add Money Modülünde Add Butonuna Tıklanır
* Element "AmountErrorText" var mı kontrol et yoksa hata mesajı ver "amount must be a `number` type hatası gelmedi"

Add Money Card Holder 30 Karakterden Fazla Girince Hata Kontrolü
-----------------------------------------------------------------
tags:addMoneyCardHolderOtuzKarakterdenFazlaGirinceHataKontrolu
* Add Money Butonuna Tıklanır
* Elementi bekle "AddMoneyCardNumberInput"
* "1234123412341234" textini "AddMoneyCardNumberInput" elemente yaz
* "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu" textini "AddMoneyCardHolderInput" elemente yaz
* Ekrana gelen alert kabul edilir
* Element "TooLongText" var mı kontrol et yoksa hata mesajı ver "Too long hatası gelmedi"

//Sayfada hata olduğu için fail alması bekleniyor
Add Money Tutar Eklediğimde Home Page Amount Değerinin Doğru Bir Şekilde Güncellenmesi Kontrolü
-----------
tags:addMoneyTutarEkledigimdeHomePageAmountDegerininDogruBirSekildeGuncellenmesiKontrolu,reg
* "MyAccountAmount" elementinden alınan değeri noktalama işaretleri ve son üç karakter silinerek double olarak "amount" değişkenine kaydet
* Add Money Butonuna Tıklanır
* Add Money Modülünde "1234123412341234" Kart Numarası,"test test" Kart Sahibi,"1027" Geçerlilik Tarihi,"110" Cvv Girilir
* "AddMoneyAmount" elementinden alınan value değerini double olarak "addamount" değişkenine kaydet
* Elementine tıkla "AddMoneyAddButon"
* "5000" milisaniye bekle
* "amount" + "addamount" değişkenlerini topla ve arayüzde görünen amount ile "MyAccountAmount" eşit mi kontrol et

Add Money Kart Numarası Input ALanı Boş Bırakıldığında Hata Vermesi Kontrolü
-----------
tags:addMoneyKartNumarasiInputAlaniBosBirakildigindaHataVermesiKontrolu
* Add Money Butonuna Tıklanır
* Add Money Modülünde "" Kart Numarası,"test test" Kart Sahibi,"1027" Geçerlilik Tarihi,"110" Cvv Girilir
* Add Money Modülünde "100" Amount Girilir ve "addamount"'e Kaydedilir
* Add Money Modülünde Add Butonuna Tıklanır
* Elementi bekle "AddMoneyRequiredCardNumber"

Add Money Kart Sahibi Input Alanı Boş Bırakıldığında Hata Vermesi Kontrolü
---------------------
tags:addMoneyKartSahibiInputAlaniAlaniBosBirakildigindaHataVermesiKontrolu
* Add Money Butonuna Tıklanır
* Add Money Modülünde "1234123412341234" Kart Numarası,"" Kart Sahibi,"1027" Geçerlilik Tarihi,"110" Cvv Girilir
* Add Money Modülünde Add Butonuna Tıklanır
* Elementi bekle "AddMoneyRequiredCardHolder"

Add Money Expiry Date Input Alanı Boş Bırakıldığında Hata Vermesi Kontrolü
--------------------------
tags:addMoneyExpiryDateInputAlaniBosBirakildigindaHataVermesiKontrolu
* Add Money Butonuna Tıklanır
* Add Money Modülünde "1234123412341234" Kart Numarası,"test test" Kart Sahibi,"" Geçerlilik Tarihi,"110" Cvv Girilir
* Add Money Modülünde Add Butonuna Tıklanır
* Elementi bekle "AddMoneyRequiredExpiryDate"

Add Money Cvv Alanı Input Alanı Boş Bırakıldığında Hata Vermesi Kontrolü
------------------------------------------------------------------------
tags:addMoneyCvvInputAlaniBosBirakildigindaHataVermesiKontrolu
* Add Money Butonuna Tıklanır
* Add Money Modülünde "1234123412341234" Kart Numarası,"test test" Kart Sahibi,"1027" Geçerlilik Tarihi,"" Cvv Girilir
* Add Money Modülünde Add Butonuna Tıklanır
* Elementi bekle "AddMoneyRequiredCvv"

Add Money Amount Input Alanı Boş Bırakıldığında Hata Vermesi Kontrolü
---------------------------------------------------------------------
tags:addMoneyAmountInputAlaniBosBirakildigindaHataVermesiKontrolu
* Add Money Butonuna Tıklanır
* Add Money Modülünde "1234123412341234" Kart Numarası,"test test" Kart Sahibi,"1027" Geçerlilik Tarihi,"110" Cvv Girilir
* Add Money Modülünde Add Butonuna Tıklanır
* Elementi bekle "AddMoneyAmountCvv"

Add Money Amount Eklenen Tarih ve Saat Transactionda Doğru Geldiğinin Kontrolu
------------------------------------------------------------------------------
tags: AddMoneyEklenenTarihVeSaatTransactiondaDogruGeldigininKontrolu,reg
* Add Money Butonuna Tıklanır
* Add Money Modülünde "1234123412341234" Kart Numarası,"test test" Kart Sahibi,"1027" Geçerlilik Tarihi,"110" Cvv Girilir
* Add Money Modülünde "100" Amount Girilir ve "addamount"'e Kaydedilir
* "AddMoneyAddButon" elementine tıkla ardından güncel tarih ve saati "currentdate" değişkenine kaydet
* "1000" milisaniye bekle
* "HomePageTransactionTime" elementi "currentdate" değişken değerini içeriyor mu kontrol et

Add Money Geçersiz Ay Değeri Girildiginde Hata Vermesi Kontrolü
---------------------------------------------------------------
tags:addMoneyGecersizAyDegeriGirildigindeHataVermesiKontrolu
* Add Money Butonuna Tıklanır
* Add Money Modülünde "1234123412341234" Kart Numarası,"test test" Kart Sahibi,"1527" Geçerlilik Tarihi,"110" Cvv Girilir
* Add Money Modülünde "100" Amount Girilir ve "addamount"'e Kaydedilir
* Add Money Modülünde Add Butonuna Tıklanır
* Elementi bekle "AddMoneyWrongDate"

17 Haneli Kart Numarası Girildikten Sonra Sayfayı Kapatınca Hata Almadan Ana Sayfaya Yönlenme Kontrolü
-----------------------------------------------------
tags:onYediHaneliKartNumarasiGirildiktenSonraSayfayiKapatincaHataAlmadanAnaSayfayaYonlenmeKontrolu
* "MyAccountAmount" elementinden alınan value değerini "amountValueString" değişkenine kaydet
* Add Money Butonuna Tıklanır
* Elementi bekle "AddMoneyCardNumberInput"
* "123412341234123412" textini "AddMoneyCardNumberInput" elemente yaz
* Element "TooLongText" var mı kontrol et yoksa hata mesajı ver "Too long hatası gelmedi"
* Elementine tıkla "AddMoneyCloseButon" 
* Element yok mu kontrol et "AddMoneySomethingWentWrongHataMesaj"

Add Money Amount Değeri Maksimum 9 Karakterli Girilebileceği Kontrolü
------------------------------
tags:addMoneyAAmountDegeriMaksimumDokuzKarakterliGirilebilecegiKontrolu
* Add Money Butonuna Tıklanır
* Add Money Modülünde "1234123412341234" Kart Numarası,"test test" Kart Sahibi,"1127" Geçerlilik Tarihi,"110" Cvv Girilir
* "1212121212" textini "AddMoneyAmount" elemente yaz
* Ekrana alert geldi mi?

Add Money Amount Değeri Maksimum 10 Karakterli Girildiğinde Hata Verdiğinde Alerti Kapatarak Para Eklemeye Çalışıldığında Ekleyememesi Kontrolü
------------------------------
tags:addMoneyAAmountDegeriMaksimumOnKarakterliGirildigindeHataVerdigindeAlertiKapatarakParaEklemeyeCalisildigindaEkleyemesiKontrolu
* "MyAccountAmount" elementinden alınan value değerini "amountValueString" değişkenine kaydet
* Add Money Butonuna Tıklanır
* Add Money Modülünde "1234123412341234" Kart Numarası,"test test" Kart Sahibi,"1127" Geçerlilik Tarihi,"110" Cvv Girilir
* "1212121212" textini "AddMoneyAmount" elemente yaz
* Ekrana alert geldi mi?
* Ekrana gelen alert kabul edilir
* Add Money Modülünde Add Butonuna Tıklanır
* "5000" milisaniye bekle
* Kaydedilen "amountValueString" deger "MyAccountAmount" elementinde hala aynı mı






