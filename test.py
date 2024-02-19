from main import StudentsInMLOps

def test_enrollStudents():
    # Create an instance of StudentsInMLOps
    class_instance = StudentsInMLOps()

    # Test enrolling students
    class_instance.enrollStudents(5)
    assert class_instance.getTotalStrength() == 5

def test_dropStudents():
    # Create an instance of StudentsInMLOps
    class_instance = StudentsInMLOps()

    # Test dropping students
    class_instance.enrollStudents(10)
    class_instance.dropStudents(3)
    assert class_instance.getTotalStrength() == 7

def test_getTotalStrength():
    # Create an instance of StudentsInMLOps
    class_instance = StudentsInMLOps()

    # Test getting total strength
    class_instance.enrollStudents(8)
    assert class_instance.getTotalStrength() == 8

def test_getClassName():
    # Create an instance of StudentsInMLOps
    class_instance = StudentsInMLOps()

    # Test getting class name
    assert class_instance.getClassName() == "StudentsInMLOps"

# Run the tests
if __name__ == "__main__":
    test_enrollStudents()
    test_dropStudents()
    test_getTotalStrength()
    test_getClassName()
    print("All tests passed successfully!")
