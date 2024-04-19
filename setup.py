import os

def create_distribution():
    source_dir = 'fileconvertpy'
    dist_dir = 'dist'
    os.makedirs(dist_dir, exist_ok=True)
    for filename in os.listdir(source_dir):
        if filename.endswith('.py') or filename.lower() == 'readme.md':  # Include Python files and README
            with open(os.path.join(source_dir, filename), 'r') as source_file:
                with open(os.path.join(dist_dir, filename), 'w') as dest_file:
                    dest_file.write(source_file.read())

if __name__ == "__main__":
    create_distribution()