import cv2
import os

#Carrega o classificador Haar Cascade para gatos
cat_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')

def processa_frame(video_path):
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print(f"Erro ao abrir o vídeo: {video_path}")
        return

    while True:
        ret, frame = video.read()
        if not ret:
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gatos = cat_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=3, minSize=(75, 75))

        for (x, y, w, h) in gatos:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('Detecção de Gatos', frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    #Tive problemas tentando rodar o video entao utilizei este caminho absoluto, caso o seu de problemas tambem
    video_path = os.path.abspath(r'C:\Users\vitor.toniolo\Documents\Estudos\IA-VisaoComp\env-visao\visao-computacional\vagas\video\cat.mp4')
    #video_path = 'video/cat.mp4'
    processa_frame(video_path)
