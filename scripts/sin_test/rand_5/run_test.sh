#!/bin/bash
#GPU_ID='2'
# Choose GPU ID with CUDA_VISIBLE_DEVICES={id}
CONFIG_MAIN=avod/configs/simple/test.config
CONFIG_EVALSIN=avod/configs/simple/rand_5/evalsin_test.config
EVAL_CKPTS='-1'

# Train model for clean data
python avod/experiments/run_training.py \
        --data_split='train' \
        --pipeline_config=${CONFIG_MAIN}
echo "CLEAN RUN INFERENCE"
# Eval data on validation set (Clean)
python avod/experiments/run_inference.py \
        --experiment_config=${CONFIG_MAIN} \
        --data_split='val' \
        --ckpt_indices ${EVAL_CKPTS}      