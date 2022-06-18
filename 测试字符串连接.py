
import os

tran_path="F:\语音识别数据库\数据库\data_thchs30\data"

wav_filename="F:\\语音识别数据库\\数据库\\data_thchs30\\data\\D7_768.wav"
tran_file = os.path.join(tran_path, wav_filename + '.trn')

print(tran_file)