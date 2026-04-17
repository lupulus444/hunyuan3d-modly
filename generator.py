def generate(prompt="a 3D object"):
    print(f"Generating: {prompt}")
    
    # faux modèle 3D pour test
    with open("output.obj", "w") as f:
        f.write("# simple 3D model")

if __name__ == "__main__":
    generate()
