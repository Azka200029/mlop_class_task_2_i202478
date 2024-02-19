from main import StudentsInMLOps

def test_enrollStudents():
    # Create an instance of StudentsInMLOps
    class_instance = StudentsInMLOps()

    # Test enrolling students
    class_instance.enrollStudents(5)
    assert class_instance.getTotalStrength() == 5
    print("test_enrollStudents: Passed successfully!")

def test_dropStudents():
    # Create an instance of StudentsInMLOps
    class_instance = StudentsInMLOps()

    # Test dropping students
    class_instance.enrollStudents(10)
    class_instance.dropStudents(3)
    assert class_instance.getTotalStrength() == 7
    print("test_dropStudents: Passed successfully!")

def test_getTotalStrength():
    # Create an instance of StudentsInMLOps
    class_instance = StudentsInMLOps()

    # Test getting total strength
    class_instance.enrollStudents(8)
    assert class_instance.getTotalStrength() == 8
    print("test_getTotalStrength: Passed successfully!")

def test_getClassName():
    # Create an instance of StudentsInMLOps
    class_instance = StudentsInMLOps()

    # Test getting class name
    assert class_instance.getClassName() == "StudentsInMLOps"
    print("test_getClassName: Passed successfully!")

# Run the tests
if __name__ == "__main__":
    test_enrollStudents()
    # print("test_enrollStudents: Passed successfully!")
    
    test_dropStudents()
    # print("test_dropStudents: Passed successfully!")
    
    test_getTotalStrength()
    # print("test_getTotalStrength: Passed successfully!")
    
    test_getClassName()
    # print("test_getClassName: Passed successfully!")
    
    print("All tests passed successfully!")
