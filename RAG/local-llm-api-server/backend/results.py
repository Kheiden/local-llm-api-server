import os
from typing import List
# from backend.utils import FaissEmbeddingStorage

class Results:

  def __init__(self):
    data_dir = os.getenv('DATASET_DIR')
    # faiss_storage = FaissEmbeddingStorage(data_dir=data_dir,
    #                                           dimension=os.getenv('DIMENSION_COUNT'))


  def returnTop3Matches(self, query)-> List[str]:
    # TODO: integrate with vector storage query
    return ['foobar1','foobar2','foobar3']