import ast
import astor


class LightWalk(astor.TreeWalk):
    def init_count(self):
        self.count = 0

    def pre_Name(self):
        if type(self.parent) == ast.Call:
            return

        self.count += 1

    def pre_Num(self):
        self.count += 1


class BoomWalk(astor.TreeWalk):
    def pre_Name(self):
        if type(self.parent) == ast.Call:
            return

        self.count += 1
        if 2**self.count & self.path:
            self.replace(ast.BinOp(self.cur_node, ast.Add(), ast.Num(1)))

    def pre_Num(self):
        self.count += 1
        if 2**self.count & self.path:
            self.replace(ast.Num(self.cur_node.n + 1))
