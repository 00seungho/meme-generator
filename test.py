import os
import subprocess
import argparse
paser = argparse.ArgumentParser(description="인자 처리 프로그램")
paser.add_argument('path', help="경로 입력")
args = paser.parse_args()
current_directory = os.getcwd()
file_path = os.path.dirname(args.path.split('path=')[-1])
file_name_extension = os.path.basename(args.path)   
file_name = os.path.splitext(file_name_extension)[0]
print(file_path)
print(file_name_extension)
os.chdir(file_path)
subprocess.run(f"pdftotext -layout {file_name_extension} temp.txt")
os.remove("temp.txt")