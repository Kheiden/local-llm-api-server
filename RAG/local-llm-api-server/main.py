import sys
import os
from dotenv import load_dotenv
load_dotenv()
module_path = rf'RAG\trt-llm-rag-windows-main'
sys.path.append(os.path.join(os.getenv('CHAT_WITH_RTX_ROOT'), module_path))  # Add directory to search path
module_path = rf'RAG\trt-llm-rag-windows-main'
os.chdir(os.path.join(os.getenv('CHAT_WITH_RTX_ROOT'), module_path))
import app