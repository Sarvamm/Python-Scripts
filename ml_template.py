import os

def create_ml_project_structure(base_dir):
    folders = [
        "data/raw",
        "data/processed",
        "notebooks",
        "scripts",
        "models",
        "reports/figures",
        "tests",
        "configs",
        "utils"
    ]

    files = {
        ".gitignore": "*.pyc\n__pycache__/\n.env\n.DS_Store\nmodels/\ndata/raw/\n",
        "README.md": "# Machine Learning Project\n\nProject Description.",
        "requirements.txt": "# Add your Python dependencies here\nscikit-learn\npandas\nnumpy\nmatplotlib\n",
        "configs/config.yaml": "# Configuration file",
        "scripts/train.py": "# Training script",
        "scripts/evaluate.py": "# Evaluation script",
        "utils/__init__.py": "",
        "tests/test_pipeline.py": "# Add your tests here",
        "notebooks/example.ipynb": "",  # Placeholder Jupyter Notebook
    }

    # Create folders
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Create files
    for file_path, content in files.items():
        full_path = os.path.join(base_dir, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)

    print(f"✅ ML project structure created in: {base_dir}")

# Usage
if __name__ == "__main__":
    project_name = input("Enter your project name: ")
    create_ml_project_structure(project_name)
