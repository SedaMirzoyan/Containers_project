class Stack:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.stack = []

    def is_empty(self):
        if (self.top == -1):
            print("Stack is empty")
            return True
        else:
            return False

    def is_full(self):
        if (self.top == self.size-1):
            print("Stack is Full")
            return True
        else:
            return False


    def push(self, data):
        is_full = self.is_full()

        if(is_full):
            print("Can't push element, stack is full")
            return self.size-1
        
        self.top += 1
        self.size += 1
        self.stack.append(data)



    def pop(self):
        is_empty = self.is_empty()

        if(is_empty):
            print("Can't pop element, stack is empty")
            return self.size-1
        
        elem = self.stack[self.top]
        self.stack.remove(self.stack[self.top])
        self.top -= 1
        self.size -= 1
        
        return elem
    

    def peek(self):
        elem = self.stack[self.top]
        print(f"Top element is {elem}")

        return elem
        


    def print_stack(self):
        i = self.top
        while(i >= 0):
            print(self.stack[i])
            i -= 1

  
    def clean(self):
        i = self.top
        while(i >= 0):
            self.stack.remove(self.stack[i])
            i -= 1   
        self.top = i


    def reverse(self):
        temp_list = []

        #make list from stack elements
        i = self.top
        while(i >= 0):
            temp_list.append(self.stack[i])
            i -= 1

        #clean stack
        self.clean()

        #move elements from list to stack
        for i in temp_list:
            temp_data = i
            self.push(temp_data)


    def check_if_palindrome(self, input_str):
        for i in input_str:
            self.push(i) 

        bottom_ptr = 0
        top_ptr = self.top
        flag = False

        while(bottom_ptr <= self.size - 1 and top_ptr >= 0):
            if(self.stack[top_ptr] == self.stack[bottom_ptr]):
                flag = True
            else:
                flag = False
                break
            bottom_ptr += 1
            top_ptr -= 1
            if (bottom_ptr == top_ptr):
                break

        return flag




def main():
    stack_size = 8
    obj = Stack(stack_size)

    for i in range(1, stack_size+1):
        obj.push(i)

    print("Printing stack")
    obj.print_stack()
    print("Printing stack after removing element")
    obj.pop()
    obj.print_stack()

    print("Printing stack after reverse")
    obj.reverse()
    obj.print_stack()
    obj.peek()

    #check for palindrome
    obj.clean()
    input_str1 = "rotator"
    input_str2 = "khekhe"
    input_str3 = "madam"
    input_str4 = "abcdefdcba"
    print(obj.check_if_palindrome(input_str1))
    obj.clean()
    print(obj.check_if_palindrome(input_str2))
    obj.clean()
    print(obj.check_if_palindrome(input_str3))
    obj.clean()
    print(obj.check_if_palindrome(input_str4))



if __name__ == "__main__":
    main()