from __future__ import print_function
from svmutil import *
from math import pow

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

    print("The chosen C is %s , with accuracy of %s " % (best_c, max_acc))
    return best_c


def main():
	# read the training data
    y1, x1 = svm_read_problem('../data/train.txt')
    prob = svm_problem(y1, x1)

    y2, x2 = svm_read_problem('../data/test.txt')
    selected_c = [];

    # exit()

    # find c for degree 1 to 5
    for d in range(1,6):
    	print("Degree ", d)
    	# kernel -- polynomial: (1*u'*v + 1)^degree (d from 1 to 5)
    	param = '-t 1 -g 1 -r 1 -d '+ str(d)
    	c = find_c(prob, param)
    	selected_c.append(c);

    for l in selected_c:
    	print("For poly kernel with degree d = %s , c = %s" % (selected_c.index(l)+1, l))



    # train model with chosen c
    for d in range(1,6):
	    c = selected_c[d-1]
	    print("Training with d = %s, c = %s" % (d, c))
	    model = svm_train(prob, '-q -t 1 -g 1 -r 1 -d %s -c %s' % (d, c))
	    svm_save_model('../model/model_d%s' % d, model)

	    # predict the training data
	    print("Traning data")
	    p_labels, p_acc, p_vals = svm_predict(y1, x1, model)

	    # predict the testing data
	    print("testing data")
	    p_labels, p_acc, p_vals = svm_predict(y2, x2, model)
	    
	    # write output into file
	    f = open('../output/output_d%s' % d, 'w')
	    for i in p_labels:
	    	print(i, file=f)


if __name__ == "__main__":
    main()
