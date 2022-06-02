import os, argparse
parser = argparse.ArgumentParser()
parser.add_argument('--weights-path', type=str, default='best.pt')
parser.add_argument('--input-dir', type=str, default='../all_videos/')
parser.add_argument('--output-dir', type=str, default='../detected_videos')
args = vars(parser)

os.chdir('./yolov5/')
os.system(f'python detect.py --weights {args['weights_path']} --img 720 --conf 0.25 --source {args['input_dir']} --nosave --save-crop --save-crop-vid-path {args['output_dir']}')