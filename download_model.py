from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="intfloat/multilingual-e5-small", 
    cache_dir="./models"
)
