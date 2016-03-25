#!/bin/bash
for i in {1..5}
do
    python plot_train.py ../data/train.txt ../sv/sv_d$i sv_d$i.png
	python plot_test.py ../data/test.txt  ../output/output_d$i test_data_d$i.png
done
