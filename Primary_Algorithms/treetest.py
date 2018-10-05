# coding=utf-8
class TreeNode(object):
    def __init__(self, x, i):
        self.val = x
        self.loc = i


class BuildTree():
    def findNode(self, x, form):
        for i in range(len(form)):
            for j in range(len(form[i])):
                if form[i][j] == x:
                    return i, j

    def transform(self, form):
        node_i, node_j = self.findNode(0, form)
        root = TreeNode(0, 0)
        pass

    def find_path(self, graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = self.find_path(graph, node, end, path)
                if newpath:
                    return newpath
        return None
