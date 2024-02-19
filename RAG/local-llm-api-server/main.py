import sys
import os
from dotenv import load_dotenv
load_dotenv()
module_path = rf'RAG\trt-llm-rag-windows-main'
full_module_path = os.path.join(os.getenv('CHAT_WITH_RTX_ROOT'), module_path)
sys.path.append(full_module_path)
import shutil
# Empty the dataset dir
# TODO: Consider making deletion a configuration
dirpath = os.path.join(full_module_path, 'dataset')
if os.path.exists(dirpath) and os.path.isdir(dirpath):
  shutil.rmtree(dirpath)
# Empty the dataset embeddings dir
dirpath = os.path.join(full_module_path, 'dataset_vector_embedding')
if os.path.exists(dirpath) and os.path.isdir(dirpath):
  shutil.rmtree(dirpath)
# copy the local dataset dir to the RTX dataset dir
dataset_source = os.path.join(os.getcwd(), 'dataset')
dataset_destination = os.path.join(full_module_path, 'dataset')
shutil.copytree(dataset_source, dataset_destination, dirs_exist_ok=True) 
# # Copy the ChatWithRTX object oriented patch
patch_source = os.path.join(os.getcwd(), 'ChatWithRTX_patch', 'app.py')
patch_destination = os.path.join(full_module_path, 'app.py')
shutil.copy(patch_source, patch_destination) 
os.chdir(full_module_path)
print('opening app...')
import app
# app.start_interface()
app.start_api_interface()