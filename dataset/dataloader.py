from sympy import false
import util.utils as utils
from json import load
from sklearn.datasets import load_files
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from keras.preprocessing import image                  
from PIL import ImageFile                            
ImageFile.LOAD_TRUNCATED_IMAGES = True   
import numpy
import os


class Dataloader:  
    
    def __init__(self) :
        print('Dataloader path',os.getcwd())
        #load files from LogosInTheWild direcotry with logo categories givn by their subfoloder name 
        
        self.data = load_files('dataset/LogosInTheWild-v2/data_cleaned/voc_format')
        logo_files = numpy.array(self.data['filenames'])
        jpg_indices = [index for index ,name in enumerate(logo_files) if 'jpg' == name.split('.')[-1]]
        logo_target = np_utils.to_categorical(numpy.array(self.data['target'],max(self.data['target']+1)))
        self.all_files,self.all_targets = logo_files[jpg_indices],logo_target[jpg_indices]
        print(f"got training data size:{len(self.all_files)}")

    def train_and_val_split(self):
        # split into 80% training+validation files+labels, and 20% test files+labels
        train_and_val_files, self.test_files, train_and_val_targets, self.test_targets = train_test_split(self.all_files, self.all_targets, test_size=0.2)
        # further split into 80% training files+labels, and 20% validation files+labels
        self.train_files, self.val_files, self.train_targets, self.val_targets = train_test_split(train_and_val_files, train_and_val_targets, test_size=0.2)
        return self.train_files, self.train_targets, self.val_files, self.val_targets, self.test_targets

                
    def path_to_tensor(self,img_path):
        try:
            if os.path.exists(img_path):
                # loads RGB image as PIL format with 224x224 pixels
                if utils.is_valid_image(img_path):
                    img = image.load_img(img_path, target_size=(224, 224))
                    # convert to 3D tensor with shape (224, 224, 3) with 3 RGB channels
                    x = image.img_to_array(img)
                    return numpy.expand_dims(x, axis=0)
                else:
                    raise ValueError(f"image is not valid:{img_path}")
        except Exception as e:
            print(f"File was not found:{img_path} ,error:{e}")
            raise
        # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return it
       

    def paths_to_tensor(self,img_paths):
        list_of_tensors = []
        valid_indices = []
        for i, img_path in enumerate(img_paths):
            try:
                tensor = self.path_to_tensor(img_path)
                list_of_tensors.append(tensor)
                valid_indices.append(i)
            except Exception as ef:
                print(f"Skipping invalid image: {img_path}")
        #stack the (1,224,224,3) 4D tensor arrays to a (# images,224,224,3) 4D tensor
        return numpy.vstack(list_of_tensors),valid_indices

    def getTrain_val_test_tensors(self):
        #create 4D tensors and rescale each pixel by dividing by RGB max value 255
        train_tensors,tran_valid_indices = self.paths_to_tensor(self.train_files)
        train_tensors = train_tensors.astype('float32')/255
        self.train_targets = self.train_targets[tran_valid_indices]


        val_tensors, val_valid_indices = self.paths_to_tensor(self.val_files)
        val_tensors = val_tensors.astype('float32') / 255
        self.val_targets = self.val_targets[val_valid_indices]

        test_tensors, test_valid_indices = self.paths_to_tensor(self.test_files)
        test_tensors = test_tensors.astype('float32') / 255
        self.test_targets = self.test_targets[test_valid_indices]
        return train_tensors, self.train_targets, val_tensors, self.val_targets, test_tensors, self.test_targets

