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
    
    return start_index, end_index - 1
