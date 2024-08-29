# # Enter your code here. Read input from STDIN. Print output to STDOUT

# def make_op(result, ops, cmd, _ops):
#     a = cmd.split(' ')
#     if a[0] == '1':
#         [result.append(c) for c in a[1]]
#         ops.append(cmd)
#     elif a[0] == '2':
#         ops.append(cmd)
#         try:
#             for c in range(int(a[1])):
#                 _ops.append(result.pop())
#         except:
#             pass
#     elif a[0] == '3':
#         print(result[int(a[1])-1])
#     elif a[0] == '4':
#         cmd = ops.pop()
#         a = cmd.split(' ')
#         if a[0] == '1':
#             try:
#                 [result.pop() for c in a[1]]
#             except:
#                 pass
#         elif a[0] == '2':
#             _ops = _ops[::-1]
#             for i, c in enumerate(_ops):
#                 result.append(c)
#                 _ops.pop(i)
#     # print(result, _ops)

# result = []
# ops = []
# _ops = []
# q = int(input())
# for i in range(q):
#     cmd = input()
#     make_op(result, ops, cmd, _ops)
    
class TextEditor:
    def __init__(self):
        self.current_str = []
        self.stack = []
    
    def append(self, s):
        self.stack.append("".join(self.current_str))
        self.current_str.extend(list(s))
        
    def delete(self, k):
        self.stack.append("".join(self.current_str))
        for _ in range(k):
            _ = self.current_str.pop()
    
    def print(self, k):
        print(self.current_str[k-1])

    def undo(self):
        self.current_str = list(self.stack.pop())
        
    def command(self, s):
        op = int(s[0])
        # print(self.current_str, self.stack)
        if op == 1:
            self.append(s.split(" ")[-1])
        elif op == 2:
            self.delete(int(s.split(" ")[-1]))
        elif op == 3:
            self.print(int(s.split(" ")[-1]))
        elif op == 4:
            self.undo()

if __name__ == "__main__":
    Q = int(input())
    editor = TextEditor()
    for _ in range(Q):
        command = input()
        editor.command(command)
