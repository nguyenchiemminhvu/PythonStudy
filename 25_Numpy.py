import os
import numpy

if __name__ == "__main__":
    print(numpy.zeros(3))
    print(numpy.ones(3))
    print(numpy.empty(3))
    print(numpy.arange(0, 10, 1))
    print(numpy.arange(0, 10, 2))
    print(numpy.arange(0, 10, 3))
    print(numpy.linspace(0, 10, 1))
    print(numpy.linspace(0, 10, 2))
    print(numpy.linspace(0, 10, 3))
    
    arr = numpy.array([2, 4, 1, 3, 6, 5, 8, 0])
    print(arr)
    arr = numpy.sort(arr)
    print(arr)
    arr = numpy.concatenate((arr, arr))
    print(arr)
    arr = arr.reshape(2, 8)
    print(arr)
    arr = arr.reshape(16, )
    print(arr)
    arr = arr.reshape(4, 4)
    print(arr)
    
    print(arr[0])
    print(arr[0:2])
    print(arr[0][0:3])
    print(arr[arr < 5])
    print(arr[arr < 5].reshape(2, 5))
    print(arr[arr % 2 == 0])
    print(arr % 2 == 0)
    print(arr > 3)
    print(numpy.unique(arr))
    print(numpy.unique(arr[1:], return_index=True))
    print(numpy.unique(arr[1:], return_counts=True))
    
    for a, b in zip(arr[0], arr[1]):
        print(a, b)
    
    a = numpy.array([[1, 1],
                     [2, 2]])
    b = numpy.array([[3, 3],
                     [4, 4]])
    print(a)
    print(b)
    print(numpy.hstack((a, b)))
    print(numpy.vstack((a, b)))
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a * 2)
    print(b / 2)
    
    print(arr.min())
    print(arr.max())
    print(arr.sum())
    
    print(numpy.hstack((a, b)).transpose())
    print(numpy.hstack((a, b)).transpose()[::-1])
    
    arr.tofile("temp.txt")
    arr = numpy.fromfile("temp.txt")
    print(arr)
    os.remove("temp.txt")