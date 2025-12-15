from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="oakink/OakInk-v1",
    repo_type="dataset",
    local_dir="./OakInk-v1"
)
