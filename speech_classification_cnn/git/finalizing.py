from getting_trainingData import *
from recoder import *
try:
    import dill as pickle
except ImportError:
    import pickle



def training():
	get_model()
	print("training complete....")


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

def load_model():
	model1 = pickle.load(open('model.pkl','rb'))
	print("model is loaded")
	return model1

model2 = pickle.load(open('model.pkl','rb'))
# making the predictions
def makePred():
    print(predict('test.wav', model=model2))


