#!/bin/bash

set -e
echo $1 "first 1"
cd $1 
# ../teams/DSC180A_FA21_A00/a15/avod_data/kitti_avod/object/outputs/test/predictions_sin_rand_5.0_5/image/kitti_native_eval/
echo "$3" | tee -a ./$4_results_$2.txt
# ./evaluate_object_3d_offline ~/Kitti/object/training/label_2/ $2/$3 | tee -a ./$4_results_$2.txt
~/avod_ssn/scripts/offline_eval/kitti_native_eval/evaluate_object_3d_offline ~/teams/DSC180A_FA21_A00/a15/avod_data/Kitti/object/training/label_2/ $2/$3 | tee -a ./$4_results_$2.txt
echo $2/$3 "results directory"
echo $4_results_$2.txt $5 "print run_eval.sh"
cat ./$4_results_$2.txt  && echo "CATTING run_eval.sh"
pwd && echo "WORKING DIR"
cd ~/avod_ssn
cp -R $4_results_$2.txt $5
echo "END OF FILE RUN EVAL"