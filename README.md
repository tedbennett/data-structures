## data-structures

### Description
My implementations of the data structures described in *Data Structures and Algorithms in Python* by Goodrich, 
Tamassia and Goldwasser. After reading the textbook, I decided to have a go at implementing the structures based 
only on their description and the necessary functionality.

### Stack
A stack supports push(item), pop(), top(), is_empty() and len() member functions. It's implemented as a Python array.

### Queue
A queue supports similar a similar interface to a stack, except that the pop() and top() are replaced by dequeue() 
and first(), which simply refer to the first element of the queue. The queue is implemented similarly to the stack, 
except that dequeue() calls replace the returned element with None and the class keeps track of the index of the 
first item of the dequeue.

The circular queue inherits from the QueueBase class, and has a maximum length. This is a space-saving version, as the
queue can wrap around the array it is implemented as.
