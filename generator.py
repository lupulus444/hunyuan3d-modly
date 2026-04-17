class Generator:
    def __init__(self):
        pass

    def generate(self, prompt="a 3D object"):
        print(f"Generating: {prompt}")
        
        with open("output.obj", "w") as f:
            f.write("# fake 3D model")

        return "output.obj"
