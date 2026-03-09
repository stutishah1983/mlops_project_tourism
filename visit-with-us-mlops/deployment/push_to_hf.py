from huggingface_hub import HfApi

api = HfApi()

repo_id = "StutiShah/tourism-predictor-space"

files = [
    "app.py",
    "requirements.txt",
    "Dockerfile"
]

for file in files:
    api.upload_file(
        path_or_fileobj=file,
        path_in_repo=file,
        repo_id=repo_id,
        repo_type="space"
    )

print("Deployment files uploaded successfully!")
