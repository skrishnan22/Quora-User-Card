from flask import Flask,jsonify,render_template,request
from bs4 import BeautifulSoup
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("main.html")



@app.route("/quoracard/<username>",methods=["GET"])
def get_details(username):
	baseUrl = "https://www.quora.com/profile/"
	soup = BeautifulSoup(requests.get(baseUrl+username).text,'lxml')
	imgUrl = soup.find('img',{'class':'profile_photo_img'}).get('src')
	profileName = soup.find('div',{'class':'ProfileNameAndSig'}).find('span',{'class':'user'}).text
	answerCount = soup.find('div',{'class':'primary'}).findAll('span',{'class':'list_count'})[0].text
	followerCount = soup.find('div',{'class':'secondary'}).findAll('span',{'class':'list_count'})[0].text
	try:
		viewCount = soup.find('div',{'class':'AboutListItem AnswerViewsAboutListItem'}).text.split(' ')[0]
	except(AttributeError):
		viewCount = 0	
	return render_template("card.html",imgUrl=imgUrl,profileName=profileName,answerCount=answerCount,followerCount=followerCount,viewCount=viewCount)
	



if __name__ == '__main__':
	app.run(debug=True)