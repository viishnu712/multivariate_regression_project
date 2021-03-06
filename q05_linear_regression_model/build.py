from greyatomlib.multivariate_regression_project.q01_load_data.build import load_data
from greyatomlib.multivariate_regression_project.q02_data_split.build import split_dataset

from sklearn.linear_model import LinearRegression
from greyatomlib.multivariate_regression_project.q03_data_encoding.build import label_encode

df = load_data('data/student-mat.csv')

x_train, x_test, y_train, y_test =  split_dataset(df)

x_train, x_test = label_encode(x_train,x_test)


def linear_regression(X,y):
    lr = LinearRegression()
    return lr.fit(X,y)
