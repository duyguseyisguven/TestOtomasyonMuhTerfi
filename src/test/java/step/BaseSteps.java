package step;

import com.thoughtworks.gauge.Logger;
import io.restassured.response.Response;
import base.BaseTest;
import model.ElementInfo;
import org.junit.jupiter.api.Assertions;
import org.openqa.selenium.*;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;
import com.thoughtworks.gauge.Step;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

public class BaseSteps extends BaseTest {


    public static int DEFAULT_MAX_ITERATION_COUNT = 150;
    public static int DEFAULT_MILLISECOND_WAIT_AMOUNT = 100;
    private static String SAVED_ATTRIBUTE;
    public static Response response;

    public BaseSteps() {
        initMap(getFileList());
    }


    WebElement findElement(String key) {
        By infoParam = getElementInfoToBy(findElementInfoByKey(key));
        WebDriverWait webDriverWait = new WebDriverWait(driver, 30);
        WebElement webElement = webDriverWait
                .until(ExpectedConditions.presenceOfElementLocated(infoParam));
        ((JavascriptExecutor) driver).executeScript(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'})",
                webElement);
        return webElement;
    }

    Map<String, Double> dynamicVariables = new HashMap<>();
    Map<String, Integer> dynamicIntVariables = new HashMap<>();
    Map<String, String> dynamicStringVariables = new HashMap<>();

    public By getElementInfoToBy(ElementInfo elementInfo) {
        By by = null;
        if (elementInfo.getType().equals("css")) {
            by = By.cssSelector(elementInfo.getValue());
        } else if (elementInfo.getType().equals(("name"))) {
            by = By.name(elementInfo.getValue());
        } else if (elementInfo.getType().equals("id")) {
            by = By.id(elementInfo.getValue());
        } else if (elementInfo.getType().equals("xpath")) {
            by = By.xpath(elementInfo.getValue());
        } else if (elementInfo.getType().equals("linkText")) {
            by = By.linkText(elementInfo.getValue());
        } else if (elementInfo.getType().equals(("partialLinkText"))) {
            by = By.partialLinkText(elementInfo.getValue());
        }
        return by;
    }

    private void clickElement(WebElement element) {
        element.click();
    }

    private void hoverElement(WebElement element) {
        actions.moveToElement(element).build().perform();
    }

    private boolean isDisplayedBy(By by) {
        return driver.findElement(by).isDisplayed();
    }

    public static String getSavedAttribute() {
        return SAVED_ATTRIBUTE;
    }

    public WebElement findElementWithKey(String key) {
        return findElement(key);
    }

    public String getElementText(String key) {
        return findElement(key).getText();
    }

    public String getElementAttributeValue(String key, String attribute) {
        return findElement(key).getAttribute(attribute);
    }

    @Step("<long> milisaniye bekle")
    public void waitByMilliSeconds(long milliseconds) {
        try {
            logger.info(milliseconds + " milisaniye bekleniyor.");
            Thread.sleep(milliseconds);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    @Step("Elementi bekle <key>")
    public void checkElementExistsThenClickk(String key) {
        getElementWithKeyIfExists(key);
        logger.info(key + " elementine tıklandı.");
    }

    @Step("Elementine tıkla <key>")
    public void clickElement(String key) {
        if (!key.isEmpty()) {
            //hoverElement(findElement(key));
            clickElement(findElement(key));
            logger.info(key + " elementine tıklandı.");
        }
    }

    @Step("Element var mı kontrol et <key>")
    public WebElement getElementWithKeyIfExists(String key) {
        WebElement webElement;
        int loopCount = 0;
        while (loopCount < DEFAULT_MAX_ITERATION_COUNT) {
            try {
                webElement = findElementWithKey(key);
                logger.info(key + " elementi bulundu.");
                return webElement;
            } catch (WebDriverException e) {
            }
            loopCount++;
            waitByMilliSeconds(DEFAULT_MILLISECOND_WAIT_AMOUNT);
        }
        assertFalse(Boolean.parseBoolean("Element: '" + key + "' doesn't exist."));
        return null;
    }

    @Step("<key> elementinden alınan value değerini double olarak <variablename> değişkenine kaydet")
    public void saveVariable(String key, String variablename) {
        String inputvalue = findElement(key).getAttribute("value");
        double value = Double.parseDouble(inputvalue);
        dynamicVariables.put(variablename, value);
        logger.info(value + "değeri" + variablename + "değişkenine kaydedildi");
    }
    @Step("<key> elementinden alınan value değerini <variablename> değişkenine kaydet")
    public void saveVariableString(String key, String variablename) {
        String inputvalue = findElement(key).getText();

        dynamicStringVariables.put(variablename, inputvalue);
        logger.info(inputvalue + "değeri" + variablename + "değişkenine kaydedildi");
    }

    @Step("<key> elementinden alınan değeri noktalama işaretleri ve son üç karakter silinerek double olarak <variablename> değişkenine kaydet")
    public void saveVariablee(String key, String variablename) {
        WebElement element = findElement(key);
        String elementText = element.getText();
        String cleanElement = elementText.replace(",", "").replace(".00", "");
        double value = Double.parseDouble(cleanElement);
        dynamicVariables.put(variablename, value);
        logger.info(value + "değeri" + variablename + "değişkenine kaydedildi");
    }

    @Step("<variablename1> + <variablename2> değişkenlerini topla ve arayüzde görünen amount ile <key> eşit mi kontrol et")
    public void checkSumElement(String variablename1, String variablename2, String key) {
        double amount = (double) dynamicVariables.get(variablename1);
        double inputValue = (double) dynamicVariables.get(variablename2);

        double toplamDeger = amount + inputValue;

        DecimalFormatSymbols symbols = new DecimalFormatSymbols(Locale.US);
        symbols.setGroupingSeparator(',');
        symbols.setDecimalSeparator('.');
        DecimalFormat decimalFormat = new DecimalFormat("#,##0.00", symbols);
        String format = decimalFormat.format(toplamDeger);
        logger.info("Hesaplanan toplam değer" + format);

        String sonAmountText = findElement(key).getText();
        logger.info("Arayüzden alınan değer" + sonAmountText);
        assertEquals(format, sonAmountText,"Beklenen ve elde edilen değerler eşit değil");

    }

    @Step("<variablename1> - <variablename2> değişkenlerini çıkar ve arayüzde görünen amount ile <key> eşit mi kontrol et")
    public void checkMinesElement(String variablename1, String variablename2, String key) {
        double amount = dynamicVariables.get(variablename1);
        double inputValue = Double.parseDouble(variablename2);

        double toplamDeger = amount - inputValue;

        DecimalFormatSymbols symbols = new DecimalFormatSymbols(Locale.US);
        symbols.setGroupingSeparator(',');
        symbols.setDecimalSeparator('.');
        DecimalFormat decimalFormat = new DecimalFormat("#,##0.00", symbols);
        String format = decimalFormat.format(toplamDeger);
        logger.info("Hesaplanan toplam değer" + format);

        String sonAmountText = findElement(key).getText();
        logger.info("Arayüzden alınan değer" + sonAmountText);
        assertEquals(format, sonAmountText,"Beklenen ve elde edilen değerler eşit değil");
    }

    @Step("<key> alanı üzerinde CTRL+a tuşuna bas")
    public void clickCtrlA(String key) {
        findElement(key).click();
        Actions actions = new Actions(driver);
        actions.keyDown(Keys.CONTROL)
                .sendKeys("a")
                .keyUp(Keys.CONTROL)
                .perform();
    }

    @Step("<key> elementine tıkla ardından güncel tarih ve saati <variablename> değişkenine kaydet")
    public void getCurrentDateandClick(String key, String variablename) {
        findElement(key).click();
        LocalDateTime today = LocalDateTime.now();
        // Belirtilen formata göre tarihi formatla
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("DD-MM-YYYY HH:mm");
        String value = today.format(formatter);
        dynamicStringVariables.put(variablename, value);
        logger.info("Kaydedilen tarih:" + value);
    }

    @Step("<key> elementinin iki fazlasını <variablename> değişkenine kaydet")
    public void saveAmount(String key, String variablename) {
        int deger = (int) Double.parseDouble(findElement(key).getText().replace(",", "").replace(".00", ""));
        dynamicIntVariables.put(variablename, deger + 2);
        logger.info("Kaydedilen değer" + deger);

    }

    @Step("<key> alanına kaydedilen <variablename> değişken değerini yaz")
    public void sendSavedValue(String key, String variablename) {
        int deger = dynamicIntVariables.get(variablename);
        findElement(key).sendKeys(String.valueOf(deger));
    }

    @Step("<key> elementi <variablename> değişken değerini içeriyor mu kontrol et")
    public void getCurrentDateandClickkk(String key, String variablename) {
        String currentTime = findElement(key).getText();
        logger.info(dynamicStringVariables.get(variablename) + " : " + currentTime);
        assertTrue(currentTime.contains(dynamicStringVariables.get(variablename)), "Beklenen stering eşleşmesi hatalı");
    }

    @Step("Kaydedilen <variablename> deger <key> elementinde hala aynı mı")
    public void checkSavedValueStillSame(String variablename,String key) {
        assertEquals(findElement(key).getText(),dynamicStringVariables.get(variablename));
        logger.info(findElement(key).getText() + " : " + dynamicStringVariables.get(variablename));
    }

    @Step("<key> selecti altındaki random option boxi seçilir")
    public void selectRandomOption(String key) {
        Select dropdown = new Select(findElement(key));

        List<WebElement> options = dropdown.getOptions();

        Random random = new Random();
        int randomIndex = random.nextInt(options.size());

        dropdown.selectByIndex(randomIndex);
    }


    @Step("Element <key> var mı kontrol et yoksa hata mesajı ver <message>")
    public void getElementWithKeyIfExistsWithMessage(String key, String message) {
        ElementInfo elementInfo = findElementInfoByKey(key);
        By by = getElementInfoToBy(elementInfo);

        int loopCount = 0;
        while (loopCount < DEFAULT_MAX_ITERATION_COUNT) {
            if (driver.findElements(by).size() > 0) {
                logger.info(key + " elementi bulundu.");
                return;
            }
            loopCount++;
            waitByMilliSeconds(DEFAULT_MILLISECOND_WAIT_AMOUNT);
        }
        Assertions.fail(message);
    }

    @Step("<key> elementinin tarih ve ve zamanının <key2> elementinden sonra olduğunu kontrol et")
    public void isKeyTimeAfterKey2Time(String key, String key2) {
        try {
            SimpleDateFormat dateFormat = new SimpleDateFormat("dd-MM-yyyy HH:mm:ss");

            String keyElement = findElement(key).getText();
            Date keyTime = dateFormat.parse(keyElement);

            String keyElement2 = findElement(key2).getText();
            Date key2Time = dateFormat.parse(keyElement2);

            boolean result = keyTime.after(key2Time);

            assertTrue(result, "<key> alanındaki zaman, <key2> alanındaki zamandan sonra değildir.");

            Logger.info("<key> alanındaki zaman, <key2> alanındaki zamandan sonradır.");
        } catch (ParseException e) {
            Logger.info("Tarih formatı çözümlenemedi: " + e.getMessage());
            throw new AssertionError("Tarih formatı çözümlenemedi: " + e.getMessage());
        } catch (Exception e) {
            Logger.info("Hata: " + e.getMessage());
            throw new AssertionError("Hata: " + e.getMessage());
        }
    }

    @Step("Element yok mu kontrol et <key>")
    public void checkElementNotExists(String key) {
        ElementInfo elementInfo = findElementInfoByKey(key);
        By by = getElementInfoToBy(elementInfo);

        int loopCount = 0;
        while (loopCount < DEFAULT_MAX_ITERATION_COUNT) {
            if (driver.findElements(by).size() == 0) {
                logger.info(key + " elementinin olmadığı kontrol edildi.");
                return;
            }
            loopCount++;
            waitByMilliSeconds(DEFAULT_MILLISECOND_WAIT_AMOUNT);
        }
        Assertions.fail("Element '" + key + "' still exist.");
    }


    @Step("<text> textini <key> elemente yaz")
    public void ssendKeys(String text, String key) {
        if (!key.equals("")) {
            findElement(key).sendKeys(text);
            logger.info(key + " elementine " + text + " texti yazıldı.");
        }
    }

    @Step("Ekrana gelen alert kabul edilir")
    public void acceptAlert() {
        try {
            Alert alert = driver.switchTo().alert();
            alert.accept(); // Alert'i kabul eder
            logger.info("Alert kabul edildi.");
        } catch (NoAlertPresentException e) {
            logger.info("Alert bulunamadı: " + e.getMessage());
        }
    }
    @Step("Ekrana alert geldi mi?")
    public boolean isAlertPresent() {
        try {
            driver.switchTo().alert();
            logger.info("Alert mevcut.");
            return true;
        } catch (NoAlertPresentException e) {
            logger.info("Alert mevcut değil.");
            return false;
        }
    }

    @Step({"Check if element <key> contains text <expectedText>",
            "<key> elementi <text> değerini içeriyor mu kontrol et"})
    public void checkElementContainsText(String key, String expectedText) {
        Boolean containsText = findElement(key).getText().contains(expectedText);
        assertTrue(containsText, "Expected text is not contained");
        logger.info(key + " elementi " + expectedText + " değerini içeriyor.");
    }
}