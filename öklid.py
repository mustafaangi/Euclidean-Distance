import math

def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

points = []
i = 1


while True:
    try:
        girdi = input(f"{i}. nokta için x ve y değerlerini virgülle ayırarak girin (Örnek: 1,2): ")
        x, y = map(int, girdi.split(',')) 
        point = (x, y) 
        points.append(point)  
        i += 1
        devam = input("Başka nokta eklemek istiyor musunuz? (e/h): ")
        if devam.lower() != 'e':
            break
    except ValueError:
        print("Geçersiz giriş. Lütfen virgülle ayrılmış iki sayı girin.")


distances = []
for i in range(1, len(points)):
    distance = euclideanDistance(points[i-1], points[i])
    distances.append(distance)


print("Girdiğiniz noktalar:", points)
print("Girilen noktalar arasındaki mesafeler:", distances)


if distances:
    print("En kısa mesafe:", min(distances))
else:
    print("Yeterli nokta girilmedi.")