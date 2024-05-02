from django.shortcuts import render
from django.http import HttpResponse

nav_names = ["Forms","NGOs","Solutions","Causes","Home"]
logo_link ="https://tse4.mm.bing.net/th/id/OIG3.mlONeZu1lGfbij1d4cFH?pid=ImgGn"
img_links = ["ABS","123"]
causes = ["1","2","3","4"]
link_causes = []
solutions = ["2","3","4"]
link_solutions = []

for i in solutions:
     link_solutions.append("#"+str(i))

for i in causes:
     link_causes.append("#"+str(i))
 # Create your views here.

def index(request):
     return render(request, "evs/index.html",{"name":
     "Home","nav_names":nav_names,"logo":logo_link,"images":img_links,
     "img_links":img_links})
def Causes(request):
     return render(request,"evs/Causes.html",
     {
          "name": nav_names[1],
          "nav_names":nav_names,
          "logo":logo_link,
          "side_nav_names":causes,
          "link_side_nav_names":link_causes
     })
def Solutions(request):
     return render(request,"evs/Solution.html",
     {
          "name":nav_names[2],
          "nav_names":nav_names,
          "logo":logo_link,
          "side_nav_names":solutions,
          "link_side_nav_names":link_solutions
     })

# Create your views here.
