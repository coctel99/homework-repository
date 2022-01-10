from homework6.task1 import instances_counter


@instances_counter
class User:
    def __init__(self, name):
        self.name = name


def test_count_created_instances():
    """Testing that created instances are counted."""
    user, _, _ = User("Alex"), User("Mike"), User("Ivan")
    assert user.get_created_instances() == 3 and user.name == "Alex"


def test_reset_instances_counter():
    """Testing that counter of created instances is being reset."""
    user, _, _ = User("Alex"), User("Mike"), User("Ivan")
    user.reset_instances_counter()
    assert user.get_created_instances() == 0 and user.name == "Alex"
