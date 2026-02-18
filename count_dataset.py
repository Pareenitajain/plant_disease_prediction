import os

def count_images(folder_path):
    total_images = 0
    
    for class_name in os.listdir(folder_path):
        class_path = os.path.join(folder_path, class_name)
        
        if os.path.isdir(class_path):
            images = os.listdir(class_path)
            num_images = len(images)
            total_images += num_images
            
            print(f"{class_name} -> {num_images} images")
    
    print("\nTotal Images:", total_images)


print("TRAIN DATASET")
count_images("dataset/train")

print("\nTEST DATASET")
count_images("dataset/test")
