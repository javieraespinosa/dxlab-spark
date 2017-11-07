

# Graph Processing with Spark GraphX


The objective of this section is to help you get started with the [Playing with graphs using GraphX](http://vargas-solar.com/datacentric-sciences/hands-on/graph-processing/) hands-on.

Open a terminal and download the docker dependencies:

`$ docker-compose pull`


After that, you can start the graphx environment by executing the following instruction:

`$ docker-compose run graphx`

This will launch a spark-shell interpreter where you can play with graphix. 


# Stream Processing with Spark Streaming

## 1. Objective
The objective of this hands on is to let you “touch” the challenges implied in processing streams. In class, we will use Spark for implementing a streaming version of word count and an example using:

+ A TCP server.
+ Twitter streaming.


## 2. Material 

- [Download][1]


## 3. Getting started with Spark Streaming


Spark streaming is an extension of the core Spark API that enables stream processing of live data streams. Data can be harvested from many sources like Kafka, Flume, Twitter, ZeroMQ, Kinesis, or TCP sockets, and can be processed using complex algorithms expressed with high-level functions like map, reduce, join and window. Finally, processed data can be pushed out to file systems, databases, and live dashboards 


Internally Spark streaming receives live input data streams and divides the data into batches, which are then processed by the Spark engine to generate the final stream of results in batches. 


> Insertar imagen

Spark Streaming is based on the notion of discretized stream or DStream, which represents a continuous stream of data. DStreams can be created either from input data streams from sources such as Kafka, Flume, and Kinesis, or by applying high-level operations on other DStreams. Internally, a DStream is represented as a sequence of RDDs. 

This guide shows you how to start writing Spark Streaming programs with DStreams. You can write Spark Streaming programs in Scala, Java or Python (see [spark guide][2] for details)

. You will find tabs throughout this guide that let you choose between code snippets of different languages.




``` python
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
# Create a local StreamingContext with two working thread and batch interval of 1 second
ssc = StreamingContext(sc, 1)

```





[1]: https://github.com/javieraespinosa/dxlab-spark 
[2]: https://spark.apache.org/docs/latest/streaming-programming-guide.html










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















