from typing import Union, Optional
import atexit
import json


class NewNode:
    """
        节点数据库
        注意：节点数据库节点不得储存除节点末端以外的任何数据
    """

    def __init__(self):
        self.__dict = dict()
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
        _len = self.find_node(self.pointer).__len__()
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

    def finish_node(self):
        pass

    def add_node(self, new_node, node_position="root"):
        """
        :param new_node: 由create_new_node创建
        :param node_position: 父节点位置
        :return: 返回整个节点
        """
        if node_position == "root":
            self.__dict = new_node
            return self.__dict

        self.find_node_parent(node_position)[node_position] = new_node
        return self.__dict

    @staticmethod
    def create_new_node(parent_node, count: int) -> dict:
        """
        :param parent_node: 父节点位置
        :param count: 新节点数量
        :return: 新的节点
        最多可以容纳9个选项，足够满足
        """
        if parent_node == "root":
            parent_node = ""

        _list = [f"{parent_node}{_a}" for _a in range(1, count+1)]
        return dict.fromkeys(_list)

    def find_node(self, node_number: str) -> Optional[dict]:
        """
        :param node_number: 节点数字
        :return: 返回查询到的节点, 可能是None，可能是一个字典，如果为None则已经到底，如果是一个字典则为中间节点
        """
        if node_number == "root":
            return self.__dict

        _list_node = [_a for _a in node_number]
        _now_node = self.__dict[_list_node[0]]
        if len(_list_node) > 1:
            for _d in range(1, len(_list_node)-1):
                _now_node = _now_node[node_number[:_d+1]]
            return _now_node[node_number]
        return _now_node

    def find_node_parent(self, node_number: Union[str, dict]) -> dict:
        """
        :param node_number: 节点数字| 节点
        :return: 返回查询到的父节点
        """
        if isinstance(node_number, str):
            if node_number == "root":
                return self.__dict

            _list_node = [_a for _a in node_number]
            if len(_list_node) == 1:
                return self.__dict

            _now_node = self.__dict[_list_node[0]]
            for _d in range(1, len(_list_node)-1):
                _now_node = _now_node[_list_node[:_d]]
            return _now_node

        if isinstance(node_number, dict):
            return self.find_node_parent(list(node_number.keys())[0][:-1])

    def traverse(self, match=None) -> list:
        """
        获得所有指定匹配的节点
        :param match:
        :return: 返回列表
        """
        _list = []

        def run(node: dict):
            if node != match:
                for a, b in node.items():
                    if run(b) == "isNone":
                        _list.append(a)
            else:
                return "isNone"

        run(self.__dict)
        return _list

    def del_all(self):
        """
        销毁所有数据
        :return:
        """
        self.__dict = dict()

    def del_node(self, node_number: str):
        """
        删除整个节点
        :param node_number:
        :return:
        """
        a = self.find_node_parent(node_number)
        a[node_number] = None
        del a[node_number]

    def del_node_child(self, node_number: str):
        """
        删除节点下的数据
        :param node_number:
        :return:
        """
        a = self.find_node_parent(node_number)
        a[node_number] = None

    def register(self):
        """
        强制回收未完成的节点数据,调用后自动注册
        :return:
        """
        def _register():
            if self.__dict:
                with open('register.json', 'w') as f:
                    f.write(json.dumps(self.__dict))
        atexit.register(_register)

    def load_register(self):
        """
        回收后恢复，请确保储存文件未丢失
        :return:
        """
        with open('register.json', 'r') as f:
            self.__dict = json.loads(f.read())


if __name__ == "__main__":
    new = NewNode()
    return_ = new.add_node(NewNode.create_new_node("", 3), node_position="root")

    new.add_node(NewNode.create_new_node("1", 2), node_position="1")

    new.add_node(NewNode.create_new_node("2", 2), node_position="2")

    new.add_node(NewNode.create_new_node("3", 3), node_position="3")

    new.add_node(NewNode.create_new_node("12", 2), node_position="12")

    new.add_node(NewNode.create_new_node("31", 4), node_position="31")

    new.add_node(NewNode.create_new_node("32", 2), node_position="32")

    print(new.find_node("root"))
    new.set_pointer("31")
    new.get_pointer()

    print(new.next_pointer())

    print(new.parent_pointer())

    print(new.child_pointer())

    print(new.next_pointer())

    print(new.previous_pointer())

    print(new.traverse())

    print(new.del_all())
    print(new.find_node("root"))

