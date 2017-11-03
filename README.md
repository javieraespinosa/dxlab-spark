# dxlab-spark


## WordCount via TCP

**Terminal 1**. Netcat server

```$ docker-compose run netcat nc -l -p 9999```

**Terminal 2**. Spark interpreter for python (pyspark)

```$ docker-compose run pyspark```

Follow the [instructions][1] for defining your own spark streaming python application. Inside pyspark, you can access the netcat server either by name (**netcat**) or IP (**11.0.0.10**).


## Wordcount with tweets

**Terminal 3**. Prepare the tweets producer.

```$ docker-compose run tweets```

**Terminal 4**. Start receiving tweets in spark.

```$ docker-compose run pyspark```

Once inside pyspark, copy/paste the code in ```python/spark-streaming.py```.

[1]: https://spark.apache.org/docs/latest/streaming-programming-guide.html


