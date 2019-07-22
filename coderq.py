import pyqrcode

def generateQR():
	#Input the url of site of which you want to create QR code
	postlink="https://www.cricbuzz.com/"   
	url=pyqrcode.create(postlink)
    # score.png is the output image produced
	url.png('score.png',scale=5)
	print("Generating QR code")
	print(url.terminal())

if __name__=='__main__':
	generateQR()