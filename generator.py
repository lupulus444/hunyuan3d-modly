class Generator:
    def generate(self, image=None, prompt=None):
        output_path = "output.obj"
        
        with open(output_path, "w") as f:
            f.write("# fake 3D model")

        return {
            "model": output_path
        }
