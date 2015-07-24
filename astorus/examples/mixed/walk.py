import ast
import astor


class LightWalk(astor.TreeWalk):
    def init_count(self):
        self.count = 0

    def pre_If(self):
        self.count += 1

    def pre_Compare(self):
        self.count += 1

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

    def pre_If(self):
        self.count += 1
        if 2**self.count & self.path:
            self.replace(ast.If(ast.UnaryOp(ast.Not(), self.cur_node.test),
                                self.cur_node.body,
                                self.cur_node.orelse))

    def pre_Compare(self):
        # cmpop = Eq | NotEq | Lt | LtE | Gt | GtE | Is | IsNot | In | NotIn

        opposites = {
            ast.Lt: ast.Gt,
            ast.Gt: ast.Lt,
            ast.LtE: ast.GtE,
            ast.GtE: ast.LtE,
        }

        self.count += 1
        if 2**self.count & self.path:
            newops = []
            for op in self.cur_node.ops:
                if type(op) not in opposites:
                    newops.append(op)
                    continue
                newops.append(opposites[type(op)]())

            self.replace(ast.Compare(self.cur_node.left,
                                     newops,
                                     self.cur_node.comparators))
