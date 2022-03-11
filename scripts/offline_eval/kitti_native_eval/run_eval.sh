#!/bin/bash
set -e
repo=$(pwd)
cd $1 
$repo/scripts/offline_eval/kitti_native_eval/evaluate_object_3d_offline ../avod_data/Kitti/object/training/label_2/ $2/$3 | tee -a ./$4_results_$2.txt
cwd=$(pwd)
cd ~/avod_ssn
cp -R $cwd/$4_results_$2.txt $5
cd $cwd