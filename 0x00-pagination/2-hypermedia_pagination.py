#!/usr/bin/env python3
""" 2-hypermedia_pagination """
import csv
import math
from typing import List, Tuple, Dict


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """ returns a tuple of size two
        containing a start and end index
        """
        last = page * page_size
        first = last - page_size

        return (first, last)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get the page dataset of the file """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        dataset = self.dataset()

        try:
            first, last = self.index_range(page, page_size)
            return dataset[first:last]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ returns a key value pair of some info """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.get_page(page, page_size)
        first, last = self.index_range(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        if (page < total_pages):
            next_page = page + 1
        else:
            next_page = None

        if (page == 1):
            prev_page = None
        else:
            prev_page = page - 1

        return {'page_size': len(data),
                'page': page,
                'data': data[first:last],
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages}
