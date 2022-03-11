#!/bin/bash
set -e
repo=$(pwd)
prev=$(cd ../ && pwd)
cd $1 
$repo/scripts/offline_eval/kitti_native_eval/evaluate_object_3d_offline $prev/avod_data/Kitti/object/training/label_2/ $2/$3 | tee -a ./$4_results_$2.txt
