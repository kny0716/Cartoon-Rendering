# Cartoon-Rendering
<br>
OpenCV를 사용해 이미지를 만화 스타일로 변환해주는 간단한 프로젝트입니다.

<br>
<br>

## 만화 스타일이 잘 표현되는 이미지 

 - 원본 이미지

<img width="299" alt="image" src="https://github.com/user-attachments/assets/370d1872-1c3d-46a2-9a63-96b25c3f2c01" />

<br>

 - 만화 스타일로 변환된 이미지


<img width="299" alt="image" src="https://github.com/user-attachments/assets/30bc77c8-91a0-4b44-a09f-82425702831f" />

<br>
<br>

 ## 만화 스타일이 잘 표현되지 않는 이미지
 

 - 원본 이미지
   

<img width="446" alt="image" src="https://github.com/user-attachments/assets/e551426c-91ab-46ad-868d-b805f4c9fb9e" />

<br>

 - 만화 스타일로 변환된 이미지
   

<img width="446" alt="image" src="https://github.com/user-attachments/assets/7ba10106-6900-46e6-805a-19b2210c14d0" />

<br>

## 이 알고리즘의 한계점 
이 알고리즘으로 이미지를 만화 스타일로 표현하기에는 한계가 있습니다. <br>
이 알고리즘은 엣지를 감지하여 윤곽선을 생성하고 색상을 단순화하고 엣지를 결합하여 이미지를 만화 스타일로 변환하기 때문에 선명한 경계와 색상이 뚜렷한 이미지에서만 좋은 결과를 보입니다. <br>
첫 번째 예시를 보면 이미 선이 명확하기 때문에 만화 스타일로 잘 표현되는 반면에, 두 번째 예시를 보면 흐릿하고 디테일이 적어 윤곽선이 잘 검출되지 않습니다.<br>
이뿐만이 아니라 잔디나 머리카락 등 디테일이 너무 많거나 어둡고 흐린 이미지의 경우 만화 스타일이 잘 표현되지 않습니다. <br>
더 높은 퀄리티의 만화 스타일로 변환된 이미지를 얻으려면 OpenCV 대신 CycleGAN, CartoonGAN 같은 딥러닝 기반 모델을 적용하거나 cv2.Canny()를 사용해 더 선명한 윤곽선을 검출해야 합니다.

