from svmutil import *
from math import pow
# from __future__ import print_function

# use 5-fold cross validation, and return the best C
def find_c(prob, param):
    C_RANGE_MIN = pow(2, -5)
    C_RANGE_MAX = pow(2, 5)    
    max_acc = 0
    best_c = 0
    c = C_RANGE_MIN
    # -q : quiet, -v: cross validation
    param = svm_parameter(param + ' -q -v 5 -c ' + str(c))

    while c <= C_RANGE_MAX:
	    # print "c = ", c
	    acc = svm_train(prob, param)
	    
	    if(acc > max_acc):
	    	max_acc = acc
	    	best_c = c
	    
	    c *= 2;

    print "The chosen C is " + str(best_c) + " ,with accuracy of " + str(max_acc)
    return best_c


def main():
	# read the training data
    y1, x1 = svm_read_problem('../data/train.txt')
    prob = svm_problem(y1, x1)

    y2, x2 = svm_read_problem('../data/test.txt')
    result_list = [];

    # train model
    model = svm_train(prob, '-q -t 1 -g 1 -r 1 -d 1 -c 0.25')
    svm_save_model('../model/model', model)

    # predict the training data
    print "Traning data"
    p_labels, p_acc, p_vals = svm_predict(y1, x1, model)

    # predict the testing data
    print "testing data"
    p_labels, p_acc, p_vals = svm_predict(y2, x2, model)
    
    print p_labels[:10]
    # f = open('workfile', 'w')
    # for i in p_labels:
    # 	print(i, file=f)
    
    # (ACC, MSE, SCC) = evaluations(y2, p_labels)
    # print ACC, MSE, SCC
    exit();


    # find c for degree 1 to 5
    for d in range(1,6):
    	print "Degree ", d
    	# kernel -- polynomial: (1*u'*v + 1)^degree (d from 1 to 5)
    	param = '-t 1 -g 1 -r 1 -d '+ str(d)
    	c = find_c(prob, param)
    	result_list.append(c);

    for l in result_list:
    	print "For poly kernel with degree d = " , result_list.index(l)+1 , ", i = ", l


if __name__ == "__main__":
    main()
