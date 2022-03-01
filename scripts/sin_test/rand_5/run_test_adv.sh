#!/bin/bash
#GPU_ID='2'
# Choose GPU ID with CUDA_VISIBLE_DEVICES={id}
CONFIG_MAIN=avod/configs/simple/test_adv.config
OUTPUT_DIR=outputs
# EVAL_CKPTS='60 90 120' 
EVAL_CKPTS='120'

echo "TRAINING test adv"
# Train model for clean data
# python avod/experiments/run_training.py \
#         --pipeline_config=${CONFIG_MAIN} \
#         --data_split='train' # \
#         # --output_dir=${OUTPUT_DIR}
echo "INFERENCE CLEAN test adv"
# Eval data on validation set (Clean)
python avod/experiments/run_inference.py \
        --experiment_config=${CONFIG_MAIN} \
        --data_split='val' \
        --ckpt_indices ${EVAL_CKPTS}
        # --output_dir=${OUTPUT_DIR} \        