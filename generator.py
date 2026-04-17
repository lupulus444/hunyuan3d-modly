class Generator:
    def __init__(self, *args, **kwargs):
        # accepte n'importe quels arguments (important)
        pass

    def generate(self, image=None, prompt=None):
        output_path = "output.obj"

        with open(output_path, "w") as f:
            f.write("# fake 3D model")

        return {
            "model": output_path
        }
