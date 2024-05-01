from django.shortcuts import render
from django.http import HttpResponse

nav_names = ["Home","Causes","Solutions","NGOs","Forms"]
logo_link = "https://img.freepik.com/free-vector/sea-animal-cartoon-sticker-with-cute-fish_1308-75896.jpg?w=1380&t=st=1714400607~exp=1714401207~hmac=6f3a5b850685ab51e8bee2ac36ea2fad282bcd1b75d3b034fcb76846433b71a7"
img_links = ["ABS","123"]
causes = ["1","2","3","4"]
link_causes = []

for i in causes:
     link_causes.append("#"+str(i))
 # Create your views here.

def index(request):
     return render(request, "evs/index.html",{"name":
     "Home","nav_names":nav_names,"logo":logo_link,"images":img_links,
     "img_links":img_links})
def Causes(request):
     return render(request,"evs/Causes.html",
     {"name": nav_names[1],"nav_names":nav_names,"logo":logo_link
     ,"causes":causes,"link_causes":link_causes})

# Create your views here.
