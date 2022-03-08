#!/bin/bash
#GPU_ID='2'
# Choose GPU ID with CUDA_VISIBLE_DEVICES={id}
CONFIG_MAIN=avod/configs/simple/test_adv.config
CONFIG_CLEAN=avod/configs/simple/test_adv_clean.config
CONFIG_EVALSIN=avod/configs/simple/rand_5/pyramid_cars_with_aug_simple_evalsin_rand_5.config
OUTPUT_DIR=outputs
# EVAL_CKPTS='60 90 120' 
EVAL_CKPTS='-1'

echo "training an adversarial model"
python avod/experiments/run_training.py \
        --pipeline_config=${CONFIG_MAIN} \
        --data_split='train' \
        --output_dir=${OUTPUT_DIR}

echo "inference on adversarial data"
python avod/experiments/run_inference.py \
        --experiment_config=${CONFIG_MAIN} \
        --data_split='val' \
        --ckpt_indices ${EVAL_CKPTS} \
        --output_dir=${OUTPUT_DIR}      

echo "inference on clean data"
python avod/experiments/run_inference.py \
        --experiment_config=${CONFIG_CLEAN} \
        --data_split='val' \
        --ckpt_indices ${EVAL_CKPTS} \
        --output_dir=${OUTPUT_DIR}      

echo "inference on ssn"
# Eval data on validation set (SIN)
python avod/experiments/run_inference.py \
        --experiment_config=${CONFIG_EVALSIN} \
        --data_split='val' \
        --ckpt_indices ${EVAL_CKPTS} \
        --output_dir=${OUTPUT_DIR}      

echo "evaluate ssn results"
python ./utils_sin/sin_calc_avg_kitti_eval.py \
        --experiment_config=${CONFIG_EVALSIN} \
        --data_split='val'