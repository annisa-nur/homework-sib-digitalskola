from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()

text = "HELLO SPARK, MY NAME IS ANNISA NUR, HOW MANY WORKER DO YOU HAVE? HELLO DOCKER"

words = spark.sparkContext.parallelize(text.split(" "))

wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

for word in wordCounts.collect():
    print(word[0], word[1])

spark.stop()