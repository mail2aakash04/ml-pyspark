import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
import seaborn as sns


def main():

    mpg_df = pd.read_csv("C://Users//aaakashagrawal//Downloads//personal//study//datatset//Car-mpg.csv")
    #print(mpg_df.describe())
    #print(mpg_df.head(10))

    mpg_df = mpg_df.drop("car_name", axis=1)

    mpg_df['origin'] = mpg_df['origin'].replace({1: 'america', 2: 'europe', 3: 'asia'})

    mpg_df = pd.get_dummies(mpg_df,columns=['origin'])

    print(mpg_df.describe().transpose())










    print(mpg_df)


# entry point for PySpark ETL application
if __name__ == '__main__':
    main()