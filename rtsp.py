import cv2
import imutils
from imutils.video import VideoStream

# replace this with the url generated by the Wyze app
#rtsp_url = "rtsp://<camera_name>:<some_uuid>@10.32.38.120/live"
#rtsp_url = "rtsp://admin:FlirPass.21@10.32.38.117:554/ch1"
rtsp_url = "rtsp://10.32.38.99/axis-media/media.amp"
#rtsp_url = "rtsp://50.32.32.4/axis-media/media.amp"
#rtsp_url = 'rtsp://root:CamPass.21@10.32.38.99/axis-media/media.amp'
#rtsp_url = "axrtsp://10.32.38.99/axis-media/media.amp"



vs = VideoStream(rtsp_url).start()

while True:
    frame = vs.read()

    if frame is None:
        continue

    frame = imutils.resize(frame, width=1200)

    cv2.imshow('WyzeCam', frame)
    
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

cv2.destroyAllWindows()
vs.stop()
