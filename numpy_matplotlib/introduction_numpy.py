import numpy as np

# tek boyutlu dizi
x = np.array([1, 2, 3], np.uint16)
print(x)
print(type(x))
print(x[0])
print(x[1])
print(x[2])
print(x[-1])
print("2 boyutlar---------")
# İki boyutlu diziler
y = np.array([[1, 2, 3], [4, 5, 6]], np.int8)
print(y)
print(y[0][1])
print(y[0, 1])
print("----------")

# sadece sütunlara erişmek istiyorsak
print(y[:, 0])  # tüm diziyi tara istenilen sütunları al
print(y[:, 2])
print("---------")
print(y[0, :])  # tüm satırları çeker örneğin 0. satırın tüm elemanlarını getirir
print("3 boyutlar---------")

# üç boyutlu diziler
z = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], np.int16)

print(z)
print(z[1, 1, 0])
print(z[1][1][2])

print("ndarray ------------------")
# ndarray n dimensional array yani n boyutlu dizi demektir

q = np.array([[-2, -1, 0, 5], [9, 4, 5, 7]], np.int8)
print(q)

print(q.shape)  # dizi satır ve sütun 2x4 olduğunu söyler
print(
    q.ndim)  # kaç boyut olduğunu verir örnek olarak bu 2 boyutlu bir dizi (2,2,4)verirse ilki kaç tane düzlem olduğu diğer 2,4 ise boyutları
print(q.dtype)  # data type verir
print(q.size)  # elaman sayısını verir
print(q.transpose())  # transpozunu verir yani satır = sütun yapar

# farklı dizi oluşturma yöntemleri
print("farklı dizi oluşturma yöntemleri---------------")
w = np.empty([3, 3], np.int8)  # 3 e 3 lük bir dizi oluşturuyor random sayı atıyor
print(w)
print("----------")
e = np.full((3, 3, 3), dtype=np.int16, fill_value=5)
print(e)
print("----------")

ones = np.ones((2, 5, 5), dtype=np.int8)  # beyaz ekran
print(ones)
print("----------")

zeros = np.zeros((2, 3, 4), dtype=np.int8)  # siyah ekran
print(zeros)
