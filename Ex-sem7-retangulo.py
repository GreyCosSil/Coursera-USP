largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

while largura<0 or altura<0:
    largura = int(input('digite a largura: '))
    altura = int(input('digite a altura: '))
    continue

y = 1
while y <= altura:
    x = 1
    while x <= largura:
        print('#', end = "")
        x += 1
    y += 1
    print("")