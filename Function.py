def Video_Take_Photo(Path_Out):
    import cv2
    import os

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    vidcap = cv2.VideoCapture(0)
    count = 0
    while True:
        success, img = vidcap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        for (x, y, w, h) in faces:
            width = x + w
            high = y + h
            roi = img[y:high, x:width]
            cv2.rectangle(img, (x, y), (width, high), (255, 0, 0), 2)
            cv2.putText(img, str(w * h), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
            cv2.imshow('Show', roi)
            if count <= 19:
                cv2.imwrite(os.path.join(Path_Out, '%d.png') % count, roi)
                count += 1
                print('save' + str(count))
            else:
                continue

        cv2.imshow('Camera', img)
        if cv2.waitKey(1) == ord('q'):
            break;
    cv2.destroyAllWindows()
    vidcap.release()

def Camera_Take_Photo(Path_In, Path_Out):
    import cv2
    import os

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    img = cv2.imread(Path_In, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (1920,1080))
    count = 0
    while True:
        faces = face_cascade.detectMultiScale(img, 1.1, 5)
        for (x, y, w, h) in faces:
            width = x + w
            high = y + h
            roi = img[y:high, x:width]
            if w*h <= 6000:
                cv2.rectangle(img, (x, y), (width, high), (255, 0, 0), 2)
                cv2.putText(img, str(w * h), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
                cv2.imshow('Show', roi)
                if count <= 19:
                    cv2.imwrite(os.path.join(Path_Out, '%d.png') % count, roi)
                    count += 1
                else:
                    continue

        cv2.imshow('Camera', img)
        if cv2.waitKey(1) == ord('q'):
            break;
    cv2.destroyAllWindows()
