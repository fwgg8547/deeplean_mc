from keras.utils import np_utils
from keras import layers, models
from keras import optimizers
import numpy as np
import mydefines


nb_classes = len(categories)
training_data = np.load(root_dir + training_data_dir + '/' + training_data_name)

train = []
for f in training_data.files:
    train.append(training_data[f])

X_train = train[0].astype('float') /255
Y_train = np_utils.to_categorical(train[1], nb_classes)

# model
model = models.Sequential()
model.add(layers.Conv2D(32,(3,3),activation="relu",input_shape=(img_width,img_height,3)))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64,(3,3),activation="relu"))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(128,(3,3),activation="relu"))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(128,(3,3),activation="relu"))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Flatten())
model.add(layers.Dense(512,activation="relu"))
model.add(layers.Dense(10,activation="sigmoid")) #分類先の種類分設定

#モデル構成の確認
model.summary()

# compile model
model.compile(loss="binary_crossentropy",
              optimizer=optimizers.RMSprop(lr=1e-4),
              metrics=["acc"])

# do leaning
model = model.fit(X_train,
                  y_train,
                  epochs=10,
                  batch_size=6,
                  validation_data=(X_test,y_test))

