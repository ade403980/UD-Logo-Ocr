class Predictory:
    def __init__(self,model) :
        self.model = model
    
    def predict(self,input_tensor):
        return  self.model.predict(input_tensor)
    
    def evaluate(self,test_tensors,test_targets):
        return self.model.evaluate(test_tensors,test_targets,verbose=0)