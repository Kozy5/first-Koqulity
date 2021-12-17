NickNametext = "Deft"
본명text = "혁규"
jobtext = "LOL Progamer"
positiontext = "AD Carry"

#Deft = Gamer("Hyeok Gyu", "LOL Progamer", "AD Carry")
#Faker = Gamer("Sang Hyeok", "LOL Progamer", "MID")
#ShowMaker = Gamer("Heo su", "LOL Progamer", "MID")
#Khan = Gamer("Dong Ha", "LOL Progamer", "Top")
#Gumayusi = Gamer("Min Hyeong", "LOL Progamer", "AD Carry")
#Keria = Gamer("Min Seok", "LOL Progamer", "Supporter")


class Gamer:
    def __init__(self, name, job, position):
      self.name = name 
      self.job = job
      self.position = position
      
      

    def introduce(self):
        print("안녕하세요 저는" + self.name + " 입니다" \
         + self.job +"으로 활동하고있습니다. 포지션은" \
             + self.position +"입니다")
        #print("안녕하세요! 저는" + name + "입니다. 저는" + job +"을 하고있고 포지션은"+position+"입니다.")

NickNametext = Gamer(본명text, jobtext,positiontext )



NickNametext.introduce()




