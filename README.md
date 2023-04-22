# NodeType
节点型数据类，任务型数据库，每一个节点都包含该节点所处坐标，快速索引， 支持指针索引，用于处理每一个分支任务的储存


    注意单个节点的位置数为1-9，不得使用除此以外的任何数值，如需扩展，可用多个数据节点并行即可
    new = NodeType(5) 创建节点类

    new.add_node(NodeType(2, "1"), "1") 向1的位置添加2个子节点

    new.add_node(NodeType(1, "2"), "2") 向2位置添加1个子节点节点

    new.add_node(NodeType(2, "11"), "11")
    
    new.add_node(NodeType(3, "21"), "21")
    
    new.add_node(NodeType(2, "211"), "211")
    
    new.add_node(NodeType(2, "3"), "3")
    

得到结果
    {'1': {'11': {'111': None, '112': None}, '12': None}, '2': {'21': {'211': {'2111': None, '2112': None}, '212': None, '213': None}}, '3': {'31': None, '32': None}, '4': None, '5': None}
    
索引

    new.find_node_parent()  获得整个节点
    new.find_node("11")  获得指定节点下的节点 返回 {'111': None, '112': None}
    new.find_node_parent("21") 获得父级下的节点 返回  {'211': {'2111': None, '2112': None}, '212': None, '213': None}}
    
指针操作 本指针均指向节点的字符串，均为对节点的字符串进行操作

    new.set_pointer("31")  设置指针位置 指针指向'31'
    new.get_pointer()  返回指向的 None
    new.next_pointer() 向右指针移动，指针指向“32”

    new.parent_pointer() 获得父级指针，此时指针指向3

    new.child_pointer() 获得第一个子级指针，此时指针指向31
    
    new.next_pointer() 向右指针移动，指针指向“32”
    
    new.previous_pointer() 向左指针移动，指针指向“31”
    
匹配/删除

    new.traverse() # 获取所有末端返回一个字典
    {'111': None, '112': None, '12': None, '2111': None, '2112': None, '212': None, '213': None, '31': None, '32': None, '4': None, '5': None}
    
    new.del_node_child('11') 删除指定节点下的所有数据
        {'1': {'11': None, '12': None}, '2': {'21': {'211': {'2111': None, '2112': None}, '212': None, '213': None}}, '3': {'31': None, '32': None}, '4': None, '5': None}
        
节点时间戳

    new.get_timestamp() 获取节点的时间戳
    new.find_node("11").get_timestamp() 获取子节点的时间戳




