from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D, Dropout, Dense,BatchNormalization
from keras.models import Sequential
from onnx import load_model
from keras.regularizers import l2

class UdLogoOCRModel():


    def __init__(self,input_shape,num_class,train_tensors):

        self.model = Sequential()

        #after the input layer, add the first convolutional layer with 32 2x2-filters 
        self.model.add(Conv2D (kernel_size = (3,3), filters = 32, padding='same',
                            input_shape=train_tensors.shape[1:], activation='relu',kernel_regularizer=l2(0.00)))
         # 添加批归一化层
        self.model.add(BatchNormalization())
        #add a max pooling layer with a 2x2 pooling window
        self.model.add(MaxPooling2D(pool_size=2))
        # 添加Dropout层，丢弃20%的节点
        self.model.add(Dropout(0.15))

        #add the second convolutional layer with 64 2x2-filters 
        self.model.add(Conv2D(kernel_size =  (3,3), filters = 64,padding='same', activation='relu',kernel_regularizer=l2(0.008)))
          # 添加批归一化层
        self.model.add(BatchNormalization())
        self.model.add(MaxPooling2D(pool_size=2))
        # 添加Dropout层，丢弃20%的节点
        self.model.add(Dropout(0.15))

        #add the third convolutional layer with 128 2x2-filters 
        self.model.add(Conv2D(kernel_size =  (3,3), filters = 128,padding='same', activation='relu',kernel_regularizer=l2(0.008)))
          # 添加批归一化层
        self.model.add(BatchNormalization())
        self.model.add(MaxPooling2D(pool_size=2))
        # 添加Dropout层，丢弃20%的节点
        self.model.add(Dropout(0.15))

        #add the third convolutional layer with 256 2x2-filters 
        self.model.add(Conv2D(kernel_size =  (3,3), filters = 128, padding='same',activation='relu',kernel_regularizer=l2(0.008)))
          # 添加批归一化层
        self.model.add(BatchNormalization())
        self.model.add(MaxPooling2D(pool_size = 2))
        #add a dropout layer so that each node has a chance of 20% to be dropped when training
        self.model.add(Dropout(0.15))
    
        #add a global average pooling layer
        self.model.add(GlobalAveragePooling2D())
        #add the final fully connected output layer with 109 node for all 109 logo classes
        self.model.add(Dense(num_class, activation = 'softmax'))
        self.model.summary()

    def compile(self,optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy']):
        self.model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    def save_model(self,filepath):
        self.model.save(filepath)

    def load_model(self,filepath):
        self.model = load_model(filepath)

        

