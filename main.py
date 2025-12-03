#1-misol
yosh = int(input("Yoshingizni kiriting: "))

if yosh >= 18:
    print("Kattasiz")
else:
    print("Kattasiz emas")


#2-misol
a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))

if a > b:
    print("Birinchi son katta")
else:
    print("Ikkinchi son katta")


#3-misol
son = int(input("Son kiriting: "))

if son > 0:
    print("Musbat son")
else:
    print("Manfiy son")


#4-misol
raqam = int(input("Raqam kiriting: "))

if raqam < 10:
    print("10 dan kichik")
elif raqam == 10:
    print("10 ga teng")
else:
    print("10 dan katta")


#5-misol
x = int(input("Birinchi sonni kiriting: "))
y = int(input("Ikkinchi sonni kiriting: "))

if x == y:
    print("Sonlar teng")
else:
    print("Sonlar teng emas")


#6-misol
s = input("So'z kiriting: ")

if s == "hello":
    print("Salom!")
elif s == "bye":
    print("Xayr!")
else:
    print("Noma'lum so'z")
