class Generator:
    def generate(self, image=None, prompt=None):
        print("Input image:", image)
        print("Prompt:", prompt)

        with open("output.obj", "w") as f:
            f.write("# fake 3D model")

        return "output.obj"
