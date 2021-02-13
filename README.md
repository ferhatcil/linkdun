<p align="center">
<img title="Linkdun" src="https://img.shields.io/badge/Linkdun-%20-SCRIPT?colorA=red&colorB=black&colorC=white&style=for-the-badge"></a>
</p>

<p align="center">
<a href="https://github.com/ferhatcil/linkdun"><img title="Linkdun" src="https://img.shields.io/badge/Tool-Linkdun-red.svg"></a>
<a href="https://github.com/ferhatcil/linkdun"><img title="Version" src="https://img.shields.io/badge/Version-1.0-red.svg?style=flat-square"></a>
</p>

<p align="center">  
<a href="https://github.com/ferhatcil/linkdun"><img title="Linkdun" width="450" height="225" src="https://media.npr.org/assets/img/2011/12/06/95527_d0239_wide-685eb6d0fd6783dbacf037c948ed2f605c9e9d97.jpg"></img></a>
</p>

<p align="center">
<a href="https://github.com/ferhatcil"><img title="Github" src="https://img.shields.io/badge/Ferhat%20%C3%87il-%20-red?style=for-the-badge&logo=github"></a>
<a href="https://www.youtube.com/channel/UCNFlGKonTAN9dfXgg_VrGoA"><img title="YouTube" src="https://img.shields.io/badge/Ferhat%20%C3%87il-%20-red?style=for-the-badge&logo=Youtube"></a>
</p>

<p align="center">
<a href="https://github.com/ferhatcil"><img title="Language" src="https://img.shields.io/badge/Made%20with-Python-yellowgreen"></a>
<a href="https://github.com/ferhatcil"><img title="Followers" src="https://img.shields.io/github/followers/ferhatcil?color=yellowgreen&style=flat-square"></a>
<a href="https://github.com/ferhatcil"><img title="Stars" src="https://img.shields.io/github/stars/ferhatcil/linkdun?color=yellowgreen&style=flat-square"></a>
<a href="https://github.com/ferhatcil"><img title="Forks" src="https://img.shields.io/github/forks/ferhatcil/linkdun?color=yellowgreen&style=flat-square"></a>
<a href="https://github.com/ferhatcil"><img title="Watching" src="https://img.shields.io/github/watchers/ferhatcil/linkdun?label=Watchers&color=yellowgreen&style=flat-square"></a>
<a href="https://github.com/ferhatcil"><img title="Licence" src="https://img.shields.io/badge/License-MIT-yellowgreen.svg"></a>
</p>

### Linkedin Marketing Api ile Şirket Sayfası Üzerinde Gönderi Paylaşmak

Başlıklar

- LinkedIn Developers platform üzerinde uygulama oluşturma.
- Linkdun App üzerinde kullanılacak erişim kodunu Linkedin'den elde etme.
- Uygulamayı çalıştırma

### LinkedIn Developers platform üzerinde uygulama oluşturma.

LinkedIn Uygulamanızı oluşturmak için aşağıda yer alan bağlantıya tıklayın.

`https://www.linkedin.com/developers/`

"Uygulama oluştur" butonuna tıklayın.

![cyberdetails.org](https://raw.githubusercontent.com/ferhatcil/linkdun/main/images/bot-1.PNG)

İstenen verileri sağlayın

![cyberdetails.org](https://raw.githubusercontent.com/ferhatcil/linkdun/main/images/bot-2.PNG)

"Verify" butonuna tıklayarak linkedin sayfanızı doğrulayın.

![cyberdetails.org](https://raw.githubusercontent.com/ferhatcil/linkdun/main/images/bot-3.PNG)

"Generate URL" butonuna tıklayın ve LinkedIn tarafından istenen birkaç adımı tamamlayın.

Product sayfasını açın, Share on LinkedIn ve Marketing Developer Platform  uygulamalarını aktif edin.

- Share on LinkedIn profilinizi yönetmek içindir.
- Marketing Developer Platform sayfanızı yönetmek içindir.

![cyberdetails.org](https://raw.githubusercontent.com/ferhatcil/linkdun/main/images/bot-4.PNG)

Marketing Developer Platformu kullanmak için linkedin'e bir form göndermeniz gerekiyor. Bu form Linkedin tarafından 2 iş günü içerisinde onaylanır.

### Linkdun App üzerinde kullanılacak erişim kodunu Linkedin'den elde etme.

Auth sekmesine tıklayın Client ID ve the Client Secret bilgilerini not alın.

![cyberdetails.org](https://raw.githubusercontent.com/ferhatcil/linkdun/main/images/bot-5.PNG)

Uygulamanızın yetkilendirme adresini ayarlayın. (google.com olarak kullanabilirsiniz)

![cyberdetails.org](https://raw.githubusercontent.com/ferhatcil/linkdun/main/images/bot-6.PNG)

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

![cyberdetails.org](https://raw.githubusercontent.com/ferhatcil/linkdun/main/images/bot-7.PNG)

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

![cyberdetails.org](https://raw.githubusercontent.com/ferhatcil/linkdun/main/images/postman-1.PNG)

![cyberdetails.org](https://raw.githubusercontent.com/ferhatcil/linkdun/main/images/postman-2.PNG)

İsteği gönderdikten sonra Access_token parametresinden dönen değeri kopyalayın ve not edin.

![cyberdetails.org](https://raw.githubusercontent.com/ferhatcil/linkdun/main/images/access-token.PNG)

### Uygulamayı çalıştırma

Linkdun App'in 2 bilgiye ihtiyacı vardır.

- Access Token (Bu değeri aldık)
- Organization ID (Şirket ID'si)

Organization ID'yi şirket sayfanızı ziyaret ederek alabilirsiniz.

`
https://www.linkedin.com/company/<organizationID>/admin/
`

Elde etiğimiz 2 değeri Linkdun App'a verelim ve sendPostJustText fonksiyonunu çalıştıralım. (run methoduna bakabilirsiniz)

![cyberdetails.org](https://raw.githubusercontent.com/ferhatcil/linkdun/main/images/code.PNG)

![cyberdetails.org](https://raw.githubusercontent.com/ferhatcil/linkdun/main/images/post.PNG)

<p align="center">
<a href="https://github.com/ferhatcil"><img title="Github" src="https://img.shields.io/badge/Ferhat%20%C3%87il-%20-red?style=for-the-badge&logo=github"></a>
<a href="https://www.youtube.com/channel/UCNFlGKonTAN9dfXgg_VrGoA"><img title="YouTube" src="https://img.shields.io/badge/Ferhat%20%C3%87il-%20-red?style=for-the-badge&logo=Youtube"></a>
<a href="https://www.linkedin.com/in/ferhatcil/"><img title="Linkedin" src="https://img.shields.io/badge/Ferhat%20%C3%87il-%20-red?style=for-the-badge&logo=Linkedin"></a>
<a href="https://packetstormsecurity.com/user/ferhatcil/"><img title="Packet storm" src="https://img.shields.io/badge/Packet%20storm-Ferhat%20%C3%87il-red?style=for-the-badge"></a>
</p>
