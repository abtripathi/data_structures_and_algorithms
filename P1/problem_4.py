## Problem-4 Active Directory

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
    
    
def print_hierarchy(parent,init):
   
    groups = parent.get_groups()
    users = parent.get_users()
    print('-'*init,'Group {}:'.format(parent.get_name()))
    for user in users:
        k=init+4      
        print('-'*k,'User:',user)
    for group in groups:
        print_hierarchy(group,k)
        
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against      
    """
    if user is not None:        
        users = group.get_users()
        if user in users:
            return True
        else:
            for group in group.get_groups():
                if is_user_in_group(user,group):
                    return True
    return False
    
    
parent = Group("parent")
child = Group("child")
subchild1 = Group("subchild1")

sub_child_user = "sub_child1_user1"
subchild1.add_user(sub_child_user)

child.add_group(subchild1)
parent.add_group(child)
parent.add_user('parent_user1')
parent.add_user('parent_user2')
parent.add_user('sub_child1_user1')
child.add_user('child_user1')
child.add_user('child_user2')
subchild1.add_user('sub_child1_user2')
subchild2 = Group('subchild2')
child.add_group(subchild2)
subchild2.add_user('sub_child2_user1')
subchild2.add_user('sub_child2_user2')