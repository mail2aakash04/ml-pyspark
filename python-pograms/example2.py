from datetime import date, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from pyspark.sql.types import *
from pyspark.sql import SparkSession

def main():

    spark = SparkSession \
        .builder \
        .appName("python-programs") \
        .master("local")    \
        .getOrCreate()

    sc = spark.sparkContext

    sdate = date(2008, 8, 15)
    edate = date(2008, 9, 15)  # end date
    delta = edate - sdate  # as timedelta

    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)

    patientdf : pd.DataFrame = pd.read_csv("../datasets/patientData") #,names=['patientId','startDate','endDate'],header=0)

    patient = sc.textFile("../datasets/patientData.csv").toDF()

    print(patient)
    #.map(lambda l: l.split(","))
    #people = patient.map(lambda p: Row(patientId=p[0], startDate=date(p[1]),endDate= date(p[2]))).toDF()


# entry point for PySpark ETL application
if __name__ == '__main__':
    main()

