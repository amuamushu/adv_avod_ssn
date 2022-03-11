#!/bin/bash
#GPU_ID='2'
# Choose GPU ID with CUDA_VISIBLE_DEVICES={id}
CONFIG_MAIN=avod/configs/simple/pyramid_cars_with_aug_simple.config
CONFIG_EVALSIN=avod/configs/simple/rand_5/pyramid_cars_with_aug_simple_evalsin_rand_5.config
CONFIG_EVALAIN=avod/configs/simple/rand_5/pyramid_cars_with_aug_simple_evalain_rand_5.config
CONFIG_ADV=avod/configs/simple/pyramid_cars_with_aug_simple_adv.config
OUTPUT_DIR=outputs
EVAL_CKPTS='-1'

echo "TRAINING run_pyramid_cars_with_aug_simple"
# Train model for clean data
python avod/experiments/run_training.py \
        --pipeline_config=${CONFIG_MAIN} \
        --data_split='train' \
        --output_dir=${OUTPUT_DIR}
echo "INFERENCE CLEAN run_pyramid_cars_with_aug_simple"
# Eval data on validation set (Clean)
python avod/experiments/run_inference.py \
        --experiment_config=${CONFIG_MAIN} \
        --data_split='val' \
        --ckpt_indices ${EVAL_CKPTS} \
        --output_dir=${OUTPUT_DIR}      
echo "INFERENCE adversarial run_pyramid_cars_with_aug_simple"
# Eval data on validation set (adversarial)
python avod/experiments/run_inference.py \
        --experiment_config=${CONFIG_ADV} \
        --data_split='val' \
        --ckpt_indices ${EVAL_CKPTS} \
        --output_dir=${OUTPUT_DIR}