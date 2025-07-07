import os
from PIL import Image
from tqdm import tqdm



path = "Machine Learning Sets"
for dir in os.listdir(path):
    print(dir)
    if "Tap" in dir:
          for i in os.listdir(f"{path}/{dir}"):
               img = Image.open(f"{path}/{dir}/{i}")
               img.save(f"classified/tap/{i}")
    elif "Fertilizer" in dir:
        for i in os.listdir(f"{path}/{dir}"):
               img = Image.open(f"{path}/{dir}/{i}")
               img.save(f"classified/fertilizer/{i}")
    else: pass

# for dir in tqdm(os.listdir("Machine Learning Sets")):
#     print(dir)
#     if "Algae" in dir or "Dust" in dir or "Green" in dir: 
#         print("passing\n\n\n")
#         pass

#     elif "Tap" in dir or "Fertilizer" in dir or "Water" in dir:
#         for image in tqdm(os.listdir(f"Machine Learning Sets/{dir}"), leave=True):
#                 img = Image.open(f"Machine Learning Sets/{dir}/{image}")
#                 img.save(f"Machine Learning Sets/{dir}/{dir}_{image}")
#     else:
#         for subdir in tqdm(os.listdir(f"Machine Learning Sets/{dir}"), leave=True):
#             for image in tqdm(os.listdir(f"Machine Learning Sets/{dir}/{subdir}"), leave=True):
#                 img = Image.open(f"Machine Learning Sets/{dir}//{subdir}/{image}")
#                 img.save(f"Machine Learning Sets/{dir}/{dir}_{subdir}_{image}")