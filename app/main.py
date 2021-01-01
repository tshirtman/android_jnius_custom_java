"""Demonstrate loading custom java code using jnius
"""
from kivy.app import App
from jnius import autoclass


class Application(App):
    """see module documentation
    """

    def test_jnius(self, name):
        """Lookup our test class, instanciate and call its method
        """
        cls = autoclass("org.test.TestClass")
        result = cls(name).get_result()
        self.root.ids.result_box.text = result


if __name__ == "__main__":
    Application().run()
