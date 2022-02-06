# AVOD for Single Source Robustness Against Adversarial Attacks.
This project is worked on by Amy Nguyen ([@amuamushu](https://github.com/amuamushu)) and Ayush More ([@ayushmore](https://github.com/ayushmore)) over the course of roughly 6 months under the mentorship of Lily Weng. For context on our work, please take a look at our project proposal: https://docs.google.com/document/d/1Bgs7Imq6swV6FdzWi7xMLcEBQPIgxPxYTfv1dqjEyYM.

## Setup
### Container Setup
To mimic our environment, please build a docker container using the image `amytn/avod-adv:latest`. To prevent memory errors, please ensure your container has **at least 16 GB of RAM** available. For faster runtime, including a GPU may be useful.

### Cloning the repository
Since this reposity contains a submodule, cloning would require an additional commandline argument. 

Make sure to clone the reposity in your home directory so the Python paths in the Docker image match up. If the repository is cloned elsewhere, please set up the python path yourself (see [Setting up Necessary Python Paths](#setting-up-necessary-python-paths)).

```
git clone -- recurse-submodules https://github.com/amuamushu/adv_avod_ssn.git
```

### Test Run
```
python3 run.py [test] [clean]
```
#### `test` target: 
Runs training and inference on test data found under `test/testdata` and writes the predictions and AP scores to the `outputs/<checkpoint_name>` directory. For this target, the checkpoint name is `test_data`.

#### `clean` target: 
Deletes all files in the `outputs` folder.

#### Configuration Files: 
The configuration files used can be found under `config/test.json`. 

**Here are what the configurations mean:**

`pipeline_config`: Specifies the path to the model configurations (batch size, number of steps, learning rate, number of iterations, etc).

`data_split`: Can be `train`, `val`, or `test`. Whichever keyword is specified determines which samples are used.

`output_dir`: Path to where the results and AP scores are written to.

`ckpt_indices`: This value specifies which model checkpoint to use for inference. 
  - Every couple of steps during training, the current trained model is saved to a checkpoint. 

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

#### Visualization with bounding boxes, IoU scores, and confidence level: 
Run the below code to generate bounding boxes on top of the images used during inference. Images will be saved to `outputs/<checkpoint_name>/predictions/images_2d`

```
python3 demos/show_predictions_2d.py <checkpoint_name>
```

**Here is an example of a generated image**:
![000152](https://user-images.githubusercontent.com/35519361/152208158-833ca90f-911a-4ab5-a846-e167cfc2e1a3.png)

## The dataset
The dataset we will be using is the [KITTI dataset](http://www.cvlibs.net/datasets/kitti/). For the dataset and mini-batch setup, please follow the steps listed in the [AVOD repository](https://github.com/kujason/avod#dataset). If you are not using the sample data in `test/testdata`, preparing the data is necessary for training and inference.

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

We referred to the KITTI dataset webiste (http://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=3d) and its related papers to better understand our dataset.
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
export PYTHONPATH=$PYTHONPATH:'<path to avod>'
```
