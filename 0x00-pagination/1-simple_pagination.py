import csv
from typing import List

def index_range(page, page_size):
    """
    Calculate the start and end indexes for a given page and page size.
    
    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.
        
    Returns:
        tuple: A tuple containing the start index and end index for the page.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")
    
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    
    return start_index, end_index - 1  # Subtracting 1 to make the end index inclusive

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."
        
        dataset = self.dataset()
        total_items = len(dataset)
        
        start_index, end_index = index_range(page, page_size)
        
        if start_index >= total_items:
            return []
        
        return dataset[start_index:end_index + 1]
