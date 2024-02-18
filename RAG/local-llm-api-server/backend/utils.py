import logging
from flask import render_template_string

class Utils:

  def templatizeFile(self, filename, **kwargs):
    with open('RAG/local-llm-api-server/templates/' + filename) as f:
      filestr = f.read()
    templete_str = render_template_string(filestr, **kwargs)
    return templete_str
  
class FaissEmbeddingStorage:

  def __init__(*args, **kwargs):
    import sys
    import os
    # chat_with_rtx_root = rf"C:\Users\kurtw\AppData\Local\NVIDIA\ChatWithRTX"
    module_path = rf'RAG\trt-llm-rag-windows-main'
    sys.path.append(os.path.join(os.getenv('CHAT_WITH_RTX_ROOT'), module_path))  # Add directory to search path
    module_path = rf'env_nvd_rag\Lib\site-packages'
    sys.path.append(os.path.join(os.getenv('CHAT_WITH_RTX_ROOT'), module_path))  # Add directory to search path
    from faiss_vector_storage import FaissEmbeddingStorage
    return FaissEmbeddingStorage(args, kwargs)