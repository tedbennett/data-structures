## data-structures

### Description
My implementations of the data structures described in *Data Structures and Algorithms in Python* by Goodrich, 
Tamassia and Goldwasser. After reading the textbook, I decided to have a go at implementing the structures based 
only on their description and the necessary functionality.

### Simple Data Structures

#### Stack
A stack supports push(item), pop(), top(), is_empty() and len() member functions. It's implemented as a Python array.

#### Queue
A queue supports similar a similar interface to a stack, except that the pop() and top() are replaced by dequeue() 
and first(), which simply refer to the first element of the queue. The queue is implemented similarly to the stack, 
except that dequeue() calls replace the returned element with None and the class keeps track of the index of the 
first item of the dequeue.

The circular queue inherits from the QueueBase class, and has a maximum length. This is a space-saving version, as the
queue can wrap around the array it is implemented as.

#### Deque
A double-ended queue allows for adding and removing elements from both ends of the queue. This is implemented as an 
expanded circular queue.

### Linked Lists

#### Singly-Linked Lists
A linked list comprises nodes, which refer to the data they contain, and the next node
in the container. This is used to implement a stack and a queue.

#### Doubly-Linked Lists
These nodes also include a reference to the previous item in the list. The list is
enclosed by 'sentinels', which are nodes that signify the ends of the list, making
operations at the ends simpler.

#### Positional List
Implemented as a doubly-linked list, this ADT includes Position objects that refer
to a node in the list. Adjacent positions can be accessed as well as an iterator.

