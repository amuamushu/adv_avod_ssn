import sys
import os
import json
import shutil
import subprocess

OUTPUT_PATH = "./outputs"

def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'. 
    
    `main` runs the targets in order of data=>analysis=>model.
    '''
    if 'clean' in targets:
        if os.path.exists(OUTPUT_PATH):
            shutil.rmtree(OUTPUT_PATH)
        os.mkdir(OUTPUT_PATH)
        
    if 'test' in targets:
        subprocess.call('scripts/sin_test/rand_5/run_test_data.sh')
        return

    if 'adv-model' in targets:
        # Runs the training and all the inferences (clean, adversarial, and SSN) on trained
        # model. Training is skipped if the model is already trained.
        subprocess.call(['scripts/sin_test/rand_5/run_adv.sh'])
        return
    
    if 'clean-model' in targets:
        # Runs the training and the adversarial inference on trained
        # model. Training is skipped if the model is already trained.
        subprocess.call(['scripts/sin_test/rand_5/run_pyramid_cars_with_aug_simple.sh'])
        return

    if 'ssn-model' in targets:
        # Runs the training and the adversarial inference on trained
        # model. Training is skipped if the model is already trained.        
        subprocess.call(['scripts/sin_test/rand_5/run_trainsin_pyramid_cars_with_aug_simple.sh'])
        return


if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)