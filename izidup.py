import requests

def main():
	# Insert in this array all the APIs or domain you want to test. The existed values are just examples
	urls = ['https://www.google.fr', 'http://127.0.0.1:4200/products/book-bindings'];
	
	for url in urls:
		try:
			r = requests.get(url);
		except requests.exceptions.RequestException as e:
			r = None
		sendMessage(r)

def sendMessage(r):
	print(r)

if __name__== "__main__":
  	main()