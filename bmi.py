import json

class BMI:


    def __init__(self):
        self.version = 0.1


    def getComment(self,bmi):
        if bmi>=40:
            return 'Very Severely Obese','Very High Risk'
        elif bmi>=35 and bmi<=39.9:
            return 'Severely Obese','High risk'
        elif bmi>=30 and bmi<=34.9:
            return 'Moderately Obese','Medium risk'
        elif bmi>=25 and bmi<=29.9:
            return 'Over Weight','Enhanced risk'
        elif bmi>=18.5 and bmi<=24.9:
            return 'Normal Weight','Low risk'
        elif bmi<=18.4:
            return 'Under Weight','Malnutrition risk'


    def getBMI(self,height,weight):
        h = height/100
        b = weight/h
        wc,hr = self.getComment(b)
        return b,wc,hr


    def execute(self,txt):
        d = json.loads(txt)
        for i in d:
            gender = i.get('Gender','')
            height = i.get('HeightCm',0)
            weight = i.get('WeightKg',0)
            if height > 0 and weight > 0:
                bmi,wc,hr = self.getBMI(height,weight)
                c = ''
            else:
                c = 'Invalid height/weight'
            
            print('Gender:',gender)
            print('Height:',height)
            print('Weight:',weight)
            if c == '':
                print('BMI:',round(bmi,2),'kg/m2')
                print('Category:',wc)
                print('Health Risk:',hr)
            else:
                print('Comment:',c)
            print('-----------------------------')

