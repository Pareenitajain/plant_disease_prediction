from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(rescale=1./255)

train_data = datagen.flow_from_directory(
    "dataset/train",
    target_size=(224, 224),
    batch_size=32,
    class_mode="categorical"
)

test_data = datagen.flow_from_directory(
    "dataset/test",
    target_size=(224, 224),
    batch_size=32,
    class_mode="categorical"
)

print("Training classes:", train_data.num_classes)
print("Testing classes:", test_data.num_classes)
