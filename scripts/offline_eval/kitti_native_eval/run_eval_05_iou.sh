#!/bin/bash

set -e

cd $1
echo "$3" | tee -a ./$4_results_05_iou_$2.txt
# ./evaluate_object_3d_offline_05_iou ~/Kitti/object/training/label_2/ $2/$3 | tee -a ./$4_results_05_iou_$2.txt
./scripts/offline_eval/kitti_native_eval/evaluate_object_3d_offline_05_iou /data/kitti_avod/object/training/label_2/ $2/$3 | tee -a ./$4_results_05_iou_$2.txt
echo $4_results_05_iou_$2.txt $5 "print run_eval_05_iou.sh"
cp $4_results_05_iou_$2.txt $5
