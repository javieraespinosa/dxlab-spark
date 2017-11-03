# dxlab-spark


## WordCount via TCP

This example illustrates how to use spark streaming for counting words recevied via a TCP connection.

### Running the example

**Terminal 1**. Netcat server

```$ docker-compose run netcat nc -l -p 9999```

**Terminal 2**. Spark interpreter for python (pyspark)

```$ docker-compose run pyspark```

Follow the [instructions][1] for defining your own spark streaming python application. Inside pyspark, you can access the netcat server either by name (**netcat**) or IP (**11.0.0.10**).


[1]: https://spark.apache.org/docs/latest/streaming-programming-guide.html


