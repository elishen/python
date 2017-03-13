from sklearn import linear_model 
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

k_features = 0
k_training = 0 
k_test = 0 

train_x = []
train_y = []
test_x = []

[k_features, k_training] = [int(x) for x in input().strip().split()]

while (k_training > 0):
    k_training -= 1
    record = [float(x) for x in input().strip().split()]
    train_x.append(record[:-1])
    train_y.append(record[-1])
    
k_test = int(input().strip())

while (k_test >0):
    record = [float(x) for x in input().strip().split()]
    test_x.append(record)
    k_test -= 1
    
poly = PolynomialFeatures(degree=4)
trans_train = poly.fit_transform(train_x)
trans_test = poly.fit_transform(test_x)

clf = linear_model.LinearRegression()
clf.fit(trans_train, train_y)

predict = clf.predict(trans_test)
for p in predict:
    print("%.2f"%p)


# 2 2 
# 1 2 3
# 4 5 6
# 2
# 1 2 
# 3 4
