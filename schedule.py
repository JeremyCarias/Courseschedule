from search_trees import BSTMap, AVLTreeMap
from schedule_item import ScheduleItem

class Schedule:
    def __init__(self):
        self.bst = BSTMap()
        self.avl = AVLTreeMap()

    def add_entry(self, item,):
        key = item.get_key()
        self.bst.insert(key, item)
        self.avl.insert(key, item)


    def find_by_subject(self, subject, tree='bst'):
        subject = subject.upper().strip()
        tree_map = self.bst if tree == 'bst' else self.avl
        return [item for _, item in tree_map.inorder_items() if item.subject.upper().strip() == subject]

    def find_by_subject_catalog(self, subject, catalog, tree='bst'):
        subject = subject.upper().strip()
        catalog = catalog.upper().strip()
        tree_map = self.bst if tree == 'bst' else self.avl
        return [item for _, item in tree_map.inorder_items() if item.subject.upper().strip() == subject and item.catalog.upper().strip() == catalog]

    def find_by_instructor_last_name(self, last_name, tree='bst'):
        last_name = last_name.upper().strip()
        tree_map = self.bst if tree == 'bst' else self.avl
        return [item for _, item in tree_map.inorder_items() if last_name in item.instructor.upper().strip()]

    def print(self, tree='bst'):
        tree_map = self.bst if tree == 'bst' else self.avl
        print_header()
        for _, item in tree_map.inorder_items():
            item.print()
        
                                           
                                           
      

       
    