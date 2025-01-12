Login Scenarios
=====================

Login Yanlış Şifre İle Login Olamama KOntrolü
--------------------------------------------
tags:loginYanlisSifreIleLoginOlamamaKontrolu
* "duygu.seyis@testinium.com" mail adresi ve "yanlisSifre" şifresiyle login olunur
* Elementi bekle "InvalidUserNameOrPasswordText"

Login Yanlış Mail İle Login Olamama KOntrolü
--------------------------------------------
tags:loginYanlisMailIleLoginOlamamaKontrolu
* "duygu.seyis@testiniummm.com" mail adresi ve "Df.080119" şifresiyle login olunur
* Elementi bekle "InvalidUserNameOrPasswordText"

Login Format Dışı Mail İle Login Olamama KOntrolü
--------------------------------------------
tags:loginFormatDisiMailIleLoginOlamamaKontrolu
* "duygu.seyis@asdf" mail adresi ve "Df.080119" şifresiyle login olunur
* Elementi bekle "InvalidUserNameOrPasswordText"

Logout Olabilme Kontrolü
----------------
tags:logoutOlabilmeKontrolu
* "duygu.seyis@testinium.com" mail adresi ve "Df.080119" şifresiyle login olunur
* Open Money Transfer Butonuna Tıklanır
* Elementine tıkla "BackButton"
* Elementine tıkla "LogoutButton"
* Element "LoginUserNameInput" var mı kontrol et yoksa hata mesajı ver "Login Sayfası Açılmadı"