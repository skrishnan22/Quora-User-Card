from bs4 import BeautifulSoup
import requests

baseUrl = "https://www.quora.com/profile/"
username='Aditi-Saini-1'
soup = BeautifulSoup(requests.get(baseUrl+username).text)
imgUrl = soup.find('img',{'class':'profile_photo_img'}).get('src')
print imgUrl
profileName = soup.find('div',{'class':'ProfileNameAndSig'}).find('span',{'class':'user'}).text
print profileName
answerCount = soup.find('div',{'class':'nav_item_selected'}).findAll('span',{'class':'list_count'})[0].text
print answerCount
followerCount = soup.find('li',{'class':'FollowersNavItem'}).findAll('span',{'class':'list_count'})[0].text
try:
		viewCount = soup.find('div',{'class':'AboutListItem AnswerViewsAboutListItem'}).text.split(' ')[0]
except(AttributeError):
		viewCount = 0	
print followerCount	
	
print viewCount
