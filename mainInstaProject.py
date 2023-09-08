import instaloader


usrName = input("Enter Username: ")  # Kullanıcıdan işlem yapacağı kullanıcı adını aldık.

x = instaloader.Instaloader()


def getUserId():  # Kullanıcı ID ceken fonksiyon.
    global user_id
    global usrName
    profile = instaloader.Profile.from_username(x.context, usrName)
    user_id = profile.userid


def downloadProfilePic():  # Kullanıcı pp indiren fonksiyon.
    x.download_profile(usrName , profile_pic_only=True)


def newUser():  # Farklı kullanıcı adı seçmemizi sağlayan fonksiyon.
    global usrName
    newUserInput = input("Enter New Username: ")
    usrName = newUserInput

def userFallowers():  # Takipçi sayısını çeken fonksiyon.
    global usrName
    profile = instaloader.Profile.from_username(x.context, usrName)
    return profile.followers

def userFollowing():  # Takip edilen kişi sayısını çeken fonksiyon.
    global usrName
    profile = instaloader.Profile.from_username(x.context, usrName)
    return profile.followees

def userPost():  # Post sayısını gösteren fonksiyon.
    global usrName
    profile = instaloader.Profile.from_username(x.context, usrName)
    return profile.mediacount


while True:


    print("1 - Profil Fotograf Indir\n2 - Profil Id Goster\n3 - Post Sayisi Goster\n4 - Takipci Sayisi Goster\n5 - Takip Ettigi Kisi Sayisi Goster\n6 - Farkli Kulanici Adi Sec\n7 - Cikis")
    
    islem = int(input("Islem Seciniz (1 / 2 / 3 / 4 / 5 / 6 / 7) : "))

    if islem == 1:
        try:
            downloadProfilePic()
            print("Islem Basarili! {} Kullanicisinin Profil Fotografi Basariyla Indirildi...".format(usrName))
        except instaloader.ProfileNotExistsException:
            print("İşlem Başarisiz! {} Kullanicisinin Profil Fotoğrafi İndirilemedi.".format(usrName))

    elif islem == 2:
        getUserId()
        print("{} Kullanicisinin Profil ID :".format(usrName) , user_id)

    elif islem == 3:
        usrPost = userPost()
        print("{} Kullanicisinin Paylastigi Gönderi Sayisi :{}".format(usrName, usrPost))

    elif islem == 4:
        usrFallowers = userFallowers()
        print("{} Kullanicisinin Takipci Sayisi :{}".format(usrName , usrFallowers))

    elif islem == 5:
        usrFollowing = userFollowing()
        print("{} Kullanicisinin Takip Ettigi Kisi Sayisi :{}".format(usrName, usrFollowing))

    elif islem == 6:
            newUser()
   
    elif islem == 7:
        break

    else:
        print("Lütfen Gecerli Islem Numarasi Giriniz!!!")
        
   




 


