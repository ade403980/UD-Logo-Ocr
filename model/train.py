

import wandb
from fsspec import Callback
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
# from wandb.integration.keras import WandbCallback


class Trainer:
    def __init__(self,model,checkpoint_path):
        self.model = model
        self.checkpointer = ModelCheckpoint(filepath=checkpoint_path,save_best_only=True,verbose=1)

    def train(self,train_tensors,train_targets,val_tensors,val_targets,epochs=100,learning_rate=0.0003):
        print(f"train data lenth:{len(train_tensors)}")
        # Data augmentation
        datagen = ImageDataGenerator(
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest'
        )
        datagen.fit(train_tensors)  
        # Early stopping and learning rate reduction callbacks
        early_stopping = EarlyStopping(monitor='val_loss', patience=15, restore_best_weights=True)
        reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=5, min_lr=learning_rate)
        # Wandb_Callback = WandbCallback()

        self.history = self.model.fit(datagen.flow(train_tensors, train_targets, batch_size=10),
                                      validation_data=(val_tensors,val_targets),steps_per_epoch=len(train_tensors)//10, epochs=epochs,
                                      callbacks=[early_stopping, reduce_lr,self.checkpointer])
        return self.history
    
    def load_best_weights(self,checkpoint_path):
        self.model.load_weights(checkpoint_path)

    
