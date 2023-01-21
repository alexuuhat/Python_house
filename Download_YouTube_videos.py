import pytube
#Ask for the url of video
url = input("Enter video url:")

#Specify the storage path of video
path ="F:"

#Magic Line to download the video
pytube.YouTube(url).streams.get_highest_resolution().download(path)
