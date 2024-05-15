from django.shortcuts import render
from django.http import HttpResponse

blank = ""

#For homepage
nav_names = ["Forms","NGOs","Solutions","Causes","Home"]
logo_link ="https://tse4.mm.bing.net/th/id/OIG3.mlONeZu1lGfbij1d4cFH?pid=ImgGn"
img_links = ["https://i.natgeofe.com/n/2e9d6cb1-be06-4b0d-a0a2-2ecd098360db/44179.jpg?w=1200","https://images.hindustantimes.com/rf/image_size_630x354/HT/p2/2018/09/19/Pictures/bjp-yuva-yamuna-cleaning_bd5567a2-bc2d-11e8-95ec-91800d079bb4.jpg"]


#For Causes
causes = ["River Water Pollution",
          "SOURCE OF POLLUTANTS IN RIVER",
          "Disposal of Untreated Sewage",
          "Littering",
          "Human Activities",
          "Oil Seepage and Agricultural Pollutants",
          "Industries and Urbanisation",
          "IMPACT OF RIVER POLLUTION",
          "CONCLUSION"]

Cause_img = ["",
             "https://upload.wikimedia.org/wikipedia/commons/b/b7/Common_Point_Source_Discharges_-_EPA_2010.png ",
             "https://www.water-pollution.org.uk/wp-content/uploads/2018/09/seawage.jpg",
             "https://ichef.bbci.co.uk/news/1024/cpsprodpb/13892/production/_118881008_plastic_gettyimages-1152932601.jpg.webp",
             "",
             "https://www.afrik21.africa/wp-content/uploads/2020/12/121310734_4766225006750913_1132573198674699453_n-1-800x400.jpg",
             "https://media.licdn.com/dms/image/D4D12AQEcup9g0ic3yg/article-cover_image-shrink_600_2000/0/1678966421490?e=2147483647&v=beta&t=kjZLK4Z3s1LWObGifi4bieTyVNu976bGyn04MhD018E",
             "https://media.assettype.com/themooknayak-en%2F2024-03%2F53fa0264-c729-4358-aa56-ee6207e85809%2FYamuna.jpg?w=1200&auto=format%2Ccompress&fit=max",
             "",""]

Cause_content =["River Water pollution occurs when pollutants are discharged directly or indirectly into rivers without adequate treatment of harmful compounds. River Water pollution affects humans, plants, and organisms living in these rivers. Water pollutants are damaging not only the individual species and populations but also the natural biological communities. Moving water dilutes and decomposes pollutants more rapidly than standing water.The main reasons for river water pollution are due to three main sources of pollution, namely industry, agriculture, and riverside residences. Industries and cities have traditionally been located along rivers because rivers provide transportation and have traditionally been a convenient place for waste disposal. Agricultural activities were mostly concentrated near rivers because river floodplains are exceptionally fertile due to the numerous nutrients deposited in the soil when the river overflows.",
                
"(A)Point source pollution-Point source pollution refers to the pollution entering the waterway through a discrete conveyance like pipes, channels, etc., from a source such as industry. (B) Non-point source pollution- Non-point source pollution refers to the pollution that does not enter the waterway through a discrete source but is accumulative. The pollutants are collected in small amounts from over a large area .",

"India produces 20,000 million liters of sewage per day (MLD), of which 30% is treated in sewage treatment plants (STP) and the rest of the sewage is discharged untreated into natural waters. A survey of sewage treatment plants in India was conducted by the Central Pollution Control Board (CPCB). According to this survey, most wastewater treatment plants are not operating at design efficiency.About 30,000 MLD of pollutants enter Indian rivers, 10,000 million liters from industrial plants alone.",

"The volume of waste in India is 0.2 to 0.6 kg of waste per capita per day. Waste is often dumped in the river or on the side of the road, which is then carried down the drain to the river. Many rivers in India are nothing more than bodies of water, little more than flowing dumps, with up to 57% of waste ending up in the rivers. The garbage falls along the banks, giving off the foul-smelling stench of a cesspool . The second part of the seventh report on the state of the environment of India - Excreta Matters  by the Center for Science and Environment (CSE) says that Indian cities wallow in their waste and that rivers become landfill become. In this report, CSE describes 71 cities on their ability to manage wastewater and maps the status of groundwater and its resources. There are other similar towns and villages that haven't even been explored, what we see now is just the tip of the iceberg.",

": The river being the most important source of water is used by humans in every possible way. People bathe, washcloths and utensils, and chattels are cleaned in the river. Open defecation is practiced widely in rural and some urban regions, during the rainy season it causes pollution, as it is washed into the river. According to UNICEF, about 626 million people or nearly 51% of the population in India still defecate in the open .",

"Spillage of oil through vessels and leakage through pipelines is one of the components responsible for river water pollution. Excess fertilizers are washed into the nearby water body and join the river course. It has been estimated  that in 1984, 5 million tones of fertilizers, 55 000 tonnes of pesticides, and 125000 tonnes of synthetic detergents were used in India. Roughly about 25% of all these can be expected to ultimately end up in the rivers every year.",

"The unimpeded flow of sewage and industrial effluents into rivers has compromised their purity. All of this industrial waste is toxic to the life forms that consume this water. Rapid urbanization in India during the recent decades has given rise to numerous environmental problems such as water supply, wastewater generation, and its collection, treatment, and disposal. Many towns and cities which came upon the banks of rivers have not given proper thought to the problem of wastewater, sewerage, etc.",

"Marine life is affected by water pollution which increases day by day, disrupting the ecosystem of the river. This pollution affects aquatic life as dams are now being built on various rivers which act as water reservoirs which is dangerous as all animals have a hard time keeping up. Not only aquatic life but also people are affected as people end up drinking that polluted water, using it for daily chores, and making themselves vulnerable to various diseases, for example, water-borne diseases such as typhus, jaundice, cholera, etc, even threatening . People are also exposed to chemically treated water for their daily activities such as cleaning, washing, etc., increasing the chances of spreading infectious diseases. A fragile ecosystem can be ruined by such pollution. If the water continues to be polluted, the ecosystem may collapse and some species are already extinct or on the verge of extinction and need to be taken care of. Chemicals released into water bodies settle to the bottom, forming a thick layer on the river bed. The bacteria present in the water feed on it, leading to a decrease in oxygen which harms the aquatic life present in the rivers. It also has a detrimental effect on the food chain of the animals present in the ecosystem. When the aquatic life tends to ingest the polluted water, the marine life may have toxins and pollutants in its body. When humans tend to feed on fish, shellfish, or other forms of aquatic life, they also end up consuming toxins and pollutants.",

"River pollution is a growing problem in India today. Factors polluting the river need to be controlled industrial, agricultural, oil, social, Untreated Sewage, Littering, urban, Human Activities, domestic, etc. India's Water Conservation Act should be followed properly. Industrial water needs to be reused after proper treatment. The government should make proper efforts to make the river water clean, and the government and the NGOs together should tell the importance of the river to the people."]

Cause_heading=["Cause","https://www.environmentbuddy.com/wp-content/uploads/2020/03/Polluted-river-with-garbage.jpeg"]

#For Solutions
solutions = ["Pollution Reduction",
             "Sustainable Fishing",
             "Plastic Reduction",
             "Marine Restoration and Rehabilitation",
             "CONCLUSION",]
Solution_img = ["https://www.implasticfree.com/wp-content/uploads/2022/10/River-Cleaning.jpg",
                "https://cdn.shopify.com/s/files/1/1014/8315/products/Sustainable_Fishery_2e0719ba-ccc5-451e-aef0-7cdc11f5dd8f.jpg?v=1543523024",
                "https://th.bing.com/th/id/OIP.EOHrpJrnKTjIW9a4DeqFHgHaEK?rs=1&pid=ImgDetMain",
                "https://th.bing.com/th/id/OIP.Fkna7cykNbhdW_e1XlXO3AHaFj?rs=1&pid=ImgDetMain",
                "",
                ]
Solution_content=[ "Human activities are a major source of pollution harming our water resources. Industrial facilities, agriculture, and sewage treatment plants all contribute. We can help by being mindful of what we dispose of and supporting businesses with sustainable practices. This includes reducing use of harsh chemicals at home, properly disposing of hazardous waste, and advocating for stricter regulations on industrial waste management.",
                  "Overfishing is a serious threat to fish populations. By choosing seafood with certifications like the Marine Stewardship Council (MSC), we support fisheries that prioritize long-term sustainability.  This ensures fish are caught responsibly and populations can replenish, protecting the delicate balance of marine ecosystems.",
                  "Plastic pollution is a growing problem in our oceans, harming marine life and ecosystems. We can all play a part in reducing plastic use. Carrying reusable water bottles and shopping bags are simple yet impactful actions. Additionally, choosing products with minimal plastic packaging or opting for package-free alternatives whenever possible helps minimize plastic waste entering our waterways.",
                  "Degraded marine habitats like coral reefs, mangroves, and seagrass meadows play a vital role in ocean health. Restoration and rehabilitation efforts focus on bringing these ecosystems back to life. This can involve planting new corals, restoring lost mangroves, and promoting seagrass growth. Healthy habitats provide critical breeding grounds, shelter for marine life, and contribute to overall ocean health.",
                  "Revitalizing our rivers requires a multi-pronged approach. By tackling pollution from industries, farms, and households, we can restore healthy water quality. Community clean-ups, stricter regulations, and individual actions like reducing chemical use all contribute to a cleaner future for our rivers and the ecosystems they sustain. "
                  ]


Solution_heading=["Solution","https://th-i.thgim.com/public/incoming/8bla2f/article65250399.ece/alternates/LANDSCAPE_1200/PTI03_17_2022_000041B.jpg"]

#For NGOS
ngo_heading=["NGO(Non-Governmental Organisation)","https://culvercitycrossroads.com/wp-content/uploads/2019/04/folar-la-river-cleanup-featured.jpg"]

ngos=["WWF INDIA",
      "Centre for Environment Education (CEE)",
      "Kalpavriksh",
      "Conservation Action Trust (CAT)",
      "Reef Watch Marine Conservation",
      "Environmentalist Foundation of India (EFI)",
      "Nature Conservation Foundation(NCF)",
      "Dakshin Foundation",
      "Ashoka Trust for Research in Ecology and the Environment (ATREE)",
      "International Collective in Support of Fisherworkers (ICSF)",
      "Terra Conscious"
      ]
ngo_content=["They work on a range of conservation projects, including river ecosystems and marine biodiversity within rivers.",
             "CEE focuses on environmental education and conservation, including river ecosystems and marine life conservation in rivers.",
             "This organization is engaged in biodiversity conservation, including projects related to river ecosystems and marine species conservation.",
             "CAT is involved in advocacy and campaigns for river conservation, including efforts to protect marine life in rivers.",
             ": ReefWatch Marine Conservation is a not-for-profit organization established in 1993 as a public charitable trust under the Societies Registration Act. They aim to adapt internationally established ecosystem restoration techniques to the Indian context by piloting them on the coast and providing consultancy to other agencies",
             "EFI takes a holistic approach that includes wildlife conservation, habitat restoration, and water conservation.Although not exclusively marine-focused, their efforts contribute to overall ecosystem health, including coastal areas.These organizations play a crucial role in safeguarding our marine biodiversity and ensuring a sustainable future for our oceans.",
             "NCF, based in Mysore, is committed to conserving India's biodiversity. They work on marine conservation, including research, habitat protection, and community engagement.",
             "Dakshin Foundation, also based in Bengaluru, works on marine and coastal conservation. They collaborate with local communities, researchers, and policymakers to protect marine biodiversity",
             "ATREE, headquartered in Bengaluru, focuses on ecological research and conservation. Their marine initiatives contribute to understanding coastal ecosystems and promoting",
             "ICSF, headquartered in Chennai, advocates for the rights of small-scale fisherfolk and promotes sustainable fisheries management. Their work contributes to marine conservation and livelihoods.",
             "Founded in 2017 by Puja Mitra, Terra Conscious aims to promote responsible tourism and conservation. Puja, previously a senior program coordinator for World Wildlife Fund (WWF) India, brings her expertise to this organisation."
             
             ]
ngo_img=["https://th.bing.com/th/id/OIP.lmCZX90fQRK580ZEiSPdwwAAAA?rs=1&pid=ImgDetMain",
         "https://www.ceeindia.org/admin/action/uploads/140621104402act.jpg",
         "https://kalpavriksh.org/wp-content/uploads/2020/11/KV-logo-web-horizontal@0.25x.png",
         "https://cat.org.in/wp-content/uploads/2019/11/Conservation-Action-Trust-Logo.png",
         "https://i0.wp.com/reefwatchindia.org/wp-content/uploads/2021/05/Copy-of-ReefwatchFINALPDF.logo-01-4.png?fit=9094%2C3189&ssl=1",
         "https://indiaenvironment.org/wp-content/uploads/2019/01/efi-logo-transparent-retina.png",
         "https://thumbor-stg.assettype.com/ncfindia/2019-08/130ad8ea-2146-4280-8960-920a0ed77abe/NCF_Logo_with_White_BG_final.jpg?w=190&auto=format,compress",
         "https://www.dakshin.org/wp-content/uploads/2021/07/cropped-Dakshin-Logo_new-colour-final-01-e1627622688625.png",
         "https://www.atree.org/wp-content/uploads/2023/05/ATREE-logo-06.svg",
         "https://www.icsf.net/wp-content/themes/ICSF/assets/images/flogo.png",
         "https://static.wixstatic.com/media/699b9c_4411508b8e4347b5abd036e1bcb66ea4~mv2.png/v1/crop/x_0,y_18,w_400,h_357/fill/w_134,h_110,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/ugh.png"]

ngo_website = ["https://www.wwfindia.org/",
               "https://www.ceeindia.org/",
               "https://kalpavriksh.org/",
               "https://cat.org.in/",
               "https://reefwatchindia.org/ ",
               "https://indiaenvironment.org/",
               "https://www.ncf-india.org/",
               "https://www.dakshin.org/",
               "https://www.atree.org/",
               "https://www.icsf.net/",
               "https://www.terraconscious.com/"
               ]

ngo_mail = ["info@wwfindia.net",
            "cee@ceeindia.org",
            "kalpavriksh@vsnl.com",
            "catindia@cat.org.in",
            "admin@reefwatchindia.org",
            "arun@indiaenvironment.org",
            "smita @ ncf-india.org",
            "info@dakshin.org",
            "infodelhi.atree@org",
            "icsf@icsf.net",
            "terraconscious.contact@gmail.com"
            ]




# For forms
forms_heading=["Forms","https://images.wallpaperscraft.com/image/single/stones_sea_water_373109_3840x2160.jpg"]
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
          ,"blank":blank
     })
def Solutions(request):
     return render(request,"evs/Solution.html",
     {
          "name":nav_names[2],
          "nav_names":nav_names,
          "logo":logo_link,
          "side_nav_names":solutions,
          "heading":Solution_heading,
          "content_list":zip(solutions,Solution_img,Solution_content),
          "blank":blank

     })
def NGOs(request):
     return render(request,"evs/NGO.html",
     {
          "name":nav_names[1],
          "nav_names":nav_names,
          "logo":logo_link,
          "side_nav_names":ngos,
          "heading":ngo_heading,
          "content_list":zip(ngos,ngo_content,ngo_website,ngo_mail,ngo_img)
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