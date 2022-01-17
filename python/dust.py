# 미세먼지 농도 
dust = 80

if dust > 150:
    print('매우나쁨')
elif 150 >= dust > 80:
    print('나쁨')
elif 80 >= dust > 30:
    print('보통')
else:
    print('좋음')