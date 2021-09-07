# BTCStealer
Python script to replace BTC adresses in the clipboard with similar looking ones, whose private key can be retrieved by a netcat listener or similar.

This Python Script works by checking the clipboard every 2 seconds and finding and replacing the first BTC address it finds with a newly generated one that looks similar to the one it's replacing (similar means the first 3 characters are equal).//
After that it will send the private key of the generated BTC address to a netcat listener (hardcoded to localhost, but port and host are easily changeable).//
Then it will wait for 2 minutes.//
ONLY BTC ADDRESSES STARTING WITH 1 ARE SUPPORTED!//

Use for educational purposes only.//
