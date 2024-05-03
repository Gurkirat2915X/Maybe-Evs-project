from django.shortcuts import render
from django.http import HttpResponse

#For homepage
nav_names = ["Forms","NGOs","Solutions","Causes","Home"]
logo_link ="https://tse4.mm.bing.net/th/id/OIG3.mlONeZu1lGfbij1d4cFH?pid=ImgGn"
img_links = ["ABS","123"]



#For Causes
causes = ["River Water Pollution","SOURCE OF POLLUTANTS IN RIVER","Point source","Non-point",]
Cause_img = ["https://tse4.mm.bing.net/th/id/OIG3.mlONeZu1lGfbij1d4cFH?pid=ImgGn",""]
Cause_content =["lol","lol","olo"]
Cause_heading=["Cause","sub-heading","https://www.environmentbuddy.com/wp-content/uploads/2020/03/Polluted-river-with-garbage.jpeg"]

#For Solutions
solutions = ["2","3","4"]
Solution_img = ["https://tse4.mm.bing.net/th/id/OIG3.mlONeZu1lGfbij1d4cFH?pid=ImgGn"]
Solution_content=["Hello"]
Solution_heading=["Solution","sub-heading","https://www.environmentbuddy.com/wp-content/uploads/2020/03/Polluted-river-with-garbage.jpeg"]

#For NGOS
ngos=["1","2"]
ngo_heading=["NGO","Sub-heading","https://www.environmentbuddy.com/wp-content/uploads/2020/03/Polluted-river-with-garbage.jpeg"]
ngo_content=["NGO1"]
ngo_img=["https://tse4.mm.bing.net/th/id/OIG3.mlONeZu1lGfbij1d4cFH?pid=ImgGn"]

# For forms
forms_heading=["Forms","Sub-heading","https://www.environmentbuddy.com/wp-content/uploads/2020/03/Polluted-river-with-garbage.jpeg"]
 # Create your views here.
def index(request):
     return render(request, "evs/index.html",{"name":
     "Home","nav_names":nav_names,"logo":logo_link,"images":img_links,
     "img_links":img_links})
def Causes(request):
     return render(request,"evs/Causes.html",
     {
          "name": nav_names[3],
          "nav_names":nav_names,
          "logo":logo_link,
          "side_nav_names":causes,
          "heading":Cause_heading,
          "content_list":zip(causes,Cause_img,Cause_content)
     })
def Solutions(request):
     return render(request,"evs/Solution.html",
     {
          "name":nav_names[2],
          "nav_names":nav_names,
          "logo":logo_link,
          "side_nav_names":solutions,
          "heading":Solution_heading,
          "content_list":zip(solutions,Solution_img,Solution_content)

     })
def NGOs(request):
     return render(request,"evs/NGO.html",
     {
          "name":nav_names[1],
          "nav_names":nav_names,
          "logo":logo_link,
          "side_nav_names":ngos,
          "heading":ngo_heading,
          "content_list":zip(ngos,ngo_img,ngo_content)
     })
def Forms(request):
     return render(request,"evs/forms.html",
     {
          "name":nav_names[0],
          "nav_names":nav_names,
          "logo":logo_link,
          "heading":forms_heading
     })

# Create your views here.