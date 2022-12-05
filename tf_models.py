from tensorflow.keras import layers, Model, Input

class VGG(Model):
    def __init__(self):
        super(VGG, self).__init__()
        self.conv0_0 = layers.Conv2D(filters=64, kernel_size=3, strides=(1, 1), padding='same')
        self.bn0_0 = layers.BatchNormalization()
        self.conv0_1 = layers.Conv2D(filters=64, kernel_size=3, strides=(1, 1), padding='same')
        self.bn0_1 = layers.BatchNormalization()
        self.conv1_0 = layers.Conv2D(filters=128, kernel_size=3, strides=(1, 1), padding='same')
        self.bn1_0 = layers.BatchNormalization()
        self.conv1_1 = layers.Conv2D(filters=128, kernel_size=3, strides=(1, 1), padding='same')
        self.bn1_1 = layers.BatchNormalization()
        self.conv2_0 = layers.Conv2D(filters=256, kernel_size=3, strides=(1, 1), padding='same')
        self.bn2_0 = layers.BatchNormalization()
        self.conv2_1 = layers.Conv2D(filters=256, kernel_size=3, strides=(1, 1), padding='same')
        self.bn2_1 = layers.BatchNormalization()
        self.conv2_2 = layers.Conv2D(filters=256, kernel_size=3, strides=(1, 1), padding='same')
        self.bn2_2 = layers.BatchNormalization()
        self.conv3_0 = layers.Conv2D(filters=512, kernel_size=3, strides=(1, 1), padding='same')
        self.bn3_0 = layers.BatchNormalization()
        self.conv3_1 = layers.Conv2D(filters=512, kernel_size=3, strides=(1, 1), padding='same')
        self.bn3_1 = layers.BatchNormalization()
        self.conv3_2 = layers.Conv2D(filters=512, kernel_size=3, strides=(1, 1), padding='same')
        self.bn3_2 = layers.BatchNormalization()
        self.conv4_0 = layers.Conv2D(filters=512, kernel_size=3, strides=(1, 1), padding='same')
        self.bn4_0 = layers.BatchNormalization()
        self.conv4_1 = layers.Conv2D(filters=512, kernel_size=3, strides=(1, 1), padding='same')
        self.bn4_1 = layers.BatchNormalization()
        self.conv4_2 = layers.Conv2D(filters=512, kernel_size=3, strides=(1, 1), padding='same')
        self.bn4_2 = layers.BatchNormalization()
        self.fc = layers.Dense(10)

        self.act = layers.ReLU()
        self.pool = layers.MaxPool2D(2,2)
        self.softmax = layers.Softmax(axis=1)

    def call(self, x, training=None, mask=None):
        x = self.act(self.bn0_0(self.conv0_0(x), training=training))
        x = self.act(self.bn0_1(self.conv0_1(x), training=training))
        x = self.pool(x)
        x = self.act(self.bn1_0(self.conv1_0(x), training=training))
        x = self.act(self.bn1_1(self.conv1_1(x), training=training))
        x = self.pool(x)
        x = self.act(self.bn2_0(self.conv2_0(x), training=training))
        x = self.act(self.bn2_1(self.conv2_1(x), training=training))
        x = self.act(self.bn2_2(self.conv2_2(x), training=training))
        x = self.pool(x)
        x = self.act(self.bn3_0(self.conv3_0(x), training=training))
        x = self.act(self.bn3_1(self.conv3_1(x), training=training))
        x = self.act(self.bn3_2(self.conv3_2(x), training=training))
        x = self.pool(x)
        x = self.act(self.bn4_0(self.conv4_0(x), training=training))
        x = self.act(self.bn4_1(self.conv4_1(x), training=training))
        x = self.act(self.bn4_2(self.conv4_2(x), training=training))
        x = layers.MaxPool2D(8,8)(x)
        x = layers.Flatten()(x)
        x = self.fc(x)
        x = self.softmax(x)
        return x

