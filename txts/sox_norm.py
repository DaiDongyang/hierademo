import os
import glob

spks = ['a', 'b', 'c', 'd', 'e', 'f']
sub_folds = ['bs', 'en', 'origin', 'ps', 'rap']

sox_temp = 'sox {0} --norm=-0.5 {1}'


def process():
    for spk in spks:
        for sub_fold in sub_folds:
            in_wav_dir = os.path.join(spk + '_origin', sub_fold)
            out_wav_dir = os.path.join(spk, sub_fold)
            os.makedirs(out_wav_dir, exist_ok=True)
            wav_names = glob.glob1(in_wav_dir, '*.wav')
            for wav_name in wav_names:
                in_path = os.path.join(in_wav_dir, wav_name)
                out_path = os.path.join(out_wav_dir, wav_name)
                sox_cmd = sox_temp.format(in_path, out_path)
                os.system(sox_cmd)
                print(sox_cmd)


if __name__ == '__main__':
    process()
