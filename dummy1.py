from bs4 import BeautifulSoup
import requests
username = 'dushka-zapata'
baseUrl = "https://www.quora.com/profile/"
soup = BeautifulSoup(requests.get(baseUrl+username).text,'html.parser')
imgUrl = soup.find('img',{'class':'profile_photo_img'}).get('src')
profileName = soup.find('div',{'class':'ProfileNameAndSig'}).find('span',{'class':'user'}).text
answerCount = soup.find('div',{'class':'nav_item_selected'}).findAll('span',{'class':'list_count'})[0].text
followerCount = soup.find('li',{'class':'FollowersNavItem'}).findAll('span',{'class':'list_count'})[0].text
try:
	viewCount = soup.find('div',{'class':'AboutListItem AnswerViewsAboutListItem'}).text.split(' ')[0]
except(AttributeError):
	viewCount = 0	


try:

	topWriter = soup.find('div',{'class':'AboutListItem TopWriterAboutListItem'}).text.split(' ')[0]
	tpFlag=1
except(AttributeError):
	tpFlag = 0

print tpFlag