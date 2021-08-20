class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def pop(self):
        self._items.pop()

    def push(self, item):
        self._items.append(item)

    def top(self):
        return self._items[-1]


def stack_test():
    st = Stack()
    st.push(2)
    st.push(7)
    st.top()
    st.pop()
    st.push(3)
    st.push(4)
    st.top()
    st.pop()
    st.top()
    st.pop()


def is_open(chr):
    return chr in "({["


def is_pair(open, close):
    return open == "{" and close == "}" or \
           open == "(" and close == ")" or \
           open == "[" and close == "]"


def is_balanced(s):
    st = Stack()

    for chr in s:
        if is_open(chr):
            st.push(chr)
        else:
            if not st.is_empty() and is_pair(st.top(), chr):
                st.pop()
            else:
                return False

    return st.is_empty()


print(is_balanced("{}[]()({[()()]})"))
print(is_balanced("[{}(])"))
print(is_balanced("()"))
print(is_balanced(""))



