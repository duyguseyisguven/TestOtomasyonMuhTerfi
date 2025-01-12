Test Otomasyon Projesi
Bu projede, Selenium ve Gauge (BDD) kullanılarak geliştirilmiş bir test otomasyon projesidir.
Yazılım dili olarak Java tercih edilmiştir.

İçindekiler
Hakkında
Bağımlılıklar
Tag Yapılandırması
Kurulum
Versiyon Bilgileri
Proje Hakkında
Bu projede, money app transfer uygulaması için test senaryolarını otomatizasyonu hedeflenmiştir.

Proje Özellikleri:
Selenium WebDriver kullanılarak web tarayıcıları üzerinde test otomasyonu yapılır.
Gauge BDD frameworkü kullanılarak test senaryoları yazılır.
Maven ile bağımlılıklar yönetilir ve proje yapılandırılır.

Bağımlılıklar
Projede kullanılan temel bağımlılıklar aşağıdaki gibidir:

<dependencies>
        
        <dependency>
            <groupId>com.thoughtworks.gauge</groupId>
            <artifactId>gauge-java</artifactId>
            <version>${gauge.version}</version>
            <scope>test</scope>
            <exclusions>
                <exclusion>
                    <groupId>com.google.guava</groupId>
                    <artifactId>guava</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-engine</artifactId>
            <version>5.1.0</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>io.rest-assured</groupId>
            <artifactId>rest-assured</artifactId>
            <version>4.3.3</version>
        </dependency>
        <dependency>
            <groupId>org.seleniumhq.selenium</groupId>
            <artifactId>selenium-java</artifactId>
            <version>${selenium.version}</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-log4j12</artifactId>
            <version>${log4j.version}</version>
        </dependency>
        <dependency>
            <groupId>com.google.code.gson</groupId>
            <artifactId>gson</artifactId>
            <version>${gson.version}</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.assertj</groupId>
            <artifactId>assertj-core</artifactId>
            <version>3.22.0</version>
            <scope>test</scope>
        </dependency>

        <dependency>
            <groupId>commons-lang</groupId>
            <artifactId>commons-lang</artifactId>
            <version>2.6</version>
            <scope>test</scope>
        </dependency>
   
    </dependencies>

Bağımlılıkları eklemek için Maven projenizin pom.xml dosyasına yukarıdaki kodu ekleyin.

Tag Yapılandırması
Gauge tagging özelliği kullanılarak ,reg altında kritik senaryolar gruplandırılmıştır

Senaryo Başlığı
tags: senaryoAdi ,reg

Gauge komutları ile belirli etiketlere sahip senaryolar çalıştırılabilir:
```bash
gauge run specs --tags "reg"
Kurulum
Projeyi çalıştırmak için aşağıdaki adımları izleyin:

Gereksinimler
Java (JDK 8 veya üstü)
Maven
Gauge
IDE
Çalıştırma Adımları
Bu repoyu klonlayın:

git clone https://github.com/kullanici_adiniz/proje_adi.git
Proje dizinine gidin:

cd proje_adi
Maven bağımlılıklarını yükleyin:

mvn clean install
Testleri çalıştırın:

gauge run specs
Versiyon Bilgileri
Araç	Versiyon
Selenium WebDriver	3.141.59
Gauge Framework	1.0.7
Java	8 ve üzeri
Maven	3.8.1 ve üzeri
Junit5	5.1.0
Log4j	2.8.8
