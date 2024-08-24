from flask import config
from model.UdLogoOCRModel import UdLogoOCRModel
from model.predictor import Predictory
from model.train import Trainer
from keras.regularizers import l2
from dataset.dataloader import Dataloader
import matplotlib.pyplot as plt 
import numpy
# import wandb 
# 使用 %matplotlib inline 命令

if (__name__ == '__main__'):

    # wandb.init(project='UD-LOGO-OCR')
    # # 配置 WandB
    # config = {
    #     "learning_rate":  0.00008,
    #     "architecture": "CNN",
    #     "dataset": "LogosInTheWild-v2",
    #     "epochs": 200
    # }
    # wandb.config.update(config)  # 使用 vars() 函数将 args 转换为字典
    # Load your data (ensure `train_tensors`, `train_targets`, `val_tensors`, `val_targets`, `test_tensors`, `test_targets` are defined)
    # from dataset.dataload import train_tensors, train_targets, val_tensors, val_targets, checkpointer, test_tensors, test_targets
    print('dataload start-------------',)
    dataloader = Dataloader()
    train_files,train_targets,val_files,val_targets,test_targets = dataloader.train_and_val_split()
    train_tensors, train_targets, val_tensors, val_targets, test_tensors, test_targets = dataloader.getTrain_val_test_tensors()
    
    # Define input shape and number of classes based on your dataset
    input_shape = train_tensors.shape[1:]
    num_classes = 481

    # Instantiate the model
    print('model compile start-------------')
    model = UdLogoOCRModel(input_shape, num_classes,train_tensors)
    model.compile()

    # Instantiate the trainer
    checkpoint_path = 'saved_keras_models/weights.best.CNN.hdf5'
    trainer = Trainer(model.model, checkpoint_path)

    print('model training start-------------')
    # Train the model
    history = trainer.train(train_tensors, train_targets, val_tensors, val_targets, epochs=200,learning_rate=0.00007)
    if history is None:
        print("The training history is None,Pls check the training process")

    # wandb.log({"train_loss": history.history['loss'][-1],"train_accuracy": history.history['accuracy'][-1],"val_loss": history.history['val_loss'][-1],"val_accuracy": history.history['val_accuracy'][-1]})
    # wandb.finish()
    print('model training end with histroy -------------',history.history)
    epochs = len(history.history["accuracy"])  
    plt.style.use("ggplot")
    plt.figure()
    plt.plot(numpy.arange(0,epochs),history.history["accuracy"],label="accuracy")
    plt.plot(numpy.arange(0,epochs),history.history["val_accuracy"],label="val_accuracy")
    plt.title("Training and Validation Accuracy")
    plt.xlabel("Epoch #")
    plt.ylabel("Accuracy")
    plt.legend(loc="upper left")
    plt.show()

    # Load the best weights after training
    trainer.load_best_weights(checkpoint_path)
    # Instantiate the predictor
    predictor = Predictory(model.model)
    # Evaluate the model on the test set
    test_loss, test_accuracy = predictor.evaluate(test_tensors, test_targets)
    print(f"Test loss: {test_loss}, Test accuracy: {test_accuracy}")

    # Optionally save the trained model
    model.save_model('saved_keras_models/final_model.h5')


    


