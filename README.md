# NodeType
节点型数据类，任务型数据库，每一个节点都包含该节点所处坐标，快速索引， 支持指针索引，用于处理每一个分支任务的储存

类型适用范围，巨大分支，只关心分支末尾的情况，但又需要比较关系的场景

    注意单个节点的位置数为1-9，不得使用除此以外的任何数值，如需扩展，可用多个数据节点并行即可
    new = NewNode() 创建节点类

    new.add_node(NewNode.create_new_node("", 3), node_position="root") 向其中添加节点

    new.add_node(NewNode.create_new_node("1", 2), node_position="1") 向指定位置添加节点

    new.add_node(NewNode.create_new_node("2", 2), node_position="2")

    new.add_node(NewNode.create_new_node("3", 3), node_position="3")

    new.add_node(NewNode.create_new_node("12", 2), node_position="12")

    new.add_node(NewNode.create_new_node("31", 4), node_position="31")

    new.add_node(NewNode.create_new_node("32", 2), node_position="32")
    

得到结果
    {'1': {'11': None, '12': {'121': None, '122': None}}, '2': {'21': None, '22': None}, '3': {'31': {'311': None, '312': None, '313': None, '314': None}, '32': {'321': None, '322': None}, '33': None}}
    
索引

    new.find_node("root")  获得整个节点
    new.find_node("12")  获得指定节点下的节点 返回 {'121': None, '122': None}
    new.find_node_parent("21") 获得父级下的节点 返回 {'21': None, '22': None}
    
指针操作 本指针均指向节点的字符串，均为对节点的字符串进行操作

    new.set_pointer("31")  设置指针位置 指针指向'31'
    new.get_pointer()  返回指向的 {'311': None, '312': None, '313': None, '314': None}
    new.next_pointer() 向右指针移动，指针指向“32”

    new.parent_pointer() 获得父级指针，此时指针指向3

    new.child_pointer() 获得第一个子级指针，此时指针指向31
    
    new.next_pointer() 向右指针移动，指针指向“32”
    
    new.previous_pointer() 向左指针移动，指针指向“31”
    
匹配/删除

    new.traverse() # 获取所有匹配的节点 仅用于匹配节点末尾，如需匹配一个节点树，直接搜索即可，默认匹配为None，获得整个数据类未完成项
    ['11', '121', '122', '21', '22', '311', '312', '313', '314', '321', '322', '33']

    new.del_all() 删除所有节点
    
    new.del_node_child('12') 删除指定节点下的所有数据
        {'1': {'11': None, '12': None}, '2': {'21': None, '22': None}, '3': {'31': {'311': None, '312': None, '313': None, '314': None}, '32': {'321': None, '322': None}, '33': None}}
        
    new.del_node('12') 删除整个指定节点
        {'1': {'11': None}, '2': {'21': None, '22': None}, '3': {'31': {'311': None, '312': None, '313': None, '314': None}, '32': {'321': None, '322': None}, '33': None}}
    
数据紧急储存/读取

     register() 程序开始自动注册，保存最后一次数据
     load_register() 自动回复





