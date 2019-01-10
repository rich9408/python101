import a
import test

print("top-level : b.py")


a.func()

if __name__ == "__main__":
    print("b.py를 직접실행")
else:
    print("b.py를 import시켜서 실행")