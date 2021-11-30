#GPU_ID='2'
# Choose GPU ID with CUDA_VISIBLE_DEVICES={id}
CONFIG_MAIN=avod/configs/simple/test.config
EVAL_CKPTS='2'

# Train model for clean data
python avod/experiments/run_training.py \
        --pipeline_config=${CONFIG_MAIN} \
        --data_split='train' # \

# Eval data on validation set (Clean)
python avod/experiments/run_inference.py \
        --experiment_config=${CONFIG_MAIN} \
        --data_split='val' \
        --ckpt_indices ${EVAL_CKPTS}