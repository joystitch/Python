import requests
import paramiko
class A(object):
    def __method(self):
        print("I am a method in A")

    def method(self):
        self.__method()

class B(A):
    def __method(self):
        print("I am a method in B")


