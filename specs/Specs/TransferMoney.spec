Transfer Money Scenarios
=====================

* "duygu.seyis@testinium.com" mail adresi ve "Df.080119" şifresiyle login olunur
* Open Money Transfer Butonuna Tıklanır


Rastgele Receiver account seçilerek para transferi
--------------------------------------------------
tags:rastgeleReceiverAccountSecilerekParaTransferi
* Transfer Money Butonuna Tıklanır
* "ReceiveraccountSelectBox" selecti altındaki random option boxi seçilir
* Transfer Money Modülünde "100" Transfer Money Amount textbox'ina girilir
* Transfer Money Modülünde Send Butonuna Tıklanır


Eksi Para Transferi Yapamama Kontrolu
----------------
tags:eksiParaTransferiYapamamaKontrolu
* "MyAccountAmount" elementinden alınan value değerini "amountValueString" değişkenine kaydet
* Transfer Money Butonuna Tıklanır
* Transfer Money Modülünde "-200" Transfer Money Amount textbox'ina girilir
* Transfer Money Modülünde Send Butonuna Tıklanır
* Kaydedilen "amountValueString" deger "MyAccountAmount" elementinde hala aynı mı

Transfer Money Para Transfer Ettiğimde Home Page Amount Değerinin Doğru Bir Şekilde Güncellenmesi Kontrolü
--------------------------------------------------
tags:transferMoneyParaTransferEttigimdeHomePageAmountDegerininDogruBirSekildeGuncellenmesiKontrolu,reg
* "MyAccountAmount" elementinden alınan değeri noktalama işaretleri ve son üç karakter silinerek double olarak "amount" değişkenine kaydet
* Transfer Money Butonuna Tıklanır
* Transfer Money Modülünde "300" Transfer Money Amount textbox'ina girilir
* Transfer Money Modülünde Send Butonuna Tıklanır
* "amount" - "300" değişkenlerini çıkar ve arayüzde görünen amount ile "MyAccountAmount" eşit mi kontrol et

Transfer Money Yüksek Miktar Para Transferi
--------------------------
tags:transferMoneyYuksekMiktarParaTransferi
* "MyAccountAmount" elementinden alınan değeri noktalama işaretleri ve son üç karakter silinerek double olarak "amount" değişkenine kaydet
* Transfer Money Butonuna Tıklanır
* Transfer Money Modülünde "1234567890" Transfer Money Amount textbox'ina girilir
* Ekrana alert geldi mi?

Transfer Money Transfer Gerçekleştikten Sonra Bakiye Yetmiyorsa Devam Edilememesi Kontrolü
---------------------------------------
tags:transferMoneyTransferGerceklestiktenSonraBakiyeYetmiyorsaDevamEdilmemesiKontrolu,reg
* "MyAccountAmount" elementinden alınan value değerini "stringamount" değişkenine kaydet
* "MyAccountAmount" elementinin iki fazlasını "accountammount" değişkenine kaydet
* Transfer Money Butonuna Tıklanır
* "TransferMoneyAmountInput" alanına kaydedilen "accountammount" değişken değerini yaz
* Transfer Money Modülünde Send Butonuna Tıklanır
* Kaydedilen "stringamount" deger "MyAccountAmount" elementinde hala aynı mı

Transfer Money Amount Değeri Maksimum 10 Karakterli Girildiğinde Hata Verdiğinde Alerti Kapatarak Para Eklemeye Çalışıldığında Ekleyememesi Kontrolü
------------------------------
tags:addMoneyAAmountDegeriMaksimumOnKarakterliGirildigindeHataVerdigindeAlertiKapatarakParaEklemeyeCalisildigindaEkleyemesiKontrolu,reg
* "MyAccountAmount" elementinden alınan value değerini "amountValueString" değişkenine kaydet
* Transfer Money Butonuna Tıklanır
* Transfer Money Modülünde "300" Transfer Money Amount textbox'ina girilir
* Transfer Money Modülünde Send Butonuna Tıklanır
* "5000" milisaniye bekle
* Kaydedilen "amountValueString" deger "MyAccountAmount" elementinde hala aynı mı

