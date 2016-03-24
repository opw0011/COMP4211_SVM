from svmutil import *
from math import pow

# use 5-fold cross validation, and return the best C
def find_c(prob, param):
    C_RANGE_MIN = pow(2, -5)
    C_RANGE_MAX = pow(2, 5)    
    max_acc = 0
    best_c = 0
    c = C_RANGE_MIN
    # with 5-fold cross validation
    param = svm_parameter(param + ' -q -v 5 -c ' + str(c))

    while c <= C_RANGE_MAX:
	    print "c = ", c
	    acc = svm_train(prob, param)
	    
	    if(acc > max_acc):
	    	max_acc = acc
	    	best_c = c
	    
	    c *= 2;

    print "The chosen C is " + str(best_c) + " ,with accuracy of " + str(max_acc)
    return best_c


def main():
	# read the training data
    y, x = svm_read_problem('../data/train.txt')
    prob = svm_problem(y, x)
    result_list = [];

    # find c for degree 1 to 5
    for d in range(1,6):
    	print "Degree ", d
    	# kernel -- polynomial: (1*u'*v + 1)^degree (d from 1 to 5)
    	param = '-t 1 -g 1 -r 1 -d '+ str(d)
    	c = find_c(prob, param)
    	result_list.append(c);

    for l in result_list:
    	print "For poly kernel with degree d = " , result_list.index(l)+1 , ", i = ", l




    # svm_save_model('model_file', m)

    # prediction
    # p_label, p_acc, p_val = svm_predict(y, x, m)

    # (ACC, MSE, SCC) = evaluations(y, p_label)
    # print y

if __name__ == "__main__":
    main()
