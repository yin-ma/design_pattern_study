class RealImage:
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"loading {self.filename}")

    def display(self):
        print(f"display {self.filename}")


class ImageProxy:
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()


if __name__ == "__main__":
    image = ImageProxy("image.jpg")
    image.display()
    image.display()
