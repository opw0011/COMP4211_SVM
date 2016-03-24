from svmutil import *

y, x = svm_read_problem('data/train.txt')

# train model
m = svm_train(y, x, '-v 5')
svm_save_model('model_file', m)

# prediction
p_label, p_acc, p_val = svm_predict(y, x, m)

(ACC, MSE, SCC) = evaluations(y, p_label)
print y
