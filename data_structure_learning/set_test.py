import string
import unittest
from set_implementation import Set

class SetTest(unittest.TestCase):
    def setUp(self):
        self.set = Set()
        self.set.add('hi')
        self.set.add('bye')
        self.set.add('hi, its me')
        self.set.add('boom')

    def test_add(self):
        self.assertEqual(self.set.set, ['hi', 'bye', 'hi, its me', 'boom'])

    def test_len(self):
        self.assertEqual(len(self.set), 4)

    def test_contains(self):
        self.assertTrue('hi, its me' in self.set)
        self.assertFalse('hiiii' in self.set)

    def test_remove(self):
        self.set.remove('boom')
        self.assertEqual(self.set, ['hi', 'bye', 'hi, its me'])

    def test_equal(self):
        self.assertTrue(self.set == ['hi', 'bye', 'hi, its me', 'boom'])
        self.assertFalse(self.set == [])

    def test_is_subset_of(self):
        self.assertTrue(self.set > ['hi', 'bye', 'hi, its me', 'boom', 0, 9, 7, 6, 5])
        self.assertFalse(self.set > [])

    def test_union(self):
        other_set = Set()
        other_set.add(1)
        other_set.add(2)
        other_set.add(3)
        other_set.add(4)
        other_set.add(5)
        union_set = self.set + other_set
        self.assertEqual(len(union_set), 9)
        self.assertEqual(union_set, ['hi', 'bye', 'hi, its me', 'boom', 1, 2, 3, 4, 5])

    def test_intersect(self):
        intersect_set = self.set * [1]
        self.assertFalse(intersect_set)
        intersect_set = self.set * ['hi', 'bye', 1, 2, 3, 4, 5, 6, 2]
        self.assertNotEqual(self.set, intersect_set)
        self.assertTrue(intersect_set > self.set)

    def test_word_count(self):
        word_count = []
        article = """\
        Turtle graphics is a popular way for introducing programming to kids. It was part of the original Logo programming language developed by Wally Feurzig and Seymour Papert in 1966.Imagine a robotic turtle starting at (0, 0) in the x-y plane. After an import turtle, give it the command turtle.forward(15), and it moves (on-screen!) 15 pixels in the directionit is facing, drawing a line as it moves. Give it the command turtle.right(25), and it rotates in-place 25 degrees clockwise.By combining together these and similar commands, intricate shapes and pictures can easily be drawn.The turtle module is an extended reimplementation of the same-named module from the Python standard distribution up to version Python 2.5.It tries to keep the merits of the old turtle module and to be (nearly) 100% compatible with it. This means in the first place to enable the learning programmer to use all the commands, classes and methods interactively when using the module from within IDLE run with the -n switch.The turtle module provides turtle graphics primitives, in both object-oriented and procedure-oriented ways. Because it uses Tkinter for the underlying graphics, it needs a version of Python installed with Tk support.The object-oriented interface uses essentially two+two classes:The TurtleScreen class defines graphics windows as a playground for the drawing turtles. Its constructor needs a Tkinter.Canvas or a ScrolledCanvas as argument. It should be used when turtle is used as part of some application.The function Screen() returns a singleton object of a TurtleScreen subclass. This function should be used when turtle is used as a standalone tool for doing graphics. As a singleton object, inheriting from its class is not possible.All methods of TurtleScreen/Screen also exist as functions, i.e. as part of the procedure-oriented interface.RawTurtle (alias: RawPen) defines Turtle objects which draw on a TurtleScreen. Its constructor needs a Canvas, ScrolledCanvas or TurtleScreen as argument, so the RawTurtle objects know where to draw.Derived from RawTurtle is the subclass Turtle (alias: Pen), which draws on the Screen - instance which is automatically created, if not already present.All methods of RawTurtle/Turtle also exist as functions, i.e. part of the procedure
-oriented interface.The procedural interface provides functions which 
 are derived from the methods of the classes Screen and Turtle. They have the same names as the corresponding methods. A screen  object is automatically created whenever a function derived from a Screen method is called. An (unnamed) turtle object is automatically created whenever any of the functions derived from a Turtle method is called.To use multiple turtles an a screen one has to use the object-oriented interface.Note In the following documentation the argument list for functions is given. Methods, of course, have the additional first argument self which is omitted here"""

        article = article.translate(string.maketrans('', ''), string.punctuation)
        article = article.split(' ')
        s = Set()
        for word in article:
            s.add(word)
        for word in s.set:
            count = article.count(word)
            word_count.append(word + ':' + str(count))
        print word_count

if __name__ == '__main__':
    unittest.main()
