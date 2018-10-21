

#from keras.models import Sequential
#from keras.layers import Dense
from keras.models import model_from_json
import numpy as np
import cv2
from keras import optimizers

def read_img(img):
    #img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (200,200))
    img=np.resize(img,(1,200,200,3))
    img=img/255.0
    return img

def find_race(image,gender):
    json_file = open('trained_models/race_model/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    if gender=='female':

        loaded_model.load_weights("trained_models/Fweights/weights-improvement.hdf5")

    else:
        loaded_model.load_weights("trained_models/Mweights/weights-improvement.hdf5")


    image=read_img(image)

    loaded_model.compile(loss='categorical_crossentropy', optimizer=optimizers.SGD(lr=1e-4, momentum=0.9),
                  metrics=['accuracy'])


    x=np.argmax(loaded_model.predict(image))

    cls=['Asian','Black','Indian','White']

    return cls[x]

if __name__ == '__main__':
    print(find_race('4.png','female'))

