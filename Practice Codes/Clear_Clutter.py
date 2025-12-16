import os

path = r"C:\Users\admin\OneDrive\Pictures\Saved Pictures\PPt Matrieal"
fn=0
for file in os.listdir(path):
    
    if file.endswith(".png"):
        fn+=1
        old_path = os.path.join(path,file)
        new_path = os.path.join(path,f"Image{fn}.png")
        os.rename(old_path,new_path)
        print(file)
    elif file.endswith(".jpg"):
        fn+=1
        old_path = os.path.join(path,file)
        new_path = os.path.join(path,f"pic{fn}.jpg")
        os.rename(old_path,new_path)
        print(file)
        
        