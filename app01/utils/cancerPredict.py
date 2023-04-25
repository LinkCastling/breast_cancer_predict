import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
import sys
import json


def cancerPredict(predict_X):
    # 读入数据
    data_path = os.path.join(os.getcwd(), 'app01', 'utils', 'bcw_regulated_data.csv')
    print(data_path)
    dataframe = pd.read_csv(data_path)

    data_array = dataframe.values

    # 分割data和target 舍弃掉了sample_sn
    data = data_array[:, 1:10]
    target = data_array[:, -1:]
    # 对我们的data数据做一个拆分
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=666)

    # 数据归一化
    standarScaler = StandardScaler()
    standarScaler.fit(X_train)
    X_train_std = standarScaler.transform(X_train)
    X_test_std = standarScaler.transform(X_test)

    pca = PCA(0.9)  # 保留95%的方差的数据
    pca.fit(X_train_std)
    X_train_reduction = pca.transform(X_train_std)
    X_test_reduction = pca.transform(X_test_std)

    knn_clf = KNeighborsClassifier(n_neighbors=3, p=1, weights="distance")
    knn_clf.fit(X_train_reduction, y_train)

    predict_X = np.array(predict_X)

    predict_X = pca.transform([predict_X])  # 原始参数属性先降维)
    res = knn_clf.predict(predict_X)
    if res == 1:
        return True
    else:
        return False
