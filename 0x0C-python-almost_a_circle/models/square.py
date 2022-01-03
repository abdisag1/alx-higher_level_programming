#!/usr/bin/python3
"""
And now, the Square!
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        function
        :param size:
        :param x:
        :param y:
        :param id:
        """

        self.size = size
        super().__init__(size, size, x, y, id )

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__size = value

    def update(self, *args, **kwargs):
        for arg in args:
            i = args.index(arg)
            while i < len(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.x = arg
                else:
                    self.y = arg
                i += 1
        for key, value in kwargs.items():
            if key == "id":
                self.width = value
            elif key == "size":
                self.x = value
            elif key == "x":
                self.y = value
            elif key == "y":
                self.id = value
   def to_dictionary(self):
        """dictionary representation of a Square"""
        dic = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return dic
