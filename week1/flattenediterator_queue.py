from queue import Queue 

class FlattenedIterator:
    def __init__(self, iterators):
        iter_queue = Queue()
        for iterator in iterators:
            if iterator.hasNext():
                iter_queue.put(iterator)
        self._iter_queue = iter_queue

    def __iter__(self):
        return self

    def __next__(self):      
        if not self.hasNext():
            raise StopIteration
        curr_iter = self._iter_queue.get()
        next_elem = next(curr_iter)
        
        if curr_iter.hasNext():
            self._iter_queue.put(curr_iter)
            
        return next_elem

    def hasNext(self):
        return not self._iter_queue.empty()
