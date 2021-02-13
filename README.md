### Linkedin Marketing Api ile Şirket Sayfası Üzerinde Gönderi Paylaşmak

Başlıklar

- LinkedIn Developers platform üzerinde uygulama oluşturma.
- Linkdun App üzerinde kullanılacak erişim kodunu Linkedin'den elde etme.
- Uygulamayı çalıştırma

### LinkedIn Developers platform üzerinde uygulama oluşturma.

LinkedIn Uygulamanızı oluşturmak için aşağıda yer alan bağlantıya tıklayın.

`https://www.linkedin.com/developers/`

"Uygulama oluştur" butonuna tıklayın.

bot-1

İstenen verileri sağlayın

bot-2

"Verify" butonuna tıklayarak linkedin sayfanızı doğrulayın.

bot-3

"Generate URL" butonuna tıklayın ve LinkedIn tarafından istenen birkaç adımı tamamlayın.

Product sayfasını açın, Share on LinkedIn ve Marketing Developer Platform  uygulamalarını aktif edin.

- Share on LinkedIn profilinizi yönetmek içindir.
- Marketing Developer Platform sayfanızı yönetmek içindir.

bot-4

Marketing Developer Platformu kullanmak için linkedin'e bir form göndermeniz gerekiyor. Bu form Linkedin tarafından 2 iş günü içerisinde onaylanır.

### Linkdun App üzerinde kullanılacak erişim kodunu Linkedin'den elde etme.

Auth sekmesine tıklayın Client ID ve the Client Secret bilgilerini not alın.

bot-5

Uygulamanızın yetkilendirme adresini ayarlayın. (google.com olarak kullanabilirsiniz)

bot-6

Aşağıdaki bağlantıyı kendinize göre düzenleyin ve tarayıcınızda ziyaret edin. Eğer her şeyi doğru yaptıysanız karşınıza linkedin login ekranı gelecektir.

```
https://www.linkedin.com/oauth/v2/authorization?
response_type=code&
client_id=sizin_client_id_niz&
redirect_uri=https://www.cyberdetails.org/&
state=istediginiz_bir_deger_onemli_degil&
scope=w_member_social,r_liteprofile,w_organization_social
```

NOT : redirect_uri kısmında belirttiğiniz adrese yönlendiriliceksiniz. Bu adresin auth penceresindeki adres ile aynı olduğundan emin olun.
Örnek : https://ww.cyberdetails.org/?code=sizin_kodunuz&state=istediginiz_bir_deger_onemli_degil

Linkedin bilgilerinizi girin ve "Oturum Aç" butonuna tıklayın.

bot-7

Code parametresinden gelen değeri not alın.

Access Tokenı almak için aşağıdaki istegi POST olarak "Content-Type:application/x-www-form-urlencoded" şeklinde gönderin. (Postman kullanarak bu isteği gönderebilirsiniz)

```
https://www.linkedin.com/oauth/v2/accessToken?
grant_type=authorization_code&
client_id=sizin_client_id_niz&
client_secret=sizin_secret_id_niz&
redirect_uri=https://ww.cyberdetails.org/&
code=yukarıdaki_get_isteginden_gelen_CODE_degeri
```

postman-1
postman-2

İsteği gönderdikten sonra Access_token parametresinden dönen değeri kopyalayın ve not edin.

access-token

### Uygulamayı çalıştırma

Linkdun App'in 2 bilgiye ihtiyacı vardır.

- Access Token (Bu değeri aldık)
- Organization ID (Şirket ID'si)

Organization ID'yi şirket sayfanızı ziyaret ederek alabilirsiniz.

`
https://www.linkedin.com/company/<organizationID>/admin/
`

Elde etiğimiz 2 değeri Linkdun App'a verelim ve sendPostJustText fonksiyonunu çalıştıralım. (run methoduna bakabilirsiniz)

code

post
