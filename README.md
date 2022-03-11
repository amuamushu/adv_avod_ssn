# AVOD for Single Source Robustness Against Adversarial Attacks.
This project is worked on by Amy Nguyen ([@amuamushu](https://github.com/amuamushu)) and Ayush More ([@ayushmore](https://github.com/ayushmore)) over the course of roughly 6 months under the mentorship of Lily Weng. 

Visual Presentation: https://ayushmore.github.io/2022-03-07-improving-robustness-via-adversarial-training/

## Setup
### Container Setup
To mimic our environment, please build a docker container using the image `amytn/avod-adv:latest`. To prevent memory errors, please ensure your container has **at least 16 GB of RAM** available. For faster runtime, including a GPU may be useful.

### Cloning the repository
Since this reposity contains a submodule, cloning would require an additional commandline argument. 

Make sure to clone the reposity in your home directory so the Python paths in the Docker image match up. If the repository is cloned elsewhere, please set up the python path yourself (see [Setting up Necessary Python Paths](#setting-up-necessary-python-paths)).

```
git clone --recurse-submodules https://github.com/amuamushu/adv_avod_ssn.git
```


### The dataset
The dataset we will be using is the [KITTI dataset](http://www.cvlibs.net/datasets/kitti/). For the dataset and mini-batch setup, please follow the download steps listed in the [AVOD repository](https://github.com/kujason/avod#dataset).

For the dataset, we will be follow a slightly different setup to the one on the AVOD repository.

In your home directory, the layout should look like this:

```
home
..\avod_data
....\Kitti
......\object
........\testing
........\training
..........\calib # camera calibration (can ignore)
..........\image_2 # the 2D images
..........\label_2 # true labels and bounding boxes
..........\planes 
..........\velodyne # the lidar point clouds
....... train.txt # list of sample names to use for training
....... val.txt # list of sample names to use for validation
..\adv_avod_ssn # this repository!
  
```
More information about the true labels can be found here: https://github.com/kujason/avod/wiki/Data-Formats

## Run
```
python3 run.py [clean] [test] [clean-model] [adv-model] [ssn-model]
```
### `clean` target: 
Deletes all files in the `outputs` folder.

### `test` target: 
Runs training and inference on test data found under `test/testdata` and writes the predictions and AP scores to the `outputs/<checkpoint_name>` directory. For this target, the checkpoint name is `test_data`.
- Note: If you plan on only using the test data and not downloading the full dataset, in `scripts/offline_eval/kitti_native/eval/run_eval.sh`, please update `$prev/avod_data/Kitti/object/training/label_2/` to be `$repo/test/testdata/Kitti/object/training/label_2/`. `run_eval.sh` is used for computing the AP Scores after running inference. 

### `clean-model` target:
Runs training for a clean model and adversarial inference on the full dataset found at `home/avod_data` and writes the predictions and AP scores to the `outputs/<checkpoint_name>` directory. For this target, the checkpoint name is `pyramid_cars_with_aug_simple`.
- Calling this target runs the `run_pyramid_cars_with_aug_simple.sh` script. More details on what is happening is provided in the next section.

### `adv-model` target:
Runs training for an adversarial model and all three types of inference (clean, adversarial, SSN) on the full dataset found at `home/avod_data` and writes the predictions and AP scores to the `outputs/<checkpoint_name>` directory. For this target, the checkpoint name is `test_adv`.
- Calling this target runs the `run_adv.sh` script. More details on what is happening is provided in the next section.
- **NOTE**: Since the adversarial model only fine-tunes the clean model, running this target requires the clean model to be completely trained.

### `ssn-model` target:
Runs training for a clean model and adversarial inference on the full dataset found at `home/avod_data` and writes the predictions and AP scores to the `outputs/<checkpoint_name>` directory. For this target, the checkpoint name is `trainsin_pyramid_cars_with_aug_simple_rand_5`.
- Calling this target runs the `run_trainsin_pyramid_cars_with_aug_simple.sh` script. More details on what is happening is provided in the next section.
- **NOTE**: Since the single-source-noise model only fine-tunes the clean model, running this target requires the clean model to be completely trained.

Note: `pyramid_cars_with_aug_simple` and `trainsin_pyramid_cars_with_aug_simple_rand_5` are the same checkpoint names that our previous work author Taewan Kim had so we kept it for ease of comparison.

## The Shell Script
Each shell script is responsible for running the entire experiment for one model. Details about the specific experiments are covered in the paper.

**Arguments for training, inference, and evaluation:**

`pipeline_config`: Specifies the path to the experiment configurations (batch size, number of steps, learning rate, number of iterations, dataset path, etc).

`data_split`: Can be `train`, `val`, or `test`. Whichever keyword is specified determines which samples are used.

`output_dir`: Path to where the results and AP scores are written to.

`ckpt_indices`: This value specifies which model checkpoint to use for inference. 
  - Every couple of steps during training, the current trained model is saved to a checkpoint. 

#### Configuration Files: 
The configuration files for the test data target can be found under `./config`. 

The more comprehensive configuration files are found under `./avod/configs`.

## Experimental Configurations
Each shell script references multiple `.config` files: one for training the model and one or more for inference. 

### `model_config`:
Contains configurations for the object detection model. Notable configurations are:
- `model_name`: Should be `avod_model` for all the experiments we run.
- `checkpoint_name`: The name of the experiment checkpoint. This determines what folder the outputs are saved to.
- `is_adversarial`: A boolean value defaulted to False. Train the model adversarially and runs adversarial inference if True, otherwise train the model normally.
- `adv_epsilon`: The epsilon to use for our perturbation. To replicate our paper, this should be 0.9. Only used if the model is being trained or run inference on adversarially.

### `train_config`: 
- `pretrained_ckpt`: What checkpoint to continue training from. This would be used and should be updated as the model is being fine-tuned.

### `eval_config`:
- `dataset_dir`: The dataset used for training and infernece. 
- `pretrained_chkpt`: What trained model checkpoint to use for inference. This is useful if the inference `.config` file is different from the training `.config` file. 


### Viewing Results
#### AP Scores: 
The AP scores can be found under `outputs/<checkpoint_name>/offline_eval/results` where the 3 values provided for each test corresponds to easy, medium, and hard respectively.

**Here is an exmaple of what the AP Scores look like**:
```
car_detection AP: 89.973267 87.620293 80.301704
car_detection_BEV AP: 89.292168 86.383148 79.538277
car_heading_BEV AP: 89.177887 85.891479 78.938744
car_detection_3D AP: 77.332970 67.945251 66.929985
car_heading_3D AP: 77.288345 67.749474 66.543098
```

After inference, if the AP scores are not saved properly, they can be manually calculated and saved again using this command:
```
bash scripts/offline_eval/kitti_native_eval/run_eval.sh ./outputs/<checkpoint_name>/<prediction_type>/kitti_native_eval/ 0.1_val <training_step> <checkpoint_name>
```
- `checkpoint_name`: name of the checkpoint as specified in the `.config` file
- `prediction_type`: would be ...
   - `prediction` if inference results on clean data is wanted
   - `prediction_adv` if inference results on adversarial data is wanted
   - `predictions_sin_rand_5.0_5` if inference results on SSN data is wanted


#### Visualization with bounding boxes, IoU scores, and confidence level: 
Run the below code to generate bounding boxes on top of the images used during inference. Images will be saved to `outputs/<checkpoint_name>/predictions/images_2d`

```
python3 demos/show_predictions_2d.py <checkpoint_name>
```

**Here is an example of a generated image**:
![000152](https://user-images.githubusercontent.com/35519361/152208158-833ca90f-911a-4ab5-a846-e167cfc2e1a3.png)



## References
This project builds off of Kim, Taewan and Ghosh, Joydeep's work on "Single Source Robustness in Deep Fusion Models." In their GitHub repository (https://github.com/twankim/avod_ssn), they incorporate single source noise into the inputs of the AVOD 3D object detection model. We expand on their work and code by incorporating adversarial noise, rather than Gaussian noise, into the input images.
```
@inproceedings{kim2019single,
  title={On Single Source Robustness in Deep Fusion Models},
  author={Kim, Taewan and Ghosh, Joydeep},
  booktitle={Advances in Neural Information Processing Systems},
  pages={4815--4826},
  year={2019}
}
```

We also relied on the documentation of the original AVOD code (https://github.com/kujason/avod) for setting up the model and data as well as understanding our results.
```
@article{ku2018joint, 
  title={Joint 3D Proposal Generation and Object Detection from View Aggregation}, 
  author={Ku, Jason and Mozifian, Melissa and Lee, Jungwook and Harakeh, Ali and Waslander, Steven}, 
  journal={IROS}, 
  year={2018}
}
```

We referred to the KITTI dataset website (http://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=3d) and its related papers to better understand our dataset.
```
A. Geiger, P. Lenz and R. Urtasun, "Are we ready for autonomous driving? The KITTI vision benchmark suite," 
2012 IEEE Conference on Computer Vision and Pattern Recognition, 2012, pp. 3354-3361, doi: 10.1109/CVPR.2012.6248074. 
http://www.cvlibs.net/publications/Geiger2012CVPR.pdf
```


## Appendix
### Setting Up Necessary Python Paths
Run these two commands to set the Python paths for `avod_ssn` and `wavedata`:
```
export PYTHONPATH=$PYTHONPATH:'<path to avod>'
export PYTHONPATH=$PYTHONPATH:'<path to wavedata>'
```

### Pretrained Models:
Since training takes many hours, we included our pretrained clean model here:
https://drive.google.com/drive/folders/18U7t-4gU4sXvAD33GEuVnwSwUSItHdPX?usp=sharing
