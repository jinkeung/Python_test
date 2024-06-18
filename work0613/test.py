import requests

class image_down:

    def __init__(self,request):
        response=requests.get(request,{"User_Agent":"Mozilla/5.0"})
        with open("img.jpg","wb") as file:
            file.write(response.content)

