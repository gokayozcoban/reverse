text = input("Write something: ")
print(text)
print(text[::-1])

dosya=open("ters çevir.txt","w")
print(text,file=dosya)
print(                         )
print(text[::-1],file=dosya)

dosya.close()



