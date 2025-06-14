import os

n_epochs = 500
batch_size = 100
chunk_len = 200

hidden_sizes = [128, 256]
n_layers = [1, 2]
learning_rates = [0.01, 0.005]

os.makedirs("logs", exist_ok=True)
os.makedirs("models", exist_ok=True)

for hs in hidden_sizes:
    for nl in n_layers:
        for lr in learning_rates:
            run_name = f"hs{hs}_nl{nl}_lr{lr}"
            model_path = f"models/lstm_{hs}_{nl}_{lr}.pt"
            log_path = f"logs/{run_name}.txt"

            print(f"\nTraining: {run_name}\n")

            command = f"""
python train.py data/sarcasm.txt \\
    --model lstm \\
    --n_epochs {n_epochs} \\
    --hidden_size {hs} \\
    --n_layers {nl} \\
    --learning_rate {lr} \\
    --chunk_len {chunk_len} \\
    --batch_size {batch_size} \\
    --save_as {model_path} \\
    > {log_path}
"""
            os.system(command)

