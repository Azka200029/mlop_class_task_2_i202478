class StudentsInMLOps:
    def __init__(self):
        self.total_strength = 0

    def enrollStudents(self, count):
        """
        Enroll students into the class.

        Args:
        - count (int): The number of students to enroll.

        Returns:
        - None
        """
        self.total_strength += count

    def dropStudents(self, count):
        """
        Drop students from the class.

        Args:
        - count (int): The number of students to drop.

        Returns:
        - None
        """
        if count > self.total_strength:
            print("Error: Cannot drop more students than total strength.")
        else:
            self.total_strength -= count

    def getTotalStrength(self):
        """
        Get the total strength of students in the class.

        Returns:
        - int: Total number of students in the class.
        """
        return self.total_strength

    def getClassName(self):
        """
        Get the class name.

        Returns:
        - str: Name of the class.
        """
        return "StudentsInMLOps"
