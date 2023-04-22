import warnings
from typing import Optional, TypeVar, Any
from nodetype import nodetype
import time

T = TypeVar('T', bound='NodeType')


class NodeType(nodetype):
    """
    树状节点储存类
    """

    def __init__(self, count=0, parent_node=""):
        super(NodeType, self).__init__(count, parent_node)
        self.pointer = ""

    def set_pointer(self, node_position):
        """
        指针操作：设置当前指向
        :param node_position: 指针位置
        :return:
        """
        self.pointer = node_position  # pointer储存的是地址，不是对象本身
        return self.find_node(node_position)

    def get_pointer(self):
        """
        指针操作：获取当前指向
        :return: 返回指针
        """
        return self.find_node(self.pointer)

    def len_pointer(self):
        """
        指针操作：获取当前长度
        :return: 返回长度
        """
        return self.find_node(self.pointer).__len__()

    def next_pointer(self):
        """
        指针操作：移动到下一个
        :return: 返回下一个指向的位置
        """
        _next = str(int(self.pointer)+1)
        _len = self.find_node_parent(self.pointer).__len__()
        if _next[-1] > str(_len):
            print("不可能移动到下一个")
            return None
        self.pointer = _next

        return self.find_node(_next)

    def previous_pointer(self):
        """
        指针操作：移动到上一个
        :return: 返回上一个指向的位置
        """
        _next = int(self.pointer)-1
        _len = self.find_node_parent(self.pointer).__len__()
        if _next < 1:
            print("不可能移动到上一个")
            return None
        self.pointer = str(_next)
        return self.find_node(str(_next))

    def child_pointer(self):
        """
        指针操作：移动到第一个子级
        :return: 指向子级
        """
        _new = self.pointer + "1"
        try:
            self.find_node(_new)
        except Exception:
            print("子级未定义")
            return None
        self.pointer += "1"
        return self.find_node(self.pointer)

    def parent_pointer(self):
        """
        指针操作：移动到父级
        :return: 指向父级
        """
        self.find_node_parent(self.pointer)
        self.pointer = self.pointer[:-1]
        return self.pointer

    def add_node(self, new_node: T, node_position) -> T:
        """
        :param new_node: 必须为NodeType
        :param node_position: 父节点位置
        :return: 返回整个节点
        """
        self.find_node_parent(node_position)[node_position] = new_node
        return self

    def find_node(self, node_number: str) -> Optional[T]:
        """
        :param node_number: 节点数字
        :return: 返回查询到的节点, 可能是None，可能是一个字典，如果为None则已经到底，如果是一个字典则为中间节点
        """
        _list_node = [_a for _a in node_number]
        _now_node = self[_list_node[0]]
        if len(_list_node) > 1:
            for _d in range(1, len(_list_node)-1):
                _now_node = _now_node[node_number[:_d+1]]
            return _now_node[node_number]
        return _now_node

    def find_node_parent(self, node_number=Optional[str]) -> Optional[T]:
        """
        :param node_number: 节点数字| 节点
        :return: 返回查询到的父节点
        """
        if not node_number:
            return self.find_node_parent(list(self.keys())[0][-1])
        if isinstance(node_number, str):
            _len = len(node_number)
            _now = self
            if _len == 1:
                return self
            for _ in range(_len-1):
                _now = _now[str(node_number[:_+1])]
            return _now
        if isinstance(node_number, NodeType):
            return self.find_node_parent(list(node_number.keys())[0][:-1])

    def padding(self, node_number, _v: Any):
        """
        对节点进行填充
        :param node_number: 节点位置
        :param _v:
        :return:None
        """
        self.set_timestamp()
        self.find_node_parent(node_number)[node_number] = _v

    def traverse(self, match=None) -> dict:
        """
        对节点末端进行筛选和处理
        :param match:
        :return: 返回一个字典
        """
        _dict = dict()

        def run(node: dict):
            if node != match:
                for _a, _b in node.items():
                    if run(_b) == "isNone":
                        _dict.update({_a: _b})
            else:
                return "isNone"
        run(self)
        return _dict

    def del_node(self, node_number: str):
        """
        删除整个节点
        :param node_number:
        :return:
        """
        warnings.warn("对节点本身删除是不安全的", DeprecationWarning)
        _a = self.find_node_parent(node_number)
        _a[node_number] = None
        del _a[node_number]

    def del_node_child(self, node_number: str):
        """
        删除节点下的数据
        :param node_number:
        :return:
        """
        _a = self.find_node_parent(node_number)
        _a[node_number] = None


if __name__ == "__main__":
    new = NodeType(5)
    new.add_node(NodeType(2, "1"), "1")
    new.add_node(NodeType(1, "2"), "2")
    new.add_node(NodeType(2, "11"), "11")
    new.add_node(NodeType(3, "21"), "21")
    new.add_node(NodeType(2, "211"), "211")
    new.add_node(NodeType(2, "3"), "3")
    print(new)

    new.set_pointer("31")
    new.get_pointer()
    new.next_pointer()
    new.find_node_parent("21")
    new.parent_pointer()

    new.child_pointer()

    new.next_pointer()
    print(new.pointer)
    new.previous_pointer()

    print(new.traverse())
    print(new.find_node("11"))


