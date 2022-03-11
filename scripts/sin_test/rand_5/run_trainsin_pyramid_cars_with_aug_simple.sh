#!/bin/bash
#GPU_ID='2'
# Choose GPU ID with CUDA_VISIBLE_DEVICES={id}
CONFIG_MAIN=avod/configs/simple/rand_5/trainsin_pyramid_cars_with_aug_simple_rand_5.config
CONFIG_ADV=avod/configs/simple/rand_5/trainsin_pyramid_cars_with_aug_simple_rand_5_adv.config
OUTPUT_DIR=outputs
EVAL_CKPTS='-1'

# Fine-Tune model for noisy data
python avod/experiments/run_training.py \
        --pipeline_config=${CONFIG_MAIN} \
        --data_split='train' \
        --output_dir=${OUTPUT_DIR}

# Eval data on adversarial data
python avod/experiments/run_inference.py \
        --experiment_config=${CONFIG_ADV} \
        --data_split='val' \
        --ckpt_indices ${EVAL_CKPTS}        
        --output_dir=${OUTPUT_DIR}