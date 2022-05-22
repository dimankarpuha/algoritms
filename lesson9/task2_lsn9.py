# 2. Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter
from binarytree import Node


def cod_haffman(s):
    binary_str = [format(ord(x), 'b') for x in s]
    cnt = Counter(binary_str)

    while len(cnt) > 1:
        min_count = cnt.most_common()[:-3:-1]  # берем два мин эл-та
        el1 = min_count[0][0]
        el2 = min_count[1][0]
        size_el1 = min_count[0][1]   # сохраняем какое количество было в очереди
        size_el2 = min_count[1][1]
        node = Node(size_el1 + size_el2)   # создаем новую ноду(в имени у нее размер, но можно и просто пустую оставить
        # условия иначе класс Нод выдает ошибку, если будем записывать просто число
        if not isinstance(el1, Node) and not isinstance(el2, Node):
            node.left = Node(el1)
            node.right = Node(el2)
        elif isinstance(el1, Node) and isinstance(el2, Node):
            node.left = el1
            node.right = el2
        elif isinstance(el1, Node):
            node.left = el1
            node.right = Node(el2)
        elif isinstance(el2, Node):
            node.left = Node(el1)
            node.right = el2
        #  В счетчик помещаем Ноду
        cnt += Counter({node: size_el1 + size_el2})
        # удаляем из счетчика два объединенных элемента (который мы только что добавили)
        del cnt[el1]
        del cnt[el2]
    return cnt


def create_table_daffman(btree):
    table_daffman = {}
    path = []
    def _create_table_daffman(btree, path):
        if btree.left is not None:
            path.append(0)
            _create_table_daffman(btree.left, path[:]) # в рекурсию отправляем срез пути иначе мы отправим ссылку
            path.pop()
        if btree.right is not None:
            path.append(1)
            _create_table_daffman(btree.right, path[:])
            path.pop()
        if btree.left is None and btree.right is None:
            table_daffman[btree.value] = path
    _create_table_daffman(btree, path)
    return table_daffman



str_for_code = 'beep boop beer!'
btree_cnt = cod_haffman(str_for_code)
btree = list(btree_cnt.elements())[0]
print(btree)
print(create_table_daffman(btree))




