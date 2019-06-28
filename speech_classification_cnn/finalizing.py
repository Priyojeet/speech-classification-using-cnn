from getting_trainingData import *
from recoder import *



# getting the audio
def getAudio():
    rec = Recorder()
    print("Start recording")
    rec.start()
    time.sleep(5)
    print("Stop recording")
    rec.stop()
    print("Saving")
    rec.save("test.wav")


# making the predictions
def makePred():
    print(predict('test.wav', model=model))

