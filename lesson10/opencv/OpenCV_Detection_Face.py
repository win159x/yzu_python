# -*- coding=utf-8 -*-
# 安裝 py-opencv
import cv2

# 各種已訓練好的偵測器資源檔：
# https://github.com/opencv/opencv/blob/master/data/haarcascades/


face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt2.xml')

# 設定攝像鏡頭
cap = cv2.VideoCapture(0)

# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # 捕捉 frame-by-frame
    ret, frame = cap.read()  # ret : 讀到的 frame 是正確的化會回傳 true

    # 定義灰度圖像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 監測人臉
    faces = face_cascade.detectMultiScale(
        gray,  # 待檢測圖片，一般為灰度圖像加快檢測速度
        scaleFactor=1.1,  # 檢測粒度 scaleFactor 。更大的粒度將會加快檢測的速度，但是會對檢測準確性產生影響。相反的，一個更小的粒度將會影響檢測的時間，但是會增加準確性。
        # 表示在前後兩次相繼的掃描中，搜尋視窗的比例係數。預設為1.1，即每次搜尋視窗依次擴大10%
        minNeighbors=5,  # 每個目標至少檢測到幾次以上，才可被認定是真數據。
        minSize=(30, 30),  # 設定數據搜尋的最小尺寸 ，如 minSize=(30,30)，也就是太小的臉就忽略辨識
        flags=cv2.CASCADE_SCALE_IMAGE
        # CASCADE_DO_CANNY_PRUNING=1 -> 利用canny邊緣檢測來排除一些邊緣很少或者很多的影象區域
        # CASCADE_SCALE_IMAGE=2 -> 正常比例檢測
        # CASCADE_FIND_BIGGEST_OBJECT=4 -> 只檢測最大的物體
        # CASCADE_DO_ROUGH_SEARCH=8 粗略的檢測
    )

    # 找到的人臉個數
    print("Found {0} faces!".format(len(faces)))

    # 在臉部周圍畫矩形框
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)  # 注意：(0, 255, 0) 是 BGR

    # 將 frame 顯示
    cv2.imshow('Detect face', frame)

    # 按下 q 離開迴圈 (「1」表示停 1ms 來偵測是否使用者有按下q。若設定為「0」就表示持續等待至使用者按下按鍵為止)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# 釋放資源與關閉視窗
cap.release()
cv2.destroyAllWindows()