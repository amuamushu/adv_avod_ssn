"""Detection model trainer.
This runs the DetectionModel trainer.
"""

import argparse
import os
from sys import argv

import tensorflow as tf

import avod
import avod.builders.config_builder_util as config_builder
from avod.builders.dataset_builder import DatasetBuilder
from avod.core.models.avod_model import AvodModel
from avod.core.models.rpn_model import RpnModel
from avod.core import trainer

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

def train(model_config, train_config, dataset_config):

    dataset = DatasetBuilder.build_kitti_dataset(dataset_config,
                                                 use_defaults=False)

    train_val_test = 'train'
    model_name = model_config.model_name

    with tf.Graph().as_default():
        if model_name == 'rpn_model':
            model = RpnModel(model_config,
                             train_val_test=train_val_test,
                             dataset=dataset)
        elif model_name == 'avod_model':
            model = AvodModel(model_config,
                              train_val_test=train_val_test,
                              dataset=dataset)
        else:
            raise ValueError('Invalid model_name')

        trainer.train(model, train_config)


def main(args):
    parser = argparse.ArgumentParser()

    # Defaults
    default_pipeline_config_path = avod.root_dir() + \
        '/configs/avod_cars_example.config'
    default_data_split = 'train'
    default_output_dir = './outputs'

    parser.add_argument('--pipeline_config',
                        type=str,
                        dest='pipeline_config_path',
                        default=default_pipeline_config_path,
                        help='Path to the pipeline config')

    parser.add_argument('--data_split',
                        type=str,
                        dest='data_split',
                        default=default_data_split,
                        help='Data split for training')

    parser.add_argument('--device',
                        type=str,
                        dest='device',
                        default=None,
                        help='CUDA device id')

    parser.add_argument('--output_dir',
                        type=str,
                        dest='output_dir',
                        default=default_output_dir,
                        help='output dir to save checkpoints')

    args, unknown = parser.parse_known_args(args=args)
    # Parse pipeline config
    model_config, train_config, _, dataset_config = \
        config_builder.get_configs_from_pipeline_file(
            args.pipeline_config_path, is_training=True,
            output_dir=args.output_dir)

    # Overwrite data split
    dataset_config.data_split = args.data_split

    # Set CUDA device id
    if args.device:
        os.environ['CUDA_VISIBLE_DEVICES'] = args.device

    train(model_config, train_config, dataset_config)


if __name__ == '__main__':
    tf.compat.v1.app.run(argv=argv)