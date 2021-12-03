from homework6.task1 import instances_counter


@instances_counter
class User:
    pass


def test_count_created_instances():
    """Testing that created instances are counted."""
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3  # 3


def test_reset_instances_counter():
    """Testing that counter of created instances is being reset."""
    user, _, _ = User(), User(), User()
    user.reset_instances_counter()  # 3
    assert user.get_created_instances() == 0
