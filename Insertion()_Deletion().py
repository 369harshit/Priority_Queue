# Priority Queue implementation using Queue concepts.
class P_Queue(object):
    def __init__(self):
        self.q = []

    # In built function isEmpty to checking if the queue is empty
    def isEmpty(self):
        return len(self.q) == []

    # In built function for inserting an element in the queue
    def insert(self, data):
        self.q.append(data)

    # delete function for pop out an element based on theirPriority
    def popout(self):
        try:
            # initialization of variable.
            max = 0
            # for loop for finding maximum value in the queue.
            for i in range(len(self.q)):
                if self.q[i] > self.q[max]:
                    max = i
            # store maximum value  element in x.
            x = self.q[max]
            # del function use to delete the maximum value from queue.
            del self.q[max]
            # return max value
            return x
        except IndexError:
            print()
            exit()


# class object
ob = P_Queue()
# taking queue size from users
x = int(input("Enter the size of queue"))
# for loop to insert the element into he queue by calling insert function.
for i in range(x):
    ob.insert(int(input("Enter the  element ")))
# print element according to their priority
while not ob.isEmpty():
    print(ob.popout())
