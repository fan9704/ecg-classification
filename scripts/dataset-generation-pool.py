import multiprocessing as mp
import os.path as osp
import subprocess
from glob import glob

from tqdm import tqdm

input_dir = "../mit-bih/*.atr"
ecg_data = sorted([osp.splitext(i)[0] for i in glob(input_dir)])
print(ecg_data)
pbar = tqdm(total=len(ecg_data))


def run(file):
    params = ["pipenv","run","python", "dataset-generation.py", "--file", file]#Windows ver and add pipenv
    #params = ["python3", "dataset-generation.py", "--file", file] #Linux ver
    subprocess.check_call(params)
    pbar.update(1)


if __name__ == "__main__":
    p = mp.Pool(processes=mp.cpu_count())
    p.map(run, ecg_data)
