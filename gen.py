import os

for file in sorted(os.listdir("wavs")):
    if file.startswith("genuine"):
        continue
    else:
        model, file_id = file.split("+")
        print(f'| {model} | {file_id[:-4]} | <audio class="audio-player" src="genuine+{file_id}" controls preload></audio> | <audio class="audio-player" src="{file}" controls preload></audio> |')