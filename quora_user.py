from bs4 import BeautifulSoup
import requests

baseUrl = "https://www.quora.com/profile/"
userName = raw_input("")

soup = BeautifulSoup(requests.get(baseUrl+userName).text,'lxml')



imgUrl = soup.find('img',{'class':'profile_photo_img'}).get('src')
profileName = soup.find('div',{'class':'ProfileNameAndSig'}).find('span',{'class':'user'}).text
answerCount = soup.find('div',{'class':'primary'}).findAll('span',{'class':'list_count'})[0].text
followerCount = soup.find('div',{'class':'secondary'}).findAll('span',{'class':'list_count'})[0].text
viewCount = soup.find('div',{'class':'AboutListItem AnswerViewsAboutListItem'}).text.split(' ')[0]



print answerCount,followerCount,viewCount 