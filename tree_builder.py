class EmployeeNode:
    """
    A class to represent a node in the binary tree.

    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    """

    def __init__(self, name: str):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    """
    A class to represent a binary tree for managing a team structure.

    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.

    Methods:
        insert(manager_name, employee_name, side, current_node=None):
            Inserts a new employee under the specified manager.
        print_tree(node=None, level=0):
            Prints the tree structure starting from the given node.
    """

    def __init__(self):
        self.root = None

    def insert(
        self, manager_name: str, employee_name: str, side: str, current_node=None
    ) -> bool:
        """
        Recursively search for manager_name and insert employee_name on the given side.

        Returns:
            bool: True if inserted successfully, False otherwise.
        """

        # Validate side
        if side not in ["left", "right"]:
            print("❌ Invalid side. Please enter LEFT or RIGHT.")
            return False

        # If tree is empty, cannot insert under a manager
        if self.root is None:
            print("❌ No team lead exists yet. Please add a team lead first.")
            return False

        # Initialize current_node on the first call
        if current_node is None:
            current_node = self.root

        # If we found the manager, attempt insertion
        if current_node.name.strip().lower() == manager_name.strip().lower():
            if side == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the LEFT of {manager_name}")
                    return True
                print(f"⚠️ LEFT side of {manager_name} is already occupied.")
                return False

            if side == "right":
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the RIGHT of {manager_name}")
                    return True
                print(f"⚠️ RIGHT side of {manager_name} is already occupied.")
                return False

        # Otherwise, keep searching both branches
        inserted_left = False
        inserted_right = False

        if current_node.left is not None:
            inserted_left = self.insert(
                manager_name, employee_name, side, current_node.left
            )
            if inserted_left:
                return True

        if current_node.right is not None:
            inserted_right = self.insert(
                manager_name, employee_name, side, current_node.right
            )
            if inserted_right:
                return True

        # Only print manager not found if we are back at the root level and nothing inserted
        if current_node == self.root and not (inserted_left or inserted_right):
            print(
                f"❌ Manager '{manager_name}' not found in the current team structure."
            )
        return False

    def print_tree(self, node=None, level: int = 0) -> None:
        """
        Recursively prints the team structure using indentation.
        """
        if node is None:
            if level == 0:
                node = self.root
                if node is None:
                    print("(empty)")
                    return
            else:
                return

        indent = "  " * level
        print(f"{indent}- {node.name}")

        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ").strip()
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ").strip()
            employee = input("Enter the new employee's name: ").strip()
            side = input(
                "Should this employee be on the LEFT or RIGHT of the manager? "
            )
            side = side.lower().strip()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    company_directory()


"""
DESIGN MEMO

This project helped me better understand how recursive insertion works within a tree based data structure. Recursive insertion allowed the program to search through each level of the tree until it either found the correct manager node or reached the end of a branch. Instead of manually tracking where each employee should be placed, the recursion handled moving through the left and right child nodes automatically. This made the logic cleaner and more scalable as the tree grew. Each recursive call narrowed the search space until the correct insertion point was found, then the new employee node was attached to the correct side.

One challenge was locating the target manager while also confirming whether the requested left or right position was available. It was important to avoid overwriting an existing employee and to return clear messages when insertion was not possible. Another challenge was handling base cases correctly, especially when the current node is None. Without clear stopping conditions, recursion can continue too far or fail without feedback. Implementing these checks reinforced how critical base cases and clear conditions are when using recursion.

Trees are preferable when modeling hierarchical relationships such as reporting structures, file systems, and decision processes. Unlike lists or dictionaries, trees naturally represent parent child relationships and support traversal across multiple levels. In systems where hierarchy matters, trees provide a clear structure that scales as relationships grow.
"""
