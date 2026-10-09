import subprocess
import time

print("Starting auto test...")
print("================================")

while 1:
    result = subprocess.run(['pytest', 'test_student.py', '-v'], 
                            capture_output=True,
                            text=True
                            )
    print("\n================================")
    print("Test results:")
    print("\n================================")

    print(result.stdout)

    if result.returncode == 0:
        print("All tests passed!")
    else:
        print("Some tests failed!")

    time.sleep(3)