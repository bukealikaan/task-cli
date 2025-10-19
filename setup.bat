@echo off

::Klasör Yolu
set "folder=C:\tasks"

::Klasörü oluştur (zaten varsa hata vermez)
mkdir "%folder%"

::Dosya oluştur ve içine örnek bir metin yaz
echo Made by Santa > "%folder%\tasks.txt"

::Kullanıcıya bilgi ver
echo "%folder%\tasks.txt" dosyası oluşturuldu
pause