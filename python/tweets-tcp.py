
import socket
import tweepy
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("HOST")
parser.add_argument("PORT")

args = parser.parse_args()

HOST = args.HOST
PORT = int(args.PORT)
TAGS = ['#barcelona', 'bcn']


# Twitter credentials
consumer_key="SUmeKHuOFUClxSReAzZDbanPq"
consumer_secret="WIyevTfFL8PSIxCpGyNfXw6i17fZK1Z5W4RIgeLeVmKYc7Hy2O"
access_token="124131670-TSPg4mMX35UFRwtjH815RX3E7jfJqEttEPrneOnq"
access_token_secret="RqdlvBXgVUmjaJiXKSle3AH2BDeOzsOaDQDLYQwVW1pc0"

connection = ""

# Send tweet via socket
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        text = status.text.encode('utf-8') 
        print(text)
        connection.sendall(text)


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (HOST, PORT)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
        
    try:
        print('connection from', client_address)
        
        # Authenticate app 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
        # Start receiving tweets 
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=auth, listener=myStreamListener)
        myStream.filter(track=TAGS)
    
    except: 
        continue
    
    finally:
        # Clean up the connection
        connection.close()


