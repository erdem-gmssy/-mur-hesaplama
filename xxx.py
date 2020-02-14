print (input("isim giriniz: "))
print (input("soyisim giriniz: "))

a = int(input("olduğunuz yılı giriniz: "))
b = int(input("olduğunuz ayı giriniz: "))
c = int(input("olduğunuz günü giriniz: "))
d = int(input("doğum yılı giriniz: "))
e = int(input("doğum ayı giriniz: "))
f = int(input("doğum günü giriniz: "))

print("örünüz = " , abs(a-d) ,"yıl", abs(b-e) ,"ay" , abs(c-f) , "gün" )
