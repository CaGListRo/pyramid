height = input("How high should the pyramid be?: ")
pyramid = ""
for i in range(int(height)):
    pyramid = '#' * (i+1)
    print(pyramid)