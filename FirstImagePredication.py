from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd()
prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath( execution_path + "\resnet50_weights_tf_dim_ordering_tf_kernels.h5")
prediction.loadModel()


predictions, percentage_probabilities = prediction.predictImage("C:\Users\MyUser\Downloads\sample.jpg", result_count=5)
for index in range(len(predictions)):
print(predictions[index] , " : " , percentage_probabilities[index])
