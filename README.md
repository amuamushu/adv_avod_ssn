- targets, contributers, reference repositories (links to kitti and aovd and avod ssn) and our project proposal and report

# AVOD for Single Source Robustness Against Adversarial Attacks.
This project is worked on by Amy Nguyen (@amuamushu) and Ayush More (@amore) over the course of roughly 6 months. For context on our work, please take a look at our project proposal: https://docs.google.com/document/d/1Bgs7Imq6swV6FdzWi7xMLcEBQPIgxPxYTfv1dqjEyYM.

## Setup
### Container Setup
To mimic our environment, please build a docker container using the image `amytn/avod-adv:latest`. For prevent memory errors, please ensure your container has **at least 4 GB of RAM** available.

### Cloning the repository
Since this reposity contains a submodule, cloning would require an additional commandline argument. 

Make sure to clone the reposity in your home directory so the python paths set in the dockerfile match up. If the repository is cloned elsewhere, please set up the python path yourself (see Setting up Necessary Python Paths).

```
git clone -- recurse-submodules https://github.com/amuamushu/adv_avod_ssn.git
```

### Test Run
```
python3 run.py [test] [clean]
```
`test` target: runs training and inference on test data found under `test/testdata` and writes the predictions and AP scores to the `outputs/<checkpoint_name>` directory. For this target, the checkpoint name is `test_data`.

`clean` target: deletes all files in the `outputs` folder

**Configuration Files**: The configuration files directly used can be found under `config/test.json`. Here are what the configurations mean:
pipeline_config: specifies the path to the model configurations (batch size, number of steps, learning rate, number of iterations, etc).
data_split: Can be `train`, `val`, or `test`. Whichever keyword is specified determines which samples are used.
output_dir: path to where the results and ap scores should be written to.
ckpt_indices: Every couple of steps during training, the current trained model is saved to a checkpoint. This value specifies which model checkpoint to use for inference. 


### Viewing Results
**AP Scores**: The AP scores can be found under `outputs/<checkpoint_name>/offline_eval/results` where the 3 values provided for each test corresponds to easy, medium, and hard respectively.

Here is an exmaple of what the AP Scores look like:
```
car_detection AP: 89.973267 87.620293 80.301704
car_detection_BEV AP: 89.292168 86.383148 79.538277
car_heading_BEV AP: 89.177887 85.891479 78.938744
car_detection_3D AP: 77.332970 67.945251 66.929985
car_heading_3D AP: 77.288345 67.749474 66.543098
```

**Visualization with bounding boxes and AP scores**: run `python3 demos/show_predictions_2d.py <checkpoint_name>` to generate bounding boxes on top of the images used during inference.

Here is an example of such an image:
![000152](https://user-images.githubusercontent.com/35519361/152208158-833ca90f-911a-4ab5-a846-e167cfc2e1a3.png)


## References
This project builds off of Kim, Taewan and Ghosh, Joydeep's work on "Single Source Robustness in Deep Fusion Models." In their GitHub repository for their paper (https://github.com/twankim/avod_ssn), they incorporate single source noise into the inputs of the AVOD 3D object detection model. We expand on their work and code by incorporating adversarial noise, rather than Gaussian noise, into the input images.
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
## Appendix
### Setting Up Necessary Python Paths

