#!/bin/bash
#GPU_ID='2'
# Choose GPU ID with CUDA_VISIBLE_DEVICES={id}
CONFIG_MAIN=avod/configs/simple/test_data.config
CONFIG_ADV=avod/configs/simple/test_data_adv.config
OUTPUT_DIR=outputs
EVAL_CKPTS='-1'

echo "training on test data"
# Train model for clean data
python avod/experiments/run_training.py \
        --pipeline_config=${CONFIG_MAIN} \
        --data_split='train' \
        --output_dir=${OUTPUT_DIR}
echo "INFERENCE CLEAN test data"
# Eval data on validation set (Clean)
python avod/experiments/run_inference.py \
        --experiment_config=${CONFIG_MAIN} \
        --data_split='val' \
        --ckpt_indices ${EVAL_CKPTS} \
        --output_dir=${OUTPUT_DIR}      
echo "INFERENCE adversarial test data"
# Eval data on validation set (adversarial)
python avod/experiments/run_inference.py \
        --experiment_config=${CONFIG_ADV} \
        --data_split='val' \
        --ckpt_indices ${EVAL_CKPTS} \
        --output_dir=${OUTPUT_DIR}
