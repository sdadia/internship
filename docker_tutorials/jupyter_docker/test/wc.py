from __future__ import print_function
from operator import add
from pyspark.sql import SparkSession
import findspark
import sys
findspark.init()

spark = SparkSession\
    .builder\
    .appName("PythonWordCount")\
    .getOrCreate()

lines = spark.read.text("./my_data.txt").rdd.map(lambda r: r[0])
counts = lines.flatMap(lambda x: x.split(' ')) \
              .map(lambda x: (x, 1)) \
              .reduceByKey(add)
output = counts.collect()
for (word, count) in output:
    print("%s: %i" % (word, count))

# spark.stop()