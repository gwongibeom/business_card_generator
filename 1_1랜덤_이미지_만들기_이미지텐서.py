import numpy as np

np.random.randint(100,400)






"""#언팩킹 (변수 여러개에 한번에 매칭하기)"""

x,y = [1,2]


x,y = np.random.randint(100,400,size=2)





























"""#랜덤 이미지 만들기

이미지 텐서
"""
image_tensor = np.random.randint(256,size=(x,y,3))

image_tensor.shape


image_tensor.astype('uint8')




"""데이터의 사이즈"""



"""이미지 텐서는 uint8 로"""



"""**위의 작업들을 한번에** """





"""이미지 생성하기"""
from PIL import Image

result = Image.fromarray(image_tensor,'RGB')


"""이미지 저장하기"""
result.save("test.jpg")


"""이미지 닫기"""
result.close
