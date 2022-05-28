import pytest
from src.maps.tree_map import TreeMap


def test_delkey():
    '''test of del'''
    tree_mapa = TreeMap()
    tree_mapa['ab'] = 1
    del tree_mapa ['ab']
    with pytest.raises(KeyError):
        tree_mapa.__getitem__('ab')


if __name__ == "__main__":
    test_delkey()

