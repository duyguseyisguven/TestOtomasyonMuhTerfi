HomePage Scenarios
=====================

* "duygu.seyis@testinium.com" mail adresi ve "Df.080119" şifresiyle login olunur
* Open Money Transfer Butonuna Tıklanır
* Elementi bekle "HomePageTransferMoneyButon"

Ana Sayfada Bulunan Butonların Tıklama Sonrası Doğru Alana Yönlendirmesi
------------------------------------------------------------------------
tags:anaSayfadaBulunanButonlarınTiklamaSonrasiDogruAlanaYonlendirmesi
* Elementi bekle "HomePageTransferMoneyButon"
* Elementine tıkla "HomePageTransferMoneyButon"
* Elementi bekle "TransferMoneySenderAccount"
* Elementi bekle "TransferMoneySendButon"
* Elementine tıkla "TransferMoneyCloseButon"
* Elementine tıkla "OpenAddMoneyButon"
* Elementi bekle "AddMoneyCardNumberInput"
* Elementine tıkla "AddMoneyCloseButon"
* Elementine tıkla "OpenEditAccountButon"
* Elementi bekle "EditAccountUpdateButon"
* Elementi bekle "EditAccountAccountNameInput"

Ana Sayfada Transaction Alanında En Son Yaptığım İşlemin Görünmesi Kontrolü
---------------
tags:transactionAlanindaEnSonYaptigimIsleminGorunmesiKontrolu
* Elementi bekle "HomePageTransferMoneyButon"
* "HomePageTransactionTime" elementinin tarih ve ve zamanının "HomePageIkinciTransactionTime" elementinden sonra olduğunu kontrol et