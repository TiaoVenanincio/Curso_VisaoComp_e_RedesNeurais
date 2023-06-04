import cv2
import time

#rastreador = cv2.TrackerKCF_create()
rastreador = cv2.TrackerCSRT_create()

video = cv2.VideoCapture('./4_Rastreamento_Codigo/race.mp4')
ok, frame = video.read()

bbox = cv2.selectROI("Selecione a area",frame) #roi - Regiao de interesse
#print(bbox)

ok = rastreador.init(frame, bbox)
#print(ok)
t_inicio = time.time()
while True:
    ok, frame = video.read()
    if not ok:
        break

    ok, bbox = rastreador.update(frame)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2, 1)
    else:
        cv2.putText(frame, 'Erro', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Rastreamento", frame)
    if cv2.waitKey(5) & 0XFF == 27:  #encerra se pressionar esc
        break
t_fim = time.time()
print(t_fim - t_inicio)