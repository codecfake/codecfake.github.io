import os

for file in sorted(os.listdir("wavs")):
    if file.startswith("genuine"):
        continue
    else:
        model, file_id = file.split("+")
        print(f'| <center> {model} </center> | <center> {file_id[:-4]} </center> | <audio class="audio-player" src="wavs/genuine+{file_id}" controls preload></audio> | <audio class="audio-player" src="wavs/{file}" controls preload></audio> |')