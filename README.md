# How to run and publish: _**ocr2speech21**_

### Step 1
Get the latest version of the 21 software. You should be at version `2.3.3`.

```
$ 21 update
$ 21 --version
21 v2.3.3
```

### Step 2
Clone the ocr2speech21 repository.

```
$ git clone https://github.com/21dotco/ocr2speech21.git
$ cd ocr2speech21
$ sudo easy_install3 pip
$ sudo pip3 install -r requirements.txt
```

### Step 3
Join the `21market` Marketplace, and start a local
server to accept ocr2speech21 requests. The server will run in the
background and process requests.  You can optionally edit the file
to change the default price, which is 15000 Satoshis per request.

```
$ 21 join 21market
$ python3 ocr2speech21-server.py &
```

### Step 4
Now use `21 publish` to submit the manifest file describing the
ocr2speech21 service you just started. You can pass in arguments to override the
default values in the file.  The name and email should be your own. The price
field should match the price in the `@payment.required` decorator in `ocr2speech21-server.py`.
The host of `'AUTO'` is a special input that tells the publish command to use
the IP of your bitcoin computer within the `21market` Marketplace (see
[here](https://21.co/learn/21-marketplace/#the-21-network for details)). The
port of 6005 is the default port specified within the
`ocr2speech21-server.py` code that you are running.

```
$ 21 publish submit manifest.yaml -p 'title="OCR to Speech" name="Satoshi Nakamoto" email="satoshi@example.com" price="15000" host="AUTO" port="6005"'
```

### Step 5
After a brief wait of a second or so, you should be able to use `21 publish list`
to see the endpoint you just put up:

```
$ 21 publish list
```

You can also search the 21 Marketplace for your app:

```
$ 21 search "ocr2speech21"
```

### Step 6
You can now use bitcoin to buy that endpoint from yourself to test it out:

```
$ 21 buy url $HOST:$PORT/?image_url=http://i.imgur.com/U86mtM1.png
```

where `$HOST` is your Bitcoin Computer's IP address on the 21 Marketplace and
`$PORT` is the port the web service is running on (you can find `$HOST` and
`$PORT` by running `21 publish list`).

### Step 7
And you can see a receipt for this transaction:

```
$ 21 log
```
