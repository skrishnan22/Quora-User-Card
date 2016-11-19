from flask import Flask,jsonify
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)

@app.route("/quoracard/<username>")
def get_details(username):
	baseUrl = "https://www.quora.com/profile/"

	soup = BeautifulSoup(requests.get(baseUrl+userName).text,'lxml')
	imgUrl = soup.find('img',{'class':'profile_photo_img'}).get('src')
	profileName = soup.find('div',{'class':'ProfileNameAndSig'}).find('span',{'class':'user'}).text
	answerCount = soup.find('div',{'class':'primary'}).findAll('span',{'class':'list_count'})[0].text
	followerCount = soup.find('div',{'class':'secondary'}).findAll('span',{'class':'list_count'})[0].text
	viewCount = soup.find('div',{'class':'AboutListItem AnswerViewsAboutListItem'}).text.split(' ')[0]

	return jsonify(name=profileName,
				   imgSrc=imgUrl,
				   answer=answerCount,
				   followers=followerCount,
				   views=viewCount)

if __name__ == '__main__':
	app.run(debug=True)