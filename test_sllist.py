# Test cases to ensure functionality of SingleLinkedList class.

from nose.tools import *
from sllist import SingleLinkedList


def test_push():
    colors = SingleLinkedList()
    colors.push('blue')
    assert colors.count() == 1
    colors.push('red')
    assert colors.count() == 2


def test_pop():
    colors = SingleLinkedList()
    colors.push('magenta')
    colors.push('red')
    assert colors.pop() == 'red'
    assert colors.pop() == 'magenta'
    assert colors.pop() == None


def test_popleft():
    colors = SingleLinkedList()
    colors.push('purple')
    colors.push('green')
    colors.push('yellow')
    assert colors.popleft() == 'purple'
    assert colors.popleft() == 'green'
    assert colors.popleft() == 'yellow'
    assert colors.popleft() == None


def test_remove():
    colors = SingleLinkedList()
    colors.push('red')
    colors.push('white')
    colors.push('blue')
    colors.push('yellow')
    assert colors.count() == 4

    assert colors.remove('white') == True
    assert colors.count() == 3
    assert colors.dump() == '[red, blue, yellow]'

    assert colors.remove('blue') == True
    assert colors.count() == 2

    assert colors.remove('banana') == False
    
    assert colors.remove('yellow') == True
    assert colors.count() == 1


def test_first():
    colors = SingleLinkedList()
    colors.push('red')
    assert colors.first() == 'red'

    colors.push('yellow')
    assert colors.first() == 'red'

    colors.push('blue')
    assert colors.first() == 'red'


def test_last():
    colors = SingleLinkedList()
    colors.push('red')
    assert colors.last() == 'red'

    colors.push('yellow')
    assert colors.last() == 'yellow'

    colors.push('blue')
    assert colors.last() == 'blue'


def test_dump():
    colors = SingleLinkedList()
    colors.push('red')
    colors.push('white')
    colors.push('blue')
    colors.push('yellow')
    assert colors.dump() == '[red, white, blue, yellow]'

    colors.remove('white')
    assert colors.dump() == '[red, blue, yellow]'

    colors.pop()
    assert colors.dump() == '[red, blue]'

    colors.popleft()
    assert colors.dump() == '[blue]'


def test_get():
    colors = SingleLinkedList()
    colors.push('red')
    assert colors.get(0) == 'red'

    colors.push('yellow')
    assert colors.get(0) == 'red'
    assert colors.get(1) == 'yellow'

    colors.push('green')
    assert colors.get(0) == 'red'
    assert colors.get(1) == 'yellow'
    assert colors.get(2) == 'green'

    colors.pop()
    assert colors.get(0) == 'red'
    assert colors.get(1) == 'yellow'
    assert colors.get(2) == None

    colors.pop()
    assert colors.get(0) == 'red'
    assert colors.get(1) == None
    assert colors.get(2) == None

    colors.pop()
    assert colors.get(0) == None
    assert colors.get(1) == None
    assert colors.get(2) == None
